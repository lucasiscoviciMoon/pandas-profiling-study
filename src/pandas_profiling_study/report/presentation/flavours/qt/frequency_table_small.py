from PyQt5.QtWidgets import QPushButton

from .....report.presentation.core import FrequencyTableSmall


class QtFrequencyTableSmall(FrequencyTableSmall):
    def render(self):
        return QPushButton("Small Frequency Table")
