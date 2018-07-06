#!/bin/bash

rm -f result;

for ((i=1;i<=35;++i))
do
    dt=`date -d "20180531 ${i} days" +"%Y%m%d"`;
    yesterday=`date -d "${dt} 1 days ago" +"%Y%m%d"`;
    last_week=`date -d "${dt} 7 days ago" +"%Y%m%d"`;
    echo $dt
    echo $yesterday
    echo $last_week
    sed -i "s/20170621/${last_week}/g" jk.sql;
    sed -i "s/20170627/${yesterday}/g" jk.sql;
    sed -i "s/20170628/${dt}/g" jk.sql;
    cat jk.sql | mql h35 > jk_${dt};
    python delta_monitor_use.py jk_${dt} ${dt} 'arppu' 'huan' 'today_payment' 'today_pay_cnt' 'yesterday_payment' 'yesterday_pay_cnt' >> result;
    sed -i "s/${dt}/20170628/g" jk.sql;
    sed -i "s/${yesterday}/20170627/g" jk.sql;
    sed -i "s/${last_week}/20170621/g" jk.sql;
done

sed -i 's/\t/","/g' result;
sed -i 's/^/insert into dw_h35_delta_monitor_day values("/g' result;
sed -i 's/$/");/g' result;
cat result | mql h35;

rm -f jk_*;
