#sc_list_structure
import math
class D_data:
  def __init__(self, Xk, Yk,next):
    self.Xk = Xk
    self.Yk = Yk
    self.next = next
class C_list:
    def __init__(self):
        self.root = None
    def addNode(self,Xk,Yk):
        newNode = D_data(Xk=Xk,Yk=Yk,next=None)
        if self.root==None:
            self.root=newNode
        else:
            cursor = self.root
            while cursor.next != None:
                cursor=cursor.next
            cursor.next=newNode

#used to decide which number to select to use in a file
#sc_io
def calregression(digit1,digit2,xk):
 test_x=digit1
 test_y=digit2

 t_list=C_list()
 f = open('d3.txt','r') #read the data from file
 for line in open('d3.txt','r'):
    line = f.readline()
    Xk = line.split('\t',3)[test_x]
    Yk = line.split('\t',3)[test_y]
    t_list.addNode(Xk,Yk)

#sc_calculate
 x_tot=0
 y_tot=0
 xy_tot=0
 x2_tot=0
 y2_tot=0
 n=0
 first=t_list.root
 while first!=None:
    x_tot = x_tot + float(first.Xk)
    y_tot = y_tot + float(first.Yk)
    xy_tot = xy_tot + float(first.Xk)*float(first.Yk)
    x2_tot = x2_tot + float(first.Xk)*float(first.Xk)
    y2_tot = y2_tot + float(first.Yk)*float(first.Yk)
    n = n + 1
    first=first.next
 # print(xy_tot,x2_tot,n)
 x_avg=x_tot/n
 y_avg=y_tot/n
 # print(x_avg,y_avg)


 #m1 m2 m3 m4 m5 are only used to calculate
 m1=xy_tot-n*x_avg*y_avg
 m1 = round(m1,0)
 m2=x2_tot-n*pow(x_avg,2)
 m2 = round(m2,0)
 # print(m1,m2)
 bate1 = m1/m2
 bate1 = round(bate1,6)
 # print(bate1)
 bate0=y_avg-bate1*x_avg
 bate0=round(bate0,4)
 # print(bate0,bate1)

 m3=n*xy_tot-x_tot*y_tot
 m4=(n*x2_tot-pow(x_tot,2))*(n*y2_tot-pow(y_tot,2))
 r_xy=m3/pow(m4,1/2)
 r2=pow(r_xy,2)
 r_xy=round(r_xy,4)
 r2=round(r2,4)
 # print(r_xy,r2)

 x_test=xk
 y_test=bate0 + bate1 * x_test
 y_test=round(y_test,4)
 print("beta0 and beta1 :",bate0,bate1)
 print("rxy and r2 :",r_xy,r2)
 print("yk:",y_test)

#sc_test
print("test1")
y1=calregression(0,2,386) #test1
print('\n')
print("test2")
y2=calregression(0,3,386) #test2
print('\n')
print("test3")
y3=calregression(1,2,386) #test3
print('\n')
print("test4")
y4=calregression(1,3,386) #test4
