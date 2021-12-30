c=input("enter character :")
ascii=ord(c)
print(ascii)

txt=input("enter the string :")
txtlen=len(txt)
print(txtlen)
for char in txt:
    ascii=ord(char)
    print(char, '\t',ascii)