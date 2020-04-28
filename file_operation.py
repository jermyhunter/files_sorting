# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:18:01 2020

@author: Yugar
"""

import re
import os
import shutil


def sort_files(source_path, output_path):

    pattern = "[\d\D]*\.([A-Za-z\d]*$)"

    postfixs = dict()
    
    sep = '/'

    for (root, dirs ,files) in os.walk(source_path ,topdown=True):
        for file in files:
            Mobj = re.match(pattern, file)
            # get postfix
            postfix = Mobj.group(1)
            
            if postfix not in postfixs: # if not existed, create a new array
                postfixs[postfix] = []
                postfixs[postfix].append(file)
            else:
                postfixs[postfix].append(file)
                
    # print(postfixs)
    '''
        生成新文件夹
    '''
    
    # test if the output folder exists
    # if so, remove iteratively
    # try:
    #     os.mkdir(output_path)
    # except FileExistsError:
    #     pass
        # print('existed')
        # shutil.rmtree(output_path)
        # os.mkdir(output_path)
    
    
    # print(os.getcwd())
    
    for postfix in postfixs:
        os.mkdir(output_path + '/' + postfix)
        for file in postfixs[postfix]:
            src_file = sep.join((source_path, file))
            dst_file = sep.join((output_path, postfix, file))
            # mv
    #        os.rename(src_file, dst_file)
            # copy
            shutil.copy(src_file, dst_file)

if __name__ == '__main__':
    # src_folder = 'files'
    # source_path = './' + src_folder 
    
    # output_folder = 'output'
    # output_path = source_path + '/' + output_folder
    
    # sort_files(source_path, output_path)
    # pass    
    output_path = './1'
    try:
        os.mkdir(output_path)
    except FileExistsError:
        try:
            os.removedirs(output_path)
        except OSError:
            print('输出文件夹需要为空文件夹！')
