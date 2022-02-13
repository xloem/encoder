#!/usr/bin/env python3
from imageio import v3 as iio
import numpy as np
import click

@click.command()
@click.option('--size', default=4096, help='Height of wheel.')
@click.option('--ratio', default=1.0, help='Aspect ratio of wheel. width = ratio * size')
@click.option('--dpi', default=1, help='Size multiplier.')
@click.option('--output', help='Output filename.')
def generate(size, ratio, dpi, output):
    height = size * dpi
    width = height * ratio
    img = np.random.randint(0,0xffff,size=(int(width+.5),height,3),dtype=np.uint16)
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
