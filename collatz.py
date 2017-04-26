def collatz(number):
    if number % 2 == 0:
        print(int(number // 2))
    else:
        print(int(3 * number + 1))

print('Hello navegator! Type a number of your choice: ')
number = int(input())
collatz(number)


