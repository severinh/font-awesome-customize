import logging

from optparse import OptionParser

from .core import FontDescription
from .builder import Builder

def build(icon_names, output_dir):
    target = FontDescription(output_dir)

    with Builder() as builder:
        for icon_name in icon_names:
            builder.add_glyph(icon_name)

        builder.write(target)

def main():
    usage = 'Usage: %prog [options] ICON_NAMES'
    parser = OptionParser(usage=usage, version=0.1)
    parser.add_option('-o', '--output-dir', dest='output_dir',
        default='.', help='create custom font in OUTPUT_DIR [default: %default]')
    parser.add_option('-v', '--verbose', dest='verbose',
        default=False, help='output detailed information during generation')
    (options, icon_names) = parser.parse_args()

    if len(icon_names) == 0:
        parser.error('must specify at least one icon name')

    level = logging.INFO
    if options.verbose:
        level = logging.DEBUG
    logging.basicConfig(level=level)

    build(icon_names, options.output_dir)