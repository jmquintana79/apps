import PySimpleGUI as sg
import os
import pandas as pd

# set theme
sg.theme('Dark') 
# windows layout
layout = [
    [sg.Text('Path File'), sg.InputText(), sg.FileBrowse(), sg.Checkbox('tail')],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]

# create windows
window = sg.Window('Read CSV', layout)

# event loop
while True:       
    # read windows
    event, values = window.read()
    # EVENT: stop
    if event in (None, 'Exit', 'Cancel'):
        break
    # EVENT: run
    if event == 'Submit':
        # parse values
        path_file = values[0]
        istail = values[1]
        # validate if path file exists
        if not os.path.exists(path_file):
            print('[warning] this file not exists.')
        else:
            df = pd.read_csv(path_file)
            if istail:
                print(df.tail())
            else:
                print(df.head())

window.close()