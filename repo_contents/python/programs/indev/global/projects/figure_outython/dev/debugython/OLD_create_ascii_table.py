import string
import subprocess

#index = 101
#char = "f"

#print("Given:", index, "=", char)
#print("")

#returnedChar = chr(index)
#indexOfReturnedChar = ord(str(returnedChar))

#returnedIndex = ord(str(char))
#charOfReturnedIndex = chr(returnedIndex)

#print("Given\tReturned\tReversed\tResult")

#if (index == returnedIndex) and (index == indexOfReturnedChar):
    #print("".join(list(map(str, [index, "\t\t", returnedChar, "\t\t\t", indexOfReturnedChar, "\t\t\t", True]))))
#else:
    #print("".join(list(map(str, [index, "\t\t", returnedChar, "\t\t\t", indexOfReturnedChar, "\t\t\t", False]))))
#if (char == returnedChar) and (char == charOfReturnedIndex):
    #print("".join(list(map(str, [char, "\t\t", returnedIndex, "\t\t\t", charOfReturnedIndex, "\t\t\t", True]))))
#else:
    #print("".join(list(map(str, [char, "\t\t", returnedIndex, "\t\t\t", charOfReturnedIndex, "\t\t\t", False]))))

#print(string.printable)
#print(chr(55))





asciiTable = open("ASCII_Table.txt","w+")

asciiTable.write("#ASCII Table\n\n\n")


asciiTable.write("#Useable Control Character Codes:\n\n")

asciiTable.write("#Abbreviation = Escape Sequence\t#  Dec = Name --- 'Keyboard Key'\n")
asciiTable.write("".join(list(map(str, ["HT = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab --- 'tab'\n"]))))
asciiTable.write("".join(list(map(str, ["LF = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed --- 'enter' (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["CR = ", chr(34), chr(92), chr(114), chr(34), "\t#  13 = Carriage Return --- 'enter' (not recommended)\n"]))))
asciiTable.write("#Unless you are using python 2, are writing to a binary file, or are working within the Windows OS its self use Line Feed 'LF' for the 'enter' key ('newline').\n")
asciiTable.write("#In Python 3 and Python 2 on Windows text documents are opened by default in 'text' and 'universal' mode. In python 2 'universal' mode can be\n")
asciiTable.write("#In Python 2 for operating systems other than Windows 'universal' mode can be enabled by passing the 'U' flag when opening the text file.\n")
asciiTable.write("#If you are working within an OS: Windows requires both 'CR' and 'LF' to be used in that order and without a space between them like this: 'CRLF',\n"
                 "#Linux, Unix, and Modern Mac OS require LF to be used, and Classic Mac OS requires CR to be used.\n")
asciiTable.write("#Also, when using 'print()' 'CR' doe not function as 'enter' while 'LF' still will. CR will move the cursor to the beginning of the current line\n"
                 "#and write over its contents character by character.\n\n")

asciiTable.write("#Alternate Control Character Code Variables:\n\n")

asciiTable.write("#Horizontal Tab --- 'tab' key\n")
asciiTable.write("#Alternate Variable Name = Escape Sequence\t#  Dec = Name\n")
asciiTable.write("".join(list(map(str, ["ht = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab\n"]))))
asciiTable.write("".join(list(map(str, ["TAB = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab\n"]))))
asciiTable.write("".join(list(map(str, ["tab = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab\n"]))))
asciiTable.write("".join(list(map(str, ["HORIZONTALTAB = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab\n"]))))
asciiTable.write("".join(list(map(str, ["horizontalTab = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab\n\n"]))))

asciiTable.write("#Line Feed --- 'enter' key (recommended)\n")
asciiTable.write("#Alternate Variable Name = Escape Sequence\t#  Dec = Name\n")
asciiTable.write("".join(list(map(str, ["lf = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["ENTER = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["enter = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["NEWLINE = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["newline = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["LINEFEED = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["lineFeed = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed (recommended)\n\n"]))))

asciiTable.write("#Carriage Return --- 'enter' key (not recommended)\n")
asciiTable.write("#Alternate Variable Name = Escape Sequence\t#  Dec = Name\n")
asciiTable.write("".join(list(map(str, ["cr = ", chr(34), chr(92), chr(114), chr(34), "\t#  13 = Carriage Return (not recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["CARAGERETURN = ", chr(34), chr(92), chr(114), chr(34), "\t#  13 = Carriage Return (not recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["carageReturn = ", chr(34), chr(92), chr(114), chr(34), "\t#  13 = Carriage Return (not recommended)\n\n\n"]))))


asciiTable.write("#Printable Character Codes:\n\n")

asciiTable.write("#Glyph = chr(Dec)\t#  Dec = Name\n")

glyphInvalidVarName = ["space", "exclamationMark", "doubleQuotes", "number", "dollar", "perCentSign", "ampersand", "singleQuote", "openParenthesis", "closeParenthesis", "asterisk", 
                       "plus", "comma", "hyphen", "period", "slash", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "colon", "semicolon", "lessThan", 
                       "equals", "greaterThan", "questionMark", "atSymbol", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
                       None, None, None, None, None, None, None, None, "openingBracket", "backslash", "closingBracket", "caret", "underscore", "graveAccent", None, None, None, None, 
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "openingBrace", "verticalBar", 
                       "closingBrace", "equivalencySign"]

for i in range(32, 127):
    asciiGlyph = chr(i)
    
    if ((i >= 65) and (i <= 90)) or ((i >= 97) and (i <= 122)):
        if asciiGlyph.isupper() is True:
            asciiTable.write("".join(list(map(str, [chr(i), " = ", "chr(", i, ")", "\t#  ", i, " = Uppercase ", chr(34), asciiGlyph, chr(34), "\n"]))))
        elif asciiGlyph.isupper() is False:
            asciiTable.write("".join(list(map(str, [chr(i), " = ", "chr(", i, ")", "\t#  ", i, " = Lowercase ", chr(34), asciiGlyph, chr(34), "\n"]))))
        else:
            print("Error in letters on i ==", i, "and chr(i) ==", chr(i))
    elif (((i >= 32) and (i <= 64)) or ((i >= 91) and (i <= 96)) or ((i >= 123) and (i <= 127))):
        asciiTable.write("".join(list(map(str, [glyphInvalidVarName[i - 32], " = ", "chr(", i, ")", "\t#  ", i, " = ", chr(34), asciiGlyph, chr(34), "\n"]))))
    else:
        print("Error at bottom of loop on i ==", i, "and chr(i) ==", chr(i))

asciiTable.write("\n#Alternate Printable Control Character Code Variables:\n\n")

asciiTable.write("#TODO Horizontal Tab --- 'tab' key\n")


asciiTable.close()

sp = subprocess.Popen([r"C:\Program Files (x86)\Notepad++\notepad++.exe", "ASCII_Table.txt"])