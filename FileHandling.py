new_file = open('Coningal.txt', 'x')
new_file.close()
import os 
print("Checking if my file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("Codingal")
else:
    print("file does not exsist")
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()
os.remove('Codingal.txt')
