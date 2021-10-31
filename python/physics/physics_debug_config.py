

space = " "
dash = "-"
doubleDash = "="
lineStart = "||  "
lineEnd = "  ||\n"
doubleDashLineStart = "|==="
doubleDashLineEnd = "===|\n"
tab = "\t"
columnLine = " | "

pageCharWidth = 107
pageTabWidth = 24
tabLength = 4

charSingleMargin = len(lineStart)
charTotalMargin = charSingleMargin * 2

charLineLength = pageCharWidth - charTotalMargin

#Default Columns
widthColOne = 30
widthColTwo = 20
widthColThree = 20
widthColFour = 20

posColLineOne = widthColOne + len(lineStart)
posColLineTwo = posColLineOne + len(columnLine) + widthColTwo
posColLineThree = posColLineTwo + len(columnLine) + widthColThree