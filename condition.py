# a=10
# b=20
# c=11

# if a>b and a>c:  
#     print("a is gerater than b,c")
# elif b>a and  b>c:
#     print("b is greater than a,c")
# else:
#     print("cis greater than a,b")



# a=int(input("enter tha value of a:"))
# b=int(input("enter tha value of b:"))
# c=int(input("enter tha value of c:"))

# if a>b and a>c:  
#     print("a is gerater than b,c")
# elif b>a and  b>c:
#     print("b is greater than a,c")
# else:
#     print("c is greater than a,b")


# username=input("enter usernane:")
# password=input("enter password:")
# if username=="admin" and password=="admin123":
#     print(f"Welcomme {username}")
# else:
#     print("invalid username or password")


nep = int(input("enter marks:"))
sci = int(input("enter marks:"))
comp = int(input("enter marks:"))
maths = int(input("enter marks:"))
eng = int(input("enter marks:"))


obtainedmarks= int(nep+sci+comp+maths+eng)
per= int((obtainedmarks/500)*100)
print(per)
if per>80:
    print("distinction")
elif per<80 and per>60:
    print("first division")
elif per<60 and per>40:
    print("second division")
elif per>40:
    print("fail")



print("party invite")
x= int(input("enter your age:"))
if x<18:
    print("you aer not invited")

