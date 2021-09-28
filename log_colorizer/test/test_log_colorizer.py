# -*- coding: utf-8 -*-
# Copyright (C) 2011 by Florian Mounier, Kozea
# This file is part of brigit, licensed under a 3-clause BSD license.
import logging
import sys
from logging import (DEBUG, INFO, WARNING, ERROR, CRITICAL)
from log_colorizer import (
    ColorFormatter, make_colored_stream_handler, get_color_logger)

if sys.version_info[0] < 3:
    from io import BytesIO as StringIO
else:
    from io import StringIO


class FakeRecord(logging.LogRecord):

    def __init__(self,
               name='name', level=DEBUG, pathname='pathname', lineno=0,
               msg='msg', args=None, exc_info=None, func=None):
        logging.LogRecord.__init__(self,
            name, level, pathname, lineno,
            msg, args, exc_info, func)


def test_normal():
    color_formatter = ColorFormatter("%(msg)s")
    assert color_formatter.format(
        FakeRecord(level=DEBUG)) == "\x1b[0mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(level=INFO)) == "\x1b[0mmsg\x1b[0m"
    assert color_formatter.format(FakeRecord(msg='A')) == '\x1b[0mA\x1b[0m'
    assert color_formatter.format(FakeRecord(msg='À')) == '\x1b[0mÀ\x1b[0m'


def test_levels():
    color_formatter = ColorFormatter("$COLOR%(message)s")
    assert color_formatter.format(
        FakeRecord(level=DEBUG)) == "\x1b[0m\x1b[32mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(level=INFO)) == "\x1b[0m\x1b[34mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(level=WARNING)) == "\x1b[0m\x1b[33mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(level=ERROR)) == "\x1b[0m\x1b[31mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(level=CRITICAL)) == "\x1b[0m\x1b[35mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(level='UNKNOWN')) == "\x1b[0m\x1b[37mmsg\x1b[0m"


def test_log():
    sio = StringIO()
    handler = make_colored_stream_handler(std=sio)
    logr = logging.getLogger('test_log_colorizer')
    logr.addHandler(handler)
    logr.warning('HALP!')

    sio.seek(0)
    res = sio.read()
    assert res.startswith('\x1b[0m\x1b[?77h\x1b[33m')
    assert res.endswith(
            '\x1b[0mHALP! at '
            '\x1b[1m\x1b[33mtest_log:57'
            '\x1b[0m\x1b[?77l\x1b[0m\n')


def test_get_color_logger():
    assert get_color_logger() == logging.root
    assert get_color_logger('test_get_color_logger') != logging.root
    assert get_color_logger('test_get_color_logger') == logging.getLogger(
        'test_get_color_logger')
    sio = StringIO()
    logr = get_color_logger('test_get_color_logger', std=sio)
    logr.warning('HALP!')
    sio.seek(0)
    res = sio.read()
    assert res.startswith('\x1b[0m\x1b[?77h\x1b[33m')
    assert res.endswith(
        '\x1b[0mHALP! at '
        '\x1b[1m\x1b[33mtest_get_color_logger:75'
        '\x1b[0m\x1b[?77l\x1b[0m\n')
