#!/usr/bin/env python3
from PIL import Image
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
