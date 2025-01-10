from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from num import *

import traceback

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
            traceback.print_exc()
            calc_input.text = "Error"

    def toggle_mode(self, button):
        """Handle toggle behavior for the mode buttons."""
        # Reset the style of all buttons
        button_ids = ["hex_button", "dec_button", "oct_button", "bin_button"]
        for btn_id in button_ids:
            btn = self.root.ids[btn_id]
            btn.md_bg_color = (1, 1, 1, 1)  # Reset to default background color
            btn.text_color = (0, 0, 0, 1)   # Reset to default text color
            btn.line_color = (0, 0, 0, 0)   # Remove outline

        # Style the selected button
        button.md_bg_color = (0, 0, 1, 1)  # Blue background for active
        button.text_color = (1, 1, 1, 1)   # White text for active
        button.line_color = (1, 1, 1, 1)   # White outline for active

    # Update the active mode
    # print(f"Active mode: {self.mode.name}")


    def hex_mode(self, button):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.HEX)
        self.mode = Mode.HEX
        self.toggle_mode(button)

    def dec_mode(self, button):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.DEC)
        self.mode = Mode.DEC
        self.toggle_mode(button)

    def oct_mode(self, button):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.OCT)
        self.mode = Mode.OCT
        self.toggle_mode(button)

    def bin_mode(self, button):
        text = self.root.ids.calc_input.text
        self.root.ids.calc_input.text = convert_sum(text, self.mode, Mode.BIN)
        self.mode = Mode.BIN
        self.toggle_mode(button)


if __name__ == "__main__":
    CalculatorApp().run()
