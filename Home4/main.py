myUniqueList = []
myLeftovers = []


def add( item ):
    
    if item in myUniqueList:
        addRejected(item)
    else:
        myUniqueList.append( item )
    

def addRejected( thing ):
    myLeftovers.append( thing )

print( "How many items you want to add?")
number = int(input())
print("Insert the items")

while number > 0:
    items = str(input())
    add( items )
    number -=1

print(myUniqueList)
print(myLeftovers)