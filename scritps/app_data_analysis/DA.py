import PySimpleGUI as sg
import os
import pandas as pd

# set theme
sg.theme('Dark') 
# windows layout
layout = [
    [sg.Text('path file'), sg.InputText(), sg.FileBrowse()],
    [sg.Text('delimiter:'), sg.InputText(',',size=(2, 2)),sg.Text('dt column:'), sg.InputText(size=(8, 2)), sg.Text('dt format:'), sg.InputText('%Y-%m-%d %H:%M:%S',size=(10, 2))],
    [sg.Checkbox('tail')],
    [sg.Text('Data Files:')],
    [sg.Listbox(values=[], key='_DATA_', size=(44, 6))],
    [sg.Text('Terminal:')],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]


# initialize
ddata = dict()

# create windows
window = sg.Window('Data Analysis', layout)

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
        delimiter = values[1]
        dt_column = values[2]
        dt_format = values[3]
        istail = values[4]
        # validate if path file exists
        if not os.path.exists(path_file):
            print('[warning] this file not exists.')
        else:
            # load data
            file_name = os.path.split(path_file)[-1]
            if dt_column == '':
                ddata[file_name] = pd.read_csv(path_file, delimiter = delimiter)
            else:
                pass
            # display
            print('\n[info] input file: "%s"'%file_name)
            print('[info] columns:')
            print(ddata[file_name].info())
        # update data list
        files=list(ddata.keys())
        window.FindElement('_DATA_').Update(values=files)
        #button, values = window.read()        

window.close()