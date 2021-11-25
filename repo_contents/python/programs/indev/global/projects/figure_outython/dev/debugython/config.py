

#space = chr(32)

#dash = chr(45)
#doubleDash = chr(61)
#underscore = chr(95)


#tab = "\t"
#nextLine = "\n"


lineStart = "||  "
lineEnd = "  ||\n"
doubleDashLineStart = "|==="
doubleDashLineEnd = "===|\n"
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