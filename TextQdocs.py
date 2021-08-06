#First Project
from colorama import Fore
from time import sleep
import time
import os

class TextQ(object):

  def __init__(self,selfname,colors='White'):
    self.selfname = selfname
    self.colors = colors

  def colorprint_category(self):

    if self.colors == 'Red':
      print('\n[',Fore.RED + self.selfname + Fore.RESET,']:')
    elif self.colors == 'Green':
      print('\n[',Fore.GREEN + self.selfname + Fore.RESET,']:')
    elif self.colors == 'Orange':
      print('\n[',Fore.YELLOW + self.selfname + Fore.RESET,']:')
    elif self.colors == 'Cyan':
      print('\n[',Fore.CYAN + self.selfname + Fore.RESET,']:')
    elif self.colors == 'Gray':
      print('\n[',Fore.LIGHTBLACK_EX + self.selfname + Fore.RESET,']:')
    elif self.colors == 'White':
      print('\n[',Fore.WHITE + self.selfname + Fore.RESET,']:')
    elif self.colors == 'Blue':
      print('\n[',Fore.BLUE + self.selfname + Fore.RESET,']:')
    else:
      print('Please Choose Either: Object(',self.selfname,')\n \nRed, \nGreen, \nOrange, \nCyan, \nGray, \nWhite, \nBlue \n\n[As Color Options]\n')
      msg = '54321'
      for i in range(5): print(msg[i],end='\r'); sleep(1)
      os.system('clear')
      exit()

  def speak(self,Text,Clear=True):
    if Clear == True:
      os.system('clear')

    self.colorprint_category()

    if type(Text) == str:
      letter_count = len(Text)
      for i in range(letter_count):
        print(Text[i], sep='', end='', flush=True); sleep(0.075)
      time.sleep(1)
      os.system('clear')
    elif type(Text) == list:
      counting_no = 0
      string_count = len(Text)
      counting_str = Text[counting_no]
      length_str = len(counting_str)
      for i in range(string_count):
          for i in range(length_str):
              print(counting_str[i], sep='', end='', flush=True); sleep(0.075)
          time.sleep(1)
          if Clear == True:
            os.system('clear')
            self.colorprint_category()
          else:
            print()
          counting_no = counting_no + 1
          if (counting_no != string_count):
              counting_str = Text[counting_no]
              length_str = len(counting_str)
          else:
              counting_no = 0
    else:
      print('NOTICE: Text has to either be a list, or a string!')

#Directions for use

#Import Class TextQ

#Assign to object as so

#Object = TextQ('fillInName','optional Color')
#Object.speak(Text_List) or Object.speak(str) or Object.speak(var_containing_list/str)

#Enjoy!



#Sample Code below to Experiment with!

#Just copy-paste in separate doc

#Remove triple quotes (''')

#And Run the code! :)

'''
from TextQdocs import TextQ

Sam = TextQ('Sam','Red')
Sam.speak('Hi!')
Sam.speak(['Whats Up?','How Are You','Think this is Cool?'])
var = 'Text stored in a variable'
Sam.speak(var)
'''