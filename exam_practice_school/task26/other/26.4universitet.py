# Отбор абитуриентов в железнодорожный вуз происходит по сумме баллов трех экзаменов: по русскому языку, математике и физике. На заранее известное количество мест зачисляются абитуриенты, набравшие большую сумму баллов по результатам трех экзаменов. Все абитуриенты, набравшие определенную сумму баллов или больше, зачисляются на имеющиеся места. Такой балл называется проходным. Если после заполнения имеющихся мест абитуриентами с проходным баллом остаются незаполненные места, но абитуриентов, набравших следующую сумму баллов, больше, чем вакантных мест, набранная этими абитуриентами сумма баллов называется полупроходным баллом. Из числа абитуриентов, набравших полупроходной балл, на имеющиеся места принимаются абитуриенты, имеющие более высокий балл по математике, а при равенстве баллов по математике по физике, при равенстве математики и физики по русскому.
#
# Для данного множества абитуриентов следует определить, какая сумма баллов является проходным баллом, и какой балл по физике у последнего в списке поступивших абитуриента, чтобы быть зачисленным на имеющиеся места.
#
# Входные данные:
#
# В первой строке входного файла находятся два числа: — количество поданных заявлений о приеме (натуральное число, не превышающее 1000 ) и 5 - количество имеющихся мест.
#
# В следующих и строках три оценки по русскому языке, математике и физике соотвественно, разделенные проб (все числа натуральные, не превышающие 100 ).
#
# Запиши в ответе два числа: сначала проходной балл, затем оценку по физике, необходимую для зачисления при условии набранного полупроходного балла.

f = open('')
n, s = map(int, f.readline().split())
ege = []
for s in f:
    rus, math, phys = map(int, s.split())
    ege.append([rus + math + phys, math, phys, rus])
ege.sort(reverse=True)
print(len(ege[:s]))