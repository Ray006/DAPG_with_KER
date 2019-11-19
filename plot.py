import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
import operator 

def main( ):
    paths = ["log0.csv", "log1.csv","log2.csv","log3.csv"]
    color = ["gold","red", "blue","green"]
    lables = ["25_demo_without_KER(DAPG)", "1_demo_without_KER", "1_demo_with_KER1(ours)", "1_demo_with_KER2(ours)"]
    line = []

    plt.figure(num=1)

    # from ipdb import set_trace; set_trace()
    for i, path in enumerate(paths):
        # print(i,path)
        y = []
        x = []       

        data = pd.read_csv(path,encoding='gbk') # load the data
        y = data.loc[:,'success_rate']      # y axis
        x = np.linspace(0,len(y),len(y))   # x axis

        L, = plt.plot(x,y,color=color[i],linewidth=1.0)  # plot the figure one by one in the same picture
        line.append(L) # for legends


        x0, y0 = max(enumerate(y), key=operator.itemgetter(1)) # get the highest point of a curve
        plt.scatter(x0,y0,s=50,color=color[i])     # get a point(x0,y0), size = 50
        plt.plot([0,x0],[y0,y0], color[i], lw=0.2) # draw a line between two points ,black dashed，line width = 2.5

        plt.annotate(r'$(%s,%s)$'%(x0,y0),xy=(x0,y0),xycoords='data',xytext=(-100,+3),textcoords='offset points', 
             fontsize=8,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))  # 在图中做标注。要标注的内容是“(%s,%s)”，两个%s用%(x0,y0)传进来；设定目标点xy=(x0,y0)，并将其作为原坐标点xycoords='data'

    plt.legend(handles=line, labels=lables,loc='best')
    plt.title(u'Relocation Task')
    
    plt.xlabel('Iteration')
    plt.ylabel('success rate')

    new_ticks = np.linspace(0,100,11)  # divide to 11 parts from 0 to 100
    plt.yticks(new_ticks)

    plt.savefig('plot.png')
    plt.show()

    print ("Finished")
	
if __name__ == "__main__":
    main()


