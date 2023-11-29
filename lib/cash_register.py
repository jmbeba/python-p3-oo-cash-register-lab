#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_price = 0
    
  def add_item(self, item_name, price, quantity=1):
    for n in range(quantity):
      self.items.append(item_name)
      
    self.total+= (price * quantity)
    self.last_price = price * quantity
    
  def apply_discount(self):
    if(self.discount != 0):
      self.total = int(self.total * ( (100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:  
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    self.items.pop()
    self.total -= self.last_price