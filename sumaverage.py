def calculate_stats(l):
	if not l:
		return 0,0
	total_sum=sum(l)
	average=total_sum/len(l)
	return total_sum,average

mu_list=[10,20,30,40,50]
s,a=calculate_stats(my_list)
