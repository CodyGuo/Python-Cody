# -*- coding=utf-8 -*-
import http.client

conn = http.client.HTTPConnection("www.python.org")
for retries in range(3):
    try:
        conn.request('GET', '/')
        resp = conn.getresponse()
        print(resp.msg)
    except http.client.RemoteDisconnected:
        pass