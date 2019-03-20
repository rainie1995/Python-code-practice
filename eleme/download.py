import json
import sys
url = "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wtsqqgktcrfk&latitude=32.055015&limit=24&longitude=118.77943&offset=120&terminal=web"
headers = {"Host":"www.ele.me",
           "Connection":"keep-alive",
           "upgrade-Insecure-Requests":"1",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Language":"zh-CN,zh;q=0.9",
           "Cookie":"ubt_ssid=dt0siq45l16a6d2m57d89nbe1bl39w7e_2019-01-27; _utrace=9c68b2055acb9dee0e1ae980753dfd8f_2019-01-27; cna=VBCRFOKZISICAdOiUWYtQzeE; UTUSER=1017635562; pizza7567632f76312f72=5eFWeKtCzB8Xq1BRbIlWwmQEk8Tj8uc35UGobBUlPcYlnkFQlmrV4qlty_Bf_IuU; eleme__ele_me=265fe10d957c506bbb583be441b23a09%3A8dcc4b5c03bd23ad9165b2be8211df18a4968b56; track_id=1548574127|56245b84bf99cf3eb468582a94bb949a92dded9022da962643|b4f16fdfcbf5caadce1bee2d82d0363f; USERID=1017635562; SID=hvj6SOuzdM7A6Q7WRmWCj47vtwawaPLcxzFg; isg=BNPTArtHi7e220djKG2cF_emYldRmx-O85C0FYXwq_IpBPemHFpUm211O3Rqlr9C; pizza73686f7070696e67=CPuz42fVoxnRVcVQ1x33ff-cG5MxyH3YL9F8thM7HvtEwg88F0pDOJXunrWc5ega"}        
response = requests.get(url,headers = headers)
data = json.loads(response.text)
output = sys.stdout
outputfile = open("download3.txt","w",encoding='utf-8')
sys.stdout = outputfile
for item in data:
    print(item['id'], item['name'])
outputfile.close()
sys.stdout = output