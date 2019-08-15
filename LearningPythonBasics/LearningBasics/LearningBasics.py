'''
Created on Jun 14, 2018

@author: sudiptas
'''
myvar = "Hello Python";
print(myvar);

x = 100;
pi = 3.14;
empname = "python is great";

a = b = c = 100;


print(x);
print(pi);
print(empname);

x = 1;
y = 2;

print("x = "+str(x));
print("y = "+str(y));
y,x = x,y;
print("x = "+str(x));
print("y = "+str(y));

console_input = input("Enter you name: ");
print("Hi, "+console_input+". Nice to meet you!");