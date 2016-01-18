#KINDLY EXECUTE aStarOne and aStarTwo SEPERATELY SINCE BOTH USE COMMON VARIABLES
import readGame
import traceback
import heapq
import copy
GOAL=[[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]
curpos=[]
flag1=0
np=[]
alist=[]
blist=[]
#######################################################
# These are some Helper functions which you have to use
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_wall(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNextState(self, oldPos, direction):
#######################################################
class game:
	
	def __init__(self, filePath):
        	self.gameState = readGame.readGameState(filePath)
                self.nodesExpanded = 0
                
		self.trace = []	
	
	#the implementation predicts if a corner would result on a particular move before computing the move being made which eliminates the need for is_corner function
	def is_corner(self, pos):
		########################################
		# You have to make changes from here
		# check for if the new positon is a corner or not
		# return true if the position is a corner

		return False
	
	
	#This position generates valid node on movement of a particular peg in the given direction
	def getNextPosition(self, oldPos1, direction, rowid, colid):
		#flag to keep track of new node generation
		global flag1
		flag1=0

		oldPos=oldPos1.data
		newPos=copy.deepcopy(oldPos)
		newpath=[]
		global alist
		#limiting search by eliminating the children with possible corner results
		if(direction==(-1,0) and rowid>1):
			  #checking for possible move in North
		      if(oldPos[rowid][colid]==1 and oldPos[rowid-1][colid]==1 and oldPos[rowid-2][colid]==0):
				src=str(rowid)+' '+str(colid)
				des=str(rowid-2)+' '+str(colid)
				alist=str(rowid-2)+str(colid)
				#finding values after peg move
				newPos[rowid][colid]=0
				newPos[rowid-1][colid]=0
				newPos[rowid-2][colid]=1
				flag1=1
				#tracking path taken to current node
				newpath=newpath+oldPos1.path
				newpath+=('(',src,'->',des,')')
				self.trace+=(src,'->',des)
		#eliminating search if it has possibility for corner
		elif(direction==(1,0) and rowid<5):
			  #checking for possible move in south
		      if(oldPos[rowid][colid]==1 and oldPos[rowid+1][colid]==1 and oldPos[rowid+2][colid]==0):
				src=str(rowid)+' '+str(colid)
				des=str(rowid+2)+' '+str(colid)
				alist=str(rowid+2)+str(colid)
				#finding values after peg move
				newPos[rowid][colid]=0
				newPos[rowid+1][colid]=0
				newPos[rowid+2][colid]=1
				flag1=1
				#tracking path taken to current node
				newpath=newpath+oldPos1.path
				newpath+=('(',src,'->',des,')')
				self.trace+=(src,'->',des)
		#eliminating search if it has possibility for corner
		elif(direction==(0,1) and colid<5):
			   #checking for possible move in east
		   	   if(oldPos[rowid][colid]==1 and oldPos[rowid][colid+1]==1 and oldPos[rowid][colid+2]==0):
				 src=str(rowid)+' '+str(colid)
				 des=str(rowid)+' '+str(colid+2)
				 alist=str(rowid)+str(colid+2)
				 newPos[rowid][colid]=0
				 newPos[rowid][colid+1]=0
				 newPos[rowid][colid+2]=1
				 flag1=1
				 #tracking path taken to current node
				 newpath=newpath+oldPos1.path
				 newpath+=('(',src,'->',des,')')
				 self.trace+=(src,'->',des)
		#eliminating search if it has possibility for corner
		elif(direction==(0,-1) and colid>1):
			   #checking for possible move in west
		       if(oldPos[rowid][colid]==1 and oldPos[rowid][colid-1]==1 and oldPos[rowid][colid-2]==0):
				 src=str(rowid)+' '+str(colid)
				 des=str(rowid)+' '+str(colid-2)
				 alist=str(rowid)+str(colid-2)
				 newPos[rowid][colid]=0
				 newPos[rowid][colid-1]=0
				 newPos[rowid][colid-2]=1
				 flag1=1
				 #tracking path taken to current node
				 newpath=newpath+oldPos1.path
				 newpath+=('(',src,'->',des,')')
				 self.trace+=(src,'->',des)

  		#returning traceCompute object containing new state and path followed to reach the state
  		newstate=traceCompute(newPos,newpath)
		return newstate 
	

	def is_validMove(self, oldPos, direction,rowid,colid):
	       newPos = self.getNextPosition(oldPos, direction, rowid, colid)
	       global np
	       np=newPos
	       return True
	#function to check if a state has been visited before for Multipath pruning and avoiding cycles
	def visitedbefore(self,visitedlist,data):
		for x in visitedlist:
			if x==data:
				return True
		return False


	def getNextState(self, oldPos, direction,rowid,colid):
		###############################################
		# DONT Change Things in here
	    self.nodesExpanded += 1
	    if not self.is_validMove(oldPos, direction,rowid,colid):
			 print "Error, You are not checking for valid move"
			 exit(0)
		#############################################
	    return np	
#stack containing utilities for IDS implementation
class stack:
  def __init__(self):
    self.items=[]
    
  def push(self,value):
    self.items.append(value)
    return 'TRUE'
   
  def isEmpty(self):
     return self.items==[]
     
  def pop(self):
   if not self.isEmpty():
    #print "not empty"
    return self.items.pop()
   else:
    print "empty"
    return "ERROR_Stack_Empty"
    
  def print1(self):
  	return self.items

#class traceCompute to keep track of path to reach every node
class traceCompute:
   def __init__(self, state, path):
    self.state = state
    self.newpath = path
    
#class StNode for creating node to be pushed into stack
class StNode:
   def __init__(self, data, depth, path):
     self.data=data
     self.depth=depth
     self.path=path

class pq:
	def __init__(self, state, path):
		self.state=state
		self.path=path