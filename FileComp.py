import os, itertools


path1 = input("Please enter first path: ")
path2 = input("Please enter second path: ")
output = input("Show all compared files and directories in output! (1)\n"
                "Only show different files and directories in output! (2) ")

def filesAndDirs(path1, path2):
    with os.scandir(path1) as it:
        global li1
        li1a = []
        li1b = []
        for entry in it:
            statinfo = os.stat(entry)
            if not entry.name.startswith('.'):
                if entry.is_dir():
                    li1a.append(entry.name)
                else:
                    li1b.append(entry.name)
            li1 = li1a + li1b
        #print(li1)
    with os.scandir(path2) as it:
        global li2
        li2a = []
        li2b = []
        for entry in it:
            statinfo = os.stat(entry)
            if not entry.name.startswith('.'):
                if entry.is_dir():
                    li2a.append(entry.name)
                else:
                    li2b.append(entry.name)
            li2 = li2a + li2b
        #print(li2)
        comp(li1, li2)
    #with os.scandir(path1) as it1, os.scandir(path2) as it2:
    for i,j in itertools.zip_longest(li1,li2):
        if i == None or j == None:
            print("Die gesamte Verzeichnisstruktur wurde durchsucht. Programm beendet!")
            break
        if "." not in i:
            path1 = path1 + "/" + i
            #print(path1)
        if "." not in j:
            path2 = path2 + "/" + j
            #print(path2)
        if "." not in i or "." not in j:
            filesAndDirs(path1, path2)
            l1 = path1.split("/")
            l1.pop()
            #print(l1)
            path1 = "/".join(l1)
            #print(l1)
            #print(path1)
            l2 = path2.split("/")
            l2.pop()
            #print(l2)
            path2 = "/".join(l2)
            #print(l2)
            #print(path2)
            
                      

def comp(li1, li2):
    if len(li1)==len(li2):
        for x,y in itertools.zip_longest(li1,li2):
            if output == "1":
                if x == y:
                    print(x, "   ==   ", y)
                else:
                    print(x, "   !=   ", y, "...ungleich!")
            else:
                if x != y:
                    print(x, "   !=   ", y, "...ungleich!")
    if len(li1)<len(li2):
        for x,y in itertools.zip_longest(li1,li2):
            if x != y and x != None:
                    li1.insert(li1.index(x), None)
        for x,y in itertools.zip_longest(li1,li2):
            if output == "1":
                if x == y:
                    print(x, "   ==   ", y)
                else:
                    print(x, "   !=   ", y, "...ungleich!")
            else:
                if x != y:
                    print(x, "   !=   ", y, "...ungleich!")
    if len(li2)<len(li1):
        for x,y in itertools.zip_longest(li1,li2):
            if x != y and y != None:
                li2.insert(li2.index(y), None)
        for x,y in itertools.zip_longest(li1,li2):
            if output == "1":
                if x == y:
                    print(x, "   ==   ", y)
                else:
                    print(x, "   !=   ", y, "...ungleich!")
            else:
                if x != y:
                    print(x, "   !=   ", y, "...ungleich!")
    
filesAndDirs(path1, path2)
