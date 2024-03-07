# import subprocess
import webbrowser
import pyautogui
import time
import os

python_course_link = 'https://www.udemy.com/course/complete-python-bootcamp/?couponCode=ST12MT030524'
vs_code_learn_python_path = "D:/001 - Kolehiyolo/Projects/Data Science/Python/Udemy - Bootcamp From Zero to Hero"

modes = [
  {
    "name": "Learn Python",
    "keyword": "learn_python",
    "description": 
      '''
        Focus on learning Python with the ff:
        . Udemy - The Complete Python Bootcamp From Zero to Hero in Python
        . Visual Studio Code - Bootcamp From Zero to Hero (Directory)
        . Jupyter Notebook - Bootcamp From Zero to Hero (Directory)
      '''
    ,
    "config_instructions": 
      '''
        Sample instructions...
      '''
    ,
    "check_config": lambda: (
      print("Checking config if valid..."),
      True
    ),
    "go_focus": lambda: (
      print('Activating "Learn Python" mode...'),
      pyautogui.hotkey('win', 'ctrl', 'd'),
      time.sleep(2), 
      webbrowser.open_new(python_course_link),
      os.system('start cmd /k python -m notebook'),
      os.system(f'code "{vs_code_learn_python_path}"'),
      print("Learning Python mode activated!"),
    ),
  },
  {
    "name": "Learn Unity",
    "keyword": "learn_unity",
    "description": 
      '''
        Sample description...
      '''
    ,
    "config_instructions": 
      '''
        Sample instructions...
      '''
    ,
    "check_config": lambda: (
      print("Checking config if valid..."),
      True
    ),
    "go_focus": lambda: (
      print('Activating "Learn Unity" mode...')
    ),
  },
  {
    "name": "Learn Blender",
    "keyword": "learn_blender",
    "description": 
      '''
        Sample description...
      '''
    ,
    "config_instructions": 
      '''
        Sample instructions...
      '''
    ,
    "check_config": lambda: (
      print("Checking config if valid..."),
      False
    ),
    "go_focus": lambda: (
      print('Activating "Learn Blender" mode...')
    ),
  },
]

def choose_activity():
  os.system('cls')
  print("Welcome. What would you like to do? Tell me the number:")
  for index, mode in enumerate(modes, start=1):
    print(f"{index} - {mode['name']}")
  print(f"0 - Exit")

  choice = input("\nEnter your choice: ")
  return choice

if __name__ == "__main__":
  while True:
    def is_convertible_to_int(string):
      try:
        choice = int(string)
        return choice
      except ValueError:
        return False
      
    choice = is_convertible_to_int(choose_activity()) 
    os.system('cls')  
    if (choice is False):
      print("Invalid choice. Please enter a valid option.")
    else:
      if (not (choice >= 0 and choice <= len(modes))):
        print("Invalid choice. Please enter a valid option.")
      elif (choice == 0):
        print("Exiting program.")
        break
      elif (modes[choice-1]['check_config']()[1]):
        modes[choice-1]['go_focus']()
      else:
        print(f"{modes[choice-1]['config_instructions']}")

    # Ask the user if they want to choose another activity
    another_activity = input("\nDo you want to choose another activity? (y/n): ")
    if another_activity.lower() != 'y':
        print("Exiting program.")
        break
