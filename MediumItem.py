from Item import Item
class MediumItem(Item):
  super

  def __init__(self, num, itemName, description):
    super().__init__(num, itemName, description)

  

  def caution(self):
    return ("Have a 50 50 chance of picking up. ")
