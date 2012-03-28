Log Colorizer
=============

Simple python logging colorizer formatter licensed under BSD for linux consoles
Copyright (C) 2011 by Florian Mounier, Kozea

Installation
------------

Use pip :

    pip install log_colorizer

And that's all.


Usage
-----

Basic usage:

```python
from logging import getLogger
from log_colorizer import make_colored_stream_handler
handler = make_colored_stream_handler()
logger = getLogger("library_name")
logger.addHandler(handler)

```
