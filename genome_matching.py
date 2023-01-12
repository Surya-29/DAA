str1=input("Enter the String 1:")
str2=input("Enter the String 2:")
str3=''
str4=''



n,m=len(string1)+1,len(string2)+1
matrix=[[0]*n for i in range(m)]


for i in range(n-1):
    for j in range(m-1):
        if(string1[j]==string2[i]):
            matrix[i+1][j+1]= matrix[i][j]+2
        else:
            matrix[i+1][j+1]= max(matrix[i][j],matrix[i][j+1],matrix[i+1][j])-1

            

def backtracking(i, j, str3, str4):
    if i == 0 and j == 0:
        return str4[::-1], str3[::-1]
    else:
        if str1[j-1] == str2[i-1]:
            str3 += str1[j-1]
            str4 += str2[i-1]
            return backtracking(i-1, j-1, str3, str4)
        else:
            if matrix[i][j-1] == max(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]):
                str3 += '_'
                str4 += str1[j-1]
                return backtracking(i, j-1, str3, str4)
            else:
                str4 += '_'
                str3 += str2[i-1]
                return backtracking(i-1, j, str3, str4)

str3,str4=backtracking(n-1,m-1,str3,str4)

print("Genome String:",str3,str4,sep='\n')