from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pantallas.principal import VentanaPrincipal
from pantallas.pantalla_pulso_reposo import VentanaPulsoReposo
from pantallas.pantalla_sentadillas import VentanaSentadillas
from pantallas.pantalla_pulso_esfuerzo import VentanaPulsoEsfuerzo
from pantallas.pantalla_final import Ventana_Final



# -------- Clase principal de la app --------
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(VentanaPrincipal(name="ventana_principal"))
        sm.add_widget(VentanaPulsoReposo(name="ventana_pulso_reposo"))
        sm.add_widget(VentanaSentadillas(name="ventana_sentadillas"))
        sm.add_widget(VentanaPulsoEsfuerzo(name="ventana_pulso_esfuerzo"))
        sm.add_widget(Ventana_Final(name='ventana_final'))
        return sm


# -------- Ejecutar app --------
MyApp().run()
