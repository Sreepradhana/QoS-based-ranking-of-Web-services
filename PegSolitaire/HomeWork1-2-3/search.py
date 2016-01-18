#KINDLY EXECUTE aStarOne and aStarTwo SEPERATELY SINCE BOTH USE COMMON VARIABLES
import pegSolitaireUtils
import Queue as Q
import heapq
from array import *
import math
from numpy import linalg as LA
import config
from sys import maxint
#visited list to keep track of nodes that have been expanded already
#MULTIPATH PRUNING-visited list helps in Pruning the search by not letting new paths for a node that has been reached by a previous path,
#It also avoids cycles since every node is checked for previous access before stack operation is carried out
#This also optimizes the solution since the shortest path to reach every node is considered over other paths(since all moves are of unit cost here)
visited = []
nodes=0
#function that searches for nodes incrementally
def ItrDeepSearch(pegSolitaireObject):
 stackobj=pegSolitaireUtils.stack()
 for x in xrange(0,maxint):
 	if(traverse(pegSolitaireObject,stackobj,x)):
		 print "Goal found"
		 #since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
		 #  it's updated to a variable containing nodes expanded with respect to entire state
		 pegSolitaireObject.nodesExpanded=nodes
 	 	 return

#function that expands nodes till given depth
def traverse(initial,stackobj,depth):
	rootstate=initial.gameState
	objpush=pegSolitaireUtils.StNode(rootstate,0,[])
	visited=[]
	stackobj.push(objpush)
	tc=pegSolitaireUtils.traceCompute(initial,[])
	global nodes

	while(not(stackobj.isEmpty())):
		#popping node to explore it's children
		popobj=stackobj.pop()
		state=popobj.data
		tc.state=state
		#flag to keep track of if a node has atleast one children
		added=0
		#check for goal state
		if(popobj.data==pegSolitaireUtils.GOAL):
			initial.gameState=popobj.data
			return True
		else:
			added=0
			#check if exapnsion is permissible at a depth
			if(popobj.depth+1 <=depth):
				#tracking element position
				global position
				position=0
				nodes=nodes+1
				#enumerating to every element in the given node
				for rowid,x in enumerate(state):
					for colid,y in enumerate(x):
						children=[]
						position+=1
						#finding possible children generated on moving the particular element north
						newposition=pegSolitaireUtils.game.getNextState(initial,popobj,(-1,0),rowid,colid)
						#checking for possibility of child node by moving peg in the given direction
						if(pegSolitaireUtils.flag1==1):
							if not(newposition.state==popobj.data):
								#pushing child to stack if it has not been visited before
								if not(pegSolitaireUtils.game.visitedbefore(initial,visited,newposition.state)):
										sn=pegSolitaireUtils.StNode(newposition.state,popobj.depth+1,newposition.newpath)
										stackobj.push(sn)
										added=1
								if(newposition.state==pegSolitaireUtils.GOAL):
									initial.trace=newposition.newpath
									return True
						#finding possible children generated on moving the particular element south
						newposition=pegSolitaireUtils.game.getNextState(initial,popobj,(1,0),rowid,colid)
						#checking for possibility of child node by moving peg in the given direction
						if(pegSolitaireUtils.flag1==1):
							if not(newposition.state==popobj.data):
								#pushing child to stack if it has not been visited before
								if not(pegSolitaireUtils.game.visitedbefore(initial,visited,newposition.state)):
										sn=pegSolitaireUtils.StNode(newposition.state,popobj.depth+1,newposition.newpath)
										stackobj.push(sn)
										added=1
								if(newposition.state==pegSolitaireUtils.GOAL):
									initial.trace=newposition.newpath
									return True

						#finding possible children generated on moving the particular element west
						newposition=pegSolitaireUtils.game.getNextState(initial,popobj,(0,-1),rowid,colid)
						#checking for possibility of child node by moving peg in the given direction
						if(pegSolitaireUtils.flag1==1):
								if not(newposition.state==popobj.data):
									#pushing child to stack if it has not been visited before
									if not(pegSolitaireUtils.game.visitedbefore(initial,visited,newposition.state)):
										sn=pegSolitaireUtils.StNode(newposition.state,popobj.depth+1,newposition.newpath)
										stackobj.push(sn)
										added=1
								if(newposition.state==pegSolitaireUtils.GOAL):
									print newposition.newpath
									initial.trace=newposition.newpath
									return True
						#finding possible children generated on moving the particular element east
						newposition=pegSolitaireUtils.game.getNextState(initial,popobj,(0,1),rowid,colid)
						#checking for possibility of child node by moving peg in the given direction
						if(pegSolitaireUtils.flag1==1):
								if not(newposition.state==popobj.data):
									#pushing child to stack if it has not been visited before
									if not(pegSolitaireUtils.game.visitedbefore(initial,visited,newposition.state)):
										sn=pegSolitaireUtils.StNode(newposition.state,popobj.depth+1,newposition.newpath)
										stackobj.push(sn)
										added=1
								if(newposition.state==pegSolitaireUtils.GOAL):
									print newposition.newpath
									initial.trace=newposition.newpath
									return True

        	if(added==1):
    			visited.append(popobj.data)

#The second heuristic is based on the manhattan distance between the position of the child resulting from peg move and position of the goal
# . This heuristic function aims to reduce the distance between child position and goal position so that each move takes one step towards thegoal.

def aStarTwo(gameATwoObject):

	minpath=[]#path that was taken
	visited=[]#parents that were expanded
	state=gameATwoObject.gameState
	nodes1=0#number of nodes expanded
	heap=Q.PriorityQueue()
	p=pegSolitaireUtils.pq(state,[])
	q=pegSolitaireUtils.StNode(state,0,[])#class variable contaning the state
	heap.put((0,p))
	costsofar=0
	i=0
	while(not heap==[] ):
		#flag to check if a node has been added to visited list
		added=0


		h=heap.get()

		while heap.empty()==False:
			heap.get()
		minpath.append(h[1].path)


		nodes1=nodes1+1
		q=pegSolitaireUtils.StNode(h[1].state,0,[])
		gcost=costsofar+1

		#finding children for each element in the state ,in all four directions
		for rowid,x in enumerate(q.data):
			for colid,y in enumerate(x):

				newposition=pegSolitaireUtils.game.getNextState(gameATwoObject,q,(0,1),rowid,colid)
				if pegSolitaireUtils.flag1==1:


					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]

					#if current state has not been visited,it is explored
					if not(pegSolitaireUtils.game.visitedbefore(gameATwoObject,visited,newposition.state)):
						#heuristics function returns h(n)
						#heuristics function takes the state of child,game object and destination coordinates as input
						hcost=heuristics2(row,col)
						priority=hcost+gcost
						#pushing state,path and priority into priority heapq.heappush(heap,newposition.state,priority)
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameATwoObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										#  it's updated to a variable containing nodes expanded with respect to entire state
										gameATwoObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]

				#same procedure is carried out for all four directions

				newposition=pegSolitaireUtils.game.getNextState(gameATwoObject,q,(-1,0),rowid,colid)
				if(pegSolitaireUtils.flag1==1):

					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]

					if not(pegSolitaireUtils.game.visitedbefore(gameATwoObject,visited,newposition.state)):
						hcost=heuristics2(row,col)
						priority=hcost+gcost
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameATwoObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										#  it's updated to a variable containing nodes expanded with respect to entire state
										gameATwoObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]
				newposition=pegSolitaireUtils.game.getNextState(gameATwoObject,q,(1,0),rowid,colid)
				if(pegSolitaireUtils.flag1==1):

					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]
					if not(pegSolitaireUtils.game.visitedbefore(gameATwoObject,visited,newposition.state)):
						hcost=heuristics2(row,col)
						priority=hcost+gcost
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameATwoObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										#  it's updated to a variable containing nodes expanded with respect to entire state
										gameATwoObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]
				newposition=pegSolitaireUtils.game.getNextState(gameATwoObject,q,(0,-1),rowid,colid)
				if(pegSolitaireUtils.flag1==1):
					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]
					if not(pegSolitaireUtils.game.visitedbefore(gameATwoObject,visited,newposition.state)):
						hcost=heuristics2(row,col)
						priority=hcost+gcost
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameATwoObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										# it's updated to a variable containing nodes expanded with respect to entire state
										gameATwoObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]


		i=i+1
		#if a child was generated,its parent is added to visited list
		if(added==1):
			visited.append(h[0])
		costsofar=gcost

#The first heuristic is based on the concept of eliminating isolated nodes.
# A scoring function is used to score the nodes around the goal such that nodes on the square boundary immediately around the goal are scored 1,
# nodes on the square boundary one hop away from the goal are scored 2 and nodes on the square boundary two hop away from the goal are scored 3
#  and so on.The final priority is calculated by subtracting the score of the node before the peg moves from the score of the node after
#  the peg moves.This way the heuristic function makes sure that it does not lead to an isolated peg.
#aSTarOne function is same as aStarTwo,except that heuristics function takes both source and destination coordinates as inputs
def aStarOne(gameAOneObject):

	minpath=[]#path that was taken
	visited=[]#parents that were expanded
	state=gameAOneObject.gameState
	nodes1=0#number of nodes expanded
	heap=Q.PriorityQueue()
	p=pegSolitaireUtils.pq(state,[])
	q=pegSolitaireUtils.StNode(state,0,[])#class variable contaning the state
	heap.put((0,p))
	costsofar=0
	i=0

	while(not heap==[] ):
		added=0#flag to check if a node has been added to visited list

		h=heap.get()

		i=0
		while heap.empty()==False:
			heap.get()





		minpath.append(h[1].path)
		nodes1=nodes1+1
		q=pegSolitaireUtils.StNode(h[1].state,0,[])
		gcost=costsofar+1

		#finding children for each element in the state ,in all four directions
		for rowid,x in enumerate(q.data):
			for colid,y in enumerate(x):

				newposition=pegSolitaireUtils.game.getNextState(gameAOneObject,q,(0,1),rowid,colid)
				if pegSolitaireUtils.flag1==1:


					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]

					#if current state has not been visited,it is explored
					if not(pegSolitaireUtils.game.visitedbefore(gameAOneObject,visited,newposition.state)):
						#heuristics function returns h(n)
						#heuristics function takes the state of child,game object and destination coordinates as input
						hcost=heuristics1(rowid,colid,row,col)
						priority=hcost#+gcost
						#pushing state,path and priority into priority heapq.heappush(heap,newposition.state,priority)
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameAOneObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										#  it's updated to a variable containing nodes expanded with respect to entire state
										gameAOneObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]

				#same procedure is carried out for all four directions

				newposition=pegSolitaireUtils.game.getNextState(gameAOneObject,q,(-1,0),rowid,colid)
				if(pegSolitaireUtils.flag1==1):

					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]

					if not(pegSolitaireUtils.game.visitedbefore(gameAOneObject,visited,newposition.state)):
						hcost=heuristics1(rowid,colid,row,col)
						priority=hcost+gcost
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameAOneObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										#  it's updated to a variable containing nodes expanded with respect to entire state
										gameAOneObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]
				newposition=pegSolitaireUtils.game.getNextState(gameAOneObject,q,(1,0),rowid,colid)
				if(pegSolitaireUtils.flag1==1):

					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]

					if not(pegSolitaireUtils.game.visitedbefore(gameAOneObject,visited,newposition.state)):
						hcost=heuristics1(rowid,colid,row,col)
						priority=hcost+gcost
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameAOneObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										#  it's updated to a variable containing nodes expanded with respect to entire state
										gameAOneObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]
				newposition=pegSolitaireUtils.game.getNextState(gameAOneObject,q,(0,-1),rowid,colid)
				if(pegSolitaireUtils.flag1==1):
					row=pegSolitaireUtils.alist[0]
					col=pegSolitaireUtils.alist[1]
					if not(pegSolitaireUtils.game.visitedbefore(gameAOneObject,visited,newposition.state)):
						hcost=heuristics1(rowid,colid,row,col)
						priority=hcost#+gcost
						p=pegSolitaireUtils.pq(newposition.state,newposition.newpath)

						heap.put((priority,p))
						added=1
						if(newposition.state==pegSolitaireUtils.GOAL):
										minpath.append(newposition.newpath)
										gameAOneObject.trace=minpath
										#since the gameObject.nodesexpanded variable keeps track of every node element's(49 elements per node)and exapnsion in every direction(4 directions),
										# it's updated to a variable containing nodes expanded with respect to entire state
										gameAOneObject.nodesExpanded=nodes1
										return True
				pegSolitaireUtils.alist=[]


		i=i+1
		#if a child was generated,its parent is added to visited list
		if(added==1):
			visited.append(h[0])
		costsofar=gcost


#The second heuristics makes use of manhattan distance between the destination coordinate and the goal
#The second heuristic is based on the manhattan distance between the position of the child resulting from peg move and position of the goal
# . This heuristic function aims to reduce the distance between child position and goal position so that each move takes one step towards thegoal.

def heuristics2(r,c):

	mdist=abs(abs(int(r)-3)-abs(int(c)-3))
	return mdist+1
#The first heuristic is based on the concept of eliminating isolated nodes.
# A scoring function is used to score the nodes around the goal such that nodes on the square boundary immediately around the goal are scored 1,
# nodes on the square boundary one hop away from the goal are scored 2 and nodes on the square boundary two hop away from the goal are scored 3
#  and so on.The final priority is calculated by subtracting the score of the node before the peg moves from the score of the node after
#  the peg moves.This way the heuristic function makes sure that it does not lead to an isolated peg.
#first heuristic returns the source-destination score
def heuristics1(sr,sc,dr,dc):

	sou=scoring(sr,sc)

	des=scoring(int(dr),int(dc))

	point=sou-des+1
	point=-point


	return point


#the scoring function forms the basis of first heuristic.The goal coordinate itself is given score 0,the coordinates on the square
#immediately around the goal is given score 1,the next square boundary around goal given score 2 and so on
def scoring(r,c):

	if((r in[0,6]) or c in [0,6]):
		score=3
	elif((r in[1,5]) or c in [1,5]):
		score=2
	elif((r in[2,4]) or c in [2,4]):
		score=1
	elif(r==3 and c==3):
		score=0
	return score



