import subprocess
import webbrowser
import pyautogui
import time
import os

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
          print('Activating "Learn Python" mode...')
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

# def create_new_desktop():
#     # Simulate Windows key + Ctrl + D to create a new desktop
#     pyautogui.hotkey('win', 'ctrl', 'd')

# def open_udemy_link(link):
#     webbrowser.open_new(link)

# def run_jupyter_notebook():
#     # Open a new Command Prompt window and run Jupyter Notebook
#     os.system('start cmd /k python -m notebook')

# def open_vscode(folder_path):
#     os.system(f'code "{folder_path}"')

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
        if (choice == False):
           print("Invalid choice. Please enter a valid option.")
        else:
          os.system('cls')  

          if (not (choice >= 0 and choice <= len(modes))):
            print("Invalid choice. Please enter a valid option.")
          elif (choice == 0):
            print("Exiting program.")
            break
          elif (modes[choice-1]['check_config']()[1]):
            modes[choice-1]['go_focus']()
          else:
            print(f"{modes[choice-1]['config_instructions']}")
        
        # elif choice == '2':
        #     print("Learning Python mode activated!")
        #     # Run the commands for learning Python
        #     create_new_desktop()
        #     time.sleep(2)  # Wait for desktop switch
        #     python_course_link = 'https://www.udemy.com/course/complete-python-bootcamp/?couponCode=ST12MT030524'
        #     open_udemy_link(python_course_link)
        #     run_jupyter_notebook()
        #     vs_code_learn_python_path = "D:/001 - Kolehiyolo/Projects/Data Science/Python/Udemy - Bootcamp From Zero to Hero"
        #     open_vscode(vs_code_learn_python_path)
        # elif choice == '3':
        #     print("Learning Unity mode activated!")
        #     # Add commands for learning Unity
        # elif choice == '4':
        #     print("DigiLance Cold Calling mode activated!")
        #     # Add commands for cold calling
        # elif choice == '5':
        #     print("Working on a Code Project mode activated!")
        #     # Add commands for working on a code project
        # elif choice == '6':
        #     print("Doing some music mode activated!")
        #     # Add commands for music
        # else:

        # Ask the user if they want to choose another activity
        another_activity = input("\nDo you want to choose another activity? (y/n): ")
        if another_activity.lower() != 'y':
            print("Exiting program.")
            break
