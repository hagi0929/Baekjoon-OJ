for i in range(1,50):
    print((2 * (10 ** i) - 1)+sum([(8*j)*(10**j) for j in range(i)])-i)