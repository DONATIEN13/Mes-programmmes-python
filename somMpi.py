#Dounia DOnatien

#programme parallelisé en pyhton qui fait la recherche du plus grang element dans une liste

# le temps d'execution est 9.96e-05 s


from mpi4py import MPI
import numpy as np
import time


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

start = time.time()
print("nombre de processus trouvé: ", nprocs)

if rank == 0:

	data = [1, 2, 3, 4, 5, 6]

	ave, res = divmod(len(data), nprocs)

	counts = [ave + 1 if p < res else ave for p in range(nprocs)]

	starts = [sum(counts[:p]) for p in range(nprocs)]

	ends = [sum(counts[:p+1]) for p in range(nprocs)]

	data = [data[starts[p]:ends[p]] for p in range(nprocs)]

else:

	data = None

data = comm.scatter(data, root=0)



print('Process {} broadcast data:'.format(rank), data)

som = 0
for i in range(len(data)):
	som += data[i]

result = comm.reduce(som, root=0)

end = time.time()


if(rank == 0):
    print("Le temps d'execution est:", end - start)

    print("La somme est:", result)

