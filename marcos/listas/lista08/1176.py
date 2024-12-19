
fibo = [0]
for i in range(1, 61):
    fibo.append(fibo[i-1] + fibo[i-2])


T = int(input())


for _ in range(T):
    n = int(input())
    print("Fib({}) = {}".format(n,fibo[n]))
