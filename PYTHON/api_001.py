#공공데이터 API 사용을 위한 파이썬 라이브러리


#[1]Url Encode
#공공데이터 이용을 위해 HTTP요청을 할때(GET) URL에는 쿼리 파라미터 값들이 붙게 된다.
#이 파라미터에 한글이 포함된다면?-->URL 아스키(ASCII)코드값만 사용이 가능하기 때문에 URL인코딩을 해줘야 한다.
#API호출시 파라미터에 한글 값 그대로를 사용해도 되는 경우도 있지만, 가급적 URL인코딩을 통해 전송하는 것을 권장.
#이때, 사용되는 유용한 파이썬 라이브러리가 urllib라는 패키지가 있다. --> 파이썬 자체 내장
#결론, urllib를 사용해서 URL인코딩 미 URL관련 처리 작업들을 유연하게 처리할 수 있다.

#[2]urllib
from urllib.parse import urlparse, urlunparse, parse_qs, parse_qsl, urlencode

url = urlparse('https://google.com:80/subpage/search.google?name=홍길동&password=1234#id001')
#urlparse메서드 --> URL을 6개의 요소로 분석하여 반환 --> 명명된 튜플(namedtuple) --> ParseResult의 객체라고 생각하면 됨.
#urllib.parse.ParseResult객체를 통해서 URL의 여러 값을 분석-->URL의 일반적인 구조라고 생각
#namedtuple이므로 인덱스로 접근하거나 또는 속성명으로 요소에 접근하는 것이 가능.
#namedtuple특성상-->immutable

#6개의 반환 값
print(url.scheme) #https (통신방식)
print(url.netloc) #google.com:80 (서버주소)
print(url.port) #80(포트번호 - 서버 프로세스를 구분, 80번 포트는 생략이 가능하여 생략시 80포트로 전송)
print(url.path) #/subpage/search.google (서버상의 도큐먼트 위치)
print(url.params) #
print(url.query) #name=홍길동&password=1234 (추가정보)
print(url.fragment) #id001 (식별자)

#url--> 위 요소를 모두 출력
print(url) #ParseResult

#ParseResult객체를 다시 URL로 만들고자 한다면?-->geturl() 또는 urlunparse()메서드 사용.
#urlunparse()사용법 주의-->url객체를 괄호안에 넣어줌.
print('-'*120)
print(url.geturl())

print('-'*120)
print(urlunparse(url))

#namedtuple이므로 인덱스 접근이 가능. for문 사용도 가능
print('-'*120)
print('url[0]:', url[0]) #https
print('url[1]:', url.netloc) #

for value in url:
    print(value)


#[3]parse_qs
#qs-->query string
#쿼리 스트링이 문자열 형태로 이뤄져 있는데 값의 변경이나 분리를 용이하게 해주는 함수들이 있는데-->parse_qs(), parse_qsl()
#사용을 위해서는 상단에서 import를 먼저 해준다.
#둘의 차이점은 반환 타입이 다르다는 것 --> 딕셔너리, 리스트
#parse_qs는 key에 대해 value들을 리스트로 묶어준 후-->딕셔너리로 반환.
print('-'*120)
print(url.query)
qs = parse_qs(url.query)
print(qs, type(qs)) #딕셔너리

qsl = parse_qsl(url.query)
print(qsl, type(qsl), type(qsl[0])) #리스트 --> 안쪽 요소의 타입은 튜플


#[4]urllib.parse를 이용하여 password변경해보기
print('-'*120)
test_qs = dict(parse_qsl(url.query))
print(test_qs)

test_qs['password']='5678'
print(test_qs)

test_url = url._replace(query=urlencode(test_qs))
print(test_url)

new_url = urlunparse(test_url)
print(new_url)



