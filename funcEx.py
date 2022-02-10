# def add_calc(number1, number2):
 #   answer = number1 + number2
  #  return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

# num1 = 18
# num2 = 50
# num3 = 2

# lst = [num1, num2, num3]

# if (num1 >=num2,num3):
#     largest = num1
# elif (num2 >= num1,num3):
#     largest = num2
# else:
#     largest = num3

# print("The largest of the 3 numbers is : ", max(lst))

# num1 = 10
# num2 = 2
# num3 = 5

# lst = [num1, num2, num3]
# total = 1
# for x in lst:
#     total= total*x

# print(total)


# def reverse(itr):
#   return itr[::-1]

# str1 = '1234abcd'
# print("Original string:",str1)
# print("Reverse string:",reverse('1234abcd'))
# str1 = 'reverse'
# print("\nOriginal string:",str1)
# print("Reverse string:",reverse(str1))


# def string_test(x):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in x:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", x)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('he Loud child woKe UP his slEEping DoG')

from unicodedata import name


def increment(number, by):
    return number + by

print(increment(2,by=1))
