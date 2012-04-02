# -*- coding: utf-8 -*-
# Copyright (C) 2011 by Florian Mounier, Kozea
# This file is part of brigit, licensed under a 3-clause BSD license.
import logging
from log_colorizer import ColorFormatter, make_colored_stream_handler
from io import StringIO


class FakeRecord(object):
    message = 'msg'
    levelname = 'DEBUG'
    exc_text = None
    exc_info = None
    stack_info = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def getMessage(self):
        return self.message


def test_normal():
    color_formatter = ColorFormatter("%(message)s")
    assert color_formatter.format(
        FakeRecord(levelname='DEBUG')) == "\x1b[0mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(levelname='INFO')) == "\x1b[0mmsg\x1b[0m"


def test_levels():
    color_formatter = ColorFormatter("$COLOR%(message)s")
    assert color_formatter.format(
        FakeRecord(levelname='DEBUG')) == "\x1b[0m\x1b[32mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(levelname='INFO')) == "\x1b[0m\x1b[34mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(levelname='WARNING')) == "\x1b[0m\x1b[33mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(levelname='ERROR')) == "\x1b[0m\x1b[31mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(levelname='CRITICAL')) == "\x1b[0m\x1b[35mmsg\x1b[0m"
    assert color_formatter.format(
        FakeRecord(levelname='UNKNOWN')) == "\x1b[0m\x1b[37mmsg\x1b[0m"


def test_log():
    sio = StringIO()
    handler = make_colored_stream_handler(std=sio)
    logr = logging.getLogger('test_log_colorizer')
    logr.addHandler(handler)
    logr.warning('HALP!')

    sio.seek(0)
    res = sio.read()
    assert res.startswith('\x1b[0m\x1b[33m')
    assert res.endswith(
        ' \x1b[1m\x1b[33m'
        'test_log_colorizer test_log:52 '
        '\x1b[0m HALP!\x1b[0m\n')
