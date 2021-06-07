#MATRIX ADDITION, MULTIPLICATION, TRANSPOSE 
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrixa = []
print("Enter the number for matrix A rowwise:")

for i in range(R):		 
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	matrixa.append(a)
print("\n")
for i in range(R):
	for j in range(C):
		print(matrixa[i][j], end = " ")
	print()

matrixb = []
print("Enter the numbers for matrix B rowwise:")

for i in range(R):		 
	a =[]
	for j in range(C):	 
		a.append(int(input()))
	matrixb.append(a)
print("\n")
for i in range(R):
	for j in range(C):
		print(matrixb[i][j], end = " ")
	print()
 
D = int(input("\nEnter the mathematical function: \n1.Addition\n2.Multiplication\n3.Transpose\n"))
print("\nRESULT:\n")
result=[[0 for i in range(C)] for i in range(R)]
resultb=[[0 for i in range(C)] for i in range(R)]
if D==1:   #ADDITION
    for i in range(R):
        for j in range(C):
            result[i][j]=matrixa[i][j]+matrixb[i][j]
    
    for i in range(R):
        for j in range(C):
            print(result[i][j], end = " ")
        print()

elif D==2:   #MULTIPLICATION
    for i in range(R):
        for j in range(C):
            for k in range(C): 
                result[i][j]+=matrixa[i][k]*matrixb[k][j]
    
    for i in range(R):
        for j in range(C):
            print(result[i][j], end = " ")
        print()

elif D==3: #TRANSPOSE
    for i in range(R):
        for j in range(C):
            result[j][i]=matrixa[i][j]
            resultb[j][i]=matrixb[i][j]
    for i in range(R):
        for j in range(C):
            print(result[i][j], end = " ")
        print()
    print("\n")
    for i in range(R):
        for j in range(C):
            print(resultb[i][j], end = " ")
        print()    
else:
    print("Wrong Value!!!")