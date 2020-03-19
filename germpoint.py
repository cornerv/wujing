#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip('\\')
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录存在
        print(path + ' 目录已存在')
        return False
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
       return files # 指定路径下所有非目录子文件
path=os.getcwd().replace('\\','/')
mkdir(os.getcwd().replace('\\','/')+'/胚系_result')
file_list=file_name(path+'/original_vcf')
number_list=set()
for i in file_list:
    number_list.add(i[:9])
for i in number_list:
    if i+'TD.vcf' in file_list and i+'GD.vcf' in file_list:
        print(i)
        dic_TD={}
        list_GD=[]
        file=open(path+'/胚系_result/'+i.split('.')[0]+'_germ.vcf','w')
        with open(path+'/original_vcf/'+i+'TD.vcf','r')as f1:
            for line in f1:
                line=line.strip()
                line_TD='\t'.join(line.split('\t')[0:5])
                dic_TD[line_TD]='\t'.join(line.split('\t')[5:8])
        with open(path + '/original_vcf/' + i + 'GD.vcf', 'r')as f2:
            for line in f2:
                line = line.strip('\n')
                line_GD='\t'.join(line.split('\t')[0:5])
                if line_GD in dic_TD.keys():
                    value1=dic_TD[line_GD]
                    value2='\t'.join(line.split('\t')[5:8])
                    sequence=line_GD+'\t'+value1.split('\t')[0]+'|'+value2.split('\t')[0]+'\t'+value1.split('\t')[1]+'|'+value2.split('\t')[1]+'\t'+value1.split('\t')[2]+'|'+value2.split('\t')[2]
                    # print(sequence)
                    file.write(sequence+'\n')
        file.close()


