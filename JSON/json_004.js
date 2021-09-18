//[1]:중첩데이터
window.onload = () => {
	const book = {
		"isbn":"123-456-789",
		"author":{
			"name":"홍길동",
			"email":"hong@naver.com"
		},
		"editor":{
			"name":"이순신",
			"email":"lee@naver.com"
		},
		"title":"대한민국의 정의는 죽었는가?",
		"category":[
		"Non-Fiction", "IT", "Politics"
		]
	}

	console.log(book["author"].name);
	console.log(book["editor"].name);
	console.log(book["isbn"]);
	console.log(book.sibn);
	console.log(book.title);
	console.log(book.category);
	console.log(book.author);

	//개별 엑세스
	let val ="";
	// val = book.category[0];
	// document.getElementById("aaa").innerText = val;
	
	//반목문을 이용한 엑세스
	//for
	for(let i=0; i<book.category.length; i++) {
		//val += book.category[i] + "<br>";
		val += `${book["category"][i]}<br>`;
	}
	document.getElementById("aaa").innerHTML = val;
	
	//for .. in
	for(let i in book.category) {
		val += book.category[i] + "<br>";
	}
	document.getElementById("aaa").innerHTML = val;
	
	//for .. of
	for(let value of book.category) {
		val += value + "<br>";
	}
	document.getElementById("aaa").innerHTML = val;
};


