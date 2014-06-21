#------------------------------------------------------------------------------
# Copyright (c) 2014, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
import os


__version__ = 3  # kept in sync with CPPY_VERSION


def get_include():
    return os.path.join(os.path.dirname(__file__), 'include')
