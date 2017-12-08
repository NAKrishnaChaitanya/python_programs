cabins_available=[1,2,3,4,5,6,7,8.1,8.2,8.3]
cabins_allocated=[]
costumers_inside=[]
while (1):
    print("costumer who are in ",costumers_inside)
    print("cabins allocated ",cabins_allocated)
    while(len(costumers_inside)>=0 and len(costumers_inside)<10):
        ch=int(input("Enter choice\t1-In  2-Out 111-Mall closing"))
        if ch==1:
            c_i=int(input("Enter costumer_id: "))
            if c_i in costumers_inside:
                print("Costumer is already inside")
            else:
                costumers_inside.append(c_i)
                cabins_allocated.append(min(cabins_available))
                cabins_available.remove(min(cabins_available))
                print("Allocated token to costumer: ",costumers_inside[-1],"cabin_allocated: ",cabins_allocated[-1])
        elif ch==2:
            c_i=input("Leaving costumer-token number: ")
            if c_i in costumers_inside:
                cabins_available.append(index(costumers_inside.index(c_i)))
                cabins_allocated.remove(index(costumers_inside.index(c_i)))
                costumers_inside.remove(c_i)
            else:
                print("Invallid costumer-token")
        elif ch==111:
            break
        else:
            print("Invalid choice")
    if(len(costumers_inside)>=10):
        print("You cannot allocate more it's already full:\nWait for some Time")
        print("If any one is leaving")
        c_i=input("Press 1")
        if(c_i==1):
            c_i=input("Leaving costumer-token number: ")
            if c_i in costumers_inside:
                cabins_available.append(costumers_inside.index(c_i))
                cabins_allocated.remove(costumers_inside.index(c_i))
                costumers_inside.remove(c_i)
            else:
                print("Invallid costumer-token")
    if close=='111':
        break
    close=int(input("If Mall is closing\tPress - 111"))
    if close=='111':
        break
        
print("Costumers_inside are: ",costumers_inside)
print("Cabins allocated: ",cabins_allocated)
