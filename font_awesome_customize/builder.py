import fontforge
import os
import os.path
import re
import logging

from .core import Glyph, GlyphSet, FontDescription

class Builder(object):
    def __init__(self, source=None):
        if source is None:
            source = FontDescription.of_source()

        self._source = source

        self._font_builder = FontBuilder(source)
        self._css_builder = CSSBuilder(source)
        self._builders = [self._font_builder, self._css_builder]

        self._source_glyphs = CSSBuilder.extract_glyphs(source)
        self._glyphs = GlyphSet()

    def __enter__(self):
        for builder in self._builders:
            builder.__enter__()
        return self

    def __exit__(self, *args):
        for builder in self._builders:
            builder.__exit__(*args)

    def add_icon(self, icon_name):
        if icon_name not in self._glyphs:
            glyph = self._source_glyphs[icon_name]
            self._glyphs.add(glyph)

            for builder in self._builders:
                builder.add_glyph(glyph)

    @property
    def source(self):
        return self._source

    @property
    def custom_glyphs(self):
        return list(self._glyphs.values())

    def write(self, target):
        for builder in self._builders:
            builder.write(target)


class CSSBuilder(object):
    CSS_ICON_RULE_PATTERN = re.compile(r"""
        \.icon-(?P<name>[a-z-]+):before\s+{\s+
            content:\s*"[^\w](?P<content>[a-z0-9]+)";\s+
        }""", re.MULTILINE | re.VERBOSE)

    def __init__(self, source):
        self._base_css = None

        with open(source.css_file) as f:
            css = f.read()
            self._base_css = self.CSS_ICON_RULE_PATTERN.sub(css, '')

    def add_glyph(self, glyph):
        pass

    def write(self, target):
        if not os.path.exists(target.css_folder):
            os.makedirs(target.css_folder)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    @classmethod
    def extract_glyphs(cls, source):
        glyphs = GlyphSet()

        with open(source.css_file) as f:
            css = f.read()

            logging.debug('Loading glyph map from %s...', source.css_file)
            for match in cls.CSS_ICON_RULE_PATTERN.finditer(css):
                icon_name = match.group('name')
                unicode_value = int(match.group('content'), 16)
                
                glyph = Glyph(unicode_value, icon_name)
                glyphs.add(glyph)

                logging.debug('Found glyph \'%s\'', icon_name)

        return glyphs


"""
The code of this class is based on http://www.icnfnt.com/

Copyright: (C) 2012 by Grant Gordon and Clay Johns.
"""
class FontBuilder(object):
    def __init__(self, source):
        self._new_font = fontforge.font()


        # Set up the new font shell
        self._new_font.encoding = 'UnicodeFull'
        self._new_font.fontname = source.font_name
        self._new_font.fullname = source.font_name
        self._new_font.familyname = source.font_name
        self._new_font.ascent = 850
        self._new_font.em = 1792
        self._new_font.descent = 256
        self._new_font.gasp = ((65535, (
            'gridfit',
            'antialias',
            'symmetric-smoothing',
            'gridfit+smoothing')),)
        self._new_font.gasp_version = 1
        self._new_font.hhea_descent = -34
        self._new_font.hhea_linegap = 0
        self._new_font.os2_codepages = (1, 0)
        self._new_font.os2_fstype = 4
        self._new_font.os2_panose = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self._new_font.os2_strikeypos = 1075
        self._new_font.os2_strikeysize = 90
        self._new_font.os2_subyoff = 134
        self._new_font.os2_subysize = 1075
        self._new_font.os2_supyoff = 627
        self._new_font.os2_supysize = 1075
        self._new_font.os2_typolinegap = 0
        self._new_font.weight = 'Book'

        # Fire up the reference font
        self._source_font = fontforge.open(source.tff_file)
        self._source_font.encoding = 'UnicodeFull'

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._new_font.close()
        self._source_font.close()

    def add_glyph(self, glyph):
        # Find the glyph and copy it
        self._source_font.selection.select(('more', 'unicode', None),
            glyph.unicode_value)
        self._source_font.copy()
        
        # Create a new glyph at the next generated unicode address,
        # paste the outlines, re-name it
        self._new_font.selection.select(('unicode',), glyph.unicode_value)
        self._new_font.paste()
        self._new_font[glyph.unicode_value].glyphname = glyph.icon_names[0]
        
        # Clear the selections
        self._source_font.selection.none()
        self._new_font.selection.none()

    def write(self, target):
        if not os.path.exists(target.font_folder):
            os.makedirs(target.font_folder)

        self._new_font.generate(target.eot_file)
        self._new_font.generate(target.tff_file)
        self._new_font.generate(target.woff_file)