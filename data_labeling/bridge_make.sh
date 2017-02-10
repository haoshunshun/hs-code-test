#!/bin/bash
#copy new labeled data to /root/hs/
cp /root/hs/bridge/bridge_makeresult.csv /root/hs/
#copy original data to /root/hs/
cp /etc/puppet/modules/ssp_conf/files/etc/router/transform/device_make_inmobi /root/hs/
#cat >> new labled data to original data
cat bridge_makeresult.csv>>device_make_inmobi
#new + original data recover original data
cp device_make_inmobi /etc/puppet/modules/ssp_conf/files/etc/router/transform/device_make_inmobi
#move to ./back_up
mv /root/hs/bridge_makeresult.csv ./back_up
#print OK
echo OK
