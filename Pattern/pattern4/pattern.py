def pattern(n):
    for i in range(n+1):
        for j in range(i):
            print(j+1,end="")
        print()

pattern(7)