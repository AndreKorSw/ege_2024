''' Сколько 12 разрядных чисел можно составить, чтобы четные и нечетные
цифры не стояли рядом. И цифра 4 присутствовала ровно один раз.'''
from datetime import *  # подключаем модуль таймера
t1 = datetime.now() # время старт
k=0
for i1 in '2468':
    for i2 in '13579':
        for i3 in '02468':
            for i4 in '13579':
                for i5 in '02468':
                    for i6 in '13579':
                        for i7 in '02468':
                            for i8 in '13579':
                                for i9 in '02468':
                                    for i10 in '13579':
                                        for i11 in '02468':
                                            for i12 in '13579':
                                                #for i13 in '02468':
                                                    #for i14 in '13579':
                                                        s=i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12#+i13+i14
                                                        if s.count('4')==1:
                                                            k=k+1
                                                            #print(k,i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14)
print('**',k)   #  76000000                                       
t2 = datetime.now() # время стоп       
print('*1*',t2-t1)  # время выполнения 0:03:59.728259
t3 = datetime.now() # время старт
for i1 in '13579':
    for i2 in '02468':
        for i3 in '13579':
            for i4 in '02468':
                for i5 in '13579':
                    for i6 in '02468':
                        for i7 in '13579':
                            for i8 in '02468':
                                for i9 in '13579':
                                    for i10 in '02468':
                                        for i11 in '13579':
                                            for i12 in '02468':
                                                #for i13 in '13579':
                                                    #for i14 in '02468':
                                                        s=i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12#+i13+i14
                                                        if s.count('4')==1:
                                                            k=k+1
                                                            #print(k,i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14)
print('ans==',k)  #  172000000                                         
t4 = datetime.now()  # время стоп       
print('*2*',t4-t3)   # время выполнения   0:04:45.278638                                                                                     
print('*****',t4-t3+t2-t1)   # время выполнения  0:08:45.006897                                                                                      












