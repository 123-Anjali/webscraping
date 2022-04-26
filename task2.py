
from task1 import data
import json

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if i["year"] not in years:
            years.append(year)
    movies_dict={i:[]for i in years}
    for i in movies:
        year=i["year"]
        for x in movies_dict:
            if str(x)==str(year):
                movies_dict[x].append(i)
    a=[]
    for y in movies_dict:
        a.append(y)
    i=0
    while i<len(a):
        j=0
        while j<(len(a)-i-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
            j=j+1
        i=i+1
    new_movie_dict={}
    for i in a:
        for x,y in movies_dict.items():
            if x==i:
                new_movie_dict[i]=y
    with open("task2.json","w") as f:
        json.dump(new_movie_dict,f,indent=4)
    return movies_dict
groups=group_by_year(data)
print(group_by_year(data))
    