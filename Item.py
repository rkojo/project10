class Item():
  Name= None
  Description = None
  id = 0
  def __init__(self, num, itemName, description):
    self.id = num
    self.Name = itemName
    self.Description = description

