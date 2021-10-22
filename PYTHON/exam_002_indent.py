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

#JSON문자열로 변환
jsonStr = json.dumps(members, indent=4)

#문자열 출력
print(jsonStr)
print(type(jsonStr))
