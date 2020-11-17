import PySimpleGUI as sg
from modify_pictures import transform_picture_to_bmp

def main():

    # Set theme, window title and layout
    sg.theme('Dark2')
    layout = [
        [
            sg.Text('Choose file: ',font=12),
            sg.InputText(font=12, key='file_path'),
            sg.FileBrowse('Choose file...', font=12),
        ],
        [
            sg.Checkbox('Use original dimensions', enable_events=True ,font=12, default=False, key='orig_dim_checkbox'),
            #uod,
            sg.Text('Width (px): ',font=12),
            sg.InputText(font=12, size=(7,10), key='width_tb'),
            sg.Text('Height (px): ',font=12),
            sg.InputText(font=12, size=(7,10), key='height_tb'),
            sg.Text('Scale: ', font=12),
            sg.InputText(font=12, size=(3, 10), key='scale')
         ],
        [
            sg.Submit('Transform', font=12),
            sg.Cancel('Quit', font=12)
        ]
    ]
    window = sg.Window('BMP transformer 1.0', layout)

    # Event listener
    while True:
        event, values = window.read()

        # Disable dimension inputs when checkbox active
        if(values['orig_dim_checkbox']):
            window.FindElement('width_tb').Update(disabled = True)
            window.FindElement('width_tb').Update(value='')
            window.FindElement('height_tb').Update(disabled = True)

        # Enable dimension inputs when checkbox inactive
        if (not values['orig_dim_checkbox']):
            window.FindElement('width_tb').Update(disabled=False)
            window.FindElement('height_tb').Update(disabled=False)

        # If transform is clicked ...
        if(event == "Transform"):
            # ... and original dimensions should not be used ...
            if not values['orig_dim_checkbox']:
                # ... transform with specified dimensions
                status = transform_picture_to_bmp(image_path_in=values['Choose file...'], width=values['width_tb'], height=values['height_tb'], scale=values['scale'])

                # Notify user
                if status:
                    sg.popup('Transform complete!', title='Status', custom_text='Return',any_key_closes=True, font= 12)
                    print('Transform complete! (with specified dimensions)')
                else:
                    sg.popup('Transform failed.', title='Status', custom_text='Return', any_key_closes=True, font=12)
                    print('Transform failed.')

            # ... and original dimensions should be used ...
            if values['orig_dim_checkbox']:
                # ... transform
                status = transform_picture_to_bmp(image_path_in=values['Choose file...'], use_original_dimensions=True, scale=values['scale'])

                # Notify user
                if status:
                    sg.popup('Transform complete!', title='Status', custom_text='Return', any_key_closes=True, font=12)
                    print('Transform complete! (with original dimensions)')
                else:
                    sg.popup('Transform failed.', title='Status', custom_text='Return', any_key_closes=True, font=12)
                    print('Transform failed.')

        if event in (None, 'Exit', 'Quit'):
            break

# Runs on startup
if __name__ == '__main__':
    main()
