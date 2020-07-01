#! /usr/bin/env python3
import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("Debug :  usage{}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("Cpu is overloaded")
else:
    print("Everything is ok")