font-awesome-customize - Create custom versions of `Font Awesome`_
==================================================================

font-awesome-customize is a command-line tool written in Python that generates
custom versions of the iconic `Font Awesome`_ with just the icons you need.
If you only require a small subset of the icons provided by Font Awesome,
custom versions safe precious bandwidth.

The code is heavily based on `icnfnt`_ by Grant Gordon and Clay Johns.
The corresponding `icnfnt.com`_ web interface is very convenient for one-time use.
However, as your web application grows and requires more icons,
remembering which icons you need and selecting them by hand may be a hassle.
Instead, you may prefer automating the process with font-awesome-customize.


Quick Start
-----------

On Ubuntu, install the dependencies using::

    sudo apt-get install python-pip python-fontforge

Then, install font-awesome-customize from `PyPI`_ using::

    sudo pip install font-awesome-customize

To a custom version of `Font Awesome`_ containing the icons
``music`` and ``search`` in the folder ``fontawesome-custom``, use::

	font-awesome-customize -o fontawesome-custom music search

.. _Font Awesome: http://fortawesome.github.io/Font-Awesome/
.. _icnfnt: https://github.com/johnsmclay/icnfnt
.. _icnfnt.com: http://www.icnfnt.com/
.. _PyPI: https://pypi.python.org/pypi/font-awesome-customize/0.1