Map = open('Map.txt').read().split('\n')
Map.insert(0, ''.ljust(len(Map[0]), 'E'))
Map.append(''.ljust(len(Map[0]), 'E'))
GuardDire = '^'

for i in range(len(Map)):
    Map[i] = 'E' + Map[i] + 'E'
    Map[i] = list(Map[i])
    if Map[i].count(GuardDire) == 1:
        StartGuard = [i, Map[i].index('^')]
print(StartGuard)
GFile = open('BaseMap.txt', 'w')
for i in range(len(Map)):
    Map[i] = ''.join(Map[i])
Map = '\n'.join(Map)
GFile.write(Map)
GFile.close()
GuardMap = open('BaseMap.txt').read().split('\n')
for i in range(len(GuardMap)):
    GuardMap[i] = list(GuardMap[i])
Edge = False
GuardDire = '^'
LocCoor = []


while Edge == False:
    if GuardDire == '^':
        for i in range(len(GuardMap)):
            if GuardMap[i].count(GuardDire) == 1:
                Guard = [i, GuardMap[i].index(GuardDire)]
                LocCoor.append(Guard)
        if GuardMap[Guard[0]-1][Guard[1]] == '#':
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '>')
            GuardDire = '>'
        elif GuardMap[Guard[0]-1][Guard[1]] == 'E':
            Edge = True
        else:
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '|')
            GuardMap[Guard[0]-1].pop(Guard[1])
            GuardMap[Guard[0]-1].insert(Guard[1], GuardDire)
            

    if GuardDire == '>':
        for i in range(len(GuardMap)):
            if GuardMap[i].count(GuardDire) == 1:
                Guard = [i, GuardMap[i].index(GuardDire)]
                LocCoor.append(Guard)
        if GuardMap[Guard[0]][Guard[1]+1] == '#':
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], 'v')
            GuardDire = 'v'
        elif GuardMap[Guard[0]][Guard[1]+1] == 'E':
            Edge = True
        else:
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '-')
            GuardMap[Guard[0]].pop(Guard[1]+1)
            GuardMap[Guard[0]].insert(Guard[1]+1, GuardDire)
            
            
    if GuardDire == 'v':
        for i in range(len(GuardMap)):
            if GuardMap[i].count(GuardDire) == 1:
                Guard = [i, GuardMap[i].index(GuardDire)]
                LocCoor.append(Guard)
        if GuardMap[Guard[0]+1][Guard[1]] == '#':
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '<')
            GuardDire = '<'
        elif GuardMap[Guard[0]+1][Guard[1]] == 'E':
            Edge = True
        else:
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '|')
            GuardMap[Guard[0]+1].pop(Guard[1])
            GuardMap[Guard[0]+1].insert(Guard[1], GuardDire)
            
            
    if GuardDire == '<':
        for i in range(len(GuardMap)):
            if GuardMap[i].count(GuardDire) == 1:
                Guard = [i, GuardMap[i].index(GuardDire)]
                LocCoor.append(Guard)
        
        if GuardMap[Guard[0]][Guard[1]-1] == '#':
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '^')
            GuardDire = '^'
        elif GuardMap[Guard[0]][Guard[1]-1] == 'E':
            Edge = True
        else:
            GuardMap[Guard[0]].pop(Guard[1])
            GuardMap[Guard[0]].insert(Guard[1], '-')
            GuardMap[Guard[0]].pop(Guard[1]-1)
            GuardMap[Guard[0]].insert(Guard[1]-1, GuardDire)
            

GFile = open('GuardMapObs.txt', 'w')
for i in range(len(GuardMap)):
    GuardMap[i] = ''.join(GuardMap[i])
GuardMap = '\n'.join(GuardMap)
GFile.write(GuardMap)
GFile.close()
GuardCoor = LocCoor.copy()
GuardCoor .pop(0)
Edge = False
GuardDire = '^'
loop = 0


for i in range(len(GuardCoor)):
    count = 0
    GuardMap = open('BaseMap.txt').read().split('\n')
    for n in range(len(GuardMap)):
        GuardMap[n] = list(GuardMap[n])
    Coor = GuardCoor[i]
    GuardMapCommit = []
    #print(Coor)
    GuardMap[Coor[0]].pop(Coor[1])
    GuardMap[Coor[0]].insert(Coor[1], '0')
    GFile = open('GuardCoor.txt', 'w')
    for i in range(len(GuardMap)):
        GuardMapCommit.append(''.join(GuardMap[i]))
    GuardMapCommit = '\n'.join(GuardMapCommit)
    GFile.write(GuardMapCommit)
    GFile.close()
    if Coor == [48, 36]:
            GuardMapCommit = []
    while Edge == False or count < 4:
        if GuardDire == '^':
            for m in range(len(GuardMap)):
                if GuardMap[m].count(GuardDire) == 1:
                    Guard = [m, GuardMap[m].index(GuardDire)]
            if Guard == [1, 106]:
                Edge = True
                break
            if GuardMap[Guard[0]-1][Guard[1]] == '#':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '>')
                GuardDire = '>'
            elif GuardMap[Guard[0]-1][Guard[1]] == 'E':
                Edge = True
                print('Edge:', True)
                break
            elif GuardMap[Guard[0]-1][Guard[1]] == '0':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '>')
                count += 1
                GuardDire = '>'
            else:
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '|')
                GuardMap[Guard[0]-1].pop(Guard[1])
                GuardMap[Guard[0]-1].insert(Guard[1], GuardDire)

        if GuardDire == '>':
            for x in range(len(GuardMap)):
                if GuardMap[x].count(GuardDire) == 1:
                    Guard = [x, GuardMap[x].index(GuardDire)]
            if GuardMap[Guard[0]][Guard[1]+1] == '#':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], 'v')
                GuardDire = 'v'
            elif GuardMap[Guard[0]][Guard[1]+1] == 'E':
                Edge = True
                break
            elif GuardMap[Guard[0]][Guard[1]+1] == '0':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], 'v')
                count += 1
                GuardDire = 'v'
            else:
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '-')
                GuardMap[Guard[0]].pop(Guard[1]+1)
                GuardMap[Guard[0]].insert(Guard[1]+1, GuardDire)

        if GuardDire == 'v':
            for y in range(len(GuardMap)):
                if GuardMap[y].count(GuardDire) == 1:
                    Guard = [y, GuardMap[y].index(GuardDire)]
            if GuardMap[Guard[0]+1][Guard[1]] == '#':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '<')
                GuardDire = '<'
            elif GuardMap[Guard[0]+1][Guard[1]] == 'E':
                Edge = True
                break
            elif GuardMap[Guard[0]+1][Guard[1]] == '0':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '<')
                count += 1
                GuardDire = '<'
            else:
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '|')
                GuardMap[Guard[0]+1].pop(Guard[1])
                GuardMap[Guard[0]+1].insert(Guard[1], GuardDire)

        if GuardDire == '<':
            for c in range(len(GuardMap)):
                if GuardMap[c].count(GuardDire) == 1:
                    Guard = [c, GuardMap[c].index(GuardDire)]
            if GuardMap[Guard[0]][Guard[1]-1] == '#':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '^')
                GuardDire = '^'
            elif GuardMap[Guard[0]][Guard[1]-1] == 'E':
                Edge = True
                break
            elif GuardMap[Guard[0]][Guard[1]-1] == '0':
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '^')
                count += 1
                GuardDire = '^'
            else:
                GuardMap[Guard[0]].pop(Guard[1])
                GuardMap[Guard[0]].insert(Guard[1], '-')
                GuardMap[Guard[0]].pop(Guard[1]-1)
                GuardMap[Guard[0]].insert(Guard[1]-1, GuardDire)
    

print(loop)