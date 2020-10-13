import matplotlib.pyplot as plt
import json

with open('uspop.json') as k:
    population = json.load(k)



ystart= []
pstart=[]


for i in population[1]:
    for x in i: 
        if x == 'value' and i[x] !=None:
            pstart.append(i[x])
        if x == 'date' and i[x] != '2020':
            print(i[x])
            ystart.append(int(i[x]))
#print(years,pop)
years = list(reversed((ystart)))
pop = list(reversed(pstart))

#labels
plt.ylabel('Population (in billions)')
plt.xlabel('Years 1960-2019' )

plt.title("The United States' Population from 1960-2019")
plt.plot(years,pop)
plt.tight_layout()
plt.show()
