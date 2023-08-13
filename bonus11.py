def get_average():
    with open("files/num.txt", 'r') as file:
        data = file.readlines()[1:]

    values = data[1:]
    values = [float(i) for i in values] #\n은 자동으로 무시된다.

    average_local = sum(values) / len(values) #SQL문 짜듯 합을 구하는데 반복문 필요없다..

    return average_local


average = get_average()
print(average)