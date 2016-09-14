#from poenpyxl import load_workbook
def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9x9"""
    for x in range(9):
        for y in range(9):
            if puzzle[x][y]==0:
                tmp =[1,2,3,4,5,6,7,8,9]
                #check ==========
                for i in puzzle[x]:
                    if i in tmp:
                        #if x==0:
                         #   print(i)
                        tmp.remove(i)
                #check ||||||||||||||
                for i in range(9):
                    if puzzle[i][y] in tmp:
                        #if x==0:
                         #   print(puzzle[i][y])
                        tmp.remove(puzzle[i][y])
                #check |=|
                oox = x//3
                ooy = y//3
                ooxx = x%3
                ooyy = y%3
                for ox in range(3):
                    for oy in range(3):
                        otmp = puzzle[(oox*3)+(ooxx+ox)%3][ooy*3+(ooy+oy)%3]
                        if otmp in tmp:
                            tmp.remove(otmp)
                puzzle[x][y]=tmp
    
    #check alone number then apply it, ez life
    _flag = True
    while _flag:
        _flag=False
        for x in range(9):
            for y in range(9):
                #check alone number
                if type(puzzle[x][y]) is list: 
                    if len(puzzle[x][y])==1:
                        _flag=True
                        #print(x,y)
                        tmp = puzzle[x][y][0]
                        puzzle[x][y]=tmp
                        for i in puzzle[x]:
                            if (type(i) is list)and (tmp in i):
                                #print(i,type(tmp))
                                i.remove(tmp)
                        for i in range(9):
                            if (type(i) is list)and(tmp in puzzle[i][y]):
                                puzzle[i][y].remove(tmp)
                    #check alone num in party then apply it, ez life
                    else:
                        ##check |=|
                        tmp = puzzle[x][y]
                        oox = x//3
                        ooy = y//3
                        for i in tmp:
                            for ox in range(3):
                                for oy in range(3):
                                    if puzzle[oox*3+ox][ooy*3+oy] in tmp:
                                        _flag=True
                                        tmp.remove(puzzle[oox*3+ox][ooy*3+oy])
                        ##check ||
                        for i in puzzle[x]:
                            if i in puzzle[x][y]:
                                _flag=True
                                puzzle[x][y].remove(i)
                        ##check ==
                        for i in range(9):
                            if puzzle[i][y] in puzzle[x][y]:
                                _flag=True
                                puzzle[x][y].remove(puzzle[i][y])
    
    return puzzle
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
#print(puzzle[1][3])
print(sudoku(puzzle))
