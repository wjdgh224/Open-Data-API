//JSON.parse()객체로,JSON.stringify()문자열로 -> classfiy:분류하다
//[1]:JSON.parse(jsonText) -> JSON형식의 텍스트를 자바스크립트객체
let jsonText = '{"name":"홍길동", "age":20, "nationality":"대한민국"}';

console.log("변환전->" + typeof jsonText);
const jsonObj = JSON.parse(jsonText);
console.log("변환후->" + typeof jsonObj);


console.log('-------------------------------------------');
console.log(jsonObj.name);
console.log(jsonObj.age);
console.log(jsonObj.nationality);

console.log(jsonObj.name + " " + jsonObj.age + " " + jsonObj.nationality);
console.log(`이름과 나이는 ${jsonObj.name}(${jsonObj.age})이며, 국적은 ${jsonObj.nationality}이다.`);

//[2]:JSON.stringify(dataObj) -> 데이터 객체를 JSON형식의 텍스트
console.log('-------------------------------------------');
const jsonStr = JSON.stringify(jsonObj);

console.log(jsonStr);
console.log(typeof jsonStr);