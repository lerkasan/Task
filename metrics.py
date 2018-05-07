#!/usr/bin/env python
import sys
import psutil


def print_memory_stats():
    print(psutil.virtual_memory())
    print(psutil.swap_memory())


def print_cpu_stats():
    print(psutil.cpu_percent())
    print(psutil.cpu_count())
    print(psutil.cpu_freq(percpu=True))


def print_disk_stats():
    print(psutil.disk_partitions())
    print(psutil.disk_usage("/"))
    print(psutil.disk_io_counters())


def print_processes():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        print(proc.info)


def print_program_info():
    print(psutil.Process().environ())
    print(psutil.Process().memory_percent())
    print(psutil.Process().cwd())
    print(psutil.Process().username())


def application():
    stat_args = [('cpu', print_cpu_stats),
                 ('mem', print_memory_stats),
                 ('disk', print_disk_stats),
                 ('ps', print_processes),
                 ('self', print_program_info)
                ]

    valid_args_count = 0

    for program_arg in sys.argv:
        for arg, func in stat_args:
            if program_arg == arg:
                valid_args_count += 1
                func()

    if valid_args_count == 0:
        print ("Wrong arguments: ", program_arg)
        print('''Argument usage: 
                 Valid arguments are: cpu, mem, disk, ps, self.
                 Use can use multiple arguments separated by space char.
                 Example: metrics.py cpu mem''')
    # return print_program_info()


if __name__ == '__main__':
    application()
