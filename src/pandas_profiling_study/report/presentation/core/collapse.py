from typing import Any

from ....report.presentation.abstract.renderable import Renderable
from ....report.presentation.core.toggle_button import ToggleButton
from ....report.presentation.abstract.item_renderer import ItemRenderer


class Collapse(ItemRenderer):
    def __init__(self, button: ToggleButton, item: Renderable, **kwargs):
        super().__init__("collapse", {"button": button, "item": item}, **kwargs)

    def __repr__(self):
        return "Collapse"

    def render(self) -> Any:
        raise NotImplementedError()

    @classmethod
    def convert_to_class(cls, obj, flv):
        obj.__class__ = cls
        if "button" in obj.content:
            flv(obj.content["button"])
        if "item" in obj.content:
            flv(obj.content["item"])
