# prime_numbers = [2, 3, 5, 7, 11, 13, 17]
# animal_list = ['dog', 'cat', 'frog']
# subject_list = ['MATH101', 'CS222', 'PHY102', 'ACCY203']

# print(prime_numbers[4])
# print(animal_list[1])
# print(len(animal_list))
# animal_list[2] = "emu"
# subject_list[1] = "CSIT222"

# list1 = [1, 2, 3, 4, 5]

# list1.reverse()
# print(list1)

# list1[1] = 6
# del list1[5]
# list1.pop()

# for i in range(0, len(list1)):
#      print(list1)


# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]

# def list_multiply(list1, list2):
# 	result = []
# 	for i in range(0, len(list1)):
# 		result = list1[i] * list2[i]
# 	return result

# print(list_multiply(list1, list2))

# for i in range(0, len(animal_list)):
#     print(animal_list[i])

# prime_numbers.append(21)
# prime_numbers.append(34)
# prime_numbers.append(55)

# animal_list.insert(1, "rabbit")
# animal_list.insert(1, "turtle")
# print(animal_list)

# subject_list = ["MATH101", "CS222", "PHY102", "ACCY203"]

# del subject_list[1]
# del subject_list[1]
# print(subject_list)

# subject_list.pop()
# print(subject_list)

# animal_list.reverse()
# print(animal_list)

# def list_multiply(list1, list2):
#     result = []
#     for i in range(0, len(list1)):
#         result.append(list1[i] * list2[i])
#     return result

# zalamoka = [1, 2, 3, 4, 5]
# fash5 = [10, 20, 30, 40, 50]
# print(list_multiply(zalamoka, fash5))

# make function called list_division that takes two lists as arguments and returns a
# list that contains the result of dividing the elements of the first list by the elements of
# the second list. The function should return an empty list if the two lists are not of the same length.


# \\\\\\\\\\\\\\\\ (

#     def A7A(list1, list2):
# )

# def list_addition(list1, list2):
#     result = []
#     for i in range(0, len(list1)):
#         result.append(list1[i] + list2[i])
#     return result
# fashkh = [1, 2, 3, 4, 5]
# teez = [6, 7, 8, 9, 10]
# print(list_addition(fashkh, teez))


# double the same number in list

# def doubling(list1):
#     result = []
#     for i in range(0, len(list1)):
#         result.append(list1[i])
#         result.append(list1[i])
#     return result

# fashkh = [1, 2, 3, 4, 5]
# print(doubling(fashkh))



# square_list = []
# for i in range(0, 11):
#     square_list.append(i * i)
# print(square_list)

# random_numbers = [1, 4, 4, 10, -1]
# for i in range(0, len(random_numbers)):
#     random_numbers[i] = random_numbers[i] + 20
# print(random_numbers)

# random_numbers = [1, 4, 4, 10, -1]
# for i in range(0, len(random_numbers)):
# 	random_numbers[i] =  random_numbers[i] + 20
# print(random_numbers)


# info = {
#     "CODE": "MATH101",
#     "TITLE": "ALGEBRA",
#     "CREDIT": 6,
#     "DEPARTMENT": "MATHEMATICS"
# }

# cars={
#     "brand": "Mercedes",
#     "model": "C63",
#     "year": 2020
# }

# print(cars.get("brand"))


# person = {
#     "first_name": "Anna",
#     "last_name": "Smith",
#     "age": 25
# }

# print(person.get("first_name"))
# print(person["last_name"])
# print(person["age"])

# person["age"] = 50

# print(person.get("address"))

# capital = {
#     "Egypt": "Cairo",
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Italy": "Rome",
#     "Palestine": "Ghaza"
# }

# user_input = input("Enter a country: ")
# if user_input in capital:
#     print(capital[user_input])
# else:
#     print("Sorry I don't know capital of ", user_input) 

# DIGIT_MAP = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }

# user_input = (input("Please enter a numerical code: "))
# result = ""
# for i in range(0, len(user_input)):
#         digits = DIGIT_MAP.get(user_input[i])
#         if i == 0:
#             result += digits
#         else:
#             result = result + "-" + digits
# print("You have entered ", result)

# User_input = input("Please enter a numerical code: ")

# Result = ""

# for i in range(0, len(User_input)):
#     Digits = DIGIT_MAP.get(User_input[i])
#     if i == 0:
#         Result += Digits
#     else:
#         Result = Result + "-" + Digits
# print("You have entered ", Result)




# n = int(input("ZEBY: "))

# a, b = 0, 1

# for _ in range(n):
#     print(a)
#     a , b = b, a + b


# def list_multiply(list1, list2):
#     result = []
#     for i in range(0, len(list1)):
#         result.append(list1[i] * list2[i])
#     return result
# zobry= [1, 2, 3, 4, 5]
# manga= [30, 40, 50, 10, 20]
# print(list_multiply(zobry, manga))

# def list_multiply(list1 , list2):
#     list0 = []
#     for i in range(0 , len(list1)):
#         list0.append(list1[i] * list2[i]) 
#     return list0
    
# list1 = [4 , 5 , 6]
# list2 = [10 , 0 , 1]
# print(list_multiply(list1, list2))

# def list_multiply(list1 , list2):
#     list0 = []
#     for i in range(0 , len(list1)):
#         list0.append(list1[i]*list2[i])
#     return list0
    
# list1 = [1,2,4,5,1]
# list2= [2,3,4,5,6]
# print(list_multiply(list1, list2))

# import random
# subjects = []
# while True:
#     user_input = input("Enter preferred subject code (enter QUIT to quit): ")
#     if user_input == "QUIT":
#         break
#     subjects.append(user_input)
    

# print(subjects)
# print("You have enrolled ", random.choice(subjects))

# mat=[ [ i+j for i in range (0,5)]  for j in range(0,4)]   #  4 rows  5 columns
# print (mat)

# mat2=[ [ 8*col+row for col in range (0,2)]  for row in range(0,4)]   #  4 rows  5 columns
# print(mat2)

# def doubling(list1):
#     result = []
#     for i in range(0, len(list1)):
#         result.append(list1[i])
#         result.append(list1[i])
#     return result

# fashkh = [1, 2, 3, 4, 5]
# print(doubling(fashkh))

# class Student:
# #{
#     email_domain = "solla.sollew.edu"
#     student_dir = "/user/student"

#     def __init__(self, id, first_name, last_name):
#     #{
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name

#         self.username = first_name[0].lower() + last_name[0].lower() + id[0:3]
#     #}
# #}

# class Student:
# #{

#     def __init__(self, id, first_name, last_name):
#     #{
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name

#         self.username = first_name[0].lower() + last_name[0].lower() + id[0:3]
#     #}

# #}
# Studentobj1 = Student("5532565", "Homer", "Simpson")
# print(Studentobj1.id)
# print(Studentobj1.first_name)
# print(Studentobj1.username)

# class Student:
# #{
#     email_domain = "solla.sollew.edu"
#     student_dir = "/user/student"

#     def __init__(self, id, first_name, last_name):
#     #{
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = first_name[0].capitalize() + last_name[0].lower() + id[0:3]
#     #}
# #}
# Studentobj1 = Student("5532565", "Homer", "Simpson")
# print(Studentobj1.username + "@" + Studentobj1.email_domain)
# class Student:
# #{
#     email_domain = "solla.sollew.edu"

#     @classmethod
#     def admin_email(cls):
#         return "admin@" + cls.email_domain

# class Student:
#     email_domain = "sols123.567"
#     student_dir = "/user"

#     def __init__(self, Id, FirstName, Lastname):
#         self.Id = Id
#         self.FirstName = FirstName
#         self.Lastname = Lastname
#         self.username = FirstName[0].lower() + Lastname[0].lower() + Id[0:3]
    
# studentobj1 = Student("5555", "Michal", "Jackson")
# print(studentobj1.username + "@" + studentobj1.email_domain)



# #}
    
# class Student:
# #{
#     email_domain = "solla.sollew.edu"

#     [[1]]
#     [[5]] admin_email[[2]]
#     [[4]] "admin@" + [[3]].email_domain

# #}
# class MathQuestion:
#     def __init__(self, number1, number2, operation, solution):
#         self.number1 = number1
#         self.number2 = number2
#         self.operation = operation
#         self.solution = solution
# questionObj1 = MathQuestion(20, 5, "+", 25)
# questionObj2 = MathQuestion(20, 5, "-", 15)
# questionObj3 = MathQuestion(20, 5, "*", 100)
# questionObj4 = MathQuestion(20, 5, "/", 4)

# print(questionObj1.number1, questionObj1.operation, questionObj1.number2, "=", questionObj1.solution)

# def check_answer(self, answer):
#     if answer == self.solution:
#         return True
#     else:
#         return False
    
# def question_text(self):
#     return str(self.number1) + " " + self.operation + " " + str(self.number2) + " = "

# import random

# matrix = [[random.randint(0, 9) for _ in range(4)] for _ in range(4)]
# def count_digits(matrix):
#     counts = [0] * 10  # Initialize a list of 10 zeros
#     for row in matrix:
#         for num in row:
#             counts[num] += 1  # Increment the count for this number
#     return counts
# for i in range(0, len(counts)):
    
# def triple(word):
#     result = ""
#     for i in range(0, len(word)):
#         result += word[i] * 3
#     return result
# print(triple("little fish"))

# for i in range(2,11,2):
#     if i < 10:
#         trailing = ", " 
#     else:
#         trailing = "."
#     print(i, end=trailing)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(*, end="")
#     print()

# for i in range(1, 11):
#     print("{0} + {1} = {2}".format(i, i, i + i))


# def multiply(list1, list2):
#     result = []
#     for i in range(0, len(list1)):
#         result.append(list1[i] * list2[i])
#     return result

# zobry = [1, 2, 3, 4]
# manga = [10, 20, 30, 40]
# print(multiply(zobry, manga))

# class Student:
# #{
#     email_domain = "solla.sollew.edu"
#     @staticmethod
#     def admin_email():
#         return "admin@" + Student.email_domain
    
#     def admin_email(cls):
#         return "admin@" + cls.email_domain
# class Student:
# #{
#     email_domain = "solla.sollew.edu"

#     [[1]]
#     [[5]] admin_email[[2]]
#     [[4]] "admin@" + [[3]].email_domain

#}

#}
# class MyClass:
#     @staticmethod
#     def my_static_method():
#         print("This is a static method.")
        
# # Call the static method
# MyClass.my_static_method()

# a, b = 0, 1
# for i in range(1,11):
#     print(a)
#     a, b = b, a + b
