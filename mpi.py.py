#!/usr/bin/env python

# coding: utf-8



 from mpi4py import MPI


 def main():
    
   comm = MPI.COMM_WORLD
    
   rank = comm.Get_rank
    
   size = comm.Get_size
    
   print("Hello from" + str(rank) + "in" + str(size))
    
 
if __name__ == "__main__":
    
   
   main()


