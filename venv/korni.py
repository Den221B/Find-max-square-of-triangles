import math
a= int(input())
b= int(input())
c= int(input())
print ('Квадратое уравнеие выглядит так:', a,'* x^2 +',b,'* x +',c,'= 0')
D=b*b-4*a*c
if D>=0:
    x1=(-b+D**(0.5))/(2*a)
    x2 = (-b-D**(0.5))/(2*a)
    print('x1 =',x1,'x2 =',x2)
else:
    print('Нет действительных корней')
