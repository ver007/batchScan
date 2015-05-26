#!/usr/bin/env python
#coding=utf8

class AbstractScan:
    def __init__(self, options, addr_file, out_file):
        self.options = options
        self.addr_file = addr_file
        self.out_file = out_file

    '''扫描url具体方法'''
    def scan_url(self, payload, addr_file, out_file):
        scan_rule = self.options.scan_rule
        res_rule = self.options.res_rule
        method = self.options.method
        url_list = []
        with open(addr_file) as urltxt:
            url_list = urltxt.read().split('\n')
        scanner = ScanTool(url_list, payload, scan_rule, res_rule, method, out_file)
        scanner.scan()