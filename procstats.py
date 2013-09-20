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

from datetime import datetime
from threading import Thread
import time

import psutil


class ProcStats(Thread):

    def __init__(self, pid, interval=10.0):
        Thread.__init__(self)
        self.pid = pid
        self.interval = interval
        self.stats = []

        self.proc = psutil.Process(pid)

    def run(self):
        self.is_running = True
        while self.is_running:
            stat = self.get_stat()
            self.stats.append((datetime.now(), stat))
            time.sleep(self.interval)

    def stop(self):
        self.is_running = False

    def get_stats(self):
        return self.stats

    def get_stat(self):
        p = self.proc
        name = p.name
        io = p.get_io_counters()
        io_read_count = io.read_count
        io_write_count = io.write_count
        io_read_bytes = io.read_bytes
        io_write_bytes = io.write_bytes
        cpu_percent = p.get_cpu_percent(interval=0.5)
        memory_percent = p.get_memory_percent()
        num_threads = p.get_num_threads()
        num_fds = p.get_num_fds()

        return dict(
            name=name,
            io_read_count=io_read_count,
            io_write_count=io_write_count,
            io_read_bytes=io_read_bytes,
            io_write_bytes=io_write_bytes,
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            num_threads=num_threads,
            num_fds=num_fds,
        )
