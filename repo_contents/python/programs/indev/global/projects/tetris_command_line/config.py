errorReportingEnabled = True
detailedErrorReportingEnabled = True


#UI/ Graphics:
playfieldWidth = 10
playfieldHeight = 20
#playfieldHeight = 40

currentTetromino = "#"
setTetrominos = "X"
emptyCells = None

uiTopBoarder = "="
uiBottomBoarder = "="
uiLeftBoarder = "|"
uiRightBoarder = "|"
uiCornerBuffer = 1

uiTopBoarderSize = 1
uiBottomBoarderSize = 1
uiLeftBoarderSize = 2
uiRightBoarderSize = 2

uiHorizontalSize = 4
uiVerticalSize = 2


totalPlayfieldWidth = playfieldWidth + uiHorizontalSize
totalPlayfieldHeight = playfieldHeight + uiVerticalSize



#Logic:
logicSetTetrominos = 1
logicEmptyCells = 0
logicRowValueToClearLine = 10