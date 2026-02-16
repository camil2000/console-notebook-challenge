# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
import datetime
from idlelib.configdialog import HighPage


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []


    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Data: {self.creation_date}, {self.title}: {self.text}"

class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        if not self.notes:
            new_code = 1

        else:
            new_code = max(int(node.code) for node in self.notes) + 1

        new_note = Note(new_code, title, text, importance)
        self.notes.append(new_note)
        return new_code

    def delete_note




