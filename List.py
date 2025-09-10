from Item import Item
from SmallItem import SmallItem
from MediumItem import MediumItem
from LargeItem import LargeItem

class productlist():
  _list = []
  def __init__(self):
    self.list = []

  def __str__(self):
    text = ""
    #no product
    if len(self.list) == 0:
       return "No product on this list"
    #loops all of list
    for a in self.list:
      itemsize = ""
      if type(a) == SmallItem:
          itemsize = "Small"
      elif MediumItem:
          itemsize = "Medium"
      elif LargeItem:
          itemsize = "Large"    
      text = text  + str(a.id) +" " + str(a.Name)+" " + str(a.Description) + itemsize + "\n"
    return text

  def add(self, product):
    self.list.append(product)
  
  def deleteall(self):
    self.list.clear()

  def showsize(self):
    return len(self.list)
  
  def get(self, num):
    return self.list[num]

  #for testing purposes - ensures that there is an intem which can happen. 
  def testadd(self):
     self.list.append(SmallItem(1,"test", "gege" ))
     self.list.append(MediumItem(2, "test1", "eoig"))