#!/usr/bin/env python
#
#   Copyright (c) 2013 Corey Goldberg
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup

setup(name='procstats',
      version='0.1.0',
      description='Operating System Process Stats',
      author='Corey Goldberg',
      author_email='cgoldberg _at_ gmail.com',
      url='https://github.com/cgoldberg/procstats',
      py_modules=['procstats', ],
      install_requires=['psutil', ],
      classifiers=(
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
      )
      )
