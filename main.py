from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

def get_kiv_data(file_path:str)->str:
    res = ""
    with open(file_path, "rt") as f:
        res = f.read()
    return res

class CalculatorApp(MDApp):
    def build(self):
        return Builder.load_string(get_kiv_data("kv.yml"))

    def on_button_click(self, button_text):
        """Append the button text to the input field."""
        calc_input = self.root.ids.calc_input
        calc_input.text += button_text

    def clear_input(self):
        """Clear the input field."""
        self.root.ids.calc_input.text = ""

    def calculate_result(self):
        """Evaluate the expression in the input field."""
        calc_input = self.root.ids.calc_input
        try:
            result = eval(calc_input.text)
            calc_input.text = str(result)
        except Exception:
            calc_input.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
