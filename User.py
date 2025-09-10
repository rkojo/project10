

#the user should be able to order
#check specials
#
from Objects import MainItems, SpecialsList
from Person import Person
import sys
aUser = Person()
def textout():
    print("Select 1 to order products")
    print("Select 2 to view specials List")
    print("Select 3 to view order List")
    try: 
      choice = int(input("Select an option between 1-3 or 0 to exit "))
    except:
      #Ensures that the input is a integer value
      print("ERROR")
      textout()
    match choice: 
      case 0:
          sys.exit(0)
      case 1:
          firstOption()
      case 2:
          secondOption()
      case 3:
          thirdOption()
      case 4:
          fourthOption()
      case _:
          textout() 

def firstOption():
  print("order")
  reorder = True 
  #it allows multiple reording to occur
  while reorder:
    try:
      print(MainItems)
      inp = int(input("Select products or select 0 to order or exit "))
      if inp == 0:
        reorder = False
        textout()
      else:
        try:
          aUser.addOrder(MainItems.get(inp-1))
          print("Added " + aUser.get((aUser.showsize()) -1).Name)
        except:
          print("No product exists")
    except:
       print("Please Try Again")
  


def secondOption():
  print(SpecialsList)

  textout()

def thirdOption():
   print(aUser)
   textout()

def fourthOption():
   print(aUser.caution())
   aUser.clear()
   textout()
