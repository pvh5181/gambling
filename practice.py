

softlst = ["A, 2", "A, 3", "A, 4", "A, 5", "A, 6", "A, 7", "A, 8"]


keyA2 = ["h", "h", "h", "d", "d", "h", "h", "h", "h", "h"]
keyA3 = ["h", "h", "h", "d", "d", "h", "h", "h", "h", "h"]
keyA4 = ["h", "h", "d", "d", "d", "h", "h", "h", "h", "h"]
keyA5 = ["h", "h", "d", "d", "d", "h", "h", "h", "h", "h"]
keyA6 = ["h", "d", "d", "d", "d", "h", "h", "h", "h", "h"]
keyA7 = ["s", "d", "d", "d", "d", "s", "s", "h", "h", "h"]
keyA8 = ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s"]

softkeyabrv = [ ["h", "h", "h", "d", "d", "h", "h", "h", "h", "h"], ["h", "h", "h", "d", "d", "h", "h", "h", "h", "h"], ["h", "h", "d", "d", "d", "h", "h", "h", "h", "h"], ["h", "h", "d", "d", "d", "h", "h", "h", "h", "h"], ["h", "d", "d", "d", "d", "h", "h", "h", "h", "h"],  ["s", "d", "d", "d", "d", "s", "s", "h", "h", "h"], ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s"]]



splitlst = ["2, 2", "3, 3", "4, 4", "5, 5", "6, 6", "7, 7", "8, 8", "9, 9", "T, T", "A, A"]
deallst = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "A"]


key22 = ["split", "split", "split", "split", "split", "split", "hit", "hit", "hit", "hit"]
key33 = ["split", "split", "split", "split", "split", "split", "hit", "hit", "hit", "hit"]
key44 = ["hit", "hit", "hit", "split", "split", "hit", "hit", "hit", "hit", "hit"]
key55 = ["double", "double", "double", "double", "double", "double", "double", "double", "hit", "hit"]
key66 = ["split", "split", "split", "split", "split", "hit", "hit", "hit", "hit", "hit"]
key77 = ["split", "split", "split", "split", "split", "split", "hit", "hit", "hit", "hit"]
key88 = ["split", "split", "split", "split", "split", "split", "split", "split", "split", "split"]
key99 = ["split", "split", "split", "split", "split", "stand", "split", "split", "stand", "stand"]
keyTT = ["stand", "stand", "stand", "stand", "stand", "stand", "stand", "stand", "stand", "stand"]
keyAA = ["split", "split", "split", "split", "split", "split", "split", "split", "split", "split"]

splitkey = [["split", "split", "split", "split", "split", "split", "hit", "hit", "hit", "hit"], ["split", "split", "split", "split", "split", "split", "hit", "hit", "hit", "hit"], ["hit", "hit", "hit", "split", "split", "hit", "hit", "hit", "hit", "hit"], ["double", "double", "double", "double", "double", "double", "double", "double", "hit", "hit"], ["split", "split", "split", "split", "split", "hit", "hit", "hit", "hit", "hit"], ["split", "split", "split", "split", "split", "split", "hit", "hit", "hit", "hit"], ["split", "split", "split", "split", "split", "split", "split", "split", "split", "split"], ["split", "split", "split", "split", "split", "stand", "split", "split", "stand", "stand"], ["stand", "stand", "stand", "stand", "stand", "stand", "stand", "stand", "stand", "stand"],  ["split", "split", "split", "split", "split", "split", "split", "split", "split", "split"]]

splitkeyabrv = [["p", "p", "p", "p", "p", "p", "h", "h", "h", "h"], ["p", "p", "p", "p", "p", "p", "h", "h", "h", "h"], ["h", "h", "h", "p", "p", "h", "h", "h", "h", "h"], ["d", "d", "d", "d", "d", "d", "d", "d", "h", "h"], ["p", "p", "p", "p", "p", "h", "h", "h", "h", "h"], ["p", "p", "p", "p", "p", "p", "h", "h", "h", "h"], ["p", "p", "p", "p", "p", "p", "p", "p", "p", "p"], ["p", "p", "p", "p", "p", "s", "p", "p", "s", "s"], ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],  ["p", "p", "p", "p", "p", "p", "p", "p", "p", "p"]]

for i in range(len(splitlst)):
    for j in range(len(deallst)):
        print("dealer:    " + deallst[j])
        print("your hand: " + splitlst[i])
        x = input("action? \n")
        if (x==(splitkey[i][j])):
            print()
            print("correct")
            print("--------")
            print()
        else:
            print()
            print("wrong")
            print("--------")
            print()

for i in range(len(softlst)):
    for j in range(len(deallst)):
        print("dealer:    " + deallst[j])
        print("your hand: " + softlst[i])
        x = input("action? \n")
        if (x==(softkeyabrv[i][j])):
            print()
            print("correct")
            print("--------")
            print()
        else:
            print()
            print("WRONG!!!!!!!!!!!!!!!!!!")
            print("--------")
            print()
