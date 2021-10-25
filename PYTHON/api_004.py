#공공데이터 API를 이용하여 제공받은 JSON데이터를 CSV파일로 저장하기

from urllib.parse import urlencode, unquote
import requests
import json

url = 'http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking'

queryString = '?' + urlencode(
    {
        'ServiceKey':unquote('VBi2NmffUZqPs%2BbDL9USamWvoO%2Fs6IoEGSHftuGLhpTiFRS1Yuh%2F5K5zrmi3r19ElrYfOzJf1HZgeY8xFYTFVQ%3D%3D'),
        'searchYearCd':'2017',
        'siDo':'11',
        'guGun':'680',
        'type':'json',
        'numOfRows':'10',
        'pageNo':'1'
    }
)

queryURL = url + queryString
print(queryURL)

response = requests.get(queryURL)

print('-'*120)
print(response.text)
# print(type(response.text)) #str
print('-'*120)


#공공데이터 포털로 부터 제공받은 JSON데이터에서 원하는 값들만 출력


