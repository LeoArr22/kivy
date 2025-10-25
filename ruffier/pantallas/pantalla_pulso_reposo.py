from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from util.widgets_personalizados import ScrButton, Seconds
from util.intrucciones import instruccion_pantalla_pulso_reposo

# -------- Pantalla 2: Pulso en Reposo --------
class VentanaPulsoReposo(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #layouts
        layout = BoxLayout(orientation='vertical', padding=20)
        layout_superior = BoxLayout(orientation='vertical')
        formulario = BoxLayout(orientation='vertical', size_hint=(None, None), width=250, spacing=10)
        contenedor = AnchorLayout(anchor_x='center', anchor_y='bottom', padding=[0, 20, 0, 20])
        
        #widgets
        txt = Label(text=instruccion_pantalla_pulso_reposo)
        start_button = Button(text="Temporizador 15seg", size_hint=(1, 0.3))
        start_button.bind(on_press=self.iniciar_conteo)
        self.timer = Seconds(total=15)
        self.input_p0 = TextInput(hint_text="Pulsos en P0", multiline=False, size_hint_y=None, height=40)
        btn_sig = ScrButton(self, 'left', 'ventana_sentadillas', text="Siguiente", size_hint_y=None, height=50)
        btn_sig.bind(on_press=self.guardar_datos)
        btn_atras = ScrButton(self, 'right', 'ventana_principal', text="Regresar", size_hint_y=None, height=50)
        
        #add widget
        layout_superior.add_widget(txt)
        layout_superior.add_widget(start_button)
        layout_superior.add_widget(self.timer)
        formulario.add_widget(Label(text="Ingrese la cantidad de pulsos:", size_hint_y=None, height=30))
        formulario.add_widget(self.input_p0)
        formulario.add_widget(btn_sig)
        formulario.add_widget(btn_atras)
        
        #add layout
        contenedor.add_widget(formulario)
        
        layout.add_widget(layout_superior)
        layout.add_widget(contenedor)
        self.add_widget(layout)
        
    def guardar_datos(self, instance):
        app = App.get_running_app() #Obtenemos la instancia actual
        app.p0 = self.input_p0.text #A esa instancia, le agregamos un nuevo atributo
        
    def iniciar_conteo(self, instance):
        self.timer.start()
        