import json
import random
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "500")

from assets.list_words import list_words
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.app import App

#TODO: Сделать слайды в карточках описания слов.
#TODO: Сделать вывод слов которые не угадал(список с переходом на карточку???).

class WordCheck(Widget):

    box = ObjectProperty(None)
    box_end = ObjectProperty(None)
    box_menu = ObjectProperty(None)
    box_words = ObjectProperty(None)
    box_ticket = ObjectProperty(None)
    grid_words = ObjectProperty(None)
    grid_ticket = ObjectProperty(None)
    label_end_count = ObjectProperty(None)
    button_next = ObjectProperty(None)
    buttons = ObjectProperty(None)
    input_search = ObjectProperty(None)
    input_infinitive = ObjectProperty(None)
    input_past_simple = ObjectProperty(None)
    input_participle = ObjectProperty(None)
    rus_word = ObjectProperty(None)
    rus_word_ticket = ObjectProperty(None)
    label_counter = ObjectProperty(None)
    ticket_infinitive = ObjectProperty(None)
    ticket_infinitive_trans = ObjectProperty(None)
    ticket_past_simple = ObjectProperty(None)
    ticket_past_simple_trans = ObjectProperty(None)
    ticket_participle = ObjectProperty(None)
    ticket_participle_trans = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(WordCheck, self).__init__(**kwargs)
        self.counter = 0
        self.checked_list = []
        self.infinitive_answer = ' '
        self.past_simple_answer = ' '
        self.participle_answer = ' '
        self.refs = [
            self.checked_list,
            self.box.__self__,
            self.box_end.__self__,
            self.box_menu.__self__,
            self.box_words.__self__,
            self.box_ticket.__self__,
            self.grid_words.__self__,
            self.grid_ticket.__self__,
            self.label_end_count.__self__,
            self.button_next.__self__,
            self.buttons.__self__,
            self.input_infinitive.__self__,
            self.input_past_simple.__self__,
            self.input_participle.__self__,
            self.rus_word.__self__,
            self.rus_word_ticket.__self__,
            self.label_counter.__self__,
            self.label_checked.__self__,
            self.ticket_infinitive.__self__,
            self.ticket_infinitive_trans.__self__,
            self.ticket_past_simple.__self__,
            self.ticket_past_simple_trans.__self__,
            self.ticket_participle.__self__,
            self.ticket_participle_trans.__self__,
        ]

        # with open("assets/eng_verbs_100.json") as file:
        #     self.list_words = json.load(file)
        self.list_words = list_words

    def build(self, *args):
        new_list_words = self.list_words[:]
        self.label_counter.text = f'Правильно угадано: {self.counter}'
        self.label_checked.text = f'{len(self.checked_list)} из {len(self.list_words)} слов'
        self.box.remove_widget(self.button_next)
        while len(self.checked_list) != len(self.list_words):
            word = random.choice(new_list_words)
            if not list(word.keys())[0] in self.checked_list:
                self.rus_word.text = f'{list(word.keys())[0]}'
                self.infinitive_answer = list(word.values())[0][0][0]
                self.past_simple_answer = list(word.values())[0][1][0]
                self.participle_answer = list(word.values())[0][2][0]
                self.checked_list.append(list(word.keys())[0])
                new_list_words.remove(word)
                return self.constructor()
        else:
            self.end_game()

    def end_game(self):
        self.remove_widget(self.box)
        self.label_end_count.text = f'Вы знаете {self.counter} слов/-о'
        self.add_widget(self.box_end)

    def constructor(self):
        self.input_infinitive.text = ''
        self.input_infinitive.background_color = (254/255, 244/255, 233/255, .8)
        self.input_infinitive.hint_text_color = 'grey'
        self.input_infinitive.hint_text = 'Введите слово на английском'

        self.input_past_simple.text = ''
        self.input_past_simple.background_color = (254/255, 244/255, 233/255, .8)
        self.input_past_simple.hint_text_color = 'grey'
        self.input_past_simple.hint_text = 'Введите слово на английском'

        self.input_participle.text = ''
        self.input_participle.background_color = (254/255, 244/255, 233/255, .8)
        self.input_participle.hint_text_color = 'grey'
        self.input_participle.hint_text = 'Введите слово на английском'

        self.box.add_widget(self.buttons)

    def valid_words(self, *args):
        count = 0
        if len(self.infinitive_answer.split(" ")) == 2:
            if self.input_infinitive.text.lower().strip() == self.infinitive_answer.split(" ")[0] \
                    or self.input_infinitive.text.lower().strip() == self.infinitive_answer.split(" ")[1]:
                self.input_infinitive.background_color = "green"
                count += 1
            else:
                # self.input_infinitive.background_color = "gray"
                pass

        else:
            if self.input_infinitive.text.lower().strip() == self.infinitive_answer:
                self.input_infinitive.background_color = "green"
                count += 1
            else:
                # self.input_infinitive.background_color = "gray"
                pass

        if len(self.past_simple_answer.split(" ")) == 2:
            if self.input_past_simple.text.lower().strip() == self.past_simple_answer.split(" ")[0] \
                    or self.input_past_simple.text.lower().strip() == self.past_simple_answer.split(" ")[1]:
                self.input_past_simple.background_color = "green"
                count += 1
            else:
                # self.input_past_simple.background_color = "gray"
                pass
        else:
            if self.input_past_simple.text.lower().strip() == self.past_simple_answer:
                self.input_past_simple.background_color = "green"
                count += 1
            else:
                # self.input_past_simple.background_color = "gray"
                pass
        if len(self.participle_answer.split(" ")) == 2:
            if self.input_participle.text.lower().strip() == self.participle_answer.split(" ")[0] \
                    or self.input_participle.text.lower().strip() == self.participle_answer.split(" ")[1]:
                self.input_participle.background_color = "green"
                count += 1
            else:
                # self.input_participle.background_color = "gray"
                pass
        else:
            if self.input_participle.text.lower().strip() == self.participle_answer:
                self.input_participle.background_color = "green"
                count += 1
            else:
                # self.input_participle.background_color = "gray"
                pass
        if count == 3:
            self.counter += 1
            self.label_counter.text = f'Правильно угадано: {self.counter}'
            self.box.remove_widget(self.buttons)
            self.box.add_widget(self.button_next)

    def check_answer(self, *args):
        self.box.remove_widget(self.buttons)
        self.box.add_widget(self.button_next)
        self.input_infinitive.text = self.infinitive_answer
        self.input_infinitive.background_normal = ''
        self.input_infinitive.background_color = (245/255, 151/255, 40/255, .8)

        self.input_past_simple.text = self.past_simple_answer
        self.input_past_simple.background_normal = ''
        self.input_past_simple.background_color = (245/255, 151/255, 40/255, .8)

        self.input_participle.text = self.participle_answer
        self.input_participle.background_normal = ''
        self.input_participle.background_color = (245/255, 151/255, 40/255, .8)

    def to_word_check(self):
        self.counter = 0
        self.checked_list = []
        self.add_widget(self.box)
        try:
            self.remove_widget(self.box_menu)
        except Exception as ex:
            print(f'BOX MENU - {ex}')
        try:
            self.remove_widget(self.box_words)
        except Exception as ex:
            print(f'BOX WORDS{ex}')
        try:
            self.remove_widget(self.box_ticket)
        except Exception as ex:
            print(f'BOX TICKET - {ex}')
        try:
            self.remove_widget(self.box_end)
        except Exception as ex:
            print(F'BOX END - {ex}')

        self.box.remove_widget(self.button_next)
        self.box.remove_widget(self.buttons)
        self.build()

    def to_menu(self):
        try:
            self.remove_widget(self.box)
        except Exception as ex:
            print(f'BOX - {ex}')
        try:
            self.remove_widget(self.box_words)
        except Exception as ex:
            print(f'BOX WORDS{ex}')
        try:
            self.remove_widget(self.box_ticket)
        except Exception as ex:
            print(f'BOX TICKET - {ex}')
        try:
            self.remove_widget(self.box_end)
        except Exception as ex:
            print(F'BOX END - {ex}')
        try:
            self.add_widget(self.box_menu)
        except:

            pass

    def ticket_word(self, instance):
        self.add_widget(self.box_ticket)

        try:
            self.remove_widget(self.box_words)
        except Exception as ex:
            print(f'BOX WORDS{ex}')

        self.rus_word_ticket.text = instance.name
        for word in self.list_words:
            if instance.name in word.keys():
                print(word.keys(), word[instance.name])
                ticket_word = word[instance.name]
                self.ticket_infinitive.text = ticket_word[0][0]
                self.ticket_infinitive_trans.text = ticket_word[0][1]
                self.ticket_infinitive_trans.font_name = 'freesans'
                self.ticket_past_simple.text = ticket_word[1][0]
                self.ticket_past_simple_trans.text = ticket_word[1][1]
                self.ticket_past_simple_trans.font_name = 'freesans'
                self.ticket_participle.text = ticket_word[2][0]
                self.ticket_participle_trans.text = ticket_word[2][1]
                self.ticket_participle_trans.font_name = 'freesans'

    def to_words(self):
        # l = Label(tex='')
        try:
            self.remove_widget(self.box_menu)
        except Exception as ex:
            print(f'BOX MENU - {ex}')
        try:
            self.remove_widget(self.box_ticket)
        except Exception as ex:
            print(f'BOX TICKET - {ex}')
        self.add_widget(self.box_words)
        self.grid_words.children.clear()
        for word in self.list_words:
            self.grid_words.add_widget(Button(
                name=f'{list(word.keys())[0]}',
                text=f'{word[list(word.keys())[0]][0][0]} ({list(word.keys())[0]})',
                background_color=(254/255, 244/255, 233/255, .8),
                background_normal='',
                color=(56/255, 150/255, 80/255, 1),
                size_hint=(.5, None),
                bold=True,
                height='50dp',
                on_press=self.ticket_word
            ))

    def previously_rm_buttons(self):
        self.remove_widget(self.box)
        self.remove_widget(self.box_words)
        self.remove_widget(self.box_ticket)
        self.remove_widget(self.box_end)


LabelBase.register(name='freesans',
                   fn_regular='assets/FreeSans.ttf')


class EnglishMainApp(App):

    def build(self):
        wc = WordCheck()
        wc.previously_rm_buttons()
        return wc


if __name__ == "__main__":
    EnglishMainApp().run()
