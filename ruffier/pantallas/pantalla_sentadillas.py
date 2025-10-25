from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from util.widgets_personalizados import ScrButton, Seconds
from util.intrucciones import instruccion_pantalla_sentadillas

# -------- Pantalla 3: Sentadillas --------
class VentanaSentadillas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #layouts
        layout = BoxLayout(orientation='vertical', padding=20)
        layout_superior = BoxLayout(orientation='vertical')
        layout_inferior = BoxLayout(orientation='vertical', size_hint_y=None)
        formulario = BoxLayout(orientation='vertical', size_hint=(None, None), width=250, spacing=10)
        contenedor = AnchorLayout(anchor_x='center')
        
        #widgets
        txt = Label(text=instruccion_pantalla_sentadillas)
        start_button = Button(text="Temporizador 45seg", size_hint=(1, 0.3))
        start_button.bind(on_press=self.iniciar_conteo)
        self.timer = Seconds(total=45)
        btn_sig = ScrButton(self, 'left', 'ventana_pulso_esfuerzo', text="Siguiente", size_hint_y=None, height=50)
        btn_atras = ScrButton(self, 'right', 'ventana_pulso_reposo', text="Regresar", size_hint_y=None, height=50)
        
        #add widget
        layout_superior.add_widget(txt)
        layout_superior.add_widget(start_button)
        layout_superior.add_widget(self.timer)
        formulario.add_widget(btn_sig)
        formulario.add_widget(btn_atras)
        
        #add layout
        contenedor.add_widget(formulario)
        layout_inferior.add_widget(contenedor)
        
        layout.add_widget(layout_superior)
        layout.add_widget(layout_inferior)
        self.add_widget(layout)
        
    def iniciar_conteo(self, instance):
        self.timer.start()
        
        