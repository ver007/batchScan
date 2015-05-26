#!/usr/bin/env python
#coding=utf8

import re
import requests
import threadpool as tp

class ScanTool:
    def __init__(self, url_list, payload, scan_rule, res_rule, method, threadnum):
        self.url_list = url_list
        self.payload = payload
        self.scan_rule = scan_rule
        self.res_rule = res_rule
        self.method = method
        self.threadnum = threadnum

    '''处理GET方式'''
    def run_get(self, url_list):
        f = open('res.txt', 'a')
        for url in self.url_list:
            try:
                url_full = "%s?%s" %(url, self.payload)
                req = requests.get(url_full)
                if req.status_code != 200:
                    raise Exception
                page = req.content
                scan_reg = re.compile(r'%s' % self.scan_rule)
                res_reg = re.compile(r'%s' % res_rule)
                res = url_full
                if scan_reg.findall(page_content):
                    if res_rule != '':
                        for item in res_reg.findall(page_content):
                            res += '\t\t' + item
                        res += '\n'
                        print "[+]%s" %res
                        f.write(res)
                    else:
                        res = res + '\n'
                        res = res + '\t\t' +'vulnerable' +'\n'
                        f.write(res)
            except:
                continue

    '''处理POST方式'''
    def run_post(self, url_list):
        # post的形式：username=admin&password=admin
        f = open('res.txt', 'a')
        for url in self.url_list:
            try:
                # 将payload变为字典的形式{'username':'admin','pass':'admin'}
                data = dict([tuple(x.split("=")) for x in self.payload.split("&")])
                req = requests.post(url, data=data)
                if req.status_code != 200:
                    raise Exception
                page = req.content
                scan_reg = re.compile(r'%s' % self.scan_rule)
                res_reg = re.compile(r'%s' % res_rule)
                res = url
                if scan_reg.findall(page_content):
                    if res_rule != '':
                        for item in res_reg.findall(page_content):
                            res += '\t\t' + item
                        res += '\n'
                        print "[+]%s" %res
                        f.write(res)
                    else:
                        res = res + '\t\t' +'vulnerable' +'\n'
                        print "[+]%s" %res
                        f.write(res)
            except:
                continue

            def run(self):
                pool = tp.ThreadPool(threadnum)
                if self.method = "get":
                    reqs = tp.makeRequests(self.run_get, self.url_list)
                elif self.method = "post":
                    reqs = tp.makeRequests(self.run_get, self.url_list)
                else:
                    print "[-]ERROR MESSAGE! Your input args invaild!"
                [pool.putRequest(req) for req in reqs]
                pool.wait()