

## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

Map = [
			[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],#0, ROW - 10x10 SQUARE
			[ 1, 0, 1, 1, 1, 1, 1, 0, 0, 1 ],#1
			[ 1, 2, 0, 0, 0, 1, 1, 0, 0, 1 ],#2
			[ 1, 1, 0, 1, 0, 0, 3, 0, 0, 1 ],#3
			[ 1, 0, 0, 1, 1, 1, 1, 1, 0, 1 ],#4
			[ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],#5
                        [ 1, 3, 1, 0, 3, 0, 0, 1, 0, 1 ],#6
                        [ 1, 0, 0, 0, 1, 1, 1, 0, 0, 1 ],#7
                        [ 1, 0, 1, 0, 0, 0, 1, 0, 1, 1 ],#8
                        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] #9
	]                #0  1  2  3  4  5  6  7  8  9, COLUMN


#Define a function to print our Map and current Player location

def drawMap(currX, currY):
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            if (currX == x) and (currY == y):   #print * if they are in this square
                print("*  ", end="")
            else:
                if Map[y][x] == 0:
                    print(" "," ", end ="")
                else:
                    print (Map[y][x]," ", end ="") 
        print()
    print()

#Define our function that will move the player
#The function will first check if the player can move or hits a wall
#If the player can move, then the current location will be updated
##If the player cannot move due to a wall, the location will not be updated
def keything(x, y, key, Map):
    YN = input("would you like to use 1 of yours keys? Y/N: ")
    if YN == "Y":
        print("You opened the door")
        key = key -1
        Map[y][x] = 0
        return (x, y)
    elif YN == "N":
        return(x, y)
    
    
def movePlayer(x,y,moveDir):
    global keyCount

    if moveDir == "u": 
        if Map[y-1][x] == 3:
            if keyCount != 0:
                keything(x, y-1, keyCount, Map)
            else:
                print("You dont have a key to enter")
                return(x, y)
        if Map[y-1][x] == 0:
            return (x, y-1)
                                 

    if moveDir == "d":
        if Map[y+1][x] == 3:
            if keyCount != 0:
                YN = input("would you like to use 1 of yours keys? Y/N: ")
                keything(x, y+1, keyCount, Map)
            else:
                    print("You dont have a key to enter")
                    return(x, y)
        if Map[y+1][x] == 0:
            return (x, y+1)


    if moveDir == "l":
        if Map[y][x-1] == 3:
            if keyCount != 0:
                keything(x-1, y, keyCount, Map)
            else:
                print("You dont have a key to enter")
                return(x, y)
        if Map[y][x-1] != 1:
            return (x-1, y)

    if moveDir == "r":
        if Map[y][x+1] == 3:
            if keyCount != 0:
                keything(x+1, y, keyCount, Map)
            else:
                print("You dont have a key to enter")
                return(x, y)

        if Map[y][x+1] != 1:
            return (x+1, y)

        
       
        
    #they attempted a bad move
    print ("**Invalid move** Try again.")
    return (x,y)   #return the same location they are in since no move



#Set our starting location
currX = 1 #COLUMN
currY = 8 #ROW

#draw the map the first time before asking for a move
drawMap(currX, currY)

#Forever just let the player move around the map on the path
keyCount = 1

while True:
    moveDir = input("Enter direction (u,d,l,r): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)
    print("Your current total of key(s) is:", keyCount)

