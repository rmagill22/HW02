import json
import matplotlib.pyplot as plt
import pandas as pd
with open('usreps.json') as k:
    usreps_data = json.load(k)

#number of reps for each party
nd = 0
nr =0
numbers= []
for objects in usreps_data['objects']:
    if objects['party'] == 'Democrat': 
        nd +=1
    if objects['party'] == 'Republican': 
        nr +=1
    else:
        continue
print(nd,nr)
numbers.append(nd)
numbers.append(nr)
print(numbers)

#number of reps by gender
m_counts= []
md_count= 0
mr_count= 0

for objects in usreps_data['objects']:
    if objects['party'] == 'Democrat': 
        if objects['person']['gender'] == 'male':
            md_count +=1
    if objects['party'] == 'Republican': 
        if objects['person']['gender'] == 'male':
            mr_count +=1
    else:
        continue
m_counts.append(mr_count)
m_counts.append(md_count)
print(m_counts)

f_counts=[]
fd_count=0
fr_count=0
for objects in usreps_data['objects']:
    if objects['party'] == 'Democrat': 
        if objects['person']['gender'] == 'female':
            fd_count +=1
    if objects['party'] == 'Republican': 
        if objects['person']['gender'] == 'female':
            fr_count +=1
    else:
        continue
f_counts.append(fd_count)
f_counts.append(fr_count)
print(f_counts)

men= m_counts
women= f_counts
index= ['Democrat', 'Republican']
df=pd.DataFrame({'Men': men,'Women': women}, index=index)
ax= df.plot.bar(rot=0)
plt.title('U.S. Representatives by Political Party')
plt.ylabel('Number of U.S. Representatives')
plt.xlabel('Political Party')
plt.show()