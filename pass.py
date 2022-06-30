# print("🧑🏿‍💻🧑🏿‍💻🧑🏿‍💻🧑🏿‍💻 computer bazar 🧑🏿‍💻🧑🏿‍💻🧑🏿‍💻🧑🏿‍💻")
# print("1:dell=rs20000\n"
#     "2:toshiba=rs30000\n"
# # "3:mac=rs50000")
# a=int(input("enter your laptop option:"))
# if a == 1:
#     print("dell")
#     w=20000
# elif a == 2:
#     print("toshiba")
#     w=30000
# elif a == 3:
#     print("mac")
#     w=50000
# else:
#     print("invalid option")

# print("delivery option:\n"
#     "1:home=rs1000\n"
#     "2:pickup=free\n")
# b=int(input("enter your delivery option:"))
# if b==1:
#     z=1000
# elif b==2:
#     z=0
# else:
#     print("invalid option")

# print("packaging options:\n"
# "1:plastic bag=rs500\n"
# "2:box=rs1000\n"
# "3:gift=rs5000")
# c=int(input("enter your packaging option:"))
# if c==1:
#     y=500
# elif c==2:
#     y=1000
# elif c==3:
#     y=5000
# else:
#     print("invalid option")

# print("location:")
# print("1:kathmandu{tax=13%}")
# print("2:lalitpur")
# print("3:bhaktapur")
# d=int(input ("enter your location option:"))
# if d==1:
#     x=0.13
# else:
#     x=0

# e=int(input("enter the quantity:"))

# totalamount= int(e*w+z+y)
# tax=int((e*w)*x)
# grandtotal=int(totalamount+tax)

# print(f"totalamount is: RS{totalamount}")
# print(f"taxable amount is:RS{tax}")
# print(f"grandtotal amount is: RS{grandtotal}")



print("ringroad travells")
print("our services:\n"
"1:ghodavari to RNAC \n"
"2:RNAC to tokha\n"
"3:tokha to budanilkantha\n"
"4:budanilkantha to sundharijal\n"
"5:sundharijal to ghodavari")

x= int(input("enter tour destination"))

if x==1 :
    print("ghodavari to RNAC")
    z=15
elif x==2:
    print("RNAC to tokha")
    z=15
elif x==3:
    print("tokha to budanilkantha")
    z=15
elif x==4:
    print("budanilkantha to sundharijal")
    z=15
elif x==5:
    print("sundharijal to ghodavari")
    z=15
else:
    pass 

y=int(input("enter tour age:"))

if y>18 or y<65:
    w=0.1
else:
    w=0



