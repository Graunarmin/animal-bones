from typing import Tuple
from enum import Enum

"""
Credit to Benjamin Giese from medium.com: 
https://medium.com/@bengiese22/python-enums-how-you-should-be-using-them-92aef37714d2
"""


class Color(Enum):
    DARK_PINK = (1, (240, 62, 62), "#F03E3E")
    DARK_MAGENTA = (2, (214, 51, 108), "#D6336C")
    DARK_VIOLET = (3, (174, 62, 201), "#AE3EC9")
    DARK_BLUE = (4, (66, 99, 235), "#4263EB")
    DARK_TEAL = (5, (11, 114, 133), "#0B7285")
    DARK_GREEN = (6, (8, 127, 91), "#087F5B")
    DARK_LEMON = (7, (116, 184, 22), "#74B816")
    DARK_YELLOW = (8, (255, 146, 43), "#FF922B")
    DARK_RED = (9, (217, 72, 15), "#D9480F")

    PINK = (10, (255, 107, 107), "#FF6B6B")
    MAGENTA = (11, (240, 101, 149), "#F06595")
    VIOLET = (12, (204, 93, 232), "#CC5DE8")
    BLUE = (13, (92, 124, 250), "#5C7CFA")
    TEAL = (14, (34, 184, 207), "#22B8CF")
    GREEN = (15, (32, 201, 151), "#20C997")
    LEMON = (16, (148, 216, 45), "#94D82D")
    YELLOW = (17, (252, 196, 25), "#FCC419")
    RED = (18, (247, 103, 7), "#F76707")

    def __str__(self) -> str:
        return self.name.lower()

    def num(self) -> int:
        return self.value[0]

    def rgb(self) -> Tuple:
        return self.value[1]

    def hex(self) -> str:
        return self.value[2]
