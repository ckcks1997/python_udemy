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
    some_str = file.read() #엔터를 \n으로 받고싶지 않으면 read() 사용
print(some_str) #출력가능
```
- 파일을 열고 쓸 수 있는 open()함수는 기본값이 "r"이다. 위에서 "r"은 생략 가능하다.

##### read() vs readlines()
-만약 다음과 같은 텍스트파일을 open하여 읽는다면
```text
hello
world
```
- read():
```text
hello
world
```
- readlines():
```text
['hello\n', 'world\n']
```
위와 같은 차이가 있다.

## 8/12
#### 배운점: try-except, function (def)

- try-catch는 파이썬에서 try-except 이다.
```python
 try:
...
  except IndexError:
...

```
- python의 function은 def로 정의한다.

```python
def greet():
    message="hello"
    new_message=message.capitalize()
    return new_message
```
function은 scope를 가지며, 해당 함수안의 변수는 외부에서 접근할 수 없다.


## 8/13
#### 배운점: function의 default parameter, local modules
- 파라미터에 기본값을 설정할 수 있다.
- default파라미터가 있는것과 없는것을 섞어쓰려면, 기본파라미터가 있는 값을 뒤에 쓴다.
```python
def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(filepath, todos_arg="hello"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
```

- 문자열을 보기 좋게 끊기위해서 \를 사용할 수 있다.
```python
str = "\
hello\
world"

print(str)  #helloworld
```

#### local modules
- 모듈을 가져오는 방법은 아래와 같이 두가지가 있다.
- 첫번째는 modules 패키지 안의 functions.py에서 바로 메소드를 가져오는 방식이며
- 두번째 방식은 py파일을 import하여 가져오는 방식이다.

```python
from modules.functions import get_todos, write_todos
from modules import functions

#두번째 방식은 아래와 같이 파일명을 명시하여 사용해야한다.
functions.write_todos(todos)
```

####  `__name__` : 
- 다른 모듈에서 import 하는 경우:
다른 모듈에서 import 되는 경우,
스크립트 파일의 이름이 모듈 이름으로 사용. 
이때 __main__은 현재 스크립트 파일의 이름이 아니라 모듈 이름이 된다.
<br>
- 직접 스크립트 파일을 실행하는 경우:
스크립트 파일이 직접 실행될 때는 __main__이라는 
 특별한 값이 생성되며, 이를 이용하여 스크립트 파일 내에서 
실행할 코드 블록을 지정할 수 있다.
```python
if __name__ == "__main__": #해당파일을 직접 실행한 경우
    print('main')
```

#### `__init__.py`: 패키지임을 알리는 역할을 하는 파일


## 8/14
#### 배운점: 다양한 standard modules(time, glob, csv, shutil, webbrowser, json)

#### time: 시간을 다루는 모듈
```python
import time
print(time.strftime("%m.%d.%y"))
```

- glob: 
- csv: csv파일을 로드하는 모듈
- shutil: 압축관련 모듈
```python
import shutil

# files 디렉토리의 파일을 zip파일로 output이라는 이름으로 생성
shutil.make_archive("output", "zip", "files")
```

- random: 랜덤값 생성 모듈
```python
import random

# Get two numbers from the user and covert them to integers
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Pick a random int using randrange()
rand = random.randrange(lower_bound, upper_bound + 1) # We add 1 to upper_bound because randrange does not include the upper_bound number.

print(rand)
```

## 8/15
#### 배운 점: PySimpleGUI
- day16 패키지 참고


## 9/2
#### 배운 점: class(공부중..)
- class 이름은 Pascal case로.
- class 안에 정의된 def는 function이 아니라 method라고 한다.
- method는 파라미터로 self가 있어야 한다.
- 클래스 안에 def __init__(self)를 선언하면 생성자 역할을 한다.
- 예시:
```python
import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] == "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        if df.loc[df["id"] == self.hotel_id, "available"].squeeze() == "yes":
            return True
        else:
            return False
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj
    def generate(self):
        content = f"""
            Thank you,
            Name: {self.customer_name}
            Hotel:{self.hotel_obj.name}
        """
        return content

print(df)
hotel_id = input("enter id of the hotel")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("enter name:")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("hotel is not free")
```
- 호텔 예약을 하는 코드이다.
- 클래스 안의 인스턴스 변수는 self를 통해 정의하고 저장한다. 위 예제에서는 __init__ 메서드 안에서 인스턴스 변수를 선언하였는데, __init__안에서만 선언 가능한 것은 아니고 다른 매서드에서도 self를 통해 선언 가능하나..
```python
class A:
    def __init__(self):
        self.x = 1

    def call1(self):
        self.y = 2


a = A()
print(a.x)
#print(a.y) //오류
a.call1()
print(a.y)

```
- 위와 같이 call1()을 호출하기 전 아직 선언되지 않은 y값을 조회하려고 하면 AttributeError 오류가 발생한다.
- 이외의 전체적인 개념은 자바와 매우 유사한 느낌..

