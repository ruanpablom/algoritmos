n = int(input())

fatorial = 1

for i in range(1, n+1):
    fatorial = fatorial * i

print("%d! = %d" % (n, fatorial))