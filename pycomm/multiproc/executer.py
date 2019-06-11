#! /usr/bin/python
# -*-coding: utf-8-*-

import time
import multiprocessing
from scheduler import Scheduler

class Executer(object):
    
    def __init__(self, jobs):
        self.jobs = jobs

    @property
    def procNum(self):
        return len(self.jobs) if len(self.jobs) < 10 else 10 

    def Produce(self):
        return self.jobs.pop()

    def Execute(self, job):
        print multiprocessing.current_process().name + " " + str(job) + "\n"
        time.sleep(0.5)
        return job**2 

    def Report(self, res):
        print res

    def Stop(self):
        return len(self.jobs) == 0


def main():
    executer = Executer(list(range(1000)))
    sched = Scheduler(executer)
    sched.Schedule()

main()
    
