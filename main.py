#!/usr/bin/env python
#coding=utf8

import os
import glob
from optparse import OptionParser

options = None
arguments = None

class Item():
    def __init__(self, scan_rule, res_rule, payload, method):
        self.scan_rule = scan_rule
        self.res_rule = res_rule
        self.payload = payload
        self.method = method

def recv_args():
    global options, arguments
    parser = OptionParser()
    parser.add_option('--file', '-f', dest='file', defualt='url.txt',
        help='input file', metavar='FILE')
    parser.add_option('--out', '-o', default='res.txt', dest='output',
        help='ouput file', metavar='OUT FILE')
    parser.add_option('--thread', '-t', default='10', dest='thread',
        help='choose thread number')
    parse.add_option('--name', '-t', dest='name',
        help='from node floder choose a script')
    (options, arguments) = parser.parse_args()

def judge_arg():
    if not os.path.exists(options.file):
        parser.error('输入文件不存在')
    if not options.name:
        parser.error('没有选择攻击脚本')

def get_item():
    global options
    __import__ ('node.' + options.name)
    item = Item(dict_rule['scan_rule'], dict_rule['res_rule'], dict_rule['payload'], dict_rule['method'])
    return item

def main():
    global options
    recv_args()
    judge_arg()
    get_item()
    scanner = AbstractScanner(get_item())
    scnner.run()

if __name__ == '__main__':
    main()