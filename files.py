# # Use open function to read the content of a file!
# # f = open('Abhiii.txt', 'r')
# f = open('Abhiii.txt') # by default the mode is r
# # data = f.read()
# data = f.read(60) # reads first 60 characters from the file
# print(data)
# f.close()




# f = open('Abhiii.txt')
# # read first line
# data = f.readline() 
# print(data)

# # Read second line
# data = f.readline() 
# print(data)

# # Read third line
# data = f.readline() 
# print(data)

# # Read fourth line... and so on...
# data = f.readline() 
# print(data)
# f.close()




# f = open('NewText.txt', 'w')
# f.write("Hello there , Abhiii") 
# f.close()

f = open('NewText.txt', 'a')
f.write("Hii there , Golu") 
f.close()
