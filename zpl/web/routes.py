import zpl
import pprint
import pandas as pd
from zpl.core.frames import FrameLoad, Frames


app = zpl.app


@app.route('/1')
def one():
    FL=FrameLoad()
    FL.load_items()
    return str(Frames.items)

@app.route('/2')
def two():
    # FrameLoad=FrameLoad()
    # FrameLoad.load_items()
    return str(zpl.Frames.items)