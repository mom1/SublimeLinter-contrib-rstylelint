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

def _make_text_safeish(text, method='decode'):
    # The unicode decode here is because sublime converts to unicode inside
    # insert in such a way that unknown characters will cause errors, which is
    # distinctly non-ideal... and there's no way to tell what's coming out of
    # git in output. So...
    fallback_encoding = sublime.active_window().active_view().settings().get(
        'fallback_encoding').rpartition('(')[2].rpartition(')')[0]
    try:
        unitext = getattr(text, method)('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        unitext = getattr(text, method)(fallback_encoding)
    except AttributeError:
        # strongly implies we're already unicode, but just in case let's cast
        # to string
        unitext = str(text)
    return unitext

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
            project_data = sublime.active_window().project_data()
            project_folder = [x['path'] for x in project_data['folders']]
            
            match_filename = basename(match.groupdict()['filename'])
            linted_filename = basename(self.filename)

            if match_filename != linted_filename:
                print(_make_text_safeish("Ошибка в другом файле: " + match_filename))
                return None, None, None, None, None, '', None
            if len([i for i in project_folder if i in self.filename]) == 0:
                print(_make_text_safeish("Файл не в проекте: " + linted_filename))
                return None, None, None, None, None, '', None

            return match, line, col, error, warning, message, near
