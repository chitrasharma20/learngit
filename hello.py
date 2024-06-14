n=int(input())
arr=[n*i for i in range(1,11)]
print(arr)
for i in arr:
  arr[i]=arr[1]+arr[3]
