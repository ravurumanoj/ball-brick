def main():
    matrixSize=int(input("Enter size of the NxN matrix :"))
    enterBricksInfo = True
    gameMatrix=[[" " for x in range(matrixSize)] for x in range(matrixSize)]
    direction = ""
    ballPosition = (matrixSize - 1) // 2
    while (enterBricksInfo):
        brickInfo=input("Enter the brick's position and the brick type :")
        arrBrickInfo=""
        arrBrickInfo = brickInfo.split()
        gameMatrix[int(arrBrickInfo[0])][int(arrBrickInfo[1])] = arrBrickInfo[2]
        if(arrBrickInfo[2]=="P"):
            gameMatrix[int(arrBrickInfo[0])][int(arrBrickInfo[1])] = "1"
        entercontinueornot=input("Do you want to continue to Enter Direction (Y or N)?")
        # enterDirectionInfo = if entercontinueornot == "Y" ? True : False     
        enterBricksInfo=bool(entercontinueornot == "Y") 
    ballCount=int(input("Enter ball Count :"))
    for i in range(matrixSize):
        for j in range(matrixSize):
            if (i == 0 or j == 0 or j==matrixSize-1):
                gameMatrix[i][j] = "W"
            if (i == matrixSize-1 and (j != 0 or j != matrixSize-1 or j!= ballCount)):
                gameMatrix[i][j] = "G"
            if(i== matrixSize-1 and j== ballPosition):
                gameMatrix[i][j] = "O"
              
    DisplayMatrix(gameMatrix, matrixSize, ballCount)
    print()
    enterDirectionInfo = True
    while(enterDirectionInfo):
        direction=input("Enter the direction in which the ball need to traverse from the List [ST,LD, RD] :")
        if(direction == "ST"):
            ballCount = TraverseStraight(gameMatrix, ballPosition, ballCount, matrixSize)
        if(direction == "LD"):
            ballCount = TraverseLeft(gameMatrix, ballPosition, ballCount-1, matrixSize)
        if(direction == "RD"):
            ballCount =TraverseRight(gameMatrix, ballPosition, ballCount-1, matrixSize)
        DisplayMatrix(gameMatrix, matrixSize, ballCount)
        entercontinueornot=input("Do you want to continue to Enter Direction (Y or N)?")
            # enterDirectionInfo = if entercontinueornot == "Y"? True : False
        enterDirectionInfo=bool(entercontinueornot == "Y") 
            # Console.ReadLine()

def DisplayMatrix(gameMatrix,size,ballCount):
    for i in range(size):
        for j in range(size):
            print(gameMatrix[i][j],end=" ")
        print()   
    print("Ball count is ",ballCount)

def TraverseStraight(gamematrix,ballposition,ballcount,matrixSize):
    col = int(ballposition)
    for row in range(matrixSize-2,-1,-1):
        # if(!string.IsNullOrEmpty(gamematrix[row,col])):
        if(gamematrix[row][col]):
            if(gamematrix[row][col] == "W"):
                ballcount = ballcount - 1
            elif(gamematrix[row][col] == "DE"): 
                DestroyEverything(gamematrix, matrixSize)
                print("you win hurray...!")
                break
            elif(gamematrix[row][col] == "DS"):
                DestroySurrounding(gamematrix, matrixSize, row, col)
                break
            elif(gamematrix[row][col] == "B"):
                destroyB(gamematrix, matrixSize, row, col,ballposition)
                break
            else:
                bricktype = 0
                # TryParse(gamematrix[row, col], out bricktype)
                if gamematrix[row][col].isdigit():
                    bricktype=gamematrix[row][col] 
                else:
                    # pass
                    continue
                bricktype = int(bricktype) - 1
                if(bricktype <= 0):
                    gamematrix[row][col] = " "
                    break
                else:
                    gamematrix[row][col] = str(bricktype)
                    break
        
    return ballcount
        
def TraverseLeft(gamematrix,ballposition,ballcount,matrixSize):
    if(ballposition - 1 <= 0):
        ballcount = ballcount - 1
    else:
        ballcount = TraverseStraight(gamematrix, ballposition-1, ballcount, matrixSize)
    return ballcount
        
def TraverseRight(gamematrix,ballposition,ballcount,matrixSize):
    if(ballposition + 1 >= matrixSize-1):
        ballcount = ballcount - 1
    else:
        ballcount = TraverseStraight(gamematrix, ballposition +1 , ballcount, matrixSize)
    return ballcount

def DestroyEverything(gamematrix,matrixSize):
    for i in range(1,matrixSize - 2):
        for j in range(1,matrixSize - 2):
            # if(!string.IsNullOrEmpty(gamematrix[i, j])):
            if(gamematrix[i][j]):
                gamematrix[i][j] = " "
    # print("you win hurray...!")
        
def DestroySurrounding(gamematrix,matrixSize,row,col):
    gamematrix[row][col] = ""
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if(gamematrix[i][j] != "W" or gamematrix[i][j] != "G" or gamematrix[i][j] != "O"):
                gamematrix[i][j] = " ";    

def destroyB(gamematrix, matrixSize, row, col,ballposition):
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if(gamematrix[i][j] == "B"):
                gamematrix[i][j] = " "
                gamematrix[matrixSize-1][ballposition+1]="_"
                break   

main()                
