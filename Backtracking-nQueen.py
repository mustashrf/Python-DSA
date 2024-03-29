def solve():
    if not solveTile(board,0):
        print("Error")
    printSolution(board)

def solveTile(board,col):
    
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board,i,col):
            board[i][col] = 1
            if solveTile(board,col+1):
                return True
            board[i][col] = 0

def isSafe(board,row,col):
    
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    
    return True

def printSolution(board):

    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")

        print()
      
def createBoard(n):

    board = []
    for i in range(n):        
        board.append([])
        for j in range(n):
            board[i].append(0)

    return board



board = createBoard(4)

N = len(board)

solve()
