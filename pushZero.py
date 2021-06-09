def pushZero_at_right(array):
	size=len(array)
	store=size-1
	for i in range(size):
		if i >= store:
			break
		if array[i] == 0 :
			while array[store] == 0 :
				store-=1
			array[store],array[i] = array[i],array[store]
	return array

array=[3,2,0,0,8,5,31,0,25]
print(pushZero_at_right(array))
