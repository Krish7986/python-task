def armstrong(n):
    num1 = n
    m = n
    len = 0
    sum = 0
    while n>0:
        id = n % 10
        len+=1
        n =n // 10
    # print(len)
    while num1 > 0:
        id = num1 % 10
        sum+=id**len
        num1 = num1 // 10
    # print(sum)
    if sum == m:
        print(f"{sum} is armstrong number")
        # return True
    # return False
       
op = [armstrong(i) for i in range(10,1000)  if armstrong(i)]
print("armstrong number",op)


##perfect square
def square(num):
    num1 = num ** 0.5
    if int(num1) ** 2 == num:
        print(f"{num} its prefect square")
    # print(f" {num}its  not prefect square") 
op = [i for i in range(1,100) if square(i)]
print(op)

## FACTOR OF A NUMBER
def factor(num):
    sum= 0
    for i in range(1,num):
        if num%i == 0:
            sum+=i

    if(sum==num):
        return True
op = [x for x in range(2,20) if factor(x)]
print(op)

## SUNNY NUMBER
def sunny(n):
    m= (n+1)**0.5
    if m == int(m):
        print(f"{n} its sunny")
op = [i for i in range(1,10) if sunny(i)]
print(op)

## NEON NUMBER 
def neon(n):
    num1 = n
    m = n**2
    sum = 0
    while m > 0:
        id = m % 10
        sum+=id
        m=m // 10
    if sum == num1:
        print(f"{num1} its neon number")

op = [x for x in range(1,50) if neon(x)]
print(op)