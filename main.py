from nicegui import ui
import nicegui as ng


@ng.ui.page('/')
def main():
    ui.colors(accent='#6AD4DD')
    
    ui.button("est ce qu'il m'aime ?", icon='favorite' ,on_click=lambda: ui.notify('Yes'),color="red" ).style('position: absolute ; top: 30% ; left: 50%  ; transform: translate(-50%, -50%);  width: 40vh;  height: 20vh;  ')
    
    ui.button("est ce que je suis conne ?",on_click=lambda: ui.notify('Also Yes'), icon='help', color="blue" ).style('position: absolute ; top: 70% ; left: 50%  ; transform: translate(-50%, -50%);  width: 40vh;  height: 20vh;  ')

    

    
ng.ui.run(
    host='0.0.0.0',
    port=443,
    title="Rim",
    favicon='favicon.ico',
    dark=True
)



