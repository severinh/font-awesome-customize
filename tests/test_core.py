from font_awesome_customize.core import FontDescription
from font_awesome_customize.builder import CSSBuilder

def test_css_builder_icon_extraction():
    source = FontDescription.of_source()
    icons = CSSBuilder.extract_icons(source)

    icon = icons['music']
    assert icon.name == 'music'
    assert icon.unicode_value == 0xf001