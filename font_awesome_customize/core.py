import os.path

from collections import OrderedDict
from xstatic.pkg import font_awesome

class Glyph(object):
    def __init__(self, unicode_value, *icon_names):
        if len(icon_names) == 0:
            raise ValueError('icon must have at least one name')

        self._icon_names = icon_names
        self._unicode_value = unicode_value

    @property
    def icon_names(self):
        return list(self._icon_names)

    @property
    def unicode_value(self):
        return self._unicode_value


class GlyphSet(object):
    def __init__(self):
        self._map = OrderedDict()

    def __getitem__(self, icon_name):
        return self._map[icon_name]

    def add(self, glyph):
        for icon_name in glyph.icon_names:
            self._map[icon_name] = glyph

    def __contains__(self, icon_name):
        return icon_name in self._map


class FontDescription(object):
    def __init__(self, base_dir):
        self._base_dir = base_dir
        self._font_name = 'fontawesome'

    @staticmethod
    def of_source():
        return FontDescription(font_awesome.BASE_DIR)

    @property
    def base_dir(self):
        return self._base_dir

    @property
    def font_name(self):
        return self._font_name

    @property
    def font_folder(self):
        return os.path.join(self.base_dir, 'font')

    @property
    def eot_file(self):
        return os.path.join(self.font_folder, self.font_name + '-webfont.eot')

    @property
    def tff_file(self):
        return os.path.join(self.font_folder, self.font_name + '-webfont.ttf')

    @property
    def woff_file(self):
        return os.path.join(self.font_folder, self.font_name + '-webfont.woff')

    @property
    def css_folder(self):
        return os.path.join(self.base_dir, 'css')

    @property
    def css_file(self):
        return os.path.join(self.css_folder, 'font-awesome.css')

    @property
    def css_ie7_file(self):
        return os.path.join(self.css_folder, 'font-awesome-ie7.css')
    