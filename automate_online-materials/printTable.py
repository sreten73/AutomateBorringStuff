def printTable(tableData):
    colwidth = [[] for _ in range(len(tableData))]
    mx = []
    for i in range(len(tableData)):
        for f in tableData[i]:
            colwidth[i].append(len(f))
        mx.append(max(colwidth[i]))
    print(tableData[0][0].rjust(mx[0]) + '  ' + tableData[1][0].rjust(mx[1]) + '  ' + tableData[2][0].rjust(mx[2]))
    print(tableData[0][1].rjust(mx[0]) + '  ' + tableData[1][1].rjust(mx[1]) + '  ' + tableData[2][1].rjust(mx[2]))
    print(tableData[0][2].rjust(mx[0]) + '  ' + tableData[1][2].rjust(mx[1]) + '  ' + tableData[2][2].rjust(mx[2]))
    print(tableData[0][3].rjust(mx[0]) + '  ' + tableData[1][3].rjust(mx[1]) + '  ' + tableData[2][3].rjust(mx[2]))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carolfgggdgdfg', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
#colwidth = [[] for _ in range(len(tableData))]
#mx = []
#for i in range(len(tableData)):
#    for f in tableData[i]:
#        colwidth[i].append(len(f))
#    mx.append(max(colwidth[i]))

#print(colwidth)
#print(mx)

#print(tableData[0][0].rjust(mx[0]) + '  ' + tableData[1][0].rjust(mx[1]) + '  ' + tableData[2][0].rjust(mx[2]))
#print(tableData[0][1].rjust(mx[0]) + '  ' + tableData[1][1].rjust(mx[1]) + '  ' + tableData[2][1].rjust(mx[2]))
#print(tableData[0][2].rjust(mx[0]) + '  ' + tableData[1][2].rjust(mx[1]) + '  ' + tableData[2][2].rjust(mx[2]))
#print(tableData[0][3].rjust(mx[0]) + '  ' + tableData[1][3].rjust(mx[1]) + '  ' + tableData[2][3].rjust(mx[2]))
#picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
#printPicnic(picnicItems, 12, 5)
#printPicnic(picnicItems, 20, 6)