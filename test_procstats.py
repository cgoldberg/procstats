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

import os
import subprocess
import time
import unittest

from procstats import ProcStats


class ProcStatsTestCase(unittest.TestCase):

    def test_create_by_pid(self):
        pid = os.getpid()
        ps = ProcStats(pid)
        self.assertIsInstance(ps.pid, int)

    def test_create_by_bad_pid(self):
        invalid_pid = 9999999
        self.assertRaises(Exception, ProcStats, invalid_pid)

    def test_create_by_name(self):
        name = 'init'
        ps = ProcStats(name)
        self.assertIsInstance(ps.pid, int)

    def test_create_by_bad_name(self):
        invalid_name = 'not_a_process'
        self.assertRaises(Exception, ProcStats, invalid_name)

    def test_get_proc_stats(self):
        pid = os.getpid()
        ps = ProcStats(pid)
        stats = ps.get_stats()
        self.assertIsInstance(stats['name'], str)
        self.assertGreaterEqual(stats['cpu_percent'], 0.0)
        self.assertLessEqual(stats['cpu_percent'], 100.0)
        self.assertIsInstance(stats['cpu_percent'], float)
        self.assertGreaterEqual(stats['memory_percent'], 0.0)
        self.assertLessEqual(stats['memory_percent'], 100.0)
        self.assertIsInstance(stats['memory_percent'], float)
        self.assertIsInstance(stats['io_read_count'], int)
        self.assertIsInstance(stats['io_write_count'], int)
        self.assertIsInstance(stats['io_read_bytes'], int)
        self.assertIsInstance(stats['io_write_bytes'], int)
        self.assertIsInstance(stats['num_threads'], int)
        self.assertIsInstance(stats['num_fds'], int)


class ProcStatsRunningSubprocessTestCase(unittest.TestCase):

    def setUp(self):
        self.p = subprocess.Popen(['sleep', '2'],)
        self.addCleanup(self.p.kill)

    def test_with_subprocess(self):
        ps = ProcStats(self.p.pid)
        self.assertIsInstance(ps.pid, int)
        stats = ps.get_stats()
        self.assertEqual(stats['name'], 'sleep')


class ProcStatsDeadSubprocessTestCase(unittest.TestCase):

    def test_dead_subprocess(self):
        p = subprocess.Popen(['sleep', '0.5'],)
        ps = ProcStats(p.pid)
        time.sleep(1.0)
        self.assertRaises(Exception, ps.get_stats)


if __name__ == '__main__':
    unittest.main(verbosity=2)
