# LDOCE5 Viewer (PyQt5)

**The repo is archived, please refer to [ldoce5viewer-pyside6](https://github.com/WikiNeo/ldoce5viewer-pyside6)**

The LDOCE5 Viewer is an alternative dictionary viewer for the Longman Dictionary of Contemporary English 5th
Edition (LDOCE 5).

This project is ported to PyQt5 which supports retina (HiDPI) display.

This software is free and open source software licensed under the terms of GPLv3.

## Dependency

- [uv](https://github.com/astral-sh/uv)

## Development

```shell
uv sync
source .venv/bin/activate
python ldoce5viewer.py
```

## Install

```shell
make
sudo make install
```

## Arch Linux

```shell
sudo pacman -S libxml2-legacy
```

## References

- [https://en.wikipedia.org/wiki/Cdb\_(software)](<https://en.wikipedia.org/wiki/Cdb_(software)>)
- [http://cr.yp.to/cdb/cdb.txt](http://cr.yp.to/cdb/cdb.txt)
- [https://github.com/PyQt5/PyQtWebKit](https://github.com/PyQt5/PyQtWebKit)
