from PyQt5.QtWidgets import QPushButton

from .....report.presentation.core import Collapse


class QtCollapse(Collapse):
    def render(self):
        return QPushButton("PyQt5 button")
