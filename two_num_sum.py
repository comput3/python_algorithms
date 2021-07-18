#time O(nLog(n))
#space O(1)
def two_num_sum(array, target_sum):
	array.sort()
	left_most_value = 0
	right_most_value = len(array) -1
	while left_most_value < right_most_value:
	    test_sum = array[left_most_value] + array[right_most_value]
	    if test_sum == targetSum:
	        return [array[right_most_value], array[left_most_value]]
	    elif test_sum < target_sum:
		      left_most_value += 1
	    elif test_sum > target_sum:
		      right_most_value -= 1
	return []

{
  "array": [3, 5, 7, 8, 11, 1, -1, 6],
  "targetSum": 9
}
