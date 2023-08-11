# Python 기초 from udemy

## 7/23 <br>

### day1/2 수강
#### 배운점:
- 파이썬은 변수 선언할 때 그냥 이름만 쓰면 된다.
- input()을 불러올 때 아무것도 import 안 해도 된다.
- True/False 첫글자는 대문자다.
- python console에 help(something)을 하면 간단한 설명이 나온다.

### 7/24

#### 배운점:
- switch문은 match-case문으로 표현된다.
- trim()은 strip()이다.
- iterator 반복은 `for x in arr`로 표현한다.
- String 관련 기능 중 title()을 하면 첫 글자가 대문자가 된다.
- dir(list)같은걸 할 때 __sth__ 처럼 underscore가 2개 붙은것이 있는데,<br> 
이는 파이썬이 내부적으로 쓰는 메소드이다. (인터프리터가 해석할 때 사용)
- list [] tuple ()

## 7/29, 30
#### 배운점:for-loop, enumerate, zip
-  for문에 enumerate를 써서 index를 받을 수 있다.(for-loop)
- ``` 
  for index, item in enumerate(todos):
      row = f"{index+1}.{item.capitalize()}"
      print(row)
  ```
  
- 파일 위치를 나타낼때 경로 separator에 \를 쓴다면
open(r"c:\Users...", "w") 와 같이 r을 붙이면 된다.

- 두개의 list를 하나의 for문 안에서 사용하려면 zip()을 이용한다.
```python
    contents = ["sample1" " add extra string", "sample2", "sample3"]
    
    filenames = ["doc.txt", "report.txt", "presentation.txt"]
    
    for content, filename in zip(contents, filenames):
        file = open(f"files/{filename}", 'w')
        file.write(content)
        file.close()
```

## 8/11
#### 배운점: with context manager, file read, readlines
- ```string.strip([문자])```: 원래 문자열의 시작과 끝에서 주어진 문자를 제거 <br>
- list comprehension: ```[ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]```
- ex)```arr = [i * 2 for i in range(size)]```

- with context manager: 사용하면 open 할 때 close 별도로 선언 안해줘도 됨.
- 또한, with는 스코프를 만드는 것이 아니기 때문에, with안에서 선언한 변수는 바깥 스코프 혹은 global 스코프가 된다.
```python
with open("files/doc.txt", "r") as file:
    some_str = file.read() #엔터를 \n으로 받고싶지 않으면 readlines() 사용
print(some_str) #출력가능
```
- 파일을 열고 쓸 수 있는 open()함수는 기본값이 "r"이다. 위에서 "r"은 생략 가능하다.
- 
