from nicegui import ui
import nicegui as ng

@ng.ui.page('/')
def main():
    ui.button("est ce qu'il m'aime ?",on_click=lambda: ui.notify('Yes') )

    ui.button("est ce que je suis conne ?",on_click=lambda: ui.notify('Also Yes') )

ng.ui.run(host='0.0.0.0', port=443, title="Rim") 



