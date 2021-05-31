def fibo(n):
    if n==0:
        return 0;
    else:
        return n+fibo(n-1)
number = int(input())
print(fibo(number))





