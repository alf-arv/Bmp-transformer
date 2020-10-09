import PySimpleGUI as sg
from modify_pictures import transform_picture_to_bmp

def main():
    sg.theme('Dark2')
    layout = [
        [sg.Text('Choose file: ',
                 font=12),
         sg.InputText(font=12),
         sg.FileBrowse('Choose file...', font=12),
        ],
        [sg.Submit('Transform', font=12),
         sg.Cancel('Quit', font=12)]
    ]

    window = sg.Window('Affe\'s BMP transformer 1.0', layout)
    while True:# Event Loop
        event, values = window.read()
        # print(event, values) #debug
        if(event == "Transform"):
            status = transform_picture_to_bmp(image_path_in=values['Choose file...'])
            if status:
                sg.popup('Transform complete!', title='Status', custom_text='Return',any_key_closes=True, font= 12)
                print('Transform complete!')
            elif not status:
                sg.popup('Transform failed.', title='Status', custom_text='Return', any_key_closes=True, font=12)
                print('Transform failed.')
        if event in (None, 'Exit', 'Quit'):
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
