from config import *

totalLeftBuffer = surroundingBuffer + leftBuffer    
totalRightBuffer = surroundingBuffer + rightBuffer

totalTopBuffer = surroundingBuffer + topBuffer
totalBottomBuffer = surroundingBuffer + bottomBuffer

totalHorizontalBuffer = totalRightBuffer + totalLeftBuffer
totalVerticalBuffer = totalTopBuffer + totalBottomBuffer

#Default turtle screen buffer is 20 (automatically makes screen x-20,y-20 smaller)
defaultScreenBuffer = 20

screenSize = [graphSize[0] + totalHorizontalBuffer + defaultScreenBuffer, graphSize[1] + totalVerticalBuffer + defaultScreenBuffer]

screenZeroZero = [0 - totalLeftBuffer + (defaultScreenBuffer/2), 0 - totalBottomBuffer + (defaultScreenBuffer/2)]

screenBottomLeft = [0 - totalLeftBuffer, 0 - totalBottomBuffer]
screenTopLeft = [0 - totalLeftBuffer, screenSize[1]]
screenTopRight = screenSize
screenBottomRight = [screenSize[0], 0 - totalBottomBuffer]
screenCenter = [screenSize[0] / 2, screenSize[1] / 2]