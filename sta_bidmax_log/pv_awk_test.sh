#!/bin/bash/

YESDATE=`date +"%Y%m%d" -d "-1 day"`
echo ${YESDATE}

for FILE in /home/work/run_env/DEPLOY/BidMax/Logger/log/pv.${YESDATE}*.log
do
    echo $FILE
    awk -F'\001' '{data[$8]++} END {for(i in data) print i"\t"data[i]}' $FILE |cat>>pv_app_${YESDATE}.tmp
done
awk -F'\t' '{data[$1]+=$2} END {for(i in data) print "pv""\t"i"\t"data[i]}' pv_app_${YESDATE}.tmp |cat>pv_app_${YESDATE}.log
rm pv_app_${YESDATE}.tmp

for FILE in /home/work/run_env/DEPLOY/BidMax/Logger/log/bid.${YESDATE}*.log
do
    echo $FILE
    awk -F'\001' '{data[$10]++} END {for(i in data) print i"\t"data[i]}' $FILE |cat>>bid_app_${YESDATE}.tmp
done
#awk -F'\t' '{data[$1"\t"$2]+=$3} END {for(i in data) print "bid""\t"i"\t"data[i]}' bid_app_${YESDATE}.tmp |cat>bid_app_${YESDATE}.log
awk -F'\t' '{data[$1]+=$2} END {for(i in data) print "bid""\t"i"\t"data[i]}' bid_app_${YESDATE}.tmp |cat>bid_app_${YESDATE}.log
rm bid_app_${YESDATE}.tmp

cat pv_app_${YESDATE}.log>>pv_bid_${YESDATE}
cat bid_app_${YESDATE}.log>>pv_bid_${YESDATE}
awk -F'\t' '{if($1=="pv") {p[$2]=$3} else {b[$2]=$3}} END {for(i in p) print "pb""\t"i"\t"p[i]"\t"b[i]}' pv_bid_${YESDATE} |cat>pv_bid_${YESDATE}.log

rm pv_app_${YESDATE}.log
rm bid_app_${YESDATE}.log
rm pv_bid_${YESDATE}


for FILE in /home/work/run_env/DEPLOY/BidMax/Logger/log/pv.${YESDATE}*.log
do
    awk -F'\001' '{data[$6]++} END {for(i in data) print i"\t"data[i]}' $FILE |cat>>pv_name_${YESDATE}.tmp
done
awk -F'\t' '{data[$1]+=$2} END {for(i in data) print "pv""\t"i"\t"data[i]}' pv_name_${YESDATE}.tmp |cat>pv_name_${YESDATE}.log
rm pv_name_${YESDATE}.tmp

for FILE in /home/work/run_env/DEPLOY/BidMax/Logger/log/bid.${YESDATE}*.log
do
    awk -F'\001' '{data[$8]++} END {for(i in data) print i"\t"data[i]}' $FILE |cat>>bid_name_${YESDATE}.tmp
done
awk -F'\t' '{data[$1]+=$2} END {for(i in data) print "bid""\t"i"\t"data[i]}' bid_name_${YESDATE}.tmp |cat>bid_name_${YESDATE}.log
rm bid_name_${YESDATE}.tmp

cat pv_name_${YESDATE}.log>>pv_bid_name_${YESDATE}
cat bid_name_${YESDATE}.log>>pv_bid_name_${YESDATE}
awk -F'\t' '{if($1=="pv") {p[$2]=$3} else {b[$2]=$3}} END {for(i in p) print "pb""\t"i"\t"p[i]"\t"b[i]}' pv_bid_name_${YESDATE} |cat>pv_bid_name_${YESDATE}.log

rm pv_name_${YESDATE}.log
rm bid_name_${YESDATE}.log
rm pv_bid_name_${YESDATE}


for FILE in /home/work/run_env/DEPLOY/BidMax/Logger/log/bid.${YESDATE}*.log
do
    echo $FILE
    awk -F'\001' '{data[$34]++} END {for(i in data) print i"\t"data[i]}' $FILE |cat>>bid_creative_${YESDATE}.tmp
done
      
awk -F'\t' '{data[$1]+=$2} END {for(i in data) print "bid""\t"i"\t"data[i]}' bid_creative_${YESDATE}.tmp |cat>bid_creative_${YESDATE}.log
rm bid_creative_${YESDATE}.tmp

#scp pv_bid_${YESDATE}.log hs@192.168.0.6:/home/hs/

