class ATM:
  def _init_(self):
    self.pin=""
    self.balance=0
    self.menu()
  def menu(self):
    user_input=input("""
    Hello, Welcome Back
    1.Press 1 create pin
    2.press 2 to change pin
    3.press 3 to check balance
    4.press 4 to withdraw
    5.press q to exit
    """)
    if user_input=='1':
      self.create_pin()
    
    elif user_input=='2':
      self.change_pin()
    
    elif user_input=='3':
      self.check_balance()
    
    elif user_input=='4':
      self.withdraw()
    else: 
      exit() 

  def create_pin(self):
    user_pin=input("Enter your pin")
    self.pin=user_pin

    user_balance=int(input("Enter your balance"))
    self.balance=user_balance
    print("pin created succesfully")
    self.menu()

  def change_pin(self):
    pass
  def check_balance(self):
    user_pin=input('enter your pin')
    if user_pin == self.pin:
      print("Your current balance is:",self.balance)
    else:
      print("Bhagja chod")
    
  def withdraw(self):
    user_pin=input('enter your pin')
    if user_pin == self.pin:
      amount=int(input("Enter amount to winthdraw"))
      if amount <= self.balance:
       self.balance=self.balance-amount
       print("Withdraw {} successfully".format(amount))