import os
import secrets
from sympy import primerange

class Main():
  
  def prime_p_value(self):
    while True:
      prime_numbers = primerange(1, 1000)
      
      try:
        self.agreed_prime = int(input('Enter Prime: ')) # P value
        
        if self.agreed_prime not in prime_numbers:
          print('\nEnter a Prime Number.')
        else:
          break
        
      except ValueError:
        print('\nInvalid Value')


  def generator_g_value(self):
    self.g_value = check_input('Enter Generator of P: ')
    
    
  def private_key(self):
    value_generator = range(1, 1000)
    self.private_key_value = secrets.choice(value_generator)
    
    
  def public_key(self): # Condition: (g_value ^ private_key_value) mod agreed_prime
    self.public_key_value = (self.g_value ** self.private_key_value) % self.agreed_prime
    
  
  def shared_secret_value(self): # Condition: (public_key_value ^ private_key_value) mod agreed_prime
    self.secret_value = (self.public_key_value ** self.private_key_value) % self.agreed_prime
  
  
  def display_values(self):
    print(f'\n  Agreed Prime: {self.agreed_prime}\n  Generator of P: {self.g_value}')
    print(f'\n  Public Key: {self.public_key_value}\n  Private Key: {self.private_key_value}')
    print(f'\n  Shared Secret Value: {self.secret_value}')
    
    

def check_input(value): # function that checks whether the input is an integer or not
  
  while True:
      try:
          user_input = int(input(value))
          break
        
      except ValueError:
          print("\nInvalid Input. INTEGERS only.")
  
  return user_input

main_obj = Main()
main_obj.prime_p_value()
main_obj.generator_g_value()
main_obj.private_key()
main_obj.public_key()
main_obj.shared_secret_value()
main_obj.display_values()