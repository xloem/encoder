#!/usr/bin/env python3
from imageio import v3 as iio
import numpy as np
import click

# i used to have an idea for very precise position detection.
# i do not remember what that idea was.

def angle2intensity(distance, angle):
    return angle / np.pi / 2

@click.command()
@click.option('--size', default=4096, help='Height of wheel.')
@click.option('--ratio', default=1.0, help='Aspect ratio of wheel. width = ratio * size')
@click.option('--dpi', default=1, help='Size multiplier.')
@click.option('--output', help='Output filename.')
def generate(size, ratio, dpi, output):
    height = size * dpi
    fwidth = height * ratio
    width = int(fwidth+.5)
    x = np.tile(np.arange(width) / (fwidth - 1) * 2 - 1, (height, 1))
    y = np.tile((np.arange(height) / (height - 1) * 2 - 1)[:, None], width)
    dists = np.sqrt(x * x + y * y)
    angs = np.arctan2(x, y)
    img = (angle2intensity(dists, angs) * 0xffff + np.random.random((width, height))).astype(np.uint16)
    return write(output, img)

def write(fn, ndimg):
    first_exc = None
    for plugin, filt in (
            ('PNG-FI', lambda x:(x,)),
            (None, lambda x:x),
            ('PNG-ITK', lambda x:x)
    ):
        try:
            return iio.imwrite(fn, filt(ndimg), plugin=plugin)
        except Exception as e:
            if first_exc is None:
                first_exc = e
    raise first_exc

if __name__ == '__main__':
    generate()
