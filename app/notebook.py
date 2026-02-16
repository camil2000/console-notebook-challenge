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





