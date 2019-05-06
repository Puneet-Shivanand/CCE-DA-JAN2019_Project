import sys
import pprint
X=[]
Y=[]

def read_data():
    #adata=open('../data/anova_data.csv').readlines()  
    adata=open(sys.argv[1]).readlines()
    for line in adata:
        X.append(line.split(',')[0].strip())
        Y.append(line.split(',')[1].strip())
    del(X[0])
    del(Y[0])
    return (X,Y)


def square_it(x):
    return (x*x)


def print_out(n, DM, DT, DE, MSM, MSE, F, sumYi_Ycap, sumYi_Ybar, sumYcap_Ybar):
    print ( "DF       |\tSS          |\tMS         |\tF       |\n",
            "1       |\t%.2f   |\t%.2f  |\t%.2f   |\n" % (sumYcap_Ybar,MSM,F),
            "%.2f   |\t%.2f   |\t%.2f   |\n" %(n-2, sumYi_Ycap,MSE),
            "%.2f   |\t%.2f   |\t%.2f    |\n" % (n-1, sumYi_Ybar, (sumYi_Ybar/(n-1)))

           )
    return

def linear_reg(m=0,x=0,c=0):
    y_bar_sum = 0
    X,Y=read_data()
    for i in range(len(Y)):
        #print (Y[i])
        y_bar_sum = y_bar_sum + float(Y[i])
    y_bar = y_bar_sum/len(Y)

    y_cap=[]
    for i in range(len(Y)):
        ycap_i = float(Y[i])-y_bar
        y_cap.append(ycap_i)
    #print (y_cap, y_bar)

    ##Print y_cap_i and y_bar_i
    print (y_bar)
    print ('Y\t  (Y_cap - Y_bar)^2\t(Y_i - Y_CAP)^2\t  (Y_i - Y_bar)^2')
    #pp = pprint.PrettyPrinter(indent=4)
    sumYi_Ycap =0
    sumYi_Ybar =0
    sumYcap_Ybar =0
    for i in range(len(Y)):
#        print (float(Y[i]), y_cap[i])
#        print (float(Y[i]) - y_cap[i])
        print (("%.3f  \t%.3f     \t%.3f \t%.3f") % 
               (
                   float(Y[i]), 
                   square_it(y_cap[i] - y_bar), 
                   square_it(float(Y[i]) - y_cap[i]),
                   square_it(float(Y[i]) - y_bar) 
                )
               )
        sumYi_Ybar += square_it(float(Y[i]) - y_bar)
        sumYcap_Ybar += square_it(y_cap[i] - y_bar)
        sumYi_Ycap += square_it(float(Y[i]) - y_cap[i])

    print (sumYcap_Ybar, sumYi_Ycap, sumYi_Ybar)
    n = len(Y)
    DM =1 
    DE =n-2
    DT =n-1
    MSM = sumYcap_Ybar/DM
    MSE = sumYi_Ycap/DE
    F = MSM/MSE
    #print (MSM, MSE, sumYi_Ybar/DT)
    #print ("F Stastistic= %.3f" % F)
    print_out(n, DM, DT, DE, MSM, MSE, F, sumYi_Ycap, sumYi_Ybar, sumYcap_Ybar)
#        pprint.pprint([float(Y[i]), y_cap[i] - y_bar, float(Y[i]) - y_bar], indent=4)
    

linear_reg()
