import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Gestore Corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        # usiamo un certo modo per definire i bottoni e i dd, con il tipo di dato, funzione e cosa restituiscono/gestiscono
        self.ddPD = None
        self.ddCodins = None #lo prendo da un dropdown
        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None
        self.lvTxtOut = None


    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddPD = ft.Dropdown(label="Periodo Didattico",
                                options=[ft.dropdown.Option("I"),
                                         ft.dropdown.Option("II")], width=200)
        self.ddCodins = ft.Dropdown(label="Corso", width=200, on_change=self._controller.ddCodinsSelected)
        self._controller.fillddCodins() # per inserire le options nel dropdown, lo fa il controller, che chiama il modello che chiede al dao

        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa corsi",
                                                 on_click=self._controller.handlePrintCorsiPD, width=250)
        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa numero iscritti",
                                                         on_click=self._controller.handlePrintIscrittiCorsiPD, width=250)
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa iscritti al corso",
                                                        on_click=self._controller.handlePrintIscrittiCodins, width=250)
        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS afferenti",
                                                   on_click=self._controller.handlePrintCDSCodins, width=250)

        self.lvTxtOut = ft.ListView(expand=True)

        row1 = ft.Row([self.ddPD, self.btnPrintCorsiPD, self.btnPrintIscrittiCorsiPD], alignment=MainAxisAlignment.CENTER)
        row2 = ft.Row([self.ddCodins, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins], alignment=MainAxisAlignment.CENTER)
        self._page.add( row1, row2, self.lvTxtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
