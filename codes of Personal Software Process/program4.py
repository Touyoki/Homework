#sc_cal_mean_and_dev
import math


def cal_mean_and_dev(data,length):
    mean_1=sum(data)/length
    sum_for_dev = 0.0
    for x in data:
        sum_for_dev = sum_for_dev + pow(float(x) - mean_1, 2)
    dev_1= math.sqrt(sum_for_dev / (length - 1))  # calculate the dev
    return mean_1,dev_1

#sc_cal_ranges
def cal_ranges(mean,dev):
    r_vs=mean-2*dev
    r_s=mean-dev
    r_m=mean
    r_l=mean+dev
    r_vl=mean+2*dev
    vs=round(pow(math.e,r_vs),4)
    s=round(pow(math.e,r_s),4)
    m=round(pow(math.e,r_m),4)
    l=round(pow(math.e,r_l),4)
    vl=round(pow(math.e,r_vl),4)
    print("VS,S,M,L,VL:")
    print(vs,s,m,l,vl)

#sc_main
f = open('d4.txt','r') #read the data from file
# f = open('d5.txt','r') #read the data from file
test_x = 1
test_y = 2
# test_z = 2
length=0
result = list()
for line in open('d4.txt', 'r'):
# for line in open('d5.txt', 'r'):
    line = f.readline()
    Xk = float(line.split('\t', 3)[test_x])
    Yk = float(line.split('\t', 3)[test_y])
    # Zk = line.split('\t', 3)[test_z]
    length = length+1
    lgX=math.log(Xk/Yk)
    result.append(lgX)
mean,dev=cal_mean_and_dev(result,length)
# print(mean)
# print(dev)
cal_ranges(mean,dev)