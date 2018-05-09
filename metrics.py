#!/usr/bin/env python3

import os
import sys
import psutil
import time
import datetime
# import collections

if 'PROCFS_PATH' in os.environ:
    psutil.PROCFS_PATH = os.environ.get("PROCFS_PATH")


def print_given_stats(stats, **kwargs):
    end = kwargs.get('end', None)
    named = kwargs.get('named', None)
    if end is None:
        if named or named is None:
            for stat in stats._fields:
                print('%-20s %-20s' % (stat, getattr(stats, stat)))
        else:
            for stat in stats._fields:
                print('%-25s' % getattr(stats, stat))
    else:
        if named or named is None:
            for stat in stats._fields:
                print('%-20s %-20s' % (stat, getattr(stats, stat)), end=end)
        else:
            for stat in stats._fields:
                print('%-25s' % getattr(stats, stat), end=end)
        print()


def print_in_mb_gb(stats):
    print('Usage in: %13s %12s %9s' % ('bytes', 'MB', 'GB'))
    for stat in stats._fields:
        size_in_mb = getattr(stats, stat) / 1024 / 1024
        size_in_gb = size_in_mb/1024
        if stat is not 'percent':
            print('%-15s %-15s %-10.2f %-10.2f' % (stat, getattr(stats, stat), size_in_mb, size_in_gb))
    print('Usage in percent: %-20s' % (getattr(stats, 'percent')))


def print_memory_stats():
    mem_stats = psutil.virtual_memory()
    print('\nMemory usage:')
    print_in_mb_gb(mem_stats)
    mem_stats = psutil.swap_memory()
    print('\nSwap usage:')
    print_in_mb_gb(mem_stats)


def print_cpu_stats():
    psutil.cpu_percent(interval=None)
    psutil.cpu_times_percent(interval=None)
    print('\nCPU usage in percents:')
    print_given_stats(psutil.cpu_times_percent(interval=0.5))  #Interval 0.5 gives more reliable cpu usage percents than intervals less than 0.5
    print('\nCPU times in seconds:')
    print(print_given_stats(psutil.cpu_times()))
    # print(psutil.cpu_count())
    # print(psutil.cpu_freq())


def print_disk_stats():
    print("\nDisk partitions:")
    disk_partitions = psutil.disk_partitions()
    for stat in disk_partitions[0]._fields:
        print('%-25s' % stat, end='    ')
    print()
    for partition in disk_partitions:
        print_given_stats(partition, named=False, end='    ')
    for partition in disk_partitions:
        mountpoint = getattr(partition, 'mountpoint')
        print("\nUsage of partition: %s" % mountpoint)
        print_in_mb_gb(psutil.disk_usage(mountpoint))
    print("\nI/O statistics:")
    print_given_stats(psutil.disk_io_counters())


def cpu_usage_time_since_boot():
    total_cpu_time_since_boot = 0
    stats = psutil.cpu_times()
    for stat in stats._fields:
        total_cpu_time_since_boot += getattr(stats, stat)
    total_cpu_idle_time_since_boot = getattr(stats, 'idle') + getattr(stats, 'iowait')
    total_cpu_usage_time_since_boot = total_cpu_time_since_boot - total_cpu_idle_time_since_boot
    return total_cpu_usage_time_since_boot


def proc_cpu_time(pid):
    proc_times = 0
    proc = psutil.Process(pid)
    proc_cpu_times = proc.cpu_times()
    for stat in proc_cpu_times._fields:
        if stat not in ['idle', 'iowait']:
            proc_times += getattr(proc_cpu_times, stat)
    return proc_times


def proc_cpu_percent(pid):
    previous_cpu_usage_time_since_boot = cpu_usage_time_since_boot()
    previous_proc_times = proc_cpu_time(pid)

    time.sleep(2)

    current_cpu_usage_time_since_boot = cpu_usage_time_since_boot()
    current_proc_times = proc_cpu_time(pid)

    dif_cpu_usage_time = current_cpu_usage_time_since_boot - previous_cpu_usage_time_since_boot
    dif_proc_times = current_proc_times - previous_proc_times
    proc_cpu_time_percent = 100 * dif_proc_times / dif_cpu_usage_time

    # print("\ndif_cpu_usage_time", dif_cpu_usage_time)
    # print("\ndif_proc_times", dif_proc_times)
    # print("\nproc_cpu_percent",  proc_cpu_percent)
    return proc_cpu_time_percent


def print_processes():
    print("\n%-10s %-25s %-40s %-10s %-15s %-25s %-8s %-8s %-15s %-15s %-15s %-15s"
          % ('pid', 'user', 'process', 'parent', 'status', 'started', 'CPU %', 'RAM %', 'read bytes', 'written bytes', 'read MB', 'written MB'))
    for proc in psutil.process_iter(
            attrs=['pid', 'name', 'username', 'ppid', 'status', 'create_time', 'memory_percent']):
        proc.cpu_percent(interval=None)
        with proc.oneshot():
            proc.cpu_percent(interval=None)
            started = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%d-%m-%Y %H:%M:%S")
            pid = proc.info['pid']
            io_file = psutil.PROCFS_PATH + "/" + str(pid) + "/io"
            if not os.access(io_file, os.R_OK):
                print("%-10s %-25s %-40s %-10s %-15s %-25s %-8.2f %-8.2f %-15s %-15s %-15s %-15s" % (
                    proc.pid, proc.username(), proc.name(), proc.ppid(), proc.status(), started,
                    proc.cpu_percent(interval=0.1), proc.memory_percent(), 'n/a', 'n/a', 'n/a', 'n/a'))
                # total_mem_usage_percent += proc.memory_percent()
            else:
                try:
                    io_count = proc.io_counters()
                    read_bytes = getattr(io_count, 'read_bytes')
                    write_bytes = getattr(io_count, 'write_bytes')
                    print("%-10s %-25s %-40s %-10s %-15s %-25s %-8.2f %-8.2f %-15s %-15s %-15.2f %-15.2f" % (
                        proc.pid, proc.username(), proc.name(), proc.ppid(), proc.status(), started,
                        proc.cpu_percent(interval=0.1), proc.memory_percent(), read_bytes, write_bytes, read_bytes/1024/1024, write_bytes/1024/1024))
                    # total_mem_usage_percent += proc.memory_percent()
                except psutil._exceptions.AccessDenied:
                    print("%-10s %-25s %-40s %-10s %-15s %-25s %-8.2f %-8.2f %-15s %-15s %-15s %-15s" % (
                        proc.pid, proc.username(), proc.name(), proc.ppid(), proc.status(), started,
                        proc.cpu_percent(interval=0.1), proc.memory_percent(), 'n/a', 'n/a', 'n/a', 'n/a'))
    #             total_mem_usage_percent += proc.memory_percent()
    # print(total_mem_usage_percent)


def print_program_info():
    print("Environment variables: ", psutil.Process().environ())
    print("Memory usage by current script: ", psutil.Process().memory_percent(), "%")
    print("CPU usage by current script: ", psutil.Process().cpu_percent(), "%")
    print("Current folder: ", psutil.Process().cwd())
    print("Current user: ", psutil.Process().username())


def application():
    stat_args = [('cpu', print_cpu_stats),
                 ('mem', print_memory_stats),
                 ('disk', print_disk_stats),
                 ('ps', print_processes),
                 ('self', print_program_info)
                ]

    args = ''
    valid_args_count = 0

    for program_arg in sys.argv:
        for arg, func in stat_args:
            if program_arg == arg:
                valid_args_count += 1
                func()

    if valid_args_count == 0:
        for index in range(1, len(sys.argv)):
            args = args + sys.argv[index] + ' '
        print ("Wrong arguments: ", args)
        print('''Argument usage: 
                 Valid arguments are: cpu, mem, disk, ps, self.
                 Use can use multiple arguments separated by space char.
                 Example: metrics.py cpu mem''')


if __name__ == '__main__':
    application()


# def count_cpu_times():
#     cpu_times_user_total = 0
#     cpu_times_system_total = 0
#     processes_cpu_time = {}
#     Cpu_times_per_pid = collections.namedtuple('Cpu_times_per_pid', 'pid cpu_times_user cpu_times_system')
#     Total_cpu_time = collections.namedtuple('Total_cpu_time', 'cpu_times_user_total cpu_times_system_total')
#     for proc in psutil.process_iter(attrs=['pid', 'cpu_times', 'memory_full_info']):
#         cpu_times_user_total += getattr(proc.info['cpu_times'], 'user')
#         cpu_times_system_total += getattr(proc.info['cpu_times'], 'system')
#         cpu_times_user = getattr(proc.info['cpu_times'], 'user')
#         cpu_times_system = getattr(proc.info['cpu_times'], 'system')
#         processes_cpu_time[proc.info['pid']] = Cpu_times_per_pid(proc.info['pid'], cpu_times_user, cpu_times_system)
#     total_cpu_time = Total_cpu_time(cpu_times_user_total, cpu_times_system_total)
#     return total_cpu_time, processes_cpu_time
