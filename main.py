from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from num import *

def get_kiv_data(file_path:str)->str:
    res = ""
    with open(file_path, "rt") as f:
        res = f.read()
    return res




class CalculatorApp(MDApp):
    mode = Mode.DEC
    def build(self):
        return Builder.load_string(get_kiv_data("kv.yml"))

    def on_button_click(self, button_text):
        """Append the button text to the input field."""
        calc_input = self.root.ids.calc_input
        calc_input.text += button_text

    def clear_input(self):
        """Clear the input field."""
        self.root.ids.calc_input.text = ""

    def backspace(self):
        """Remove most recent char."""
        self.root.ids.calc_input.text = "".join(list(self.root.ids.calc_input.text)[:-1])

    def calculate_result(self):
        """Evaluate the expression in the input field."""
        calc_input = self.root.ids.calc_input
        try:
            print(convert_sum(self.root.ids.calc_input.text, self.mode, Mode.DEC))
            sum = convert_sum(self.root.ids.calc_input.text, self.mode, Mode.DEC)
            result = eval(sum)
            calc_input.text = convert_sum(str(result), Mode.DEC, self.mode)
        except Exception as e:
            print(e)
            calc_input.text = "Error"


    def hex_mode(self):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.HEX)
        self.mode = Mode.HEX

    def dec_mode(self):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.DEC)
        self.mode = Mode.DEC

    def oct_mode(self):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.OCT)
        self.mode = Mode.OCT

    def bin_mode(self):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.BIN)
        self.mode = Mode.BIN


if __name__ == "__main__":
    CalculatorApp().run()
