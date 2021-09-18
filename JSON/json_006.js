//Parsing -> 다른 형식으로 저장된 데이터를 목적에 맞는 형태의 형식으로 변환.
//JSON Parsing -> JSON 형식의 텍스트 문자열을 목적에 맞게 객체로 변환.

window.onload=()=>{
	
	document.getElementById('btn').addEventListener('click', function(){
		console.log('test..');
		//----------------------------------------------------------------------
		let json = {
			"book":[{
				"isbn":"123-456-789",
				"author":{
					"name":"홍길동",
					"email":"hong@naver.com"
				},
				"editor":{
					"name":"이순신",
					"email":"lee@naver.com"
				},
				"title":"대한민국의 정이는 죽었는가?",
				"category":[
					"Non-Fiction", "IT", "Politics"
				],
				"description":"백두산 저자의 신작",
				"comments":[{
						"name":"정인봉",
						"text":"정의에 대해서..."
				},
				{
						"name":"김진경",
						"text":"나는 경기도 안양의 김진경이다..."
				},
				{
						"name":"홍수범",
						"text":"앙기모띠..."
				},
				{
						"name":"이정길",
						"text":"정봉이..."
				},
				{
						"name":"신재원",
						"text":"심재원..."
				}],
				"comwinner":["김진경", "이정길", "신재원"],
				"add1":false,
				"add2":true
			}]
		}
		json = json["book"]
		console.log(json.length);
		console.log(json);
		console.log(json[0].isbn);
		console.log(json[0].editor);
		console.log(json[0].category);
		console.log(json[0].comments);
		console.log(json[0].comments[0]);
		console.log(json[0].comments.length);
		console.log(json[0].comments[json[0].comments.length-1]);

		console.log('------------------------------------------------------');
		for(let i=0; i<json.length; i++) {
			console.log(json[i].comments);
			console.log(json[i].comwinner);
		}
		
		console.log('----------------------------------------');
		//ul태그 노드 생성
		let ul = document.createElement('ul');
		let bookList = document.getElementById('bookList');
		bookList.appendChild(ul);

		for(let i=0; i<json.length; i++) {
			for(let j=0; j<json[i].comments.length; j++) {
				
				//댓글 참가자
				let bookComments = json[i].comments[j];
				console.log(bookComments.name + ":" + bookComments.text);
				
				//##################################################
				//li태그 노드 생성
				let li = document.createElement('li');
				
				//텍스트노드생성
				let txtNode = document.createTextNode(bookComments.name + ":" + bookComments.text);
				li.appendChild(txtNode);
				ul.appendChild(li);
				
				//리스트에 붙이기
				bookList.appendChild(ul);
				//##################################################
				 
			}
			//당첨자
			console.log(json[i].comwinner.join(", "));//배열을 문자열 형식으로...
			document.getElementById('bookListWinner').innerHTML = json[i].comwinner.join(", ");
		}
		//--------------------------------------------------------------------
	});
};