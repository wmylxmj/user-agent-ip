# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 18:10:35 2018

@author: wmy
"""

from urllib import request
import chardet
from urllib import parse
import json
from urllib import error

def GetHtmlInfo(htmlname):
    url=htmlname
    requestobject=request.Request(url)
    proxy={'http':'106.136.43.8:808'}
    proxysupport=request.ProxyHandler(proxy)
    opener=request.build_opener(proxysupport)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    request.install_opener(opener)
    try:
        response=request.urlopen(requestobject)
        html=response.read()
        charset=chardet.detect(html)
        encode=charset['encoding']
        html=html.decode(encode)
        return html
    except error.HTTPError as e:
        return 'HTTP Error:'+str(e.code)
    except error.URLError as e:
        return 'URL Error:'+str(e.reason)
    return 0

print(GetHtmlInfo('http://www.ip138.com/'))
