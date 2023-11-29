import numpy as np
import matplotlib.pyplot as plt
P_x = 6
P_y = 6

plt.figure(1,figsize=(P_x,P_y))
number1 = 0
total_number = 0
for y in range(1,P_y,1):
    for x in range(1,P_x,1):
        number1 += 1
        plt.scatter(x,y,s=300,c='b')
        plt.text(x,y,number1,fontsize=20,verticalalignment='center',horizontalalignment='center')
number_2 = 0
for y in range(1,P_y,1):
    for x in range(1,(P_x-1),1):
        number_2+=1
        plt.scatter(x+0.5,y,s=300,c='r',marker='s')
        plt.text(x+0.5,y,number_2,fontsize=20,verticalalignment='center',horizontalalignment='center')

for y in range(1,(P_y-1),1):
    for x in range(1,P_x,1):
        number_2+=1
        plt.scatter(x,y+0.5,s=300,c='r',marker='s')
        plt.text(x,y+0.5,number_2,fontsize=20,verticalalignment='center',horizontalalignment='center')


number_3 = 0
for y in range(1,(P_y-1),1):
    for x in range(1,(P_x-1),1):
        number_3+=1
        plt.scatter(x+0.5,y+0.5,s=300,c='y',marker='s')
        plt.text(x+0.5,y+0.5,number_3,fontsize=20,verticalalignment='center',horizontalalignment='center')
#畫黃色方塊的左右線段
for y in range(1,(P_y-1),1):
    for x in range(1,(P_x-1),1):
        plt.plot([x,x+0.5],[y+0.5,y+0.5], color='black')
        plt.plot([x+0.5,x+1],[y+0.5,y+0.5], color='black')
#畫黃色方塊的上下線段
for y in range(1,(P_y-1),1):
    for x in range(1,(P_x-1),1):
        plt.plot([x+0.5,x+0.5],[y,y+0.5], color='black')
        plt.plot([x+0.5,x+0.5],[y+0.5,y+1], color='black')
#畫黃色方塊的左上左下線段
for y in range(1,(P_y-1),1):
    for x in range(1,(P_x-1),1):
        plt.plot([x+0.5,x],[y+0.5,y+1], color='black')
        plt.plot([x+0.5,x],[y+0.5,y], color='black')
        total_number+=1
#畫黃色方塊的右上右下線段
for y in range(1,(P_y-1),1):
    for x in range(1,(P_x-1),1):
        plt.plot([x+0.5,x+1],[y+0.5,y], color='black')
        plt.plot([x+0.5,x+1],[y+0.5,y+1], color='black')
#############
#線編號
line_count = 1
for y in np.arange(1,P_y,0.5):
    for x in np.arange(1,P_x,0.5):
        if x < P_x-1 and y < P_y-1:
            plt.text(x+0.2, y+0.25, str(line_count), ha='center', va='center',color='black') #設定斜線字體
            line_count+=1
for y in np.arange(1,P_y,0.5):
    for x in np.arange(1,P_x,1):
        if x<P_x-1 and y<P_y-1:
            plt.text(x+0.5, y+0.25, str(line_count), ha='center', va='center',color='black') #設定直線字體
            line_count+=1
for y in np.arange(1,P_y,1):
    for x in np.arange(1,P_x,0.5):
        if x<P_x-1 and y<P_y-1:
            plt.text(x+0.25, y+0.5, str(line_count), ha='center', va='center',color='black') #設定橫線字體
            line_count+=1
#畫最外圍四方形
number_4 = 0
for y in range(1,2,1):
    for x in range(1,P_x,1):
        number_4+=1
        plt.scatter(x,y-0.5,s=300,c='g',marker='s')
        plt.text(x,y-0.5,number_4,fontsize=20,verticalalignment='center',horizontalalignment='center')
        plt.plot([x,x],[y-0.5,y], color='black')#畫線段
        plt.text(x, y-0.3, str(line_count), ha='center', va='center',color='black') #設定橫線字體
        line_count+=1
for y in range(1,P_y,1):
    for x in range(P_x,P_x+1,1):
        number_4+=1
        plt.scatter(x-0.5,y,s=300,c='g',marker='s')
        plt.text(x-0.5,y,number_4,fontsize=20,verticalalignment='center',horizontalalignment='center')
        plt.plot([x-0.5,x-1],[y,y], color='black')#畫線段
        plt.text(x-0.7, y, str(line_count), ha='center', va='center',color='black') #設定橫線字體
        line_count+=1
for y in range(P_y,P_y+1,1):
    for x in range(P_x,1,-1):
        number_4+=1
        plt.scatter(x-1,y-0.5,s=300,c='g',marker='s')
        plt.text(x-1,y-0.5,number_4,fontsize=20,verticalalignment='center',horizontalalignment='center')
        plt.plot([x-1,x-1],[y-0.5,y-1], color='black')#畫線段
        plt.text(x-1, y-0.8, str(line_count), ha='center', va='center',color='black') #設定橫線字體
        line_count+=1
for y in range(P_y,1,-1):
    for x in range(1,2,1):
        number_4+=1
        plt.scatter(x-0.5,y-1,s=300,c='g',marker='s')
        plt.text(x-0.5,y-1,number_4,fontsize=20,verticalalignment='center',horizontalalignment='center')
        plt.plot([x-0.5,x],[y-1,y-1], color='black')#畫線段
        plt.text(x-0.2, y-1, str(line_count), ha='center', va='center',color='black') #設定橫線字體
        line_count+=1
#############
plt.axis("off")
plt.show()