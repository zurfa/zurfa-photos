

def image_constraints(wh, max):
    """returns new image size constraints based on max."""
    Width, Height   = wh
    Ratio   = float(Width)/float(Height)

    if Width > Height:
        Size    = (max,int(max/Ratio))
        return Size
    elif Width < Height:
        Size    = (int(max*Ratio),max)
        return Size
    else:
        Size    = (max,max)
        return Size


