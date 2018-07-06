# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 10:00:56 2018

@author: hztengkezhen
"""

import pandas as pd
from delta_monitor import delta_monitor_number
from delta_monitor import delta_monitor_ratio
import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    dt = sys.argv[2]
    target_name = sys.argv[3]
    delta_type = sys.argv[4]

    data = pd.read_csv(filename,sep='\t')
    dimensions = ['server','os','pay_flag','new_flag']

    if len(sys.argv) == 7:
        now_target = sys.argv[5]
        before_target = sys.argv[6]
        delta_monitor_number(data,dimensions,target_name,delta_type,now_target,before_target,2,dt)
    elif len(sys.argv) == 9:
        now_n = sys.argv[5]
        now_d = sys.argv[6]
        before_n = sys.argv[7]
        before_d = sys.argv[8]
        delta_monitor_ratio(data,dimensions,target_name,delta_type,now_n,now_d,before_n,before_d,2,dt)

