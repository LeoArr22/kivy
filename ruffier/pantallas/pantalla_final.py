from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from util.widgets_personalizados import ScrButton
from util.intrucciones import texto_resumen
from util.calculos import calcular_indice_ruffier
from util.validaciones import validar_datos

# -------- Pantalla 5: mostrar todos los datos --------
class Ventana_Final(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        self.resultado = Label(text="", size_hint_y=None, height=150)
        
        btn = ScrButton(self, 'right', 'ventana_principal', text="Volver al inicio", size_hint_y=None, height=50)
        
        layout.add_widget(self.resultado)
        layout.add_widget(btn)
        self.add_widget(layout)
    
    def on_pre_enter(self): # on_pre_enter ->Se va a ejecutar antes de que la pantalla aparezca en pantalla
        app = App.get_running_app()
        nombre = getattr(app, "nombre", "") #getattr ->Esto averigua si existe el atributo "nombre" en el objeto  app
        edad = getattr(app, "edad", "") #En caso de no existir, le asigna ""
        p0 = getattr(app, "p0", "")
        p1 = getattr(app, "p1", "")
        p2 = getattr(app, "p2", "")

        try:
            nombre, edad, p0, p1, p2 = validar_datos(nombre, edad, p0, p1, p2)
            indice = calcular_indice_ruffier(p0, p1, p2)
            self.resultado.text = texto_resumen(nombre, edad, p0, p1, p2, indice)
        except ValueError as e:
            self.resultado.text = str(e)
