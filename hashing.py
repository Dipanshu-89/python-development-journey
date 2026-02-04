import random
choice=int(input("enter 1 for coding otherwise 0 for decoding:"))
if(choice==1):
    print("you choose coding ")
    message=input("enter your message:")
    str=message.split(" ")
    stnw=[]
    for i in str:
        if(len(i)>=3):
            r1='gdf'
            r2='cyd'
            str1=r1+i[1:]+i[0]+r2
            stnw.append(str1)
        else:
            stnw.append(i[::-1])
    print(" ".join(stnw))
elif(choice==0):
    message=input("enter your message:")
    words=message.split(" ")
    new=[]
    for i in words:
        if(len(i)>=3):
            strx=i[3:-3]
            strv=strx[-1]+strx[:-1]
            new.append(strv)
        else:
            new.append(i[::-1])
    print(" ".join(new))
    


    
    