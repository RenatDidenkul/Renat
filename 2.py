print("PLEASE ENTER STRING: ")
s = input()
s1 = ''
for i in s:
    if i not in ('A', 'E', 'I', 'O', 'U'):
        s1+= i
print(s1)