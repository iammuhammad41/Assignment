
# Assignment 1, Ex 1.

file = open("demo.py","r",encoding="utf8")
code = file.readlines()
for line in range(0,len(code)):
  l = code[line].split(" ")
  for word in l:
    if(word.lower() == "for" or word.lower() == "while"):
      is_upper = any(ele.isupper() for ele in word)
      if(is_upper == True):
        print(f"{word} at line {line+1}")
  
file.close()