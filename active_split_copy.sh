#!/bin/bash/

if [ -f ~/.bash_profile ]; 
then
    . ~/.bash_profile
fi
LAST_HOUR=`date -d"-0 hour" +%Y%m%d%H`
echo ${LAST_HOUR}
for FILE in /home/work/callback_server/logs/active/active.log
do
    awk -F'[\[\]\,]' '{print $1"\t"$3"\t""active""\t"$7}' ${FILE} |cat>/home/work/hs/active_log/active.${LAST_HOUR}.log
done
scp /home/work/hs/active_log/active.${LAST_HOUR}.log nhs@180.76.155.167:/home/work/disk/nhs/dingxiang
#scp /home/work/hs/active_log/active.${LAST_HOUR}.log work@180.76.155.167:/home/work/disk/hs/bes_log/
last_169_hour=`date -d"-169 hour" +%Y%m%d%H`
rm /home/work/hs/active_log/active.${last_169_hour}.log
