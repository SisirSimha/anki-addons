# -*- mode: python ; coding: utf-8 -*-
# Copyright © 2012 Roland Sieker
# This file: License: GNU GPL, version 3 or later;
# http://www.gnu.org/copyleft/gpl.html
#

"""Change the names of files to more readable versions.

Go through the collection and detect files that alook like MD5
hashes used by Anki <1.2, look at the note for a better name and
rename the files, changing the notes as well.

"""

import dehashilator
from aqt import mw
from aqt.qt import *

from dehashilator import __version__

dhma = QAction(mw)
dhma.setText("Dehashilate media")
mw.form.menuTools.addAction(dhma)
mw.connect(dhma, SIGNAL("triggered()"), dehashilator.test_and_dehashilate)
