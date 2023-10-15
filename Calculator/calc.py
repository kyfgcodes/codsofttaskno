# Build a calculator

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700)


Builder.load_file("calc.kv")


class CalcLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"
    
    
    #Create function to remove last character in text box
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        #Output back to the text
        self.ids.calc_input.text = prior
    
    def percentage(self):
        prior = self.ids.calc_input.text
        percent = int(prior)/ 100
        self.ids.calc_input.text = str(percent)
        
    
    # Create +/- function
    def pos_convert(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text= f"{prior.replace('-', '')}"
             
        else:
            self.ids.calc_input.text = f"-{prior}"
    

    #Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f"{prior}."
            #print on text box
            self.ids.calc_input.text = prior
     
        elif "." in prior:
            pass
        else:
            #Add a dot
            prior = f"{prior}."
            #print on text box
            self.ids.calc_input.text = prior
        


    # Create a button press function
    def button_press(self, button):
        # A variable that contains what was in the text already
        prior = self.ids.calc_input.text
        
        #Test for error first
        if "Error" in prior:
            prior = ""
        # Determine if 0 is in text
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{prior}{button}"

    # Create math function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        # Add a plus sign to text box
        self.ids.calc_input.text = f"{prior}{sign}"
    
        

    def equal(self):
        prior = self.ids.calc_input.text
        #Error Handling
        try:
            #Evaluate the math from the text box
            answer = eval(prior)
            #Output answer to text box
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
    
        


class CalculatorApp(App):
    def build(self):
        return CalcLayout()


if __name__ == "__main__":
    CalculatorApp().run()