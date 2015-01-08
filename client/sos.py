def changeGrid(grid1,grid2):
    print (abs(grid1-grid2))
    if abs(grid1-grid2)==1 or abs(grid1-grid2)==7:
        return True
    else:
    	return False

print (changeGrid(28,27))