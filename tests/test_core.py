from font_awesome_customize.core import FontDescription
from font_awesome_customize.builder import CSSBuilder

def test_css_builder_glyph_extraction():
    source = FontDescription.of_source()
    glyphs = CSSBuilder.extract_glyphs(source)

    glyph = glyphs['music']
    assert glyph.name == 'music'
    assert glyph.unicode_value == 0xf001