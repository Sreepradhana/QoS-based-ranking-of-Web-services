###########################################
# you need to implement five funcitons here
###########################################
n=11
m=3
k=4
iteration=0
output=[]
output2=[]
output3=[]
output4=[]
count=0
count2=0
count3=0
c4=0
c5=0
e=[]
val={}
import random
conflictval={}
from Queue import PriorityQueue
from Queue import *
import copy

def backtracking(filename):

    board1=readGameState(filename)
    global output,count

    backtrackingEval(board1,0)

    return (output, count)


def backtrackingMRV(filename):
    ###
    # use backtracking + MRV to solve sudoku puzzle here,
    # return the solution in the form of list of 
    # list as describe in the PDF with # of consistency
    # checks done
    ###
    board1=readGameState(filename)
    global output2,c2
    backtrackingMRVEval(board1)


    
    return (output2, count2)

def backtrackingMRVfwd(filename):
    ###
    # use backtracking +MRV + forward propogation
    # to solve sudoku puzzle here,
    # return the solution in the form of list of 
    # list as describe in the PDF with # of consistency
    # checks done
    ###
    board1=readGameState(filename)
    global e,val
    e,val=emp(board1)
    backtrackingFwdEval(board1)
    global output3,count3
    #print "EMPTY LOC",e
    #print "VALUES",v[(0,1)]
    return (output3, count3)

def backtrackingMRVcp(filename):
    ###
    # use backtracking + MRV + cp to solve sudoku puzzle here,
    # return the solution in the form of list of 
    # list as describe in the PDF with # of consistency
    # checks done
    ###
    board1=readGameState(filename)
    backtrackingMRVcpEval(board1)
    global output4,c4
    return (output4, c4)

def minConflict(filename):
    ###
    # use minConflict to solve sudoku puzzle here,
    # return the solution in the form of list of 
    # list as describe in the PDF with # of consistency
    # checks done
    ###

    board1=readGameState(filename)
    b=minConflictEval(board1)
    global c5
    return (b, c5)


def backtrackingEval(board,ccount): #recursive function for backtracking
    global n,m,k,count
    row=0
    col=0


    flag=0

    # finds first unassigned value
    for row1 in range(int(n)):
        for col1 in range(int(n)):

            if (board[row1][col1]=='-'):
                flag=flag+1
                if(flag==1):
                    row=row1
                    col=col1

    #if there are no unassigned values ,the board is returned as the desired output
    if flag==0:
        global output
        output=board

        return True
    else:



        #checks for a possible number to assign for the unassigned cell by checking along row,col and grid
        for n1 in range(1,int(n)+1):
            recurval=0
            count=count+1 #consistent check count incremented
            for c in range(int(n)):


                     if board[row][c] == n1:

                         recurval=recurval+1

            for r in range(int(n)):

                     if board[r][col] == n1:
                         recurval=recurval+1

            for r1 in range(int(m)):
                for  c1 in range(int(k)):

                    if (board[r1+row-(row%int(m))][c1+col-(col%int(k))] == n1):
                        recurval=recurval+1

            if(recurval==0):

                board[row][col]=n1



                if (backtrackingEval(board,ccount)):

                    return True

                board[row][col] = '-' #backtracking

        return False


def backtrackingMRVEval(board):#backtracking with minimum remaining values
    global n,m,k,count2
    row=0
    col=0


    flag=0
    #checks if there are no unassigned cells in the cell,if true returns the board as output
    for row1 in range(int(n)):
        for col1 in range(int(n)):

            if (board[row1][col1]=='-'):
                flag=flag+1


    if flag==0:
        global output2
        output2=board

        return True
    else:

        #getting the variale with minimum remaining value from a priority queue
        queue=MRV(board)
        nextplace=queue.get()

        row=nextplace[1][0]
        col=nextplace[1][1]
        #checking constraints
        for n1 in range(1,int(n)+1):
            recurval=0
            count2=count2+1 #consistent check count incremented
            for c in range(int(n)):
                     #print "row check",board[row][c]
                     if board[row][c] == n1:
                         recurval=recurval+1
            for r in range(int(n)):
                     if board[r][col] == n1:
                         recurval=recurval+1
            for r1 in range(int(m)):
                for  c1 in range(int(k)):

                    if (board[r1+row-(row%int(m))][c1+col-(col%int(k))] == n1):
                        recurval=recurval+1

            if(recurval==0):

                board[row][col]=n1



                if (backtrackingMRVEval(board)):

                    return True

                board[row][col] = '-' #backtracking

        return False




def backtrackingFwdEval(board):# backtracking with mrv and forward checking
    global n,m,k,count3
    row=0
    col=0
    global iteration
    global e,val
    flag=0
    #checking for unassigned cells
    for row1 in range(int(n)):
        for col1 in range(int(n)):

            if (board[row1][col1]=='-'):
                flag=flag+1


    if flag==0:

        global output3
        output3=board
        return True
    else:

        #getting variable with minimum remaining value
        queue=MRV(board)
        nextplace=queue.get()

        row=nextplace[1][0]
        col=nextplace[1][1]
        #finding the last remaining value for a cell after it's neighbours have been checked for constarints
        for n1 in val[(row,col)]:

            temp=copy.deepcopy(val)# storing a copy of previous state in case it backtracks
            result=prune(board,n1,row,col)# checks if all the neighbours have a valid value which can be assigned to it
            if(result==True):


                board[row][col]=n1

                if (backtrackingFwdEval(board)):

                    return True

                board[row][col] = '-' #backtracking
                val=temp #restoring values of neighbours since it is backtracking


        return False
def backtrackingMRVcpEval(board):
    global n,m,k,c4
    row=0
    col=0
    global iteration

    flag=0
    #finding if there is an unassigned cell
    for row1 in range(int(n)):
        for col1 in range(int(n)):

            if (board[row1][col1]=='-'):
                flag=flag+1



    if flag==0:

        global output4
        output4=board
        return True
    else:

        #getting the priority queue with variables and the number of values each can be assigned
        queue=MRV(board)
        nextplace=queue.get()
        #getting the cell position which has minimum remaining values
        row=nextplace[1][0]
        col=nextplace[1][1]
        #consistency check along row,col and grid
        #c4=c4+1
        for n1 in range(1,int(n)+1):
            c4=c4+1 #consistent check count incremented
            recurval=0
            for c in range(int(n)):

                     if board[row][c] == n1:
                         recurval=recurval+1
            for r in range(int(n)):
                     if board[r][col] == n1:
                         recurval=recurval+1
            for r1 in range(int(m)):
                for  c1 in range(int(k)):

                    if (board[r1+row-(row%int(m))][c1+col-(col%int(k))] == n1):
                        recurval=recurval+1

            if(recurval==0):
                #evoking constraint propogation
                cp(board)
                board[row][col]=n1




                if (backtrackingMRVcpEval(board)):

                    return True

                board[row][col] = '-' #backtracking

        return False
def minConflictEval(board):
    global n,c5
    #assigning values for all cells depending for which it poses minimum conflicts with its neighbours along row,column and grid
    for row1 in range(int(n)):
        for col1 in range(int(n)):
            val=minc(board,row1,col1) #getting a value that has minimum conflicts
            board[row1][col1]=val
    for i in range(10000): #repeat conflict resolution until a maximum threshold
        #getting all cell positions in the board with conflicts
        c=conflicts(board)
        c5=c5+1 #consistent check count incremented
        if c==[]:#if there are no conflicts then it is the desired output
            return board
        row,col=random.choice(c) #picking a random conflicting cell position

        num=minc(board,row,col)# assign a value that poses minimum conflict with its neighbours
        board[row][col]=num
    return board


#returns a list of conflicting cell positions in the current board
def conflicts(board):

    conlist=PriorityQueue()
    clist=[]
    global conflictval,n,m,k
    #consistency check along col,row and grid
    for row in range(int(n)):
        for col in range(int(n)):
            recurval=0
            for c in range(int(n)):
                     #print "row check",board[row][c]
                     if board[row][c] == board[row][col]:
                         recurval=recurval+1
            for r in range(int(n)):
                     if board[r][col] == board[row][col]:
                         recurval=recurval+1
            for r1 in range(int(m)):
                for  c1 in range(int(k)):

                    if (board[r1+row-(row%int(m))][c1+col-(col%int(k))] == board[row][col]):
                        recurval=recurval+1
            if(recurval>3):
                clist.append((row,col))
                conlist.put((recurval,(row,col)))
                #conflictval[(row,col)]=recurval

    return clist


#returns the value to be assigned in a particular row,col for which the number of conflicts is minimum
def minc(board,row,col):
    global n,m,k
    pq=PriorityQueue()
    #checks for consistency along row,col and grid
    for n1 in range(1,int(n)+1):
            recurval=0
            for c in range(int(n)):
                     if board[row][c] == n1:
                         recurval=recurval+1
            for r in range(int(n)):
                     if board[r][col] == n1:
                         recurval=recurval+1
            for r1 in range(int(m)):
                for  c1 in range(int(k)):

                    if (board[r1+row-(row%int(m))][c1+col-(col%int(k))] == n1):
                        recurval=recurval+1

            pq.put((recurval,n1)) #include each possible number with the number of conflicts it creates inside a priority queue

    number=pq.get()# get number with minimum conflicts

    return number[1]

#propogates constraints throughout the board
def cp(board):
    q=Queue()
    global c4
    global e #list of empty cells in board
    c4=c4+1 #consistent check count incremented
    for i in e:

        nei=neighborscheck(board,i[0],i[1])# getting neighbours of each cell
        for n in nei:

            q.put((i,n)) #adding the parent and neighbour of each ar inside queue
    while not q.empty():
        element=q.get()
        parent=element[0]
        nc=element[1]
        if consistencycheck(parent,nc):#checking the parent ,child pair for inconsistencies
            np=neighborscheck(board,parent[0],parent[1])
            np.remove(nc) #if the child is consistent then we remove it from set of neighbours
            for j in np: # back arc checking

                q.put((j,parent))

#checking for consistency between a particular parent and child
def consistencycheck(p,c):
    flag=False
    global val,c4

    temp=copy.deepcopy(val[p]) #retaining a copy of possible values for the parent
    for i in temp: # checking each possible value of parent
        valctemp=copy.deepcopy(val[c])
        if i in valctemp: #if the value in parent is also present in child
            valctemp.remove(i) #that value is removed from the child's set of values
        if len(valctemp)==0: #if that causes for the child of the arc to have no vlaues
            val[p].remove(i) #then we remove that value from the parent
            flag=True
    return flag
#returns a list of neighbouring cells that are unassigned
def neighborscheck(board1,row,col):

    neighbors=[]
    global n
    global m
    global k
    emptynei=[]
    for c in range(int(n)):
        if board1[row][c] == '-':
            emptynei.append((row,c))
    for r in range(int(n)):
        if board1[r][col] == '-':
            emptynei.append((r,col))

    for r1 in range(int(m)):
            for  c1 in range(int(k)):
                if board1[r1+row-(row%int(m))][c1+col-(col%int(k))] == '-':
                    emptynei.append((r1+row-(row%int(m)),c1+col-(col%int(k))))

    for em in emptynei:
        if em not in neighbors and em!=(row,col):

            neighbors.append(em)

    return neighbors
#for a given number that is assigned for a given cell,we delete that number from the possible value list of all its neighbours
def prune(board1,num,row,col):

        global val
        global count3
        neighbors=neighborscheck(board1,row,col) #get a list of unassigned neighbours

        for nei in neighbors: #get all values for each neighbour
            neighborval=val[nei]
            count3=count3+1
            if num in neighborval:

                val[nei].remove(num) #deleting the number from its neighbour's values

                if len(val[nei])==0: #if the possible values for neighbour becomes 0 then it returns false
                    return False
        return True
# finding the list of unassigned cells in the board and the corresponding values it can take for each unassigned position
def emp(board):
    empty=[]
    val={}
    for row1 in range(int(n)):
        for col1 in range(int(n)):

            if (board[row1][col1]=='-'):
                values=possiblevalues(row1,col1,board)
                empty.append((row1,col1))
                val[(row1,col1)]=values



    return empty,val

#function to find the priority queue containing the unassigned cells along with the possible values for each cell
def MRV(board):
    global count2
    q = PriorityQueue()
    count=0

    for row1 in range(int(n)):
        for col1 in range(int(n)):

            if (board[row1][col1]=='-'):
                values=possiblevalues(row1,col1,board)
                q.put((len(values), (row1,col1)))

                count=count+1
    count2=count2+count
    return q


#finding the possible values for an unassigned cell
def possiblevalues(row,col,board):
    values=[]
    for n1 in range(1,int(n)+1):
            recurval=0
            for c in range(int(n)):

                     if board[row][c] == n1:
                         recurval=recurval+1
            for r in range(int(n)):
                     if board[r][col] == n1:
                         recurval=recurval+1
            for r1 in range(int(m)):
                for  c1 in range(int(k)):

                    if (board[r1+row-(row%int(m))][c1+col-(col%int(k))] == n1):
                        recurval=recurval+1
            if(recurval==0):
                values.append(n1)
    return values

#reading the input file
def readGameState(filePath):

    global n
    global m
    global k

    board1=[]
    fileHandle = open(filePath, 'r')
    param = fileHandle.readline().strip().split(',')

    n=param[0]
    m=param[1]
    k=param[2].strip(';')

    for i in range(int(n)):
        rawState = fileHandle.readline().strip().split(',')
        board1.append([])




        for j in range(int(n)):
            if(j==int(n)-1):
                rawState[j]=rawState[j].strip(';')
            board1[i].append(rawState[j])



    return board1


