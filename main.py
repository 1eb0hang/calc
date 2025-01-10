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
    mode = Mode.HEX
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
        if self.mode = Mode.HEX:
            return
        text = self.root.ids.calc_input.text
        nums, symbols = separate(text)
        valid = True

        for i in range(len(nums)):
            if(not is_number(nums[i], self.mode)):
                valid = False
                break
            nums[i] = convert(nums[i], self.mode, Mode.HEX)

        if not valid:
            print("invalid")
            pass
        else:
            self.root.ids.calc_input.text = combine(nums, symbols)
            self.mode = Mode.HEX
            self.root.ids.calc_input.text = self.mode

    def dec_mode(self):
        if self.mode = Mode.DEC:
            return
        text = self.root.ids.calc_input.text
        nums, symbols = separate(text)
        valid = True

        for i in range(len(nums)):
            if(not is_number(nums[i], self.mode)):
                valid = False
                break
            nums[i] = convert(nums[i], self.mode, Mode.DEC)

        if not valid:
            print("invalid")
            pass
        else:
            self.root.ids.calc_input.text = combine(nums, symbols)
            self.mode = Mode.DEC

    def oct_mode(self):
        if self.mode = Mode.OCT:
            return
        text = self.root.ids.calc_input.text
        nums, symbols = separate(text)
        valid = True

        for i in range(len(nums)):
            if(not is_number(nums[i], self.mode)):
                valid = False
                break
            nums[i] = convert(nums[i], self.mode, Mode.OCT)

        if not valid:
            print("invalid")
            pass
        else:
            self.root.ids.calc_input.text = combine(nums, symbols)
            self.mode = Mode.OCT
            self.root.ids.calc_input.text = self.mode

    def bin_mode(self):
        if self.mode = Mode.BIN:
            return
        text = self.root.ids.calc_input.text
        nums, symbols = separate(text)
        valid = True

        for i in range(len(nums)):
            if(not is_number(nums[i], self.mode)):
                valid = False
                break
            nums[i] = convert(nums[i], self.mode, Mode.BIN)

        if not valid:
            print("invalid")
            pass
        else:
            self.root.ids.calc_input.text = combine(nums, symbols)
            self.mode = Mode.BIN
            self.root.ids.calc_input.text = self.mode



if __name__ == "__main__":
    CalculatorApp().run()
