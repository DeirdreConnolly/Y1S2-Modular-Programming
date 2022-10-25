# Author:       Deirdre Connolly
# Filename:     Parameters and Arguments - Green Bottles Song.py
# Description:  Parameters and Arguments - Green Bottles Song

def sing_verse():
    i = 11
    while i > 1:
        i = i - 1
        print((str(i) + " green bottles hanging on the wall, " + "\n") * 2 +
            "And if one green bottle should accidentally fall, " + "\n" +
            "There'll be " + str(i - 1) + " green bottles hanging on the wall." + "\n")

sing_verse()
