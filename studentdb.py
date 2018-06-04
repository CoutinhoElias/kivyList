from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

import urllib.request
import json


class StudentListButton(ListItemButton):
    pass


class StudentDB(BoxLayout):
    # Connects the value in the TextInput widget to these
    # fields
    id_text_input = ObjectProperty()
    nomepessoa_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):

        # Get the student name from the TextInputs
        student_name = self.id_text_input.text + " " + self.nomepessoa_text_input.text

        # Add the student to the ListView
        self.student_list.adapter.data.extend([student_name])

        # Reset the ListView
        self.student_list._trigger_reset_populate()

    def delete_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Reset the ListView
            self.student_list._trigger_reset_populate()

    def replace_student(self, *args):

        # If a list item is selected
        if self.student_list.adapter.selection:
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Get the student name from the TextInputs
            student_name = self.id_text_input.text + " " + self.nomepessoa_text_input.text

            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])

            # Reset the ListView
            self.student_list._trigger_reset_populate()

    def list_student(self):
        url = "http://sosmypc.herokuapp.com/pessoas/"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)

        data = response.read().decode('utf-8')

        persons = json.loads(data)

        lista = [(linha['id'], linha['nomepessoa']) for linha in persons]

class StudentDBApp(App):
    def build(self):
        return StudentDB()


dbApp = StudentDBApp()

dbApp.run()