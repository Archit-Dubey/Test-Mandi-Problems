N = int(input());
for i in range(1, N + 1):
    for j in range(1, N + 1):
        min = i if i < j else j;
        print(N - min + 1, end = "");
 
    for j in range(N - 1, 0, -1):
        min = i if i < j else j;
        print(N - min + 1, end = "");
    print();
   
'''
4444444
4333334
4322234
4321234
'''    