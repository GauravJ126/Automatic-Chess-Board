"""
Created on Wed Nov  2 17:33:08 2022
@author: Venom
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import requests

# a  = requests.get("https://blynk.cloud/external/api/get?token=dWrCgptmsS4xrizRBImoXCTTlcukN7t9&v0")
# print(a.text)
# first_postion = str('d2')
# new_position = str('d4')
# x=first_postion+new_position
# original = str(x)
# loc = requests.get("https://blynk.cloud/external/api/update?token=dWrCgptmsS4xrizRBImoXCTTlcukN7t9&v0="+str(original))
# print(loc.status_code)
# a  = requests.get("https://blynk.cloud/external/api/get?token=dWrCgptmsS4xrizRBImoXCTTlcukN7t9&v0")#to check update
# print(a.text)

"""  
for printing the address  
for i in range (10):
    print("a",i,",b",i,",c",i,",d",i,",e",i,",f",i,",g",i,",h",i",")
    
for i in range (9):
    print((-3.5+i,-3.5),",",(-3.5+i,-2.5),",",(-3.5+i,-1.5),",",(-3.5+i,-0.5),",",(-3.5+i,0.5),",",(-3.5+i,1.5),",",(-3.5+i,2.5),",",(-3.5+i,3.5),",")

for i in range (16):
    print((-7+i,-7),",",(-7+i,-5),",",(-7+i,-3),",",(-4+i,-1),",",(-7+i,1),",",(-7+i,3),",",(-7+i,5),",",(-7+i,7),",")
"""

[a1 ,b1 ,c1 ,d1 ,e1 ,f1 ,g1 ,h1,
 a2 ,b2 ,c2 ,d2 ,e2 ,f2 ,g2 ,h2,
 a3 ,b3 ,c3 ,d3 ,e3 ,f3 ,g3 ,h3,
 a4 ,b4 ,c4 ,d4 ,e4 ,f4 ,g4 ,h4,
 a5 ,b5 ,c5 ,d5 ,e5 ,f5 ,g5 ,h5,
 a6 ,b6 ,c6 ,d6 ,e6 ,f6 ,g6 ,h6,
 a7 ,b7 ,c7 ,d7 ,e7 ,f7 ,g7 ,h7,
 a8 ,b8 ,c8 ,d8 ,e8 ,f8 ,g8 ,h8]=[(-7, -7) , (-5, -7) , (-3, -7) , (-1, -7) , (1, -7) , (3, -7) , (5, -7) , (7, -7) ,
                                  (-7, -5) , (-5, -5) , (-3, -5) , (-1, -5) , (1, -5) , (3, -5) , (5, -5) , (7, -5) ,
                                  (-7, -3) , (-5, -3) , (-3, -3) , (-1, -3) , (1, -3) , (3, -3) , (5, -3) , (7, -3) ,
                                  (-7, -1) , (-5, -1) , (-3, -1) , (-1, -1) , (1, -1) , (3, -1) , (5, -1) , (7, -1) ,
                                  (-7, 1) , (-5, 1) , (-3, 1) , (-1, 1) , (1, 1) , (3, 1) , (5, 1) , (7, 1) ,
                                  (-7, 3) , (-5, 3) , (-3, 3) , (-1, 3) , (1, 3) , (3, 3) , (5, 3) , (7, 3) ,
                                  (-7, 5) , (-5, 5) , (-3, 5) , (-1, 5) , (1, 5) , (3, 5) , (5, 5) , (7, 5) ,
                                  (-7, 7) , (-5, 7) , (-3, 7) , (-1, 7) , (1, 7) , (3, 7) , (5, 7) , (7, 7) ]

# print(a1)
# inputs
# old = np.array([-7,-7])#original coordinates
# new = np.array([-7,-3])#new coordinates

x=old = e1 #pawn first input
y=new =  h3#pawn second input
print("user input : e1h5")
print("equvivalent cartision cooredinates:",x,y)

# print("generated path: "  ,x,y)

def plot(x,y):
     
    dx, dy = 0.015, 0.05
    plt.xlim(-8,8,dx)#board limit across x-axis
    plt.ylim(-8,8,dy)#board limit accros y-axis
    axis=plt.gca()
    plt.plot(axis.get_xlim(),[0,0],'k--')
    plt.plot([0,0],axis.get_ylim(),'k--')
    plt.plot((old[0],new[0]),(old[1],new[1]))
    plt.plot(x,y,"ro")
    plt.grid()
    plt.show()  
def linesegment(P,Q):    
    S = P
    
    if P[1]==Q[1]:#parallel to x-axis
        if S[0]<=Q[0]:
            for x in range(S[0],(Q[0]+1),1):
                # y=S[1]
                # O=(np.array([x,y]))
                plot(x,P[1])
                
        elif S[0]>=Q[0]:
            for x in range(S[0],(Q[0]-1),-1):
                # y=S[1]
                # O=(np.array([x,y]))
                plot(x,P[1]) 
                
    m = (Q[1]-P[1])/(Q[0]-P[0])            
    #print(m)
    if P[0]==Q[0]:#parallel y-axis
        if S[1]<=Q[1]:
            for y in range(S[1],(Q[1]+1),1):
                # y=S[1]
                # O=(np.array([x,y]))
                plot(P[0],y)
                
        elif S[1]>=Q[1]:
            for y in range(S[1],(Q[1]-1),-1):
                # y=S[1]
                # O=(np.array([x,y]))
                plot(P[0],y) 
                
    if P[0]<Q[0]: #for slanting lines
        m = (Q[1]-P[1])/(Q[0]-P[0])
        for x in range(S[0],(Q[0]+1),1):
            y=S[1]+m*(x-S[0])
            # O=(np.array([x,y]))
            plot(x,y)
        
    elif P[0]>Q[0]: #for slanting lines
        m = (Q[1]-P[1])/(Q[0]-P[0])
        for x in range(S[0],(Q[0]-1),-1): 
            # print(P[0])
            y=Q[1]+m*(x-Q[0])
            # O=(np.array([x,y]))
            plot(x,y)
def coordinates(x,y):
        R = 11.9999999 #radius of arm
        t2 = math.acos(((x*x)+(y*y)-(2*R*R))/(2*R*R))
        if (x<0 and y<0):
            t2=(-1)*(t2)
              
        t1= math.atan (x/y) - ( math.atan ( (R*math.sin(t2)) / (R+R*math.cos(t2))))
        t1 = math.degrees(t1)
        t2 = math.degrees(t2)
        if (x >= 0 and y >= 0):       # 1st quadrant
            t1 = 90 - t1
            
        if (x < 0 and y > 0):       # 2nd quadrant
            t1 = 90 - t1;
            
        if (x < 0 and y < 0):        # 3d quadrant
            t1 = 270 - t1;
            
        if (x > 0 and y < 0):        # 4th quadrant
              t1 = -90 - t1;
            
        if (x < 0 and y == 0): 
              t1 = 270 + t1;
        # print('theta1',round(t1),'theta2=',round(t2))
        return(round(t1),round(t2)) 
def arms(t1,t2):
    
    # l1 = 5.65
    # l2 = 5.65

    n_theta = 36
    theta_start = 0
    theta_end = (math.pi)*2                             

    theta1 = []
    theta2 = []
    
    t2=n_theta

    for i in range(t1,t2):
    	tmp = theta_start + i*(theta_end - theta_start)/(n_theta - 1)
    	theta1.append(tmp)
    	theta2.append(tmp)

    # Base of the Robot
    # x0 = 0
    # y0 = 0
    # ct = 1   
'''#change in angle

a=coordinates(old) #original point
b=coordinates(new) #new point

a = [a[0],a[1]] #old
b = [b[0],b[1]] #new
print(a,b)

# while a!=b:
#     while ()
if b[0]<a[0]:
    while (a[0]>=b[0]):
        #print('t1 change',a[0])
        a[0]=a[0]-1
        

if b[0]>a[0]:
    while(a[0]<=b[0]):
        #print('t1 change',a[0])
        a[0]=a[0]+1
        

if b[1]<a[1]:
    while (a[1]>=b[1]):
        #print('t2 change',a[1])
        a[1]=a[1]-1
        

if b[1]>a[1]:
    while (a[1]<=b[1]):
        #print('t2 change',a[1])
        a[1]=a[1]+1
'''
linesegment(old, new)
#dWrCgptmsS4xrizRBImoXCTTlcukN7t9