# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#        total *=number
#     return total


# print(multiply(2,3,4,5))


# def save_user(**user):
#     print(user["name"])
    

# save_user(id=1, name="Ainsley", age=35)




def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return  "Buzz"
 
    return input
  

input()
