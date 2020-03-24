from PyQt5.QtWidgets import QPushButton

from .....report.presentation.core import Sample


class QtSample(Sample):
    def render(self):
        return QPushButton(self.content["name"])
