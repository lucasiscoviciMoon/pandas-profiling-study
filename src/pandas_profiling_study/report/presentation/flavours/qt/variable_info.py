from PyQt5.QtWidgets import QPushButton

from .....report.presentation.core import VariableInfo


class QtVariableInfo(VariableInfo):
    def render(self):
        return QPushButton("PyQt5 button")
