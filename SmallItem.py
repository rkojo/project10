from Item import Item
class SmallItem(Item):

  def __init__(self, num, itemName, description):
    super().__init__(num, itemName, description)

  


  def caution(self):
    return ("Too small, not worth picking ")