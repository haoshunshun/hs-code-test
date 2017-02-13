"""
Samples for bmr client.
"""

import logging
import os
import sys
import time
import uuid

file_path = os.path.normpath(os.path.dirname(__file__))
sys.path.append(file_path + '/../../')

##last seven days
##user app bundle


import bmr_process_conf
from baidubce.services.bmr import bmr_client as bmr
from baidubce import exception as ex

LOG = logging.getLogger('baidubce.services.bmr.bmrclient')
fh = logging.FileHandler('log/hourly_report_process.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(fh)

CONF = bmr_process_conf

if __name__ == '__main__':
    if (len(sys.argv) >= 2) and (sys.argv[1] != "") :
        last_hour = sys.argv[1]
    else:
        last_hour = time.strftime("%Y-%m-%d_%H", time.localtime(time.time()-3600))
        last_day = last_hour[0:10]
    bmr_client = bmr.BmrClient(CONF.config)
    try:
        new_cluster_id = None
        response = bmr_client.create_cluster(
            image_type='hadoop',
            image_version='0.1.0',
            instance_groups=[
                bmr.instance_group(
                    group_type='Master',
                    instance_type='m.medium',
                    instance_count=1,
                    name='ig-master'
                ),
                bmr.instance_group(
                    group_type='Core',
                    instance_type='m.medium',
                    instance_count=2,
                    name='ig-core'
                )
            ],
            applications=[
            ],
            auto_terminate=True,
            client_token=uuid.uuid4().hex,
            log_uri='bos://bmr-base-log/bmr-temp-log/',
            name='sta_bid_iurl_'+last_hour,
            steps=[
                bmr.step(
                    step_type='Streaming',
                    action_on_failure='Continue',
                    properties=bmr.streaming_step_properties(
                        'bos://hs-test/dataLog_2.0/ssp/RES/bid/'+last_day+'/'+last_hour+'/bid.'+last_hour+'.log',
                        'bos://hs-test/dataLog_2.0/ssp/Sta/bid_iurl'+last_hour+'/',
                        'bos://hs-test/scripts/mapper_sta_bid_iurl.py',
                        'bos://hs-test/scripts/reducer_sta_bid_iurl.py',
			            '-D mapreduce.job.reduces=1'
        		    ),
        		    name='sta_bid_iurl' + last_hour
                ),
            ])
        LOG.debug('create cluster response: %s' % response)
        new_cluster_id = response.cluster_id

        if new_cluster_id is None:
            LOG.error('failed to create cluster. Skip following requests.')
            sys.exit(1)
        else:
            LOG.info(' Success starting BMR ,cluster initialing with id %s',new_cluster_id)
    except ex.BceHttpClientError as e:
        if isinstance(e.last_error, ex.BceServerError):
            LOG.error('send request failed. Response %s, code: %s, msg: %s'
                    % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            LOG.error('send request failed. Unknown exception: %s' % e)
