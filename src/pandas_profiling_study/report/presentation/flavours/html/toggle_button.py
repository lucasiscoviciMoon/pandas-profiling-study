from .....report.presentation.core import ToggleButton
from .....report.presentation.flavours.html import templates


class HTMLToggleButton(ToggleButton):
    def render(self):
        return templates.template("toggle_button.html").render(**self.content)
