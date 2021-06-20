#Importing All Libraries
import os
import time
from time import sleep
import readline
import math

#Sample Text List
Sample1 = ['Hello World', 'Goodbye', 'Made by MCSlasher'] 

#Clear System
def clear():
  os.system('clear')

#Simple Delay System
def delay(seconds):
  time.sleep(seconds)

#Speech in Lists
def list_speech(text_list_data):
    global counting_no 
    counting_no = 0
    string_count = len(text_list_data)
    counting_str = text_list_data[counting_no]
    length_str = len(counting_str)
    for i in range(string_count):
        for i in range(length_str):
            print(counting_str[i], sep='', end='', flush=True); sleep(0.075)
        time.sleep(1)
        clear()
        counting_no = counting_no + 1
        if (counting_no != string_count):
            counting_str = text_list_data[counting_no]
            length_str = len(counting_str)
        else:
            counting_no = 0

#Pre-filled input
def prefill(prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input()
   finally:
      readline.set_startup_hook()
  
#Speech in Strs
def say(word_data):
  letter_count = len(word_data)
  for i in range(letter_count):
    print(word_data[i], sep='', end='', flush=True); sleep(0.075)
  time.sleep(1)
  clear()

#Learn About Modules
def learn(module):
  print(dir(module))

#say('Hello World')
#list_speech(Sample1)
#say('balalamasala')
#delay(10)
#clear()'''
learn(math)