values = []
values.append([1, 2, 3, 4])
values.append([5, 6, 7, 8])
values.append([9, 10, 11, 12])
values.append([13, 14, 15, 16])

print("\nHere is what a list of lists looks like...")
print(values, "\n")
print(values[0][2], "\n")



print("Using range...") 
for i in range(0, len(values)): #puter loop: columns
    output = ""
    for j in range(0, len(values[i])): # inner loop: rows
        output += str(values[i][j]) + "\t"
    print(output + "\n")               


                   
print("Using enhanced loop...")                    
for value in values:
    output = ""
    for num in value:
        output += str(num) + "\t"
    print(output)




print("\nSearch the list...")
count = 0
for value in values:
    for number in value:
        if number % 5 == 0:
            count += 1
print("There are ", count, " multiples of 5 in the list.\n\n") 




lettersList = []
lettersList.append(["a", "b", "c", "d"])
lettersList.append(["e", "f", "g", "h"])
lettersList.append(["i", "j", "k", "l"])
lettersList.append(["m", "n", "o", "p"])

print("Here is a list with letters...")

for letters in lettersList:
    output = ""
    for letter in letters:
        output += letter + "\t"
    print(output)

print("\nHere is a list of words using split()")
wordsList = []

go = "father mother eagle house car office coffer make create laugh cry photo"
spList = go.split(" ")
print(spList)

spot = 0 # keeps track of where we are in spList

print("\nPrint the grid...")
for i in range(0, 3): # handles the collums
    output = ""
    wordsList.append([]) # creates new index
    for j in range(0, 4): # adds new list into the index (rows)
        wordsList[i].append(spList[spot])
        output += "{:15}".format(wordsList[i][j])
        spot += 1
    print(output)
