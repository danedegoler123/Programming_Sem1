word = input("Please enter a word: ")

def printTri():
    for i in range(len(word)-1, 0, -1):
        print(word[0:i])

printTri()         


        
