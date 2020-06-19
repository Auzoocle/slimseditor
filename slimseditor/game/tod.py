from reloadr import autoreload

from slimseditor.saveentry import RangedShort, Boolean, Integer


@autoreload
def get_tod_items():
    return {
        "Bolt counts": [
            Integer("Number of Bolts", 0x41c),
            Integer("Number of Raritanium", 0x420),
        ],
    }