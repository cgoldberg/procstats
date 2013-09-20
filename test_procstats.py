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

import datetime
import os
import subprocess
import time
import unittest

import psutil

from procstats import ProcStats


class ProcStatsTestCase(unittest.TestCase):

    def test_init(self):
        pid = os.getpid()
        ps = ProcStats(pid)
        self.assertIsInstance(ps.pid, int)
        self.assertGreaterEqual(ps.interval, 0.0)

    def test_create_by_pid(self):
        pid = os.getpid()
        ps = ProcStats(pid)
        self.assertIsInstance(ps.pid, int)

    def test_create_by_bad_pid(self):
        invalid_pid = 9999999
        self.assertRaises(psutil.NoSuchProcess, ProcStats, invalid_pid)

    def test_get_stat(self):
        pid = os.getpid()
        ps = ProcStats(pid)
        stat = ps.get_stat()
        self.assertIsInstance(stat['name'], str)
        self.assertGreaterEqual(stat['cpu_percent'], 0.0)
        self.assertLessEqual(stat['cpu_percent'], 100.0)
        self.assertIsInstance(stat['cpu_percent'], float)
        self.assertGreaterEqual(stat['memory_percent'], 0.0)
        self.assertLessEqual(stat['memory_percent'], 100.0)
        self.assertIsInstance(stat['memory_percent'], float)
        self.assertIsInstance(stat['io_read_count'], int)
        self.assertIsInstance(stat['io_write_count'], int)
        self.assertIsInstance(stat['io_read_bytes'], int)
        self.assertIsInstance(stat['io_write_bytes'], int)
        self.assertIsInstance(stat['num_threads'], int)
        self.assertIsInstance(stat['num_fds'], int)

    def test_run_get_stats(self):
        pid = os.getpid()
        ps = ProcStats(pid, 1.0)
        ps.start()
        time.sleep(3)
        ps.stop()
        stats = ps.get_stats()
        self.assertGreater(len(stats), 1)
        dt, stat = stats[0]
        self.assertIsInstance(dt, datetime.datetime)
        self.assertGreater(len(stat), 1)


class ProcStatsSubprocessTestCase(unittest.TestCase):

    def setUp(self):
        self.p = subprocess.Popen(['sleep', '2'],)
        self.addCleanup(self.p.kill)

    def test_with_subprocess(self):
        ps = ProcStats(self.p.pid)
        self.assertIsInstance(ps.pid, int)
        stat = ps.get_stat()
        self.assertEqual(stat['name'], 'sleep')

    def test_dead_subprocess(self):
        p = subprocess.Popen(['sleep', '0.5'],)
        ps = ProcStats(p.pid)
        time.sleep(1.0)
        self.assertRaises(psutil.AccessDenied, ps.get_stat)


if __name__ == '__main__':
    unittest.main(verbosity=2)
