# tests for color generation

import colorsys
import random

def from_name(name):
    random.seed(name)
    for irrelevant in range(len(name)):
        random.random()
    gr = 0.618033988749895
    hue = random.random()
    hue += gr
    hue = hue % 1
    a = colorsys.hsv_to_rgb(hue, 0.8, 0.6)
    return '#'+''.join(map(lambda x: '%0.2x' % (x*255), a))











if __name__ == "__main__":
    import sys
    name = sys.argv[1]
    print from_name(name)
