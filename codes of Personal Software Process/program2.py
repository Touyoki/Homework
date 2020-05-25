#sc_functions
#Name:  Zhang Wensheng
#Date: 20/05/21
#Description: Count the loc of each parts of the program

#def check_nullline(string)
#purpose:check if this line is a null line
def check_nullline(string):
    string = string.replace(' ','')
    # string.replace('\r','')
    # string.replace('\n', '')
    # string=string.strip()
    if(string in ['\n','\r\n']):
      return bool(1)
    else:
     return bool(0)

#def check_def(string)
#purpose:check if this line is a function
def check_def(string):
    if('def'==string[0:3]):
      return bool(1)
    else:
     return bool(0)

#def check_comment(string)
#purpose:check if this line is a comment
def check_comment(string):
    first_c = string[0]
    if('#'==first_c):
        if('sc_'!=string[1:4]):
            return 0,'yes'
        else:
            return 1,string.replace('#sc_','')
    else:
        return 2,'no'

#sc_main
f = open('program2.py', 'r')
# f = open('test1.py', 'r')
num_loc = 0 #total loc of program
num_of_part = 0
loc_part = 0 #loc of part
tmp_noOf_it = 0 #the number of item
# first_part_name = 'main'
nm_new ='main'
nm_list = list()
it_list = list()
no_list = list()

for line in open('program2.py'):
# for line in open('test1.py'):
    # print('length of line',num_loc,len(line))
    line = f.readline()
    if check_nullline(line):
        continue
    else:
        line = line.replace(' ', '')

        flg_1,flg_2=check_comment(line)
        if(0==flg_1):
            continue
        elif(1==flg_1):
            if(num_of_part!=0):
                it_list.append(tmp_noOf_it)#record the number of item
                nm_list.append(nm_new)#record the name of the part
                no_list.append(loc_part)#record the loc of the part
            num_of_part = num_of_part + 1
            nm_new = flg_2
            loc_part=0
            tmp_noOf_it=0
        else: #should be counted
            # print(line)
            if(check_def(line)):#count the functions in this part
                tmp_noOf_it = tmp_noOf_it + 1
            loc_part = loc_part + 1
            num_loc = num_loc + 1
if(num_of_part == 0):
    num_of_part=1


it_list.append(tmp_noOf_it)
nm_list.append(nm_new)
no_list.append(loc_part)

for i in range(num_of_part):
    print("part name:",nm_list.pop(0).replace('\n',''))
    print("number of items:",it_list.pop(0))
    print("loc of the part:",no_list.pop(0))
    print('\n')

print("total loc:",num_loc)