"""
Samples for bos client.
"""

import os
import random
import string
import time
import sys

import bos_sample_conf
from baidubce import exception
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

def upload_file(in_name, in_key, in_file_name, in_raw_bucket):
    bucket_name = in_name
    key = in_key
    file_name = in_file_name
    raw_bucket = in_raw_bucket

    if not bos_client.does_bucket_exist(bucket_name):
        bos_client.create_bucket(bucket_name)

    if os.path.exists(file_name):
        left_size = os.path.getsize(file_name)
        if left_size == 0:
            bos_client.put_object_from_file(bucket_name, key, file_name)
            return

        upload_id = bos_client.initiate_multipart_upload(bucket_name, key).upload_id

        offset = 0
        part_number = 1
        part_list = []
        while left_size > 0:
            part_size = 256 * 1024 * 1024
            if left_size < part_size:
                part_size = left_size

            response = bos_client.upload_part_from_file(
                    bucket_name,
                    key,
                    upload_id,
                    part_number,
                    part_size,
                    file_name,
                    offset)

            left_size -= part_size
            offset += part_size
            # your should store every part number and etag to invoke complete multi-upload
            part_list.append({
                "partNumber": part_number,
                "eTag": response.metadata.etag
            })
            part_number += 1

        # list multi-uploads
        response = bos_client.list_multipart_uploads(raw_bucket)
        for upload in response.uploads:
            __logger.debug("[Sample] list multi-uploads, upload_id:%s", upload.upload_id)

        # list parts
        response = bos_client.list_parts(bucket_name, key, upload_id)
        for part in response.parts:
            __logger.debug("[Sample] list parts, etag:%s", part.etag)

        # SuperFile step 3: complete multi-upload
        bos_client.complete_multipart_upload(bucket_name, key, upload_id, part_list)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG, filename='./bos_upload_log.log', filemode='w')
    __logger = logging.getLogger(__name__)
    if (len(sys.argv) >= 2) and (sys.argv[1] != "") :
        last_hour = sys.argv[1]
    else:
        last_hour = time.strftime("%Y%m%d%H", time.localtime(time.time()-3600))
    last_day = last_hour[0:8]
    bos_client = BosClient(bos_sample_conf.config)

    # chulihou active log upload
    active_bucket_name = 'hs-test/dataLog_2.0/bes/BidMax/active/'+last_day+'/'
    active_key = 'active.' + last_hour + '.log'
    active_file_name = '/home/work/hs/active_log/nactive.'+last_hour+'.log'
    active_raw_bucket = 'hs-test'
    upload_file(active_bucket_name, active_key, active_file_name, active_raw_bucket)
