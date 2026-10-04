#simpler code
#use enums for states instead of classes for states
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

class VendingMachine:
    def __init__(self):
        self.products = {}
        self.balance = 0

    def add_product(self, product):
        self.products[product.id] = product

    def insert_money(self, amt):
        self.balance += amt
        print(f"Inserted: ₹{amt}. Current balance: ₹{self.balance}")

    def select_product(self, product_id):
        if product_id not in self.products:
            print("Invalid code.")
            return

        prod = self.products[product_id]

        if prod.stock <= 0:
            print("Out of stock.")
            return
        if self.balance < prod.price:
            print(f"Insufficient funds. Need ₹{prod.price}, balance is ₹{self.balance}")
            return

        # Dispense & settle
        prod.stock -= 1
        self.balance -= prod.price
        print(f"Dispensed: {prod.name}. Remaining change: ₹{self.balance}")


#=======================================================================


#using state pattern
#OCP followed- adding new states will not require changes to existing code
#VENDING MACHINE
from abc import ABC,abstractmethod
class product:
  def __init__(self,id,name,price):
    self.id = id
    self.name = name
    self.price = price

class inventory:
  def __init__(self):
    self.products = {}
    self.stock = {}
  def addProduct(self,product,quantity):
    self.products[product.id] = product
    self.stock[product.id] = quantity
  def getProduct(self,id):
    return self.products[id]
  def isAvail(self,id):
    if self.stock[id] > 0:
      return True
    return False
  def reduceStock(self,id):
    if self.isAvail(id):
      self.stock[id] -= 1
    
#Interface for state defining all posiible actions
#  in different states of vending machine
class state(ABC):
  @abstractmethod
  def insertMoney(self,amt):
    pass
  @abstractmethod
  def select_product(self,amt):
    pass
  @abstractmethod
  def dispense(self,amt):
    pass

class IdleState(state):
  def insertMoney(self,vm,amt):
    vm.balance += amt
    vm.setState(vm.HasMoneyState)
    print('amount inserted itno machine')
  def select_product(self,vm,id):
    print('amount not inserted yet')
  def dispense(self,vm,id):
    print('no active transaction')

    
class HasMoneyState(state):
  def insertMoney(self,vm,amt):
    vm.balance += amt
    print('amount inserted itno machine')
    
  def select_product(self,vm,id):
    product = vm.inventory.getProduct(id)
    if not product:
      print('invalid code')
    if not vm.inventory.isAvail(id):
      print('stock unavailable')
    if vm.balance < product.price:
      print('insufficient funds')
    vm.currCode = id
    vm.setState(vm.DispenseState)
    vm.dispense()
    
  def dispense(self,vm,id):
    print('please choose item first')

    
class DispenseState(state):
  def insertMoney(self,vm, amt):
        print("Currently dispensing. Cannot accept coins.")

  def select_product(self,v,id):
      print("Currently dispensing an item.")
    
  def dispense(self,vm):
    id = vm.currCode
    product = vm.inventory.getProduct(id)

    vm.inventory.reduceStock(id)
    vm.balance -= product.price
    print(f'dispensed:{product.name}')

    vm.currCode = None
    vm.setState(vm.IdleState)


# main class user interacts with- maintains ref to 
# current state and inventory
class VendingMachine:
  def __init__(self):
    self.inventory = inventory()
    self.balance = 0
    self.currCode =None

    self.IdleState = IdleState()
    self.HasMoneyState = HasMoneyState()
    self.DispenseState = DispenseState()

    self.state = self.IdleState

  def setState(self,state):
    self.state = state

  def insertMoney(self,amt):
    self.state.insertMoney(self,amt)

  def select_product(self,id):
    self.state.select_product(self,id)
  
  def dispense(self):
    self.state.dispense(self)

#Main function
vm = VendingMachine()
p1 = product('1','A',10)
p2 = product('2','B',20)

vm.inventory.addProduct(p1,2)
vm.inventory.addProduct(p2,5)

vm.insertMoney(50)
vm.select_product('2')
    