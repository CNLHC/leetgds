import os
import pathlib
import unittest

from leetgds import question

test_root = pathlib.Path(os.path.dirname(__file__))


with open(test_root / "test.gds", "rb") as fp:
    gds_bytes = fp.read()


class TestCaseAction(unittest.TestCase):
    def test_read_raw_gds(self):
        lib = question.read_memory_gds(gds_bytes)
        self.assertEqual(1, len(lib.cells))
        self.assertEqual("root", lib.cells[0].name)

    def test_write_svg(self):
        svg = question.gds_to_svg(gds_bytes)
        self.assertIn(b"<svg", svg)

