import string
import subprocess

asciiTable = open("ascii_table.py", "w+")

asciiTable.write("class ascii_chars:\n")
asciiTable.write("\t#ASCII Table:\n\n")


asciiTable.write("\t#Useable Control Character Codes:\n")
asciiTable.write("".join(list(map(str, ["\ttab = ", chr(34), chr(92), chr(116), chr(34), "\t#  9 = Horizontal Tab --- 'tab'\n"]))))
asciiTable.write("".join(list(map(str, ["\tnewline = ", chr(34), chr(92), chr(110), chr(34), "\t#  10 = Line Feed --- 'enter' (recommended)\n"]))))
asciiTable.write("".join(list(map(str, ["\tcarriageReturn = ", chr(34), chr(92), chr(114), chr(34), "\t#  13 = Carriage Return --- 'enter' (not recommended)\n\n"]))))


glyphInvalidVarName = ["space", "exclamation", "dblQuote", "number", "dollar", "percent", "ampersand", "singleQuote", "openParentheses", "closeParentheses", "asterisk", 
                       "plus", "comma", "hyphen", "period", "slash", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "colon", "semicolon", "lessThan", 
                       "equals", "greaterThan", "question", "at", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
                       None, None, None, None, None, None, None, None, "openBracket", "backslash", "closeBracket", "caret", "underscore", "grave", None, None, None, None, 
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "openCurlyBracket", "verticalBar", 
                       "closeCurlyBracket", "tilde"]

asciiTable.write("\t#Printable Character Codes:\n")
for i in range(32, 127):
    asciiGlyph = chr(i)
    
    if ((i >= 65) and (i <= 90)) or ((i >= 97) and (i <= 122)):
        if asciiGlyph.isupper() is True:
            asciiTable.write("".join(list(map(str, ["\t", chr(i), " = ", "chr(", i, ")", "\t#  ", chr(34), asciiGlyph, chr(34), "\n"]))))
        elif asciiGlyph.isupper() is False:
            asciiTable.write("".join(list(map(str, ["\t", chr(i), " = ", "chr(", i, ")", "\t#  ", chr(34), asciiGlyph, chr(34), "\n"]))))
        else:
            print("Error in letters on i ==", i, "and chr(i) ==", chr(i))
    elif (((i >= 32) and (i <= 64)) or ((i >= 91) and (i <= 96)) or ((i >= 123) and (i <= 127))):
        asciiTable.write("".join(list(map(str, ["\t", glyphInvalidVarName[i - 32], " = ", "chr(", i, ")", "\t#  ", chr(34), asciiGlyph, chr(34), "\n"]))))
    else:
        print("Error at bottom of loop on i ==", i, "and chr(i) ==", chr(i))


asciiTable.close()

#sp = subprocess.Popen([r"C:\Program Files (x86)\Notepad++\notepad++.exe", "ASCII_Table.txt"])