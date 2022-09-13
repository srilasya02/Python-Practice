f1=open("file1.txt","r")
f2=open("file2.txt","r")
l1=f1.readlines()
l2=f2.readlines()
l2_num=[int(k) for k in l2]
print(l2_num)

# Write your code above 👆
result=[int(num) for num in l1 if int(num) in l2_num]

print(result)


