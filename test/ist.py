#print(('\n'.join()([j*i for j in range(2,10) for i in range(1,10)])))
# join is to join the list and seperaters how to use in list comphehansions

from itertools import permutations
# perm = permutations(['a', 'b', 'c'], 2)
#for i in list(perm):
   # print(i)
#print([i for i in permutations(['a', 'b', 'c'], 2)])


#print((i,j for i in range(1, 100) for j in range(1, 26)))

#f = open("multi.txt","w+")

import threading
def print_values(n, thread_name):
    for i in range(n):
        print(str(i)+'-'+thread_name)
        #with open("multi.txt", "w") as file:
            #file.write(thread_name)
            #file.close()

thread1 = threading.Thread(target=print_values,args=(100, 'thread-1'))
thread2 = threading.Thread(target=print_values,args=(100, 'thread-2'))
thread3 = threading.Thread(target=print_values,args=(100, 'thread-3'))
thread4 = threading.Thread(target=print_values,args=(100, 'thread-4'))

def write_data():
    with open('multi.txt','w') as f:
        data_th=print_values()
        for data in data_th:
            data_str=''
            for each in data:
                data_str=data_str+str(each)+','
            f.write(data_str+'\n')


#with open("multi.txt", "w") as file:
    #file.write()
    #file.close()

