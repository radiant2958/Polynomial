# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.



with open('task.txt','r') as date:
    str1=date.readline() 

with open('task001.txt','r') as date:
    str2=date.readline() 

print(str1)
print(str2)

def list_of_str(str1):
    str3=str1.replace('+'," ").replace('= 0','').replace('*', ' ').split()
    new_list=[]
    i=0
    while i<len(str3):
        if str3[i]=='x':
            i+=2
        else:
            new_list.append(int(str3[i]))
            i+=1
    new_list.append(int(str3[-1]))
    return new_list

def sum_poly(list1,list2):
    if len(list1)==len(list2):
        result=[list1[i]+list2[i] for i in range(len(list1))]
    elif len(list1)>len(list2):
        result=[list1[i]+list2[i] for i in range(len(list2))]
        for i in range(len(list2),len(list1)):
            result.append(list1[i])
    else:
        result=[list1[i]+list2[i] for i in range(len(list1))]
        for i in range(len(list1),len(list2)):
            result.append(list2[i])
    return result

def new_polynomial(lis):
    l=len(lis)-1
    new_str=''
    for i in range(l):
        if l-i!=1:
            new_str+=f'{lis[i]}*x**{l-i} + '
        else:
            new_str+=f'{lis[i]}*x + '
    new_str+=str(lis[-1])
    new_str+=' = 0'
    return new_str

def write_file(file):
   with open('task002.txt', 'w') as date:
      date.write(file)

a=list_of_str(str1)
print(a)
b=list_of_str(str2)
c=sum_poly(a,b)
write_file(new_polynomial(c))

