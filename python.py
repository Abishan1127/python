# x=10
# x=4
# if x>5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")
# for i in range(1,10):
#     print(i)
# y=9
# while y > 0:
#     print(y)
#     y = y - 1
# for i in range(10,0,-1):
#     print(i)
# def greet(name):
#     print("hello",name)

# greet("sachin")
# 1. Write a Python program that prints the numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number, 
# and for multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".

# def fizz_buzz():
#     for i in range(1, 51):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# 2. Write a Python function that checks whether a given number is even or odd.

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # 3. Write a Python program to find all the prime numbers between 1 and 100.

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def find_primes():
#     primes = [x for x in range(1, 101) if is_prime(x)]
#     print(primes)



# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(5))
squareList = []
for i in range(10):
    square = i**2
    squareList.append(square)
    
    
print(squareList)
