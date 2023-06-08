import tempfile
from functools import cached_property

import gdstk

from .models import GdsCase


def read_memory_gds(raw: bytes) -> gdstk.Library:
    with tempfile.NamedTemporaryFile("w+b", suffix=".gds", delete=False) as tmp:
        print(11, tmp.name)
        tmp.write(raw)

        tmp.seek(0)
        fun = open(tmp.name, "rb").read()
        tmp.flush()
        print(22, len(fun))
        lib = gdstk.read_gds(tmp.name)
    return lib


def gds_to_svg(raw: bytes, root_cell="root") -> bytes:
    lib = read_memory_gds(raw)
    with tempfile.NamedTemporaryFile("rb", delete=False) as tmp:
        for c in lib.cells:
            if c.name == root_cell:
                c.write_svg(tmp.name)
        tmp.seek(0)
        svg = tmp.read()

    return svg


class QuestionAction:
    def __init__(self, case_obj: GdsCase) -> None:
        self.case = case_obj

    @cached_property
    def gdstk_lib(self) -> gdstk.Library:
        return read_memory_gds(self.case.grounding)

    # def judge() -> gdstk.Library:
