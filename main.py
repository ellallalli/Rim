from nicegui import ui
import nicegui as ng


@ng.ui.page('/')
def main():
    ui.colors(accent='#6AD4DD')
    with ui.page_sticky(x_offset=670, y_offset=700):

        ui.button("est ce qu'il m'aime ?", icon='favorite' ,on_click=lambda: ui.notify('Yes'),color="red"  )
    with ui.page_sticky(x_offset=650, y_offset=600):
        ui.button("est ce que je suis conne ?",on_click=lambda: ui.notify('Also Yes'), icon='help', color="blue" )

    

    
ng.ui.run(
    host='0.0.0.0',
    port=443,
    title="Rim",
    favicon='favicon.ico',
   dark=True
)



