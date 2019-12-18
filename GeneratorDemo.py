import random
import time

names=['sunny','bunny','chinny','vinny']
subjects=['Python','Java','Blockchain']

def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
                  'id':i,
                  'name':random.choice(names),
                  'major':random.choice(subjects)
               }
        result.append(person)
    return result

def people_generator(num_people):    
    for i in range(num_people):
        person={
                  'id':i,
                  'name':random.choice(names),
                  'major':random.choice(subjects)
               }
        yield person


t1=time.clock()
people=people_list(100000000)
t2=time.clock()


'''t1=time.clock()
people=people_generator(1000000000000000)
t2=time.clock()'''

print('Took {}'.format(t2-t1))
