class eightpuzzlestate:
    def __init__(self,numbers):
        self.cells=[]
        numbers=numbers[:]
        numbers.reverse()
        for row in range(3):
            self.cells.append([])
            for col in range(3):
                self.cells[row].append(numbers.pop())
                if self.cells[row][col]==0:
                    self.blankLocation=row,col
    
    def isgoal(self):
        current=0
        for row in range(3):
            for col in range(3):
                if current!=self.cells[row][col]:
                    return False
                current+=1
            return True   
        
    def legalmoves(self):
        moves=[]
        row,col=self.blankLocation
        if(row!=0):
            moves.append('up')
        if(row!=2):
            moves.append('down')
        if(col!=0):
            moves.append('left')
        if(col!=2):
            moves.append('right')
        print("You can move the blank space")
        return moves

    


    def result(self,move):
        row,col=self.blankLocation
        if(move=='up'):
            newrow=row-1
            newcol=col
        elif(move=='down'):
            newrow=row+1
            newcol=col
        elif(move=='left'):
            newrow=row
            newcol=col-1
        elif(move=='right'):
            newrow=row
            newcol=col+1
        else:
            "illegal moves"
            
        newpuzzle=eightpuzzlestate([0,0,0,0,0,0,0,0,0])
        newpuzzle.cells=[values[:] for values in self.cells]
        newpuzzle.cells[row][col]=self.cells[newrow][newcol]
        newpuzzle.cells[newrow][newcol]=self.cells[row][col]
        newpuzzle.blankLocation=newrow,newcol
        return newpuzzle
    
    def __eq__(self, other):
        for row in range( 3 ):
            if self.cells[row] != other.cells[row]:
                return False
        return True 
    
    def __hash__(self):   #return the hash value of puzzle cells
        return hash(str(self.cells))
    
    def __getAsciiString(self):  # Display the puzzle in cube form
        lines = []
        horizontalLine = ('-' * (13))
        lines.append(horizontalLine)




        for row in self.cells:
            rowLine = '|'

            for col in row:
                if col == 0:
                    col = ' '
                rowLine = rowLine + ' ' + col.__str__() + ' |'
            lines.append(rowLine)
            lines.append(horizontalLine)
        return '\n'.join(lines)
            
    def __str__(self):
        return self.__getAsciiString()
    
class EightPuzzleSearchProblem: # This class is an implementation of searching in 8 puzzle cube
   
    # The each state of 8 puzzle is represent in class with the instance of eightpuzzlestate  

    def __init__(self,puzzle):  #  Creates a new EightPuzzleSearchProblem which stores search    information.
        self.puzzle = puzzle
        self.numNodesExpanded = 0
        self.expandedNodeSet = {}
        self.initial_state=self.puzzle
        
    def getStartState(self): #  Returns the initial state
        return self.initial_state
    
    def isGoalState(self,state): # Returns true if the state is a goal state
        return state.isgoal()
    
    def getSuccessors(self,state):
        # state: an eight puzzle

        # Returns list of (successor,cost) pairs where
        # each succesor is either left, right, up, or down
        # from the original state and the cost is 1.0 for each
        # Leave these lines in.  They keep track of the search progress


        
        self.numNodesExpanded += 1
        self.expandedNodeSet[state] = 1

        
    #Search Stats

    def displaySearchStats(self): #  Display number of nodes expanded by 'getSuccessors'
        print('Number of nodes expanded:',self.numNodesExpanded)
        print('Number of unique nodes expanded:', len(self.expandedNodeSet))

    def resetSearchStats(self):
        self.numNodesExpanded = 0
        self.expandedNodeSet = {}
        
    #def manhattanDistance(state, eightPuzzleSearchProblem):
        #state: An eight puzzle

        # Returns the sume of the distances between each
        #  tile's current location and its proper place.

        
    # Module Methods

    def loadEightPuzzle(self, puzzleNumber): # Returns an eight puzzle object generated from one       of the provided puzzles in EIGHT_PUZZLE_DATA.
        EIGHT_PUZZLE_DATA = [[1, 0, 2, 3, 4, 5, 6, 7, 8], 
                             [1, 7, 8, 2, 3, 4, 5, 6, 0], 
                             [4, 3, 2, 7, 0, 5, 1, 6, 8], 
                             [5, 1, 3, 4, 0, 2, 6, 7, 8], 
                             [1, 2, 5, 7, 6, 8, 0, 4, 3], 
                             [0, 3, 1, 6, 8, 2, 7, 5, 4]] 
        return eightpuzzlestate(EIGHT_PUZZLE_DATA[puzzleNumber])

    def createRandomEightPuzzle(moves=100):
        puzzle = EightPuzzleState([0,1,2,3,4,5,6,7,8]) 
        for i in range(moves):
        # Execute a random legal move
            
            puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
        return puzzle       

# Function Call:
n=eightpuzzlestate([1,2,0,3,4,5,6,7,8])
n.cells
n.isgoal()
n.blankLocation
print(n.legalmoves())
print("\n\n")


print("Initially")
print(n.cells)
print(n)
print("Goal test:",n.isgoal())
n2=eightpuzzlestate([0,0,0,0,0,0,0,0,0])
print("After first move")
n2=n.result('left')
print(n2.cells)
n3=eightpuzzlestate([0,0,0,0,0,0,0,0,0])
print("After second move")
n3=n2.result('left')
print(n3.cells)
print("Goal tests:",n3.isgoal())
print("\n\n")


print(n.__eq__(n3))
print(n.__hash__())
print(n.__str__())
print("\n\n")

nr=EightPuzzleSearchProblem(n)
print(nr.getStartState())
print(nr.isGoalState(n))
print("\n\n")

nr.displaySearchStats()
nr.resetSearchStats()
print(nr.loadEightPuzzle(3))
