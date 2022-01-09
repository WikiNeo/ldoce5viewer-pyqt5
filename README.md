# LDOCE5 Viewer (PyQt5)

This project is ported to PyQt5 which supports retina (HiDPI) display.  

The LDOCE5 Viewer is an alternative dictionary viewer for the Longman Dictionary of Contemporary English 5th Edition (LDOCE 5).

Website: http://hakidame.net/ldoce5viewer/

It runs on Linux, Mac OS X and Microsoft Windows.

This software is free and open source software licensed under the terms of GPLv3.

## Dependency

```shell
sudo pacman -S python-pyqt5 python-lxml python-whoosh qt5-webkit qt5-multimedia gst-plugins-good gst-plugins-ugly python-gobject
```

## Development

```shell
python ldoce5viewer.py
```

## Install

```shell
make
sudo make install
```