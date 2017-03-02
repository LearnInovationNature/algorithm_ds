#! /usr/bin/python
# -*- coding: utf-8 -*-

import pdb
'''
最长对称子字符串有两种形式
奇对称：abcba
偶对称：abccba
算法的时间复杂度为n^2
空间复杂度为n
'''
#写一个循环方便测试
while (True):
    max_sym_sub_len = 1
    max_single = 1 #奇对称最长子串
    max_double = 0 #偶对称最长子串

    raw_str = raw_input()
   
#    pdb.set_trace()

    if raw_str == 'q': #退出
        break;

    if (len(raw_str) == 1):
       pass 
    elif (len(raw_str) == 2):
        if (raw_str[0] == raw_str[1]): #长度为2,两个字符相等，最长子串为2
            max_sym_sub_len = 2
    else: #长度>3
        start_ind = 1 #从第2个字符开始判断
        tmp_ind = 0

        #奇对称的情形
        for start_ind in range(1, len(raw_str) - 1):
            max_single_tmp = 1
            # 判断当前的字符距离哪个端点更近
            tmp_range = min(start_ind, len(raw_str) - 1 - start_ind)
            # print start_ind, tmp_range
            for tmp_ind in range(1, tmp_range + 1):
                #开始判断,如果两侧的字符相等，临时最长的长度加2
                if (raw_str[start_ind - tmp_ind] == raw_str[start_ind + tmp_ind]):
                    max_single_tmp += 2
                else:
                    break;
            max_single = max(max_single, max_single_tmp)

        for start_ind in range(1, len(raw_str) - 1):
            max_double_tmp = 0
            # 判断当前的字符距离第一个字符，和当前字符的下个字符距离
            # 最后一个端点的距离中哪个更近
            tmp_range = min(start_ind, len(raw_str) - 2 - start_ind)
            # print start_ind, tmp_range
            # tmp_ind 应该从0开始
            for tmp_ind in range(tmp_range + 1):
                #开始判断,如果两侧的字符相等，临时最长的长度加2
                if (raw_str[start_ind - tmp_ind] == 
                        raw_str[start_ind + 1 + tmp_ind]):
                    max_double_tmp += 2
                else:
                    break;
            max_double= max(max_double, max_double_tmp)       
    max_sym_sub_len = max(max_single, max_double)
    print max_sym_sub_len
