n = int(input("How many characters to preview? "))
file = open("Codingal.txt", "r")
print(file.read(n))
file.close()
print()
file = open("Codingal.txt", "r")
lines = file.readlines()
file.close()
print("Totallines:", len(lines))
for i in range (len(lines)):
    print(i + 1, "->", lines[i].strip())
print()
word = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()