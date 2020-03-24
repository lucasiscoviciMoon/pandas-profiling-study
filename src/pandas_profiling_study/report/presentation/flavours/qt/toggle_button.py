from PyQt5.QtWidgets import QPushButton

from .....report.presentation.core import ToggleButton


class QtToggleButton(ToggleButton):
    def render(self):
        return QPushButton("PyQt5 button")
