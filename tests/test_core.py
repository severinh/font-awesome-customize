from nose.tools import *

from font_awesome_customize.core import Glyph, GlyphSet, FontDescription
from font_awesome_customize.builder import CSSBuilder

def test_glyph():
    '''Test creation and immutability of glyphs'''
    glyph = Glyph(0xf001, 'music')
    assert glyph.icon_names == ['music']
    assert glyph.unicode_value == 0xf001

    # Assert that the names attribute is immutable
    glyph.icon_names.append('search')
    assert glyph.icon_names == ['music']

@raises(Exception)
def test_invalid_glyph():
    '''Tests that glyphs must have at least one icon name'''
    glyph = Glyph(0xf000)


def test_glyph_set():
    '''Test creation and manipulation of glyph sets'''
    music_glyph = Glyph(0xf001, 'music')
    gear_cog_glyph = Glyph(0xf013, 'gear', 'cog')

    glyph_set = GlyphSet()
    glyph_set.add(music_glyph)
    glyph_set.add(gear_cog_glyph)

    assert glyph_set['music'] == music_glyph
    assert glyph_set['gear'] == gear_cog_glyph
    assert glyph_set['cog'] == gear_cog_glyph

    assert 'music' in glyph_set
    assert 'gear' in glyph_set
    assert 'cog' in glyph_set

def test_css_builder_glyph_extraction():
    source = FontDescription.of_source()
    glyphs = CSSBuilder.extract_glyphs(source)

    glyph = glyphs['music']
    assert glyph.icon_names == ['music']
    assert glyph.unicode_value == 0xf001