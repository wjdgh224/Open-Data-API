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
print(type(response.text)) #str
print('-'*120)


#공공데이터 포털로 부터 제공받은 JSON데이터에서 원하는 값들만 출력
jsonObj = json.loads(response.text)
print(jsonObj)
print(type(jsonObj)) #dict

#jsonRes = jsonObj.get('response')
#jsonBody = jsonRes.get('body')
jsonItems = jsonObj.get('items')
jsonItem = jsonItems.get('item')

#반복문 1-CSV파일 저장X
# for item in jsonItem:
    # print(item)
    # print(item.get('sido_sgg_nm'),",",item.get('spot_nm')) #f문자열을 사용하면 콤마 사이의 간격을 없앨 수 있다.
    # print(f'{item.get("sido_sgg_nm")}, {item.get("spot_nm")}')
    
#반복문 2 - CSV파일 저장
#CSV파일로 저장하기 위하여 쓰기모드(W)로 열어준다.
f = open('apijson.csv', 'w')

#헤더 추가하기 --> 콤마(,) 띄어쓰기는 안해주는거 좋다. --> 벌려짐
f.write('지역구,사고지역' + '\n')

#파일에 쓰기
for item in jsonItem:
    print(f'{item.get("sido_sgg_nm")}, {item.get("spot_nm")}')
    f.write(item.get('sido_sgg_nm')+","+item.get('spot_nm')+'\n')
    
#처리가 끝났으면 닫아준다. --> 반복문 밖에서
f.close()






