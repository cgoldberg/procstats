=============
    procstats
=============

procstats - Operating System Process Stats

--------
    Info
--------

:Home: https://github.com/cgoldberg/procstats
:License: GNU GPLv3
:Author: Copyright (c) 2011-2013 Corey Goldberg

-----------------------------
    Supported Python Versions
-----------------------------

  * Python 2.7
  * Python 3.3

----------------
    Requirements
----------------

    * psutil - https://pypi.python.org/pypi/psutil
    * tox - http://tox.testrun.org/ (used for testing only)

---------
    Tests
---------

To run the tests::

    $ python -m unittest discover

To sdist-package, install, and test against every supported Python version::

    $ tox
