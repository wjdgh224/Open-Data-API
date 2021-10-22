#파이썬에서의 JSON데잍 ㅓ처리

#[1]
#JSON데이터 처리란?
#클라이언트와 서버사이에서 데이터를 교환시 파이썬의 객체 타입을 문자열 데이터로 또는 문자열 데이터를 파이썬의 객체 타입으로 변환.
#파이썬의 대표적인 자료구조 4개 --> List, Tuple, Dictionary, Set

#[2]
#파이썬 딕셔너리 타입이란?
#파이썬 자료구조의 한 형태. "키(key):값(value)"쌍을 요소로 갖는 컬렌션 객체.
#키(key)를 통하여 빠르게 값(value)을 찾아내는 해시테이블(Hash Table)구조를 가지는 객체. 
#파이썬에서 딕셔너리 객체는 "dict"클래스 구현되어 있음.
#딕셔너리의 키(key)는 값을 변경할 수 없다.-->즉, Immutable(숫자, 스트링, 문자열, 튜플())속성.
#딕셔너리의 값(value)은 둘 다 가능 -->즉, Immutable, Mutable(set{}, list[], dict{:})모두 가능.
a = {'name':'홍길동'}
#a = {{1,2}:'홍길동'}
#a = {[1,2]:'홍길동'}
#a = {{1:2}:'홍길동'}
print(a)
print(type(a))
print(type(a['name']))

b=list(a)
print(b)
print(type(b)) #list
print(b[0]) #name
print(type(b[0]))

#딕셔너리 빈 요소는 --> {}
#딕셔너리 키 인덱스 --> 딕셔너리명['키'] --> 키를 인덱스처럼 사용.(주의:f문자열 사용시는 따옴표 주의!)

#[3]
#파이썬에서 제공하는 JSON 기본 묘듈이란?
#파이썬은 기본적으로 JSON데이터를 효율적을 다루는 JSON모듈을 제공한다.(그냥 import json해서 사용)
#가급적 3.x대 이상의 버전을 사용할 것.
#결론 --> json묘듈을 사용하면 JSON데이터를 아주 편리하게 객체에서 문자열로, 문자열을 객체로 변환시킬 수 있다.


#[4] 실습
import json

#파이썬 딕셔너리 타입
members = {
    'id':1004,
    'name':'Json Kim',
    'age':22,
    'email':'jsonkim@test.com',
    'logdata':[
        {'data':'2010-01-13', 'device':'pc(windows os)'},
        {'data':'2010-10-24', 'device':'mobile'},
        {'data':'2010-12-31', 'device':'pc(mac os)'}
    ]
}

print('-'*120)
print(members)
print(type(members)) #dict

#JSON문자열로 변환
jsonStr = json.dumps(members)

#문자열 출력
print(jsonStr)
print(type(jsonStr))