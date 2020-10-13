class Array:
  def __init__(self, length = 0, data = {}):
    self.length = length
    self.data = data
  
  def get(self, index):
    return self.data[index]
  
  def push(self, item):
    self.data[self.length] = item
    self.length += 1
  
  def pop(self):
    last_item = self.data[self.length - 1]
    del self.data[self.length - 1]
    self.length -= 1
    return last_item
  
  def delete(self, index):
    deleted_item = self.data[index]
    for i in range(index, self.length - 1):
      self.data[i] = self.data[i + 1]
    
    del self.data[self.length - 1]
    self.length -= 1
    return deleted_item
  
  def deleteItem(self, item):
    deleted_index = 0
    for i in range(self.length):
      if self.data[i] == item:
        deleted_index = i
    self.delete(deleted_index)
