import random
import time

names=['sagar','firoz','ankit','rahil']
subjects=['python','java','blockchain','C#']

def people_list(num_people):
    results=[]
    for i in range(num_people):
        person={'id':i,'name':random.choice(names),
                'subjects':random.choice(subjects)}
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
         person={'id':i,'name':random.choice(names),
                'subjects':random.choice(subjects)}
         yield person

'''
t1=time.clock()
g=people_list(1000000)
t2= time.clock()

'''

t1=time.clock()
g=people_generator(1000000)
t2= time.clock()

print(t2-t1)
