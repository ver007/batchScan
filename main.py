#!/usr/bin/env python
#coding=utf8

import os
import glob
import sys
from optparse import OptionParser
from lib.scan_core import AbstractScan

options = None
arguments = None

class Item():
    def __init__(self, scan_rule, res_rule, payload, method):
        self.scan_rule = scan_rule
        self.res_rule = res_rule
        self.payload = payload
        self.method = method

'''接收参数'''
def recv_args():
    global options, arguments
    parser = OptionParser()
    parser.add_option('--thread', '-t', default='10', dest='thread',
        help='choose thread number')
    parser.add_option('--name', '-n', dest='name',
        help='from node floder choose a script')
    (options, arguments) = parser.parse_args()

'''判断参数输入是否正确'''
def judge_arg():
    if not options.name:
        print '[-]ERROR MESSAGE! Not choose a script!'
        sys.exit()

def get_item():
    global options
    __import__ ('node.' + options.name)
    scan_rule = sys.modules['node.'+options.name].dict_rule['scan_rule']
    res_rule = sys.modules['node.'+options.name].dict_rule['res_rule']
    payload = sys.modules['node.'+options.name].dict_rule['payload']
    method = sys.modules['node.'+options.name].dict_rule['method']
    item = Item(scan_rule, res_rule, payload, method, options.thread)
    return item

def main():
    global options
    recv_args()
    judge_arg()
    get_item()
    scanner = AbstractScan(get_item())
    scnner.scan_url()

if __name__ == '__main__':
    main()