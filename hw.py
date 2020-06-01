# while
num = -1
while True:
    num = num + 1
    if num <= 100:
        if (num-3)%10 == 0: continue
        if (num-4)%10 == 0: continue
        print(num)
    else: break

#for
num = range(0, 101)

for i in num:
    if (i-3)%10==0: continue
    if (i-4)%10==0: continue
    else: print(i)