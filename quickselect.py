def partition(arr,start,end):
	pivot = arr[start]
	pivot_index=start
	start+=1
	size = len(arr)-1
	while start < end:
		while start!=size and arr[start] <= pivot:
			start+=1
		while arr[end] > pivot :
			end-=1
		if start < end:
			arr[start],arr[end] = arr[end],arr[start]
	arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
	return end

def quickSelect(k,arr,start,end):
	pivot_index = partition(arr,start,end)
	if pivot_index == k:
		return print(arr[pivot_index])
	else:
		if pivot_index < k:
			return quickSelect(k,arr,pivot_index+1,end)
		else:
			return quickSelect(k,arr,start,pivot_index-1)
arr=[x for x in range(10,0,-1)]
print(quickSelect(5,arr,0,len(arr)-1))
