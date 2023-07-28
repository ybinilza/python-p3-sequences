#!/usr/bin/env python3

def print_fibonacci(length):
    fibo =[0,1];
    a=[]
    b=[0]
    num1=0;
    num2=1;
    i=2;

    while(i<length):
        sum=num1+num2;
        fibo.append(sum);
        num1=num2;
        num2=sum;
        i=i+1;
    
    if length == 0:
        print(a);
    elif length == 1:
        print(b);
    else:
        print(fibo);
