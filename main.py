import PySimpleGUI as sg
from modify_pictures import transform_picture_to_bmp

def main():
    sg.theme('Dark2')
    layout = [
        [
            sg.Text('Choose file: ',font=12),
            sg.InputText(font=12),
            sg.FileBrowse('Choose file...', font=12),
        ],
        [
            sg.Checkbox('Use original dimensions', font=12),
            sg.Text('Width (px): ',font=12),
            sg.InputText(font=12, size=(7,10)),
            sg.Text('Height (px): ',font=12),
            sg.InputText(font=12, size=(7,10)),
            sg.Text('Scale: ', font=12),
            sg.InputText(font=12, size=(3, 10))
         ],
        [
            sg.Submit('Transform', font=12),
            sg.Cancel('Quit', font=12)
        ]
    ]

    window = sg.Window('Affe\'s BMP transformer 1.0', layout)
    while True:# Event Loop
        event, values = window.read()
        print(event, values) #debug
        if(event == "Transform"):
            if not values[1]:
                status = transform_picture_to_bmp(image_path_in=values['Choose file...'], width=values[2], height=values[3], scale=values[4])
                if status:
                    sg.popup('Transform complete!', title='Status', custom_text='Return',any_key_closes=True, font= 12)
                    print('Transform complete! (with specified dimensions)')
                else:
                    sg.popup('Transform failed.', title='Status', custom_text='Return', any_key_closes=True, font=12)
                    print('Transform failed.')
            if values[1]:
                status = transform_picture_to_bmp(image_path_in=values['Choose file...'], use_original_dimensions=True, scale=values[4])
                if status:
                    sg.popup('Transform complete!', title='Status', custom_text='Return', any_key_closes=True, font=12)
                    print('Transform complete! (with original dimensions)')
                else:
                    sg.popup('Transform failed.', title='Status', custom_text='Return', any_key_closes=True, font=12)
                    print('Transform failed.')
        if event in (None, 'Exit', 'Quit'):
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
