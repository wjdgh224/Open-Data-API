//[1]:JSON객체 -> 중괄호{}사용.
//JSON에서 객체란? -> key:value의 한 쌍으로 이루어진 정렬되지 않은 속성의 집합.
//콤마로 구분하여 여러개의 속성가짐.
//문자열은 반드시 큰따옴표.
{
	"name":"홍길동",
	"age":20,
	"nationality":"대한민국",
	"hobby":"영화보기"
}

//[2]:객체안의 객체 -> 계층적 구조.
{
	"group1":{
			"name":"홍길동",
		"age":20,
		"nationality":"대한민국",
		"hobby":"영화보기",
		"company":{
			"cname":"XX원자력 발전소",
			"cphone":"02-1234-5678",
			"caddress":"경기도 용인시 용인동"
		}
	}
}

//[3]:JSON배열 -> 대괄호 사용.
//콤마로 여러 객체 추가 및 구분.
"person":[
	{"name":"홍길동", "age":20, "nationality":"한국"},
	{"name":"이순신", "age":30, "nationality":"미국"},
	{"name":"강감찬", "age":40, "nationality":"영국"}
]