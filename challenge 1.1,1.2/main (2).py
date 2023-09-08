#factorial of given number
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * factorial(n -1)
num = 5
r=factorial(num)
print("factorial of {} is {} .". format(num,r))