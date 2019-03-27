import multiprocessing

def print_values(n,process_name):
    for i in range(n):
        print(str(i)+'-'+process_name)

process1=multiprocessing.Process(target=print_values,args=(100,'process-1'))
print(process1.pid)
process2=multiprocessing.Process(target=print_values,args=(100,'process-2'))
print(process2.pid)
print(process1.pid)
print(process2.pid)

process1.start()
process2.start()
