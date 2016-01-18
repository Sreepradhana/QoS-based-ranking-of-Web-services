__author__ = 'sreepradhanathirumalaiswami'
import math
import argparse
def main(args):
    trainingimage=[]
    traininglabel=[]
    testingimage=[]
    testinglabel=[]
    resprob=[]
    Posteriori=[]
    nonblanktraining=[] #features count for each i,j
    classprobability=[] # proior probabilities of num 0 to 9
    classfrequencies=[]
    classificationoutput=[]
    match=0
    truepos=0
    matchclass=[]
    total=0
    precision=[]
    recall=[]
    Fscore=[]
    trueneg=[]
    falseneg=[]
    m=args.trainingnum
    n=args.testingnum
    TrainingHandle = open(args.traininginput, 'r')
    #for line in fileHandle:
        #print line

    #param= fileHandle.readline()
    #print fileHandle
    j=0

    for num in xrange(0,10):
        falseneg.append(int('0'))
        trueneg.append(int('0'))
        matchclass.append(int('0'))
        Posteriori.append(int('0'))
        classprobability.append(int('0'))
        nonblanktraining.append([])
        for numi in xrange(0,28):
            nonblanktraining[num].append([])
            for numj in xrange(0,28):
                nonblanktraining[num][numi].append(int('0'))
    #print nonblanktraining[2][10][0]
    for i in xrange(0,m):
        trainingimage.append([])

        for j in xrange(0,28):
            trainingimage[i].append([])

            line=TrainingHandle.readline().rstrip('\n')
            for k in xrange(0,28):

                trainingimage[i][j].append([])

                trainingimage[i][j][k].append(line[k])

    #print trainingimage[4999][10]




    TraininglabelHandle = open(args.traininglabels, 'r')
    for i in xrange(0,m):


            traininglabel.append([])
            line = TraininglabelHandle.readline().rstrip('\n')
            traininglabel[i].append(line)




    for i in xrange(0,m):
        for j in xrange(0,28):
            for k in xrange(0,28):
                #print trainingimage[i][j][k][0]
                if(trainingimage[i][j][k][0] is '+' or trainingimage[i][j][k][0] is '#'):
                    label=traininglabel[i][0]
                    #for x in  nonblanktraining[int(label)][j][k]
                    #nonblanktraining[int(label)][j][k] = [x+1 for x in nonblanktraining[int(label)][j][k]]
                    nonblanktraining[int(label)][j][k] = int(nonblanktraining[int(label)][j][k])+1
    #nonblanktraining[2][9][0]=int(nonblanktraining[2][9][0])+1
    #print nonblanktraining[2][9]

    for i in xrange(0,m):
        label=traininglabel[i][0]
        classprobability[int(label)]=int(classprobability[int(label)]) +1
    classfrequencies=classprobability
    classprobability = [x/float(m) for x in classprobability]
    #for x in classprobability:
    #    x=x/5000
    #print "CLASS FREQUENCIES"
    #print classfrequencies
    #print "CLASS PROBABILITY"
    #print classprobability
    # performing laplace smoothing
    for i in xrange(0,10):
        for j in xrange(0,28):
            for k in xrange(0,28):
                nonblanktraining[i][j][k] = int(nonblanktraining[i][j][k])+1
                nonblanktraining[i][j][k]=int(nonblanktraining[i][j][k])/(float(classfrequencies[i])+2)
                #if(j==20 and k== 20):
                #print "nbt of ",i,"is",nonblanktraining[i][j][k]
                #nonblanktraining=[x/float(classfrequencies[i][0]) for x in nonblanktraining]
    #print nonblanktraining[2][9]

    TestingHandle = open(args.testinginput, 'r')
    for num in xrange(0,10):
        resprob.append(int('0'))


    for i in xrange(0,n):
        testingimage.append([])

        for j in xrange(0,28):
            testingimage[i].append([])

            line=TestingHandle.readline().rstrip('\n')
            for k in xrange(0,28):

                testingimage[i][j].append([])

                testingimage[i][j][k].append(line[k])


    TestinglabelHandle = open(args.testinglabels, 'r')
    for i in xrange(0,n):


            testinglabel.append([])
            line = TestinglabelHandle.readline().rstrip('\n')
            testinglabel[i].append(line)
    classification=0
    for temp in xrange(0,n):
        classification=0
        for x in xrange(0,10):
            Posteriori[x]=0
        for x in xrange(0,10):
            Posteriori[x]=Posteriori[x]+math.log(classprobability[x])
            #print "Posteriori",x,"is",Posteriori[x]
            for y in xrange(0,28):
                for z in xrange(0,28):
                    #Posteriori[x]=Posteriori[x]+math.log(nonblanktraining[i][j][k])
                    if(testingimage[temp][y][z][0] is '+' or testingimage[temp][y][z][0] is '#'):
                        #print "nonblanktarining",x,y,z,nonblanktraining[x][y][z]
                        Posteriori[x]=Posteriori[x]+math.log(nonblanktraining[x][y][z])

                    else:
                        Posteriori[x] = Posteriori[x]+math.log(1-nonblanktraining[x][y][z])

                    """     Posteriori[x]=Posteriori[x]+math.log(1-nonblanktraining[x][y][z])
                    else:
                    """

            #print "Posteriori"
            #print Posteriori[x]
            if(Posteriori[x]>Posteriori[classification]):
                classification=x
        #print "classification",classification,"testing",testinglabel[temp][0]
        classificationoutput.append(classification)
        for z in xrange(0,10):
            if(classification!=z and int(testinglabel[temp][0])!=z):
                trueneg[z]=trueneg[z]+1

        if(classification==int(testinglabel[temp][0])):
            match =match+1
            matchclass[classification]=matchclass[classification]+1
            #print match
    #print matchclass[classification]
    print "Number of correct classifications",match
    print "Accuracy",match/float(n)
    print "Accuracy in percentage",(match/float(n))*100
    #print classification
    #print classificationoutput
    f = open('classificationoutput.txt','w')
    for x in classificationoutput:
        f.write(str(x))
        f.write("\n")

    print "Confusion matrix parameters' computation"
    for x in xrange(0,10):
        total=0
        pos=0
        truepos=0
        for y in testinglabel:
            #print y[0]
            #print "x",x

            if(int(y[0])==x):
                total=total+1
                #print pos
                pos=pos+1
        print "Number of occurences of ",x,"is",total
        print "True positive count",matchclass[x]
        precision.append(matchclass[x]/float(total))
        falseneg[x]=total- matchclass[x]
        recall.append(trueneg[x]/float(trueneg[x]+falseneg[x]))
        Fscore.append(2*precision[x]*recall[x]/float(precision[x]+recall[x]))
        print "Falseneg of ",x ,"is ", falseneg[x]
        print "Trueneg of", x, " is ", trueneg[x]
    for i in xrange(0,10):
        print "precision of ", i ," is",precision[i]

    for i in xrange(0,10):
        print "Recall measure of ", i ," is",recall[i]

    for i in xrange(0,10):
        print "F-score of ",i , "is", Fscore[i]

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Final Project")
    parser.add_argument("--traininginput",type=str)
    parser.add_argument("--traininglabels",type=str)
    parser.add_argument("--testinginput",type=str)
    parser.add_argument("--testinglabels",type=str)
    parser.add_argument("--trainingnum",type=int)
    parser.add_argument("--testingnum",type=int)
    args=parser.parse_args()
    main(args)
