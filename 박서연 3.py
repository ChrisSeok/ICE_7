#3번문제. C111061 박서연 

string = str(input("문자열을 입력하시오: "))
numbers = ''

nb2 = ['A', 'B', 'C']
nb3 = ['D', 'E', 'F']
nb4 = ['G', 'H', 'I']
nb5 = ['J', 'K', 'L']
nb6 = ['M', 'N', 'O']
nb7 = ['P', 'Q', 'R', 'S']
nb8 = ['T', 'U', 'V']
nb9 = ['W', 'X', 'Y', 'Z']

for i in range(len(string)):
    if string[i] in nb2:
        numbers = numbers + '2'
    if string[i] in nb3:
        numbers = numbers + '3'
    if string[i] in nb4:
        numbers = numbers + '4'
    if string[i] in nb5:
        numbers = numbers + '5'
    if string[i] in nb6:
        numbers = numbers + '6'
    if string[i] in nb7:
        numbers = numbers + '7'
    if string[i] in nb8:
        numbers = numbers + '8'
    if string[i] in nb9:
        numbers = numbers + '9'

print(numbers)