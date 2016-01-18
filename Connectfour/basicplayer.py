from util import memoize, run_search_function
col1=0
from connectfour import ConnectFourBoard
def basic_evaluate(board):
    """
    The original focused-evaluate function from the lab.
    The original is kept because the lab expects the code in the lab to be modified. 
    """
    if board.is_game_over():
        # If the game has been won, we know that it must have been
        # won or ended by the previous move.
        # The previous move was made by our opponent.
        # Therefore, we can't have won, so return -1000.
        # (note that this causes a tie to be treated like a loss)
        score = -1000
    else:
        score = board.longest_chain(board.get_current_player_id()) * 10
        """chain=board.longest_chain(board.get_other_player_id())
        if(chain>=3):
            score=999
        """
        print "score"
        print "longest",score
        print "CURPLAYER",board.get_current_player_id()
        # Prefer having your pieces in the center of the board.
        for row in range(6):
            for col in range(7):

                if board.get_cell(row, col) == board.get_current_player_id():
                    score -= abs(3-col)
                    print "DECR",score
                elif board.get_cell(row, col) == board.get_other_player_id():
                    score += abs(3-col)
                    print "INCR",score
    return score


def get_all_next_moves(board):
    """ Return a generator of all moves that the current player could take from this position """
    from connectfour import InvalidMoveException

    for i in xrange(board.board_width):
        try:
            yield (i, board.do_move(i))
        except InvalidMoveException:
            pass

def is_terminal(depth, board):
    """
    Generic terminal state check, true when maximum depth is reached or
    the game has ended.
    """
    return depth <= 0 or board.is_game_over()


def minimax(board, depth, eval_fn = basic_evaluate,
            get_next_moves_fn = get_all_next_moves,
            is_terminal_fn = is_terminal,
            verbose = True):
    d=0
    #global col1
    #col1,retval=maxmove(board,2,d)
    col1,retval=negamax(board,depth,depth)

    #print "retval"
    #print retval
    print col1
    return col1
"""
fun minimax(n: node): int =
   if leaf(n) then return evaluate(n)
   if n is a max node
      v := L
      for each child of n
         v' := minimax (child)
         if v' > v, v:= v'
      return v
   if n is a min node
      v := W
      for each child of n
         v' := minimax (child)
         if v' < v, v:= v'
      return v
"""
def negamax(game, depthLeft,i):

    # If at terminal state or depth limit, return utility value and move None
    if depthLeft == 0 or game.is_game_over():
        #if ConnectFourBoard.is_win(game)!=0:
        #print ConnectFourBoard.is_win(game)
        #return None,999
        """for row in range(6):
                if(game._is_win_from_cell(row,i)):
                    score=999
                    return score
        """
        return None,basic_evaluate(game)

    # Find best move and its value from current state
    bestValue = -9999
    bestMove = None
    gboardobj=get_all_next_moves(game)
    boardobj=list(gboardobj)
    for i in xrange(0,len(boardobj)):
        # Apply a move to current state

        # Use depth-first search to find eventual utility value and back it up.
        #  Negate it because it will come back in context of next player
        move,value = negamax(boardobj[i][1],depthLeft-1,i)
        # Remove the move from current state, to prepare for trying a different move
        value = -value
        if value > bestValue:
            # Value for this move is better than moves tried so far from this state.
            bestValue = value
            bestMove = i

    return bestMove,bestValue
def alpha_beta_search(board, depth,
                      eval_fn,
                      # NOTE: You should use get_next_moves_fn when generating
                      # next board configurations, and is_terminal_fn when
                      # checking game termination.
                      # The default functions set here will work
                      # for connect_four.
                      get_next_moves_fn=get_all_next_moves,
		      is_terminal_fn=is_terminal):
    alpha=-999
    beta=999

    val,col=negamaxalphabeta(board,0,depth,alpha,beta)
    print col
    #raise NotImplementedError
    return col
def negamaxalphabeta (board, depth, maxDepth, alpha, beta):
   if depth == maxDepth:
      return basic_evaluate(board),None
   bestMove = None
   bestScore = -999
   gboardobj=get_all_next_moves(board)
   boardobj=list(gboardobj)
   for i in xrange(0,len(boardobj)):
      newBoard = boardobj[i][1]
      score,tempmove =negamaxalphabeta(newBoard, depth+1,maxDepth,
                              -beta,run_game(alphabeta_player, human_player)
                              -max(alpha, bestScore))
      score = -score
      if score > bestScore:
         bestScore = score
         bestMove = i
         # early loop exit (pruning)
         if bestScore >= beta:
             return bestScore, bestMove
   return bestScore, bestMove
"""def negamaxalphabeta(game, alpha,beta,depthLeft):

    # If at terminal state or depth limit, return utility value and move None
    if depthLeft == 0:
        return basic_evaluate(game),None
    bestValue = -9999
    bestMove = None
    gboardobj=get_all_next_moves(game)
    boardobj=list(gboardobj)
    print "BOARDOBJ",boardobj
    print "CURRENT PLAYER",game.get_current_player_id()
    if(game.get_current_player_id()==1):
        for i in xrange(0,len(boardobj)):
        # Apply a move to current state

        # Use depth-first search to find eventual utility value and back it up.
        #  Negate it because it will come back in context of next player
            temp=alpha
            cons,cols=negamaxalphabeta(boardobj[i][1],alpha,beta,depthLeft-1)
            alpha =max(alpha,cons)
            print "ALPHA",alpha
            if(temp!=alpha):
                col=boardobj[i][0]
            if(beta>=alpha):
                 return alpha,col

        return alpha,col
        # Remove the move from current state, to prepare for trying a different move
    else:
        for i in xrange(0,len(boardobj)):
                temp=beta
                cons,cols=negamaxalphabeta(boardobj[i][1],alpha,beta,depthLeft-1)
                beta=min(beta,cons)
                print "BETA",beta
                if(temp!=beta):
                    col=boardobj[i][0]
                if(beta>=alpha):
                 return beta,col

        return beta,col
    #return col
"""
"""
function AlphaBeta(State, Alpha, Beta, Player):
  if (State is terminal):
    Return Result(State);
  if (Player):
    for each possible play P from State:
      Alpha = max(Alpha, AlphaBeta(P, Alpha, Beta, !(Player));
      if (Beta >= Alpha):
        Return Alpha
    Return Alpha
  else:
    for each possible play P from State:
      Beta = min(Beta, AlphaBeta(P, Alpha, Beta, !(Player));
      if (Beta >= Alpha):
        Return Beta
    Return Beta
"""
    # Find best move and its value from current state

"""def minimaxeval(board,depth,d):
    #global col1
    print "Current player"
    curplayer=board.get_current_player_id()
    print curplayer
    #col1=10
    if d==depth:
        return basic_evaluate(board)
    if curplayer==1:
            d=d+1
            print "dvalue"
            print d
            value=-1000
            print "ISIDE PLY 1"
            gboardobj=get_all_next_moves(board)
            boardobj=list(gboardobj)
            print "boardobj"
            print boardobj

            for i in xrange(0,len(boardobj)):

                value1=minimaxeval(boardobj[i][1],depth,d)
                print "Current player",i
                curplayer=board.get_current_player_id()
                print curplayer
                print "VALUE PLY 0"
                print "i",i
                print value1
                if value1>value:
                    value=value1
                    col1=boardobj[i][0]
                    #print "updated value"
                    #print col1,value1
                    #print "column"
                    #print col1

            return value
    if curplayer==2:
            print "INISIDE PLY2"
            d=d+1
            value = 1000
            gboardobj=get_all_next_moves(board)
            print "boardobj"

            boardobj=list(gboardobj)
            print boardobj
            for i in xrange(0,len(boardobj)):
                value1=minimaxeval(boardobj[i][1],depth,d)
                #print boardobj[i][0]
                #print "VALUE PLY 1"
                #print value1
                if value1<value:
                    value=value1

                    col1=boardobj[i][0]

                    #print "column"
                    #print col1
            #print "infunction return val"
            #print value

            return value
"""

"""for i in xrange(0,len(boardobj)):
        scoreval=basic_evaluate(boardobj[i][1])
        if(curplayer==1):
            if(scoreval>max):
                max=scoreval
                col=boardobj[i][0]
                board=boardobj[i][1]
        elif(curplayer==2):
                if(scoreval<min):
                    min=scoreval
                    col=boardobj[i][0]
                    board=boardobj[i][1]
    print "max"
    print max
    print "maxcol"
    print col
    print "maxboard"
    print board
    print "min"
    print min

"""
"""print "0th obj"
    print boardobj[0][1]
    """
"""for i in xrange(next_moves):
            print basic_evaluate(i)
"""







"""
    Do a minimax search to the specified depth on the specified board.

    board -- the ConnectFourBoard instance to evaluate
    depth -- the depth of the search tree (measured in maximum distance from a leaf to the root)
    eval_fn -- (optional) the evaluation function to use to give a value to a leaf of the tree; see "focused_evaluate" in the lab for an example

    Returns an integer, the column number of the column that the search determines you should add a token to
    """
#raise NotImplementedError


def rand_select(board):
    """
    Pick a column by random
    """
    import random
    moves = [move for move, new_board in get_all_next_moves(board)]
    return moves[random.randint(0, len(moves) - 1)]


def new_evaluate(board):
    raise NotImplementedError


random_player = lambda board: rand_select(board)
basic_player = lambda board: minimax(board, depth=4, eval_fn=basic_evaluate)
#new_player = lambda board: minimax(board, depth=4, eval_fn=new_evaluate)
progressive_deepening_player = lambda board: run_search_function(board, search_fn=minimax, eval_fn=basic_evaluate)
