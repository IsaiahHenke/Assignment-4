import numpy as np

#Load both the base data and the mult data as an array.
packet_base = np.genfromtxt('packet_base.txt', delimiter=',')
packet_weight = np.genfromtxt('packet_weight.txt', delimiter=',')

#Separate your data into chunks of 8. 
row = packet_base.size//8
base_array = packet_base.reshape(row, 8)
weight_array = packet_weight.reshape(row, 8)

#Multiply your base array by your weight values for every element.
product = base_array * weight_array

#Find the minimum, maximum, mean and result.
min = np.min(product, axis=1)
max = np.max(product, axis=1)
mean = np.mean(product, axis=1)

result = (max-mean)*max

#Find the sum of all your chunk results and round down to the next integer.
sum = np.sum(result)

#Find the remainder if you divided by 4096.
remainder = sum % 4096
answer = remainder // 1

print(answer)