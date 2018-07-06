# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:50:44 2018

@author: hztengkezhen
"""

from __future__ import division

from itertools import combinations
from operator import itemgetter

def process_number(data,now_target,before_target,cmp_dims,dims):
    # local data
    local_data = group_reindex(data,cmp_dims,[now_target,before_target])
    # proportion
    local_data['proportion'] = local_data[before_target]/sum(local_data[before_target])
    local_data['delta'] = abs(local_data[now_target]-local_data[before_target])
    #local_data['delta_proportion'] = local_data['delta']/sum(local_data['delta'])
    local_data['delta_proportion'] = local_data[now_target]/sum(local_data[now_target])
    # weight
    local_data['weight'] = abs(local_data['proportion']-local_data['delta_proportion'])    
    weight_sum = sum(local_data['weight'])
    # result
    weight_result = zip(local_data[cmp_dims].to_records(index=False),local_data['weight'])
    return weight_sum,weight_result

def process_ratio(data,now_n,now_d,before_n,before_d,cmp_dims,dims):    
    # local data
    local_data = group_reindex(data,cmp_dims,[now_n,now_d,before_n,before_d])
    local_data['before_ratio'] = local_data[before_n]/local_data[before_d]
    local_data['before_ratio'] = local_data['before_ratio'].fillna(0.0)
    local_data['delta_n_theory'] = local_data['before_ratio']*(local_data[now_d]-local_data[before_d])
    local_data['delta_n'] = local_data[now_n]-local_data[before_n]
    local_data['delta_n_delta'] = local_data['delta_n']-local_data['delta_n_theory']
    # weight
    local_data['weight'] = abs(local_data['delta_n_delta']/sum(local_data[now_d]))
    local_data['weight'] = local_data['weight'].fillna(0.0)
    # ratio
    #real_ratio = sum(local_data[now_n])/sum(local_data[now_d])
    #theory_ratio = sum(local_data[before_n]+local_data['delta_n_theory'])/sum(local_data[now_d])
    weight_sum = sum(local_data['weight'])
    # result
    weight_result = zip(local_data[cmp_dims].to_records(index=False),local_data['weight'])
    return weight_sum,weight_result

def tuple_to_string(t):
    return '+'.join([str(item) for item in t])

def group_reindex(data,cmp_dims,target_dims):
    return data.groupby(by=cmp_dims).sum().reset_index()[cmp_dims+target_dims]

def delta_monitor_number(data,dimensions,target_name,delta_type,target_now,target_before,N,dt):
    dim_result = []
    weight_result = {}
    # process
    for i in range(1,len(dimensions)+1):
        for item in combinations(dimensions,i):
            weight_sum,weight_ret = process_number(
                    data,target_now,target_before,list(item),dimensions)
            dim_result.append((len(item),item,weight_sum))
            weight_result[(len(item),item)] = weight_ret
    # output
    for line in sorted(dim_result,key=lambda x:(-x[0],x[2]),reverse=True):
        flag,dims,weight = line
        weight_list = weight_result[(flag,dims)]
        #print 'NO=%d,dims=%s,weight=%.1f%%' % (flag,tuple_to_string(dims),weight*100)
        for item in sorted(weight_list,key=itemgetter(1),reverse=True)[0:N]:
            #print '    value=%s,weight=%.1f%%' % (tuple_to_string(item[0]),item[1]*100)
            print '\t'.join([dt,target_name,delta_type,str(flag),
                             tuple_to_string(dims),'%.1f' % (weight*100),
                             tuple_to_string(item[0]),'%.1f' % (item[1]*100)])

def delta_monitor_ratio(data,dimensions,target_name,delta_type,now_n,now_d,before_n,before_d,N,dt):
    dim_result = []
    weight_result = {}    
    # process
    for i in range(1,len(dimensions)+1):
        for item in combinations(dimensions,i):
            weight_sum,weight_ret = process_ratio(
                    data,now_n,now_d,before_n,before_d,list(item),dimensions)
            dim_result.append((len(item),item,weight_sum))
            weight_result[(len(item),item)] = weight_ret
    # output
    for line in sorted(dim_result,key=lambda x:(-x[0],x[2]),reverse=True):
        flag,dims,weight = line
        weight_list = weight_result[(flag,dims)]
        #print 'NO=%d,dims=%s,weight=%.1f%%' % (flag,tuple_to_string(dims),weight*100)
        for item in sorted(weight_list,key=itemgetter(1),reverse=True)[0:N]:
            #print '    value=%s,weight=%.1f%%' % (tuple_to_string(item[0]),item[1]*100)
            print '\t'.join([dt,target_name,delta_type,str(flag),
                             tuple_to_string(dims),'%.1f' % (weight*100),
                             tuple_to_string(item[0]),'%.1f' % (item[1]*100)])
