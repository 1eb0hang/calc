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
            result = eval(calc_input.text)
            calc_input.text = str(result)
        except Exception:
            calc_input.text = "Error"

    def hex_mode(self):
        text = self.root.ids.calc_input.text
        nums = get_numbers(text)
        valid = True
        for i in range(len(nums)):
            if(not is_num_hex(nums[i])):
                valid = False
                break
            nums[i] = DEC.to_hex(nums[i])

        if not valid:
            # pop up
            pass
        else:
            self.root.ids.calc_input.text = " ".join(nums)

    def dec_mode(self):
        text = self.root.ids.calc_input.text
        t = [j for i in ip.split('+') for j in i.split('.')]
        print(t)

    def oct_mode(self):
        pass

    def bin_mode(self):
        pass



if __name__ == "__main__":
    CalculatorApp().run()
