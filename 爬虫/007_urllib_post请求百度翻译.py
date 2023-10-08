import urllib.request
import urllib.parse

# post请求的特点是请求参数不能凭借到url中

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    # 这必须加cookie,不加cookie真不行啦
    'cookie':'BIDUPSID=20B48AA69066FECFB975482140CC6C45; PSTM=1692975106; BAIDUID=20B48AA69066FECF934B15B17EDBCE81:FG=1; BD_UPN=12314753; H_WISE_SIDS=110085_268592_259642_256151_269832_269904_270604_271035_271022_271171_271177_267659_271323_270102_271562_271188_272223_272279_272008_272455_269729_271689_272821_273094_273161_273121_273301_270055_273704_273734_274177_269610_273917_274234_273043_272806_272560_272802_188331; H_WISE_SIDS_BFESS=110085_268592_259642_256151_269832_269904_270604_271035_271022_271171_271177_267659_271323_270102_271562_271188_272223_272279_272008_272455_269729_271689_272821_273094_273161_273121_273301_270055_273704_273734_274177_269610_273917_274234_273043_272806_272560_272802_188331; BAIDUID_BFESS=20B48AA69066FECF934B15B17EDBCE81:FG=1; ZFY=TqDMr4CQ1E3qObSoDd5ZpZzs2dlnQb6WS4jfek09Yz4:C; BDUSS=ktsbmgxRGM4eVlPOTRoT243MDBXYk9JVW5OfnpIfmQyVk1GZ201bW1vSmpJa0psRVFBQUFBJCQAAAAAAAAAAAEAAAAnaTy8bm1jdmLM7NCrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGOVGmVjlRplR; BDUSS_BFESS=ktsbmgxRGM4eVlPOTRoT243MDBXYk9JVW5OfnpIfmQyVk1GZ201bW1vSmpJa0psRVFBQUFBJCQAAAAAAAAAAAEAAAAnaTy8bm1jdmLM7NCrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGOVGmVjlRplR; BA_HECTOR=20a5a0a4200la0al2g858ka31ihnq5c1o; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=2; delPer=0; COOKIE_SESSION=1152360_1_4_4_17_12_0_0_4_4_3_4_1292665_0_10_0_1696331977_1695037978_1696331967%7C9%23105792_16_1695037963%7C9; ab_sr=1.0.1_ZjU3MzFkNWZkYzk3MmEwYTljYmYyNTU0NmQ0ZWM2YzQ2ZWQ0YWQ5ZTdlY2UzZmEzMjI5OWJlZTMyYmUxOWRiYTJhMTFkYmVkNmVkNTBjZDdjOWY1OWRiNWFjMDAwMTkxYjQ1NmIzZWQwZTg4YjBmYTA1MTQzZDc5ZTRmYmRkNzE2MDFiODk5OWZiNDQ5MjU3OWYyMmY3YmJmYmM5OTdhZA==; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; B64_BOT=1; H_PS_PSSID=26350; H_PS_645EC=67f4xc91orAdYSXlMs79uvmcu2dWFH6ZHzDvDhWM80IxpmIAkG51W1C%2FneY0DaFGoUIb0WqONRc; BDORZ=FFFB88E999055A3F8A630C64834BD6D0'
}

data = {
    'kw':'spider'
}

# post请求的参数必须要进行二次编码
data = urllib.parse.urlencode(data).encode("utf-8")

# post的请求的参数 是不会拼接在url的后面的  而是需要放在请求对象定制的参数中
# post请求的参数 必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')

import json

obj = json.loads(content)
print(obj)

"""
总结：
# post请求方式的参数 必须编码   data = urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中  request = urllib.request.Request(url=url,data=data,headers=headers)
"""