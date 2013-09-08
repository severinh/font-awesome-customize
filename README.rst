font-awesome-customize - Create custom versions of `Font Awesome`_
==================================================================

.. image:: https://travis-ci.org/severinh/font-awesome-customize.png
   :alt: Travis CI build status
   :target: https://travis-ci.org/severinh/font-awesome-customize

font-awesome-customize is a command-line tool written in Python that generates
custom versions of the iconic `Font Awesome`_ with just the icons you need.
If you only require a small subset of the icons provided by Font Awesome,
custom versions safe precious bandwidth.

The code is heavily based on `icnfnt`_ by Grant Gordon and Clay Johns.
The corresponding `icnfnt.com`_ web interface is very convenient for one-time use.
However, as your web application grows and requires more icons,
remembering which icons you need and selecting them by hand may be a hassle.
Instead, you may prefer automating the process with font-awesome-customize.


Usage
-----

On Ubuntu, install font-awesome-customize from `PyPI`_ and its dependencies using::

    sudo apt-get install python-pip python-fontforge
    sudo pip install font-awesome-customize

To generate a custom version of `Font Awesome`_ containing the icons
``music`` and ``search`` in the current directory, use::

	font-awesome-customize music search

Alternatively, use the ``-o`` option to indicate what folder to put
the CSS and font files in.

.. _Font Awesome: http://fortawesome.github.io/Font-Awesome/
.. _icnfnt: https://github.com/johnsmclay/icnfnt
.. _icnfnt.com: http://www.icnfnt.com/
.. _PyPI: https://pypi.python.org/pypi/font-awesome-customize/0.1