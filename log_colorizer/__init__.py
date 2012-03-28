# -*- coding: utf-8 -*-
# Copyright (C) 2011 by Florian Mounier, Kozea
# This file is part of brigit, licensed under a 3-clause BSD license.

"""
Log colorizer

"""
import os
import sys
import logging


class ColorFormatter(logging.Formatter):
    """Simple python logging colorizer formatter """

    level_colors = {
        'DEBUG': 32,
        'INFO': 34,
        'WARNING': 33,
        'ERROR': 31,
        'CRITICAL': 35
    }

    def format(self, record):
        """Format the record with colors."""
        message = logging.Formatter.format(self, record)
        return ('\x1b[0m' +
                message
                   .replace('$RESET', '\x1b[0m')
                   .replace('$BOLD', '\x1b[1m')
                   .replace('$COLOR', '\x1b[%dm' %
                            self.level_colors.get(record.levelname, 37)) +
                '\x1b[0m')


def make_colored_stream_handler(
        std=sys.stdout, level=logging.DEBUG):
    """Return a colored stream handler"""
    handler = logging.StreamHandler(std)
    handler.setLevel(level)
    if not hasattr(std, 'fileno') or os.isatty(std.fileno()):
        handler.setFormatter(
            ColorFormatter(
                '$COLOR%(asctime)s $BOLD$COLOR%(name)s'
                ' %(funcName)s:%(lineno)d $RESET %(message)s'))
    return handler
