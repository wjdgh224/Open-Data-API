//[1]:데이터
const person = [
	'{"name":"홍길동", "age":20, "nationality":"대한민국"}',//string
	{"name":"이순신", "age":30, "nationality":"미국"},
	{"name":"강감찬", "age":40, "nationality":"영국"},
	{"name":"을지문덕", "age":50, "nationality":"프랑스"}
];

console.log(typeof person[0]);//string
console.log(typeof person[1]);//object

//[2]:출력
console.log('--------------------------------------------------');
console.log(person[1].name + "" + person[1].age + "" + person[1].nationality);

//[3]:반복
console.log('--------------------------------------------------');
console.log(...person);//전개 연산자
const str1 = 'kor';
console.log([...str1]);//proto(원형) -> array
console.log({...str1});//proto -> object

console.log([...person]);//proto -> array
console.log([...person].length);//proto -> array
console.log([...person][1].name);//proto -> array

console.log({...person});//proto -> object
console.log({...person}.length);//객체는 한덩어리 이기에 안됨.
console.log({...person}[1].name);//proto -> object

//[4]:반복 가능한 객체 -> for...of, ...(전개 연산자)
console.log('--------------------------------------------------');
for(let ele of person) {//person -> iterable, 반복가능한 객체 = 배열, 문자열
	console.log(ele);	
}

console.log('--------------------------------------------------');
for(let i in person[1]) {//0, 1, 2, 3 ; 객체오면 key 리턴
	console.log(i);	
}


//[5]:수정
console.log('--------------------------------------------------');
person[1].name = "이순자";
person[1].age = 22;
console.log(`이순신의 이름이 ${person[1].name}로 수정되었고, 나이는 ${person[1].age}살로 수정되었습니다.`);//출력