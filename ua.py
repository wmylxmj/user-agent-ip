# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:35:16 2018

@author: wmy
"""

from urllib import request
import chardet
from urllib import parse
import json
from urllib import error

def UA_CatchHtmlInfo(htmlname):
    url=htmlname
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    requestobject=request.Request(url,headers=head)
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

print(UA_CatchHtmlInfo('https://www.baidu.com/'))        
