import loading

loading.loading()


def clearScreen():
  print("\n" * 1000)

def options():
  button_no_on_options_screen = 1 

  def options_controls():
    print("Type w to go up a element")
    print("Type s to go down a element")
    print("Press Enter to Click that Element")

  button_controls_active  = '|||||| CONTROLS ||||||'
  button_controls_passive = '|      CONTROLS      |'
  button_back_active      = '|||||||| BACK ||||||||'
  button_back_passive     = '|        BACK        |'

  while True:
    clearScreen()
    if button_no_on_options_screen == 1:
      print(button_controls_active)
      print(button_back_passive)
    if button_no_on_options_screen == 2:
      print(button_controls_passive)
      print(button_back_active)
    inputFromUser = input("> ")
    
    if inputFromUser == "w":
      if button_no_on_options_screen != 1:
        button_no_on_options_screen = button_no_on_options_screen - 1
    
    if inputFromUser == "s":
      if button_no_on_options_screen != 2:
        button_no_on_options_screen = button_no_on_options_screen + 1
    
    if inputFromUser == "":
      if button_no_on_options_screen == 1:
        options_controls()
      if button_no_on_options_screen == 2:
        clearScreen()
        title_screen()





def title_screen():
  print("\n" * 100)
  print("Enter w or s to toggle between buttons; Press Enter to Select")
  button_no_on_title_screen = 1;

  button_play_active    = '|||||| PLAY ||||||'
  button_play_passive   = '|      PLAY      |'

  button_option_active  = '|||||OPTIONS||||||'
  button_option_passive = '|    OPTIONS     |'


  button_exit_active    = '|||||| EXIT ||||||'
  button_exit_passive   = '|      EXIT      |'


  while True:
    if button_no_on_title_screen == 1:
      print(button_play_active)
      print(button_option_passive)
      print(button_exit_passive)
    if button_no_on_title_screen == 2:
      print(button_play_passive)
      print(button_option_active)
      print(button_exit_passive)
    if button_no_on_title_screen == 3:
      print(button_play_passive)
      print(button_option_passive)
      print(button_exit_active)
    
    inputFromUser = input('> ')


    if inputFromUser == "w":
      if button_no_on_title_screen != 1:
        button_no_on_title_screen = button_no_on_title_screen - 1
    
    if inputFromUser == "s":
      if button_no_on_title_screen != 3:
        button_no_on_title_screen = button_no_on_title_screen + 1

    if inputFromUser == "":
      if button_no_on_title_screen == 3:
        exit()
      
      if button_no_on_title_screen == 2:
        options()
    clearScreen()

title_screen()