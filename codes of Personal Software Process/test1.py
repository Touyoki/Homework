#sc_main
import math

f = open('data3.txt','r') #read the data from file
result = list()
for line in open('data3.txt'):
    line = f.readline()
    result.append(line)
length = len(result)
sum = 0.0
for data in result:
    sum = sum + float(data)
mean_1 = sum/length #calculate the mean
mean = round(mean_1,2)

sum_for_dev = 0
for data in result:
    sum_for_dev = sum_for_dev + pow(float(data)-mean,2)
dev_1 = math.sqrt(sum_for_dev/(length-1)) #calculate the dev
dev = round(dev_1,2)



#sc_calculate
print( "mean:" , mean)
print("dev:",dev)