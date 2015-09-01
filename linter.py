#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by MOM
# Copyright (c) 2015 MOM
#
# License: MIT
#

"""This module exports the Rstylelint plugin class."""
import re
from SublimeLinter.lint import Linter, util



class Rstylelint(Linter):

    """Provides an interface to rstylelint."""
    syntax = 'r-style'
    cmd = ('checkSyntaxMac.cmd', '@')
    regex = (r'(?ix)(\.mac)\((?P<line>\d+),(?P<col>\d+)\):\s*\w*\s*\d*\:\s*(?P<message>.+[^\(Code]\n)*')
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    re_flags = re.IGNORECASE
    error_stream = util.STREAM_STDOUT
    

