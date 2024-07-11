# На орбите вращается спутник, производящий измерения активности солнца. Каждый результат является натуральным числом. Перед началом обработки серии измерений солнечной активности из неё исключают к наибольших и К 1 наименьших измерений (они принимаются недостоверными). По данной информации о значении каждого из измерений, а также о количестве исключённых значений необходимо определить наименьшее достоверное измерение и целую часть среднего значения всех достоверных измерений. Входные данные: в первой строке файла находятся 2 числа, записанные через пробел: - общее количество измерений (натуральное число, не больше 10000), К - количество исключаемых минимальных и максимальных значений. В следующих строках располагаются значения каждого из проведённых измерений (натуральные числа, не больше 1000), все в отдельных строках В ответ необходимо записать два числа через пробел: сначала наименьшее достоверное измерение, а затем целую часть среднего значения всех достоверных измерений.

f = open("")
colvo_izmereni, kolvo_iskl_minmaxvalues = map(int, f.readline().split())
izmerenia = sorted([int(i) for i in f])
izmerenia = izmerenia[kolvo_iskl_minmaxvalues: -kolvo_iskl_minmaxvalues]
print(min(izmerenia), sum(izmerenia)/len(izmerenia))