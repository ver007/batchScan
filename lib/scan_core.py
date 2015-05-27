#!/usr/bin/env python
#coding=utf8

from scantool import ScanTool

class AbstractScan:
    def __init__(self, options):
        self.options = options

    '''扫描url具体方法'''
    def scan_url(self, payload):
        scan_rule = self.options.scan_rule
        res_rule = self.options.res_rule
        method = self.options.method
        threadnum = self.options.thread
        url_list = []
        with open('url.txt') as urltxt:
            url_list = urltxt.read().split('\n')
        scanner = ScanTool(url_list, payload, scan_rule, res_rule, method, threadnum)
        scanner.run()