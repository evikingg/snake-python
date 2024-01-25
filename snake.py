
gameArea = [10,10] # x,y
snakeX = [5,4] # 1,2,3...
snakeY = [5,5] # 1,2,3...
score = 0
alive = True
dir = "d"

def render(head, tail, background):
    for y in range(gameArea[1]):
        boufor = []
        for x in range(gameArea[0]):
            if (x in snakeX) and (y in snakeY):
                if (x == snakeX[0]) and (y == snakeY[0]):
                    boufor.append(head)
                else:
                    boufor.append(tail)
            else:
                boufor.append(background)
        print(boufor)

def move():
    x = snakeX[0]
    y = snakeY[0]
    for i in range(len(snakeX)):
        snakeX[-i-1] == snakeX[-i-2]
    for i in range(len(snakeY)):
        snakeY[-i-1] == snakeY[-i-2]
    if dir == "w":
        snakeX[0] = x
        snakeY[0] = y+1
    if dir == "s":
        snakeX[0] = x
        snakeY[0] = y-1
    if dir == "a":
        snakeX[0] = x-1
        snakeY[0] = y
    if dir == "d":
        snakeX[0] = x+1
        snakeY[0] = y

while(alive == True):
    render("@","*","#")
