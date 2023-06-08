import gdstk

lib = gdstk.Library()
cell = lib.new_cell("root")
cell.add(gdstk.rectangle((0, 0), (1, 1)))
lib.write_gds("test.gds")
gdstk.read_gds("test.gds")
