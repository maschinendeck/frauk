import colorsys
from fnvhash import fnv1a_32

def from_name(name):
    name = name.encode('utf-8')
    gr = 0.618033988749895
    hue =  float(fnv1a_32(name)) / 2**32
    hue += gr
    hue = hue % 1
    a = colorsys.hsv_to_rgb(hue, 0.8, 0.6)
    return '#'+''.join(map(lambda x: '%0.2x' % (x*255), a))


if __name__ == "__main__":
    import sys
    name = sys.argv[1]
    print from_name(name)
