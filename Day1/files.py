# file = open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'r')
# # for each in file:
# #     print(each)
# print(file.read())

# with open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'r') as file:
#     data = file.read()
# print(data)

# with open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'r') as file:
#      data = file.readlines()
#      for line in data:
#          word = line.split()
#          print(word)

# file = open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'w')
# file.write("This is the write command")
# file.write("This is the write command -- more lines")
# file.close()
# file = open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'r')
# print(file.read())

file = open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'a')
file.write("This is the write command")
file.write("This is the write command -- more lines")
file.close()
file = open('C:/Users/MuralidharBairy/Desktop/textFile.txt', 'r')
print(file.read())