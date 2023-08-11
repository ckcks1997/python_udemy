import datetime
import time

#with 함수는 스코프를 생성하지 않습니다.
with open("files/todos.txt") as file:
    something = file.read()

print(something) #출력됨

someday = time.strftime('%Y-%m-%d', time.localtime(time.time()))
with open("files/hello.txt", "w") as file:
    file.writelines(someday)