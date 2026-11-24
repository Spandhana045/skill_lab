'''import keyword
print(keyword.kwlist)

a=[10,2.3,True,"hello"]
a.pop(0)
print(a)


a=10,20,30
print(a,type(a))

a=10,
print(a,type(a))

a=(10,2,6,5j,True,'hi',[1,2],[3,4])
print(a[-1])

a={10,20,30,40}
print(a)      

a={'a':10}
print(a['a'])  

a={'a':10,'a':20}
print(a)

a={'a':10,'a':20}
a['c']=30
print(a)


a={'a':[10,20,30],'b':40}
print(a['a'][1])

a={'a':[10,20,30],'b':40}
print(a['a'][-2])'''


'''a="Hello"
print(a[2:3+1:1])

a="Hello"
print(a[2:4])
print(a[-3:-2+1:1])

a="byebye"
print(a[-4:-2+1:1])

a="life is long"
print(a[-10:3+1:1])

a="Hello"
print(a[3:1-1:-1])
a="Hello"
print(a[3:0:-1])
a="Hello"
print(a[-2:-4-1:-1])
a="Hello"
print(a[::-1])

a="hello"
print(a[2:-4-1:-1])'''

'''a="Good Morning" 
print(a[-4:-5-1:-1])

a="Good Morning" 
print(a[-2:-8-1:-3])'''

'''a=input("enter:")
print(a)'''

'''a=input("enter:")
print(type(a))'''

'''a=eval(input("enter:"))
print(a,type(a))'''

'''a=int(input("enter:"))
print(a,type(a))'''

'''a=int(input("enter:"))
if (a%2==0):
    print("even")
else:
    print("odd")'''

'''a=eval(input("enter list:"))
if len(a)==5:
    print("yes")
else: 
    print("no")'''

'''print(ord('v'))
print(chr(65))

print(ord('A')+32)'''

'''ch=input("enter:")
if "A"<=ch<="Z":
    print('upper')
elif "a"<=ch<="z":
    print("lower")
else:
    print('not an alpha')'''

'''#instagram code
un=input("enter:")
if un=="Baby_Queen":
    print("username is correct")
    pw=input("enter:")
    if pw=="taena":
        print("password is correct")
    else:
        print("password is incorrect")
else:
    print("username is incorrect")'''

'''print('HELLO WORLD')'''

'''i=1
while i<=20:
    print(i)
    i+=1'''

'''i=2
while i<=20:
    print(i)
    i+=2'''

'''#Reverse a number
n=int(input("enter the number:"))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld   
    print(rev)'''

'''for i in range(1,9):
    print(i) '''

'''for i in range(1,51):
    if i%2==0:
        print(i,'even')'''

'''l=[10,20,30]
for i in l:
        print(i)'''

'''# for loop on strings - concatenation
s=input('enter:')
out=''
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''

'''#reverse a string
s=input('enter:')
rev=''
for i in s:
    rev=i+rev
print(rev)'''

#Pattern programming
'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if(i==j):
         print('$',end=' ')
        else:
         print(' ',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if(i==j):
         print('!',end=' ')
        else:
         print('@',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if(i<j):
         print('1',end=' ')
        else:
         print('7',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if(i>j):
         print('}',end=' ')
        else:
         print('?',end=' ')
    print()'''