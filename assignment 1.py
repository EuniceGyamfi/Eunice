#6937621
#Eunice Gyamfi
import numpy as np


L =12 #length of beam in meters
w=10 #intensity of load in kN/m



#Question a
#The bending moment(M)and the shear force(V) at end,x=0
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)

a1="a(i) The bending moment at end, x=0 is"
b1="a(i) The shear force at end,x=0 is"
print(a1+' '+str(M)+"kN/m")
print(b1+' '+str(V)+'kN')
print()

#The bending moment(M)and the shear force(V) at end,x=L
x=L
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)

c1="a(ii) The bending moment at end, x=L is"
d1="a(ii) The shear force at end,x=L is"
print(c1+' '+str(M)+"kN/m")
print(d1+' '+str(V)+'kN')
print()

#Question b
#The expression obtained when bending moment is zero is x**2-Lx+L**2/6
#From the expression
a=1
b=-L
c=L**2/6
#using almighty formula the two roots are as follows;

discriminant=b**2-4*a*c

root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a

f='The points of contraflexure are '
print('b, The points of contraflexure are '+str(root_1)+'m'+ ' '+"and"+" "+ str(root_2)+"m")


#Question c
"""
When Shear force is zero, x=1/2
"""
x=1/2
print("c, The point at which V=0 is {}".format(x))
print()


#Question d 
m=0
n=0.01
o=L+n
x=np.arange(m,o,n)
M=(w*(-6*x**2+6*L*x-L**2))/12
print("d, The bending moment at each step in the array using imitialized variable is {0}".format(M))
print()

#Question e
V=w*(L/2-x)
print("e, The shear force for each step along the span is{}".format(V))
print()

#Question f 

#Let the absolute value of the bending moment array be AM

#Also let the minimum AM be m_AM

AM=abs(M)
m_AM=min(AM)

#When the bending moment is m_AM ,we get an expression x**2-Lx+(L**2/6)+(2*m_AM)/w=0

a=1
b=-L
c=(L**2/6)+(2*m_AM)/w
#using almighty formula the two roots are as follows;

discriminant=b**2-4*a*c

root_3=(-b+np.sqrt(discriminant))/2*a
root_4=(-b-np.sqrt(discriminant))/2*a

print("f, The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}".format(root_3,root_4))


#Question g 
#Let the relative errors be t

t_1=((root_1 -root_3)/root_1*100)
t_2=((root_4-root_2)/root_4*100)

print("The relative errors between estimated points of contraflexure {0}% and{1}% ".format(t_1,t_2))



#Question h 
#Let the maximum bending moment be MM and the minimum be mM 
 

MM=max(M)
mM=min(M)

#When the bending moment is MM,we get an expression  x**2-Lx+(L**2/6)+(2*MM)/w
a=1
b=-L
c=(L**2/6)+(2*MM)/w
#using almighty formula the two roots are as follows;

discriminant=b**2-4*a*c

root_5=(-b+np.sqrt(discriminant))/2*a
root_6=(-b-np.sqrt(discriminant))/2*a

print("h1, The points at which the bending moment is maximum occurs are{0} and {1}".format(root_5,root_6))

#When the bending moment is MM,we get an expression  x**2-Lx+(L**2/6)+(2*mm)/w
a=1
b=-L
c=(L**2/6)+(2*mM)/w
#using almighty formula the two roots are as follows;

discriminant=b**2-4*a*c

root_7=(-b+np.sqrt(discriminant))/2*a
root_8=(-b-np.sqrt(discriminant))/2*a

print("h2, The points at which the bending moment is maximum occurs are{0} and {1}".format(root_7,root_8))















   