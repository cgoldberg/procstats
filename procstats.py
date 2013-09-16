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

import psutil


class ProcStats:

    def __init__(self, name_or_pid, interval=10):
        self.name_or_pid = name_or_pid
        try:
            self.proc = psutil.Process(name_or_pid)
            self.pid = name_or_pid
        except TypeError:
            pid = self.lookup_pid(name_or_pid)
            self.proc = psutil.Process(pid)
            self.pid = pid

    def start(self):
        pass

    def stop(self):
        pass

    def lookup_pid(self, name):
        pid = None
        procs = [p for p in psutil.process_iter() if p.name == name]
        if not procs:
            raise psutil.NoSuchProcess('Can not find pid for: %r' % name)
        elif len(procs) > 1:
            raise Exception('Can not find unique process for: %r' % name)
        else:
            pid = procs[0].pid
        return pid

    def get_stats(self):
        p = self.proc
        io = self.proc.get_io_counters()
        return dict(
            name=p.name,
            cpu_percent=p.get_cpu_percent(interval=0.5),
            memory_percent=p.get_memory_percent(),
            io_read_count=io.read_count,
            io_write_count=io.write_count,
            io_read_bytes=io.read_bytes,
            io_write_bytes=io.write_bytes,
            num_threads=p.get_num_threads(),
            num_fds=p.get_num_fds(),
        )
