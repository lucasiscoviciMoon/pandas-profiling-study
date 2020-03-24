from .....report.presentation.core.warnings import Warnings
from .....report.presentation.flavours.html import templates


class HTMLWarnings(Warnings):
    def render(self):
        return templates.template("warnings.html").render(**self.content)
