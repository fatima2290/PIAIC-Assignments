name = input('Enter your name: ')
num1 = int(input('Enter your 1st favorite number: '))
num2 = int(input('Enter your 2nd favorite number: '))
num3 = int(input('Enter your 3rd favorite number: '))
print(f'\nHey {name}! Lets\'s explore your favorite numbers.')
numbers = [num1, num2, num3]

tuple_list = []
square_list = []

def even_odd(number):
    if number % 2 == 0:
        tup = (f'The number {number} is even')
    else:
        tup = (f'The number {number} is odd')
    tuple_list.append(tup)

def square(number):
    sq_tup = (number, number**2)
    square_list.append(f'The number {number} and its square: {sq_tup}')

for i in numbers:
    even_odd(i)
    square(i)

for i in tuple_list:
    print(i)
for i in square_list:
    print(i)

sum =num1+num2+num3
print('\nAmazing! The sum of your favorite numbers is: ',sum)
factors = []

for i in range(1, sum+1):
    if sum % i == 0:
        factors.append(i)

if len(factors) == 2:
    print(f'Wow {sum} is a prime number!')
else:
    print(f'Wow {sum} is a composite number!')