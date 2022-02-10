#devs_money = 100
#dev_can_play_smash = False


#if devs_money > 10 and dev_can_play_smash:
#    print("Dev enters a smash tournament!")
#elif devs_money < 10 and dev_can_play_smash:
 #   print("Dev is too poor to enter")
#else:
#    print("Dev just can't play smash")


# Mark = int(input("what grade did i recieve "))
# if Mark >=85:
#     print("distinction")
# elif Mark==65 or Mark >65:
#     print ("pass")
# elif Mark <85:
#     print ("pass")
# else Mark <65:
#     print ("fail")

# Mark = int(input("what grade did i recieve "))
# def determine_grade(scores):
#     if scores >= 90 and <= 100:
#         return 'A'
#     elif scores >= 80 and <= 89:
#         return 'B'
#     elif scores >= 70 and <= 79:
#         return 'C'
#     elif scores >= 60 and <= 69:
#         return 'D'
#     elif scores >= 50 and <= 59:
#         return 'E'
#     else:
#         return 'F'

# scores = int(input("what grade did i recieve "))

# if scores >95:
#     print ("Distinction")
# elif scores >= 90 and scores <= 95:
#     print ('A')
# elif scores >= 80:
#     print('B')
# elif scores >= 70:
#     print ('C')
# elif scores >= 60:
#     print ('D')
# elif scores >= 50:
#     print ('E')
# else:
#     print ('F')

mark = int(input("What was your score? "))

if mark>=95:
    print ("Distinction")
elif mark >=90:
    print("A*")
elif mark >=80:
    print("A")
elif mark >=70:
    print("B")
elif mark >=60:
    print("C")
else:
    print("Fail")