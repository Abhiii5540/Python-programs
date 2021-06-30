# name="ABHISHEK "
# character="is a good boy"

# print(name)

# # a=type(name)

# c=name + character
# print(c)

# print(name[4])
# print(name[0:4])
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]

'''
-> negative idexing : 1st lenght starts from (-1) to -(lenght)
-> g: from (-1) to (-8) in case name = ABHISHEK
-> (-1) is used for last index and hnce can be used to extract the last digit or char..

'''
# d = name[-4:-1] # is same is name[1:4]
# print(d)

name = "HelloIsGood"
d = name[0:11]
'''
-->var_name[start_index : end_index : number_of_times_char_to_be_skipped]

-->[0:11:1] means no char skipped
-->[0:11:2] means 1 char skipped
-->[0:11:2] means 2 char skipped

'''
# x= name[0:11:3]
# z=name[2:9:2]
# print(d)
# print(x)
# print(z)


story = "once upon a time , notes were not found "

print(len(story))
print(story.endswith("notes"))
print(story.count("n"))
print(story.capitalize())
print(story.find("upon"))
print(story.replace("upon", "Code"))



 