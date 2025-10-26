import os
import psutil


def find_procs_by_name(name):
    ls = []
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls


def setPriority(name):
    for el in find_procs_by_name(name):
        proc = psutil.Process(el.pid)
        if name == 'Discord.exe':
            proc.nice(psutil.IDLE_PRIORITY_CLASS)
        elif name == 'GeometryDash.exe':
            proc.nice(psutil.REALTIME_PRIORITY_CLASS)


for process in ['GeometryDash.exe', 'Discord.exe']:
    print(setPriority(process))


































































