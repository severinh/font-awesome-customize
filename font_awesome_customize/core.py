import os.path

from xstatic.pkg import font_awesome

class Icon(object):
    def __init__(self, name, unicode_value):
        self._name = name
        self._unicode_value = unicode_value

    @property
    def name(self):
        return self._name

    @property
    def unicode_value(self):
        return self._unicode_value


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
    