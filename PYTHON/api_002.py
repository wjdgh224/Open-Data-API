#urlencode와 deseq 옵션 사용
#쿼리스트링 파라미터를 Encoding 하기 위해서-->urlencode()메서드 사용.
#인코딩된 쿼리스트링은 문자열로 반환-->str
#doseq옵션-->하나의 key에 여러개의 value가 존재할 때, 이를 각각의 쌍으로 분리할지 결정.(T/F)
#기본값은 F-->만약 doseq=False이고, 하나의 key에 여러개의 value가 존재-->이들 value를 문자열로 인식.
#반대로 True로 지정된 경우-->하나의 key에 여러 개의 값이 존재하는 것으로 처리.

print('-'*120)
from urllib.parse import urlparse, urlunparse, parse_qs, parse_qsl, urlencode

url = urlparse('https://google.com:80/search.google?name=홍길동&password=1234')

qs = parse_qs(url.query)
print(qs) #타입-->딕셔너리

result1 = urlencode(qs)
print('result1:', result1, type(result1)) #타입-->str, dosep기본값 --> F

result2 = urlencode(qs, doseq=True)
print('result2:', result2)

print('-'*120)

params = {'aaa':'111', 'bbb':['222','333']}

rst1 = urlencode(params)
rst2 = urlencode(params, doseq=True)

print('rst1:',rst1)
print('rst2:',rst2)





