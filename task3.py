import json



def group_of_decades(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            a=int(x)
            if a>=i and a<=dec10:
                for v in movies[x]:
                    moviedec[i].append(v)
    with open ("groups_of_decades.json","w") as file:
        json.dump(moviedec,file,indent=4)
    return(moviedec)
file =open("task2.json","r")
read=file.read()
data=json.loads(read)

print(group_of_decades(data))





