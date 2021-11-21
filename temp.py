# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import mpi4py
import numpy as np
import time

start = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank

if rank == 0:
    donnee = [1, 2, 3, 4]
    comm.send(donnee, dest = 1)
elif rank == 1:
    donnee = comm.recv(source = 1)
    print("processus 1, donnee est" + donnee)

end = time.time()

temps = end - start

print("temps d'execution est" + temps)
