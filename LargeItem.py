from Item import Item
class LargeItem(Item):

  def __init__(self, num, itemName, description):
    super().__init__(num, itemName, description)


  def caution(self):
    return ("Please pick this up yourself. ")
