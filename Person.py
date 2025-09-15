file = open("textfile.txt","w+")
from SmallItem import SmallItem
from MediumItem import MediumItem
from LargeItem import LargeItem

class Person():
  _order = []

  def __init__(self):
    self._order = []
  
  def __str__(self):
    text = ""
    if len(self._order) == 0:
       return "No product on this list"
    for a in self._order:
      itemsize = ""
      #check the type which is based on size
      if type(a) == SmallItem:
          itemsize = "Small"
      elif type(a) == MediumItem:
          itemsize = "Medium"
      elif type(a) == LargeItem:
          itemsize = "Large"   
          #add to text and have it as a new line 
      text = text  + str(a.id) +" " + str(a.Name)+" " + str(a.Description) + itemsize + "\n"
    return text
 

  def caution(self):
    text = ""
    for a in self._order:
      text = text + a.caution()+ "\n"
    return text
  
  def setOrder(self, order):
    self._order = order

  def addOrder(self, order):
    self._order.append(order)

  def get(self, name):
    return self._order[name]

  def showsize(self):
    return len(self._order)
  
  def clear(self):
    self._order.clear()
  