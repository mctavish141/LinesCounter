def countLinesInFile(f):
    lines = 0
    blankLines = 0
    commentedLines = 0
    logicalLines = 0

    for line in f:
        lines += 1
        isBlankLine = (not line or line.isspace())
        blankLines += isBlankLine
        logicalLines += not isBlankLine

        stringCharacter = None
        for character in line:
            if (character == "'" or character == '"') and (stringCharacter is None):
                stringCharacter = character
            elif (character is not None) and (character == stringCharacter) and (character != '#'):
                stringCharacter = None

            if (character == '#') and (stringCharacter is None):
                commentedLines += 1
                stringCharacter = character

                trimmedLine = line.lstrip()
                logicalLines -= (trimmedLine.find('#') == 0)

    maximumBlankLines = lines * 0.25
    physicalLines = lines if blankLines <= maximumBlankLines else lines - (blankLines - maximumBlankLines)

    print "---------"
    print "Lines: %d" % (lines)
    print "Blank lines: %d" % (blankLines)
    print "Commented lines: %d" % (commentedLines)
    print "Physical lines: %d" % (physicalLines)
    print "Logical lines: %d" % (logicalLines)
    print "---------"

def promptFilenameFromUser():
    userExited = False

    while not userExited:
        filename = raw_input("Enter filename to count or blank line to exit: ")
        if not filename or filename.isspace():
            userExited = True
        else:
            try:
                with open(filename, "r") as f:
                    countLinesInFile(f)
            except IOError:
                print 'File %s does not exist' % (filename)

promptFilenameFromUser()