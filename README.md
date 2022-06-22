# LDOCE5 Viewer (PyQt5)

The LDOCE5 Viewer is an alternative dictionary viewer for the Longman Dictionary of Contemporary English 5th Edition (LDOCE 5).

This project is ported to PyQt5 which supports retina (HiDPI) display.  

This software is free and open source software licensed under the terms of GPLv3.

## Dependency

### Arch Linux

```shell
sudo pacman -S python-pyqt5 python-lxml python-whoosh qt5-webkit qt5-multimedia gst-plugins-good gst-plugins-ugly python-gobject
```

### Ubuntu

```shell
sudo apt-get install git make python pyqt5-dev-tools python3-pyqt5 python3-pyqt5.qtwebkit python3-lxml python3-whoosh qtgstreamer-plugins-qt5
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
