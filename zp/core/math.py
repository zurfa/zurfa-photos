

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


def hamming(primary, secondary):
    """Returns hamming distance between two hashes."""
    if len(primary) != len(secondary):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(primary, secondary))