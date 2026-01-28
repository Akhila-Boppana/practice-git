'''Write a program to find the reverse of the given number'''

n=int(input("Enter the number:"))
r=0
while n>0:
    rev=n%10
    r=(r*10)+rev
    n=n//10

print(r)
