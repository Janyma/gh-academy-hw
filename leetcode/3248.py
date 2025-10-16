
def finalPositionOfSnake(n, commands):
        x=0
        y=0
        for i in range(len(commands)):
            if(commands[i]=="UP"):
                y-=1
            if(commands[i]=="RIGHT"):
                x+=1
            if(commands[i]=="DOWN"):
                y+=1
            if(commands[i]=="LEFT"):
                x-=1
        return (y*n)+x
print(finalPositionOfSnake(3, ["DOWN", "RIGHT", "UP"]))

        