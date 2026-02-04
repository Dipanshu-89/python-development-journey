str="welcome to our python phone_contact"
print(str.center(55))
contacts={"Atul":8595679122,"Ram":9575648274,"chacha":9627215477,"ramesh":8765742464,"rohit":7834785469}
l=["1. my contacts","2. add contact","3. delete"]
for i in l:
    print(i)
choice=int(input("enter what do you want in number(like 1,2,3..):"))
if(1==choice):
    print("your phone contacts")
    for i,j in contacts.items():
        print(f"{i}:{j}")
elif(2==choice):
    print("add the contact number")
    contacts={"Atul":8575694236,"Ram":9575648274,"abhishek":951697457,"ramesh":8765742464,"rohit":7834785469}
    while True:
        name=input("enter your friend name(or if you do not add the no. please type no):")
        if(name.lower()=="no"):
            break
        Number=int(input("enter number:"))
        contacts[name]=Number
    check=input("enter yes if you check the number is add, otherwise no")
    if(check=="yes"):
        for name,num in contacts.items():
            print(f"{name}:{num}")
    else:
        print("sorry, you give wrong input.")
elif(choice==3):
    print("delete contact number do you want.")
    cut=input("enter name:")
    if cut in contacts:
        contacts.pop(cut)
    check_1=input("enter yes if you check your phone contact list:")
    if(check_1=="yes"):
        for name,num in contacts.items():
            print(f"{name}:{num}")
    else:
        print("sorry, perhaps you give wrong input")
