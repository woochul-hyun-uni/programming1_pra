from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_pra.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_all(self):
        self.root.ids.input_name.clear_widgets()
        self.root.ids.output_label.clear_widgets()

BoxLayoutDemo().run()