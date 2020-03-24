from ipywidgets import widgets

from .....report.presentation.core import VariableInfo
from .....report.presentation.flavours.html import templates


class WidgetVariableInfo(VariableInfo):
    def render(self):
        return widgets.HTML(
            templates.template("variable_info.html").render(**self.content)
        )
