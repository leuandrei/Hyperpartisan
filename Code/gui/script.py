from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from classify import metoda1

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')


class Content(GridLayout):
    opposite_color = True
    result_text = 'HyperPartisan'

    def classify(self):
        is_hyperpartisan = metoda1(self.ids.txt_input.text)

        if is_hyperpartisan:
            self.opposite_color = True
            self.ids.resultLayout.my_color = int(self.opposite_color), int(not self.opposite_color), 0, 1
            self.ids.resultLabel.text = 'HyperPartisan'
        else:
            self.opposite_color = False
            self.ids.resultLayout.my_color = int(self.opposite_color), int(not self.opposite_color), 0, 1
            self.ids.resultLabel.text = 'Not HyperPartisan'

    def change_result_color(self):
        self.ids.resultLayout.my_color = int(self.opposite_color), int(not self.opposite_color), 0, 1
        self.ids.resultLabel.text = self.result_text
        self.opposite_color = not self.opposite_color
        self.result_text = self.get_opposite_text(self.result_text)

    @staticmethod
    def get_opposite_text(text):
        if text == 'HyperPartisan':
            return 'Not HyperPartisan'
        else:
            return 'HyperPartisan'


class HyperPartisanApp(App):

    def build(self):
        return Content()


app = HyperPartisanApp()
app.run()
