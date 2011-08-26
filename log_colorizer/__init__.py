# -*- coding: utf-8 -*-
# This file is a compilation of tricks found on the internet
"""
Log colorizer

"""
import sys
import logging

from logging import StreamHandler

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
COLORS = {
    'WARNING': YELLOW,
    'INFO': GREEN,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED,
    'RED': RED,
    'GREEN': GREEN,
    'YELLOW': YELLOW,
    'BLUE': BLUE,
    'MAGENTA': MAGENTA,
    'CYAN': CYAN,
    'WHITE': WHITE}
RESET_SEQ = '\033[0m'
COLOR_SEQ = '\033[%dm'
BOLD_SEQ = '\033[1m'


class ColorFormatter(logging.Formatter):
    """Logging formatter adding console colors to the output.
    """
    def format(self, record):
        """Format the record with colors."""
        color = COLOR_SEQ % (30 + COLORS[record.levelname])
        message = logging.Formatter.format(self, record)
        message = message.replace('$RESET', RESET_SEQ)\
            .replace('$BOLD', BOLD_SEQ)\
            .replace('$COLOR', color)
        for color, value in COLORS.items():
            message = message.replace('$' + color, COLOR_SEQ % (value + 30))\
                .replace('$BG' + color, COLOR_SEQ % (value + 40))\
                .replace('$BG-' + color, COLOR_SEQ % (value + 40))
        return message + RESET_SEQ


def make_colored_stream_handler(std=sys.stdout, level=logging.DEBUG):
    """Return a colored stream handler"""
    handler = StreamHandler(std)
    handler.setLevel(level)
    handler.setFormatter(
        ColorFormatter(
            '$RESET$COLOR%(asctime)s $BOLD$COLOR%(name)s %(funcName)s:%(lineno)d $RESET %(message)s'))
    return handler
