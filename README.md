# LDOCE5 Viewer (PyQt5)

The LDOCE5 Viewer is an alternative dictionary viewer for the Longman Dictionary of Contemporary English 5th
Edition (LDOCE 5).

This project is ported to PyQt5 which supports retina (HiDPI) display.

This software is free and open source software licensed under the terms of GPLv3.

## Dependency

- pyenv
- Python version: `3.8`

```shell
pyenv install
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
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

## References

- [https://en.wikipedia.org/wiki/Cdb\_(software)](<https://en.wikipedia.org/wiki/Cdb_(software)>)
- [http://cr.yp.to/cdb/cdb.txt](http://cr.yp.to/cdb/cdb.txt)
- [https://github.com/PyQt5/PyQtWebKit](https://github.com/PyQt5/PyQtWebKit)
