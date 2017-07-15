# tests for color generation

import colorsys
import hashlib

def from_name(name):
    print type(name)
    name = name.encode('utf-8')
    gr = 0.618033988749895
    hue = hashlib.sha224(name).hexdigest() 
    hue = '0.'+''.join([c for c in hue if ord(c) in range(ord('0'),ord('9')+1)])
    hue = float(hue)
    hue += gr
    hue = hue % 1
    a = colorsys.hsv_to_rgb(hue, 0.8, 0.6)
    return '#'+''.join(map(lambda x: '%0.2x' % (x*255), a))











if __name__ == "__main__":
    import sys
    name = sys.argv[1]
    print from_name(name)
