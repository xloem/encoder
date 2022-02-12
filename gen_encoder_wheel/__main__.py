#!/usr/bin/env python3
from PIL import Image
'''where i  left off I was looking to see if the imageio library could write 16-bit color pngs for more color depth.'''
import click

@click.command()
@click.option('--size', default=4096, help='Height of wheel.')
@click.option('--ratio', default=1.0, help='Aspect ratio of wheel. width = ratio * size')
@click.option('--dpi', default=1, help='Size multiplier.')
@click.option('--output', help='Output filename.')
def generate(size, ratio, dpi, output):
    height = size * dpi
    width = height * ratio

if __name__ == '__main__':
    generate()
