headers={"X-OverrideGateway":"140.237.30.217:15272","Connection":"keep-alive","Sec-Fetch-Mode":"cors","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36","Content-Type":"application/x-www-form-urlencoded","Accept":"*/*","Origin":"https://ad.oceanengine.com","Sec-Fetch-Site":"cross-site","Referer":"https://ad.oceanengine.com/pages/login/index.html","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9"}
import requests
# proxy={"http":"http://125.117.215.54:21188","https":"http://125.117.215.54:21188"}
data={"a":"a"}
session=requests.session()
session.cookies.clear()
# session.proxies={"http":"http://127.0.0.1:8888","https":"http://127.0.0.1:8888"}
url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=sadf&oq=sadf&rsv_pq=ad675a8700003062&rsv_t=6186TwGqWa088D2Icmh%2BiHR6W7nOj3hJCEbeJkgQjd91F0uzaT%2FrQjzuY68&rqlang=cn&rsv_enter=0&rsv_dl=tb&prefixsug=sadf&rsp=0"

global n
from requests_toolbelt.utils.dump import PrefixSettings, _get_proxy_information, _coerce_to_bytes, HTTP_VERSIONS, \
    _format_header, _build_request_path
import requests
# from requests_toolbelt.utils import dump
from requests import compat
import time
# resp = requests.get('https://www.sina.com.cn/',headers=headers,data=data)
# print(resp.request.Response)
def dump_all(response, request_prefix=b'', response_prefix=b'',n=0):

    data = bytearray()
    history = list(response.history[:])
    history.append(response)

    for response in history:
        dump_response(response, request_prefix, response_prefix,n=n)

    time.sleep(1)
    return data

def dump_response(response, request_prefix=b'', response_prefix=b'',data_array=None,data1_array=None,n=0):
    data = data_array if data_array is not None else bytearray()
    data1 = data1_array if data_array is not None else bytearray()
    prefixes = PrefixSettings(request_prefix, response_prefix)
    if not hasattr(response, 'request'):
        raise ValueError('Response has no associated request')

    proxy_info = _get_proxy_information(response)
    _dump_request_data_only(response.request, prefixes, data,
                       proxy_info=proxy_info,n=n)
    _dump_response_data_only(response, prefixes, data1,n=n)
    return data,data1

def _dump_request_data_only(request, prefixes, bytearr, proxy_info=None,n=0):
    if proxy_info is None:
        proxy_info = {}

    prefix = bytes(prefixes.request)
    method = _coerce_to_bytes(proxy_info.pop('method', request.method))
    request_path, uri = _build_request_path(request.url, proxy_info)

    # <prefix><METHOD> <request-path> HTTP/1.1

    bytearr.extend(prefix + method + b'' + request_path + b' HTTP/1.1\r\n')

    # <prefix>Host: <request-host> OR host header specified by user
    headers = request.headers.copy()
    host_header = _coerce_to_bytes(headers.pop('Host', uri.netloc))
    bytearr.extend(prefix + b'Host: ' + host_header + b'\r\n')

    for name, value in headers.items():
        bytearr.extend(prefix + _format_header(name, value))

    bytearr.extend(prefix + b'\r\n')
    if request.body:
        if isinstance(request.body, compat.basestring):
            bytearr.extend(prefix + _coerce_to_bytes(request.body))
        else:
            bytearr.extend(b'<< Request body is not a string-like type >>')
    bytearr.extend(b'\r\n')
    txt=bytearr.decode("utf-8")
    with open(r"D:\spiderman2\crawlframe\txts\/" + str(n) + r"_c.txt", "wb") as f:
        f.write(bytearr)

def _dump_response_data_only(response, prefixes, bytearr,n=0):
    prefix = prefixes.response
    # Let's interact almost entirely with urllib3's response
    raw = response.raw

    # Let's convert the version int from httplib to bytes
    version_str = HTTP_VERSIONS.get(raw.version, b'?')

    # <prefix>HTTP/<version_str> <status_code> <reason>
    bytearr.extend(prefix + b'HTTP/' + version_str + b' ' +
                   str(raw.status).encode('ascii') + b' ' +
                   _coerce_to_bytes(response.reason) + b'\r\n')

    headers = raw.headers
    for name in headers.keys():
        for value in headers.getlist(name):
            bytearr.extend(prefix + _format_header(name, value))
    bytearr.extend(prefix + b'\r\n')
    bytearr.extend(response.content)
    t = str(int(time.time()))
    # print("type---111",bytearr.decode("utf-8"))
    with open(r"D:\spiderman2\crawlframe\txts\/"+str(n)+"_s.txt", "wb") as f:
        f.write(bytearr)

# data = dump_all(resp,n=1)
# print(data.decode('utf-8'))
# print(type(data.decode('utf-8')))

if __name__ == '__main__':
    with open("../txts/str(1)"+"_s.txt", "w") as f:
        f.write("a")