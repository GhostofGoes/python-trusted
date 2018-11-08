"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m trusted` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``trusted.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``trusted.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse

from trusted import __version__


# TODO: describe what the package does
description = """

By default, PYTHONPATH is searched for the specified package. If a directory is 
specified using --dir, then it is searched instead of PYTHONPATH. If you're not 
sure where a package is, use the find or locate commands to narrow down likely 
directories, then use --search-dirs to have trusted attempt to find packages in 
those directories.
"""

parser = argparse.ArgumentParser(description=description, prog='trusted',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
# TODO: add ability to parse a single py file or code passed to stdin
parser.add_argument('package', metavar='PACKAGE', type=str, required=True,
                    help="Name of the Python package to verify")
parser.add_argument('--version', action='version',
                    version='trusted %s' % __version__)

search_dir_group = parser.add_mutually_exclusive_group(required=False)
search_dir_group.add_argument('-d', '--dir', type=str,
                              help="Path to directory containing the package")
search_dir_group.add_argument('--search-dirs', nargs='+', type=list,
                              help="Directories to search for the package "
                                   "in addition to PYTHONPATH")


def main(args=None):
    args = parser.parse_args(args=args)
    print(args.names)
