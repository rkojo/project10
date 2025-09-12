import copy
from Objects import MainItems, SpecialsList
import sys
from SmallItem import SmallItem
from MediumItem import MediumItem
from LargeItem import LargeItem
from List import productlist

def textout(): ##this is a separate function to enable returning back to this menu
  print("Select 1 to create a product")
  print("Select 2 to add to specials List")
  print("Select 3 to delete a specials list product")
  print("Select 4 to view a specials list")
  print("Select 5 to view a product list")
  try: 
    #is in a try loop to ensure that it is any integer 
    choice = int(input("Select an option between 1-5 or 0 to exit "))
  except:
    textout()
  match choice:
    case 0: #exits out of the code
      sys.exit(0)
    case 1:
      firstOption()
    case 2:
      secondOption()
    case 3:
      thirdOption()
    case 4:
      fourthOption()
    case 5:
      fifthOption()
    case _: #if it is an integer that is not one of the 6 options, it calls the same program
      textout() 

##create a product
def firstOption():
  print("Product Creation ")
  #ensures any inputerrors return to textout rather than exiting the program
  try: 
    nm = input("Enter Name ")
    num = MainItems.showsize() + 1
    sz = int(input("Enter Size (1 = Small, 2 = Medium, 3 = Large) "))
    ##ensures that sz is one of these numbers
    while (sz >0 and sz >3): 
      sz = int(input("Enter Size (1 = Small, 2 = Medium, 3 = Large) ")) 
    desc = input("Enter Description")
     ##there shouldnt be any errors, but more for redundancy
    try:
      if(sz == 1):
        MainItems.add(SmallItem(num, nm, desc))
      if(sz == 2):
        MainItems.add(MediumItem(num, nm, desc))
      if(sz == 3):
        MainItems.add(LargeItem(num, nm, desc))
      print("Item successfully Added")
    except:
      print("error - Invalid format")
      option = int(input("Press 1 to try again or 2 to return to menu"))
      if(option == 1):
        firstOption()
      if(option == 2):
        textout()
  except:
    print("Error - Please Try Again")
    textout()
  textout()

##create specials list from the productlist
def secondOption():
  print("Specials List Creation")
  print("Choose from your Products List")
  #declared as a productlist to directly copy mainitems object. 
  choicelist: productlist = copy.deepcopy(MainItems)
  bl = True
  while bl == True and choicelist:
    print(choicelist)
    a = int(input("Select each Item or select 0 to quit "))
    if(a == 0): ##if the user wants to quit
      bl = False
      textout()
    try:
      SpecialsList.add(choicelist.remove((choicelist.findIndex(a)))) 
    except:
      print("Error - Please Try Again or press 0 to quit ")
  textout()

##delete Specials list
def thirdOption():
  print("Are you sure?")
  a = input("Type \"DELETE\" to delete ")
  if a == "DELETE":
    SpecialsList.deleteall()
    textout()
  else:
    textout()

##View specials list
def fourthOption():
  print(SpecialsList)
  textout()

def fifthOption():
  print(MainItems)
  textout()


