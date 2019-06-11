#! /usr/bin/python
# -*-coding: utf-8-*-
from multiprocessing import Pool

def ExecuteWrap(executer, job):
    """
    Pool采用queue.Queue传递task，不能序列化类方法，定义一个函数作为adapter
    """
    return executer.Execute(job)

class Scheduler(object):

    def __init__(self, executer):
        self.executer = executer
        self.procNum = executer.procNum
        self.pool = Pool(self.procNum)

        self.results = []
        for i in range(executer.procNum):
            self.results.append(None)

    def Schedule(self):
        i = 0
        while not self.executer.Stop():
            if self.results[i]:
                if self.results[i].ready():
                    res = self.results[i].get()
                    self.results[i] = None
                    self.executer.Report(res)

                else:
                    i += 1
                    i %= self.procNum

            else:
                job = self.executer.Produce()
                self.results[i] = self.pool.apply_async(ExecuteWrap, (self.executer,job))
        

        self.pool.close()
        self.pool.join()

