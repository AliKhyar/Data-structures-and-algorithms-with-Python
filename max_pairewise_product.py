import random

def naive_solution(array):
	result = 0
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i]*array[j] > result:
				result = array[i]*array[j]
	return result 

def fast_solution(array):
	pairs = [array[0], array[1]]
	for i in range(2,len(array)):
		min_pairs_idx = pairs.index(min(pairs)) 
		if (array[i] > pairs[min_pairs_idx]):
			pairs[min_pairs_idx] = array[i]
	return pairs[0]*pairs[1]

def main():
	# while(True):
    	
  # 	n = random.randint(2,11)
	# 	random_array = random.sample(range(1, 1000), n)
	# 	naive_result = naive_solution(random_array)
	# 	fast_result = fast_solution(random_array)
	# 	if naive_result != fast_result:
	# 		print(f"Doesn't match for n res: {naive_result} and f res: {naive_result}")
	# 		break
	# 	else:
	# 		print(random_array)
	# 		print('OK')
  n = int(input('enter the useless length of ur array: ')) #useless
  array = list(map(int, input('enter the array like: 14 25 85').strip().split()))
  
  print(fast_solution(array))

if __name__=='__main__':
	main()
  
