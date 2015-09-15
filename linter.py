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
import sublime
from os.path import basename
from SublimeLinter.lint import Linter, util


class Rstylelint(Linter):

    """Provides an interface to rstylelint."""
    syntax = 'r-style'
    cmd = ('checkSyntaxMac.cmd', '@')
    regex = (r'(?ix)(?P<filename>.+\.mac)\((?P<line>\d+),(?P<col>\d+)\):\s*\w*\s*\d*\:\s*(?P<message>.+[^\(Code]\n)*')
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    re_flags = re.IGNORECASE
    error_stream = util.STREAM_STDOUT

    def split_match(self, match):
            """Override to ignore errors reported in imported files."""
            match, line, col, error, warning, message, near = (
                super().split_match(match)
            )

            folders = sublime.expand_variables("$folder", sublime.active_window().extract_variables())

            match_filename = basename(match.groupdict()['filename'])
            linted_filename = basename(self.filename)
            print(folders not in self.filename, match_filename != linted_filename, self.filename)

            if match_filename != linted_filename or folders not in self.filename:
                return None, None, None, None, None, '', None

            return match, line, col, error, warning, message, near
