from Item import Item
from SmallItem import SmallItem
from MediumItem import MediumItem
from LargeItem import LargeItem
class productlist():
  _list = []
  def __init__(self):
    self._list = []

  def __str__(self):
    text = ""
    #no product
    if len(self._list) == 0:
       return "No product on this list"
    #loops all of list
    for a in self._list:
      itemsize = ""
      #check the class as this determines the type 
      if type(a) == SmallItem:
          itemsize = "Small"
      elif type(a) == MediumItem:
          itemsize = "Medium"
      elif  type(a) == LargeItem:
          itemsize = "Large"    
      text = text  + str(a.id) +" " + str(a.Name)+" " + str(a.Description)+" " + itemsize + "\n"
    return text

  def print(self):
     print(self._list)

  def add(self, product):
    self._list.append(product)
  
  def deleteall(self):
    self._list.clear()

  def showsize(self):
    return len(self._list)
  
  def get(self, num):
    return self._list[num]
  
  def remove(self, num):
     removeditem = self._list.pop(num)
     return removeditem
  
  def findIndex(self, num):
     for i in range(len(self._list)):
        if(self._list[i].id == num):
           return i
     return None
  
  #for testing purposes - ensures that there is an intem which can happen. 
  def testadd(self):
     self._list.append(SmallItem(1,"test", "a test item" ))
     self._list.append(MediumItem(2, "test1", "test item 2"))