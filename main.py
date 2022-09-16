from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.core.window import Window
from kivy.config import Config
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import wget
import ssl


#Config.set('kivy', 'keyboard_mode', 'systemanddock')


#Window.size = (480, 850)

class Root(BoxLayout):
    path_save = "/storage/emulates/0"
    path_base = "base.py"

    def close_dialog_save(self, path):
        self.path_save = path
        self.popup_save.dismiss()

    def exit_dialog_save(self):
        self.popup_save.dismiss()

    def exit_dialog_base(self):
        self.popup_base.dismiss()

    def close_dialog_base(self, path):
        self.path_base = path
        self.popup_base.dismiss()

    def show_save(self):
        content = SaveDialog(close=self.close_dialog_save,
                             exit=self.exit_dialog_save)
        self.popup_save = Popup(title="choose directory", content=content)
        self.popup_save.open()

    def base_show(self):
        content = BaseDialog(close=self.close_dialog_base,
                             exit=self.exit_dialog_base)
        self.popup_base = Popup(title="choose base", content=content)
        self.popup_base.open()

    def download(self, name, start, stop):
        try:
            if self.path_base != "base.py":
                with open(self.path_base, "r") as new:
                    with open("base.py", 'w') as old:
                        old.write(new.read())
                self.path_base = "base.py"

            if name != "" and stop != "" and start != "":
                from base import base
                link = base[name.replace("-", "—")]
                s = link.split("/")
                link = ""
                for i in range(len(s)):
                    if i != 6:
                        link += s[i] + "/"
                    else:
                        link += "{}" + s[i][2:] + "/"
                link = link[:-1]
                for i in range(int(start), int(stop) + 1):
                    ssl._create_default_https_context = ssl._create_unverified_context
                    wget.download(link.format("0" + str(i)),
                                  out=self.path_save + "/" + str(i) + ".mp3",
                                  bar=None)
                    self.name.text = f"{i} скачано"
        except Exception as e:
            self.name.text = str(e)


class SaveDialog(BoxLayout):
    close = ObjectProperty(None)
    exit = ObjectProperty(None)


class BaseDialog(BoxLayout):
    close = ObjectProperty(None)
    exit = ObjectProperty(None)


class MyApp(App):
    pass


Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    MyApp().run()
