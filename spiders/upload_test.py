# -*- coding: utf-8 -*-
"""
    1.利用requests以及requests_toolbelt实现文件上传
    2.大文件一般采用分块上传,即将文件流按某种size规格进行分块,以唯一id做标识,以chunk进行块间索引连接,多次post
    3.大文件分块传输的type一般为 application/octet-stream
"""
import requests
from requests_toolbelt import MultipartEncoder

# 此处分块text/plain改为application/octet-stream
files = {
            'chunks': '大文件总块数',  # 大文件
            'chunk': '当前块索引',   # 大文件
            '其他key': '其他value',
            'imei-MD5.txt': ('imei-MD5.txt', open('D:\spiderman2\crawlframe\spiders\imei-MD5.txt', 'rb'), 'text/plain')
        }

multipart_encoder = MultipartEncoder(
    fields=files, boundary='----WebKitFormBoundaryJ2aGzfsg35YqeT7X'  # boundry为分隔符,最好与原始接口保持相同格式
)

headers = {
    "Host": "upload-zcg.safetree.com.cn",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Origin": "http://upload-zcg.safetree.com.cn",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Content-Type": multipart_encoder.content_type,  # boundry
    "Referer": "http://upload-zcg.safetree.com.cn/Home/Privacy",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

res1 = requests.post(
            f'your url',
            headers=headers,
            proxies=proxies,    # 此处加代理方便前期fiddler调试
            data=multipart_encoder,
            verify=False)
print(res1.text)


# 若post还有其他参数,则采用以下方式
files = {
            'checksum': (None, 'checksum'),  # 此项为文件校验和
            '其他key': (None, '其他value'),
            'chunks': (None, '1'),
            'chunk': (None, '0'),
            'user_package_file': (
                'imei-MD5.txt', open('D:\spiderman2\crawlframe\spiders\imei-MD5.txt', 'rb'),
                'text/plain')
        }
data = {
    'key': 'value'
}

res2 = requests.post('your url', data=data, files=files, headers=headers, verify=False)
print(res2.text)
