# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 
import random
import itertools
k=int(input('Введите степеть k '))

def list_ratios(k):
    ratios=[]
    for i in range(k+1):
        a=random.randint(0,100)
        ratios.append(a)
    return ratios


def fun_degree(ratios,k):
    my_list=[]
    first = True
    if ratios[-1]==0:
       for i in range(k):
          if ratios[i]!=0:
            if first:
              if ratios[i]>1:
                 if i!=k-1:
                    my_list.append(f'*x**{k-i} +')
                 else:
                    my_list.append('*x')
              elif ratios[i]==1:
                 if i!=k-1:
                    my_list.append(f'x**{k-i} +')
                 else:
                    my_list.append('x')
              else:
                 first=False
       
    else:
       for i in range(k):
          if ratios[i]!=0:
            if first:
               if ratios[i]>1:
                  if i!=k-1:
                     my_list.append(f'*x**{k-i} + ')
                  else:
                     my_list.append('*x + ')
               elif ratios[i]==1:
                  if i!=k-1:
                    my_list.append(f'x**{k-i} + ')
                  else:
                    my_list.append('x + ')
               else:
                  first=False
    return my_list

def connect_list(ratios,my_list):
    
    
    for i in range(len(ratios)):        
        tmg=list(itertools.zip_longest(ratios,my_list))
    return tmg

def print_polynomial(list):
   
    new_str=''
    for i in list:
        for item in i:
            if item!=0 and item!=None:
               new_str+=str(item)
    new_str+=' = 0'
  
    return new_str
    
def write_file(file):
   with open('task001.txt', 'w') as date:
      date.write(file)


m=list_ratios(k)
print(m)
l=connect_list(m,fun_degree(m,k))
write_file(print_polynomial(l))
