# Importing PySimpleGUI and saving it as psg, to use as name to call future psg methods
import PySimpleGUI as psg

# Setting font and size of text in the GUI
psg.set_options(font=('Arial Bold', 16))

# Setting up the text in the GUI and saving the input with a variable name
# Also adding a button with the handler name 'Add' to use later so an action can be applied
# Also adding an exit button
layout = [
   [psg.Text('Enter your first name: '), psg.Input(key='-FIRST-')],
   [psg.Text('Enter your last name: '), psg.Input(key='-LAST-')],
   [psg.Text('Enter your email: '), psg.Input(key='-EMAIL-')],
   [psg.Text('Enter your phone number: '), psg.Input(key='-PHONE-')],
   [psg.Button("Add"), psg.Exit('Exit')],
]

# Creating the window with it's title and layout size
window = psg.Window('Personal Information', layout, size=(715, 230))

# Creating a while loop that runs until the program is closed or the exit button is pressed.
while True:
   # Creating an event that receives a value when an action occurs (For example if 'Add' is pressed)
   event, values = window.read()
   # Method for adding the textbox information to the .txt database if 'Add' is pressed
   if event == "Add":
      f = open("SpejderSportInfo.txt", "a")
      f.write("\nName: " + values['-FIRST-'] + " " + values['-LAST-'] + "\nEmail: " + values['-EMAIL-'] + "\nPhone: " +
              values['-PHONE-'] + "\n------------------------------------------------------")
      f.close()
   # Creating the events that break the while loop
   if event == psg.WIN_CLOSED or event == 'Exit':
      break

# Close the program
window.close()

