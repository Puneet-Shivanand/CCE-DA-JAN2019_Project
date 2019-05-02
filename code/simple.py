import PySimpleGUI as sg

layout = [
 [sg.Text('Please enter your Name, Address, Phone')],
 [sg.Text('Name', size=(15, 1)), sg.InputText('name', key='name')],
 [sg.Text('Address', size=(15, 1)), sg.InputText('address', key='address')],
 [sg.Text('Phone', size=(15, 1)), sg.InputText('phone', key='phone')],
 [sg.Submit(), sg.Cancel()]
 ]

window = sg.Window('Simple data entry window').Layout(layout)

button, values = window.Read()
print(button, values['name'], values['address'], values['phone'])
