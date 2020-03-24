from .....report.presentation.core import VariableInfo
from .....report.presentation.flavours.html import templates


class HTMLVariableInfo(VariableInfo):
    def render(self):
        return templates.template("variable_info.html").render(**self.content)
