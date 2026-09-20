file = open("C:/Users/EZ/Desktop/루키즈 자료/9.17/35_이시원.txt", 'w')
file.write("babo\n")
for i in range(1,11) :
    file.write(f"{i} line\n")
file.close

file = open("C:/Users/EZ/Desktop/루키즈 자료/9.17/35_이시원.txt", 'r')
while True:
   line = file.readline()
   if not line: break
   print(line) 
file.close

file = open("C:/Users/EZ/Desktop/루키즈 자료/9.17/35_이시원.txt", 'a', encoding="utf-8")
file.write("바보바보야")
file.close

file = open("C:/Users/EZ/Desktop/루키즈 자료/9.17/35_이시원.txt", 'r', encoding="utf-8")
lines = file.readlines()
for line in lines:
    print(line)
file.close
