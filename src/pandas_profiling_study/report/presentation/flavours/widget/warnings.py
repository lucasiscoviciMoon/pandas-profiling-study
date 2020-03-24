from ipywidgets import widgets

from .....report.presentation.core import Warnings
from .....report.presentation.flavours.html import templates


class WidgetWarnings(Warnings):
    def render(self):
        return widgets.HTML(templates.template("warnings.html").render(**self.content))
