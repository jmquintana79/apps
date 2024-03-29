"""
Python script to MacOS executable: $pyinstaller --windowed hello_world.py
"""

import PySimpleGUI as sg

# Add a touch of color
sg.theme('DarkAmber')   
# All the stuff inside your window.
layout = [  [sg.Text('Hello world!!!!')],
            [sg.Text('Insert your name:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()