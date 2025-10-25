from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


# -------- Clase de botón --------
class ScrButton(Button):
    def __init__(self, pantalla_actual, direccion, destino, **kwargs):
        super().__init__(**kwargs)
        self.pantalla_actual = pantalla_actual
        self.direccion = direccion
        self.destino = destino

    def on_press(self):
        self.pantalla_actual.manager.transition.direction = self.direccion
        self.pantalla_actual.manager.current = self.destino
    
    
class Seconds(Label):
    def __init__(self, total, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.current = 0
        self.text = f"Segundos pasados: {self.current}"
        self.running = False  # evita múltiples inicios

    def start(self):
        if not self.running:
            self.running = True
            self.current = 0  # reinicia el contador
            self.text = f"Segundos pasados: {self.current}"
            Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = f"Segundos pasados: {self.current}"
        if self.current >= self.total:
            self.running = False
            return False  # detiene el Clock