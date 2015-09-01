SublimeLinter-contrib-rstylelint
================================

This linter plugin for [SublimeLinter][docs] provides an interface to [r-style][r-style]. It will be used with files that have the “RStyle” syntax.

This plugin is for Windows operating systems only becuase the [r-style][r-style] linter is Windows only.

## Installation

### SublimeLinter 3 installation

SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `rstylelint` is installed on your system. To install `rstylelint`, do the following:

#### Russian
1. checkSyntaxMac.mac - копировать в директорию видимую интерпритатором (для запуска через RSInit.exe)
2. checkSyntaxMac.cmd and RunRegRS.vbs - держать вместе и скопировать в директорию прописанную в "PATH" или указанную в настройках SublimeLine3 "paths"
3. ** IMPORTANT! ** выше перечисленные файлы и linter.py должны быть в кодировке cp1251
4. В настройках проекта
"settings":
    {
        "fallback_encoding": "Cyrillic (Windows 1251)"
    }

#### English
1. checkSyntaxMac.mac - copy the directory visible interpreter (to run through RSInit.exe)
2. checkSyntaxMac.cmd and RunRegRS.vbs - to keep together and copied to the register in the "PATH" or specified in the settings SublimeLine3 "paths"
3. ** IMPORTANT! ** Above mentioned files and linter.py must be encoded in cp1251

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `rstylelint`. Among the entries you should see `SublimeLinter-contrib-rstylelint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
[r-style]: https://github.com/mom1/SublimeRStyle