print("welcome to our virtual kbc")
question=["who is the current prime minister of india?","what is the capital of punjab?"]
option_1=["option A. yogi adityanath","option B. Arvind kejariwal","option c. jawharlal nehru","option d.narendra modi"]
option_2=["option A. Lucknow","option B. Chandigarh","option c. jalandhar","option d.Ludhiana"]
enter_1=int(input("please enter 1 key for playing the kbc:"))
print("\nfirst question is your computer screen:\n")
if(enter_1==1):
    print(question[0])
options_1=int(input("\nplease enter 1 key for options:"))
if(options_1==1):
    print(option_1[0])
    print(option_1[1])
    print(option_1[2])
    print(option_1[3])
answer=input("\nenter your option in term (like a,b,c..):")
if(answer=="d" or answer=="D"):
    print("\ncongrats,you got 50 lakh")
else:
    print("\nsorry, please leave")
proceed=input("\nplease type yes if you give correct answer, otherwise no. bcz you are user at that time:")
if(proceed=="yes" or proceed=="Yes"):
    print("\nNext question comes on your computer screen:")
    a=int(input("\nplease enter 1 key for 2nd question:"))
    if(a==1):
        print("\n")
        print(question[1])
        options_2=int(input("\nplease enter 2 key for options:"))
        if(options_2==2):
            print(option_2[0])
            print(option_2[1])
            print(option_2[2])
            print(option_2[3])
            answer_1=input("\nenter your option in term (like A,B,C,a..):")
            if(answer_1=="b" or answer_1=="B"):
                print("\ncongratulation,you won the kbc and your prize money is rs.1crore")
            else:
                print("\nbetter luck next time")
else:
    print("\nwell try,but your luck is not to you ")