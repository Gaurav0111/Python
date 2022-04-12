a = [1,2,3,4,5,6,7,8,9,10]
# for counti in a:
    # print(counti)

# for count in a :
#     if (count < 8):
#         print(count)

#     print("")
#     if(count <= 4):
#         print((count+1))
# i = 0
# while( i  < 10):
#     print(a[i])
#     i += 1

no = int(input("Enter the number of rows : "))

for i in range(no+1):
    for j in range(i+1):
        print("*")