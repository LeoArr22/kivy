from kivy.uix.button import Button


# -------- Clase de botón genérico --------
class ScrButton(Button):
    def __init__(self, pantalla_actual, direccion, destino, **kwargs):
        super().__init__(**kwargs)
        self.pantalla_actual = pantalla_actual
        self.direccion = direccion
        self.destino = destino

    def on_press(self):
        self.pantalla_actual.manager.transition.direction = self.direccion
        self.pantalla_actual.manager.current = self.destino