import loading


button_no = 1;

button_play_active    = '|||||| PLAY ||||||'
button_play_passive   = '|      PLAY      |'

button_option_active  = '|||||OPTIONS||||||'
button_option_passive = '|    OPTIONS     |'


button_exit_active    = '|||||| EXIT ||||||'
button_exit_passive   = '|      EXIT      |'

def clearScreen():
  print("\n" * 1000)

file_controls = open("controls.txt")

print("\n" * 100)
print("Enter w or s to toggle between buttons; Press Enter to Select")

while True:
  if button_no == 1:
    print(button_play_active)
    print(button_option_passive)
    print(button_exit_passive)
  if button_no == 2:
    print(button_play_passive)
    print(button_option_active)
    print(button_exit_passive)
  if button_no == 3:
    print(button_play_passive)
    print(button_option_passive)
    print(button_exit_active)
  
  inputFromUser = input('> ')


  if inputFromUser == "w":
    if button_no != 1:
      button_no = button_no - 1
  
  if inputFromUser == "s":
    if button_no != 3:
      button_no = button_no + 1

  if inputFromUser == "":
    if button_no == 3:
      exit()
  clearScreen()


