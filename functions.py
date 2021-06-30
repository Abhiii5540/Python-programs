# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
#     return p

# marks1 = [45, 78, 86, 77]
# percentage1 = percent(marks1)

# marks2 = [75, 98, 88, 78]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)






# def greet(name):
#     print("Good Day, "+ name)

# def mySum(num1, num2):
#     return num1 + num2

# nam=input("ENTER A NAME \n")
# n1=int(input("ENTER A No \n"))
# n2=int(input("ENTER A No \n"))
# greet(nam)
# s = mySum(n1, n2)
# print(s)








# default parameter value 
# is used when user pass nothing in the name area i.e.as parameter
# def greet(name="Stranger"):
#     print("Good Day, "+ name) 
# greet()
# greet("Harry")









# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)! 

# n = 0
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)



# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial_recursive(n-1)

# # f = factorial_iter(5)
# f = factorial_recursive(0)
# print(f)


# This is done in order to prevent printing statement on different lines as this is Default
# inorder to avoid this we use end=""
# this prevents control to new line

# print("Hello ,", end="")
# print("How", end=" ")
# print("are", end=" ")
# print("you?", end=" ")


# sum of n natural number 

def sum(n):
   if n <= 1:
       return n
   else:
       return n + sum(n-1)

num = -23
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",sum(num))
