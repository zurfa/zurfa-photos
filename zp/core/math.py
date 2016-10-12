

def image_constraints(wh, Max):
    """returns new image size constraints based on Max"""
    Width, Height   = wh
    Ratio   = float(Width)/float(Height)

    if Width > Height:
        Size    = (Max,int(Max/Ratio))
        return Size
    elif Width < Height:
        Size    = (int(Max*Ratio),Max)
        return Size
    else:
        Size    = (Max,Max)
        return Size