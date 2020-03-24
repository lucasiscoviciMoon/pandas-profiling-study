from PyQt5.QtWidgets import QPushButton

from .....report.presentation.core import HTML


class QtHTML(HTML):
    def render(self):
        return QPushButton(self.content["html"])
