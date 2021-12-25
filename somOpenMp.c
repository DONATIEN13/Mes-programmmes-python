#include <stdio.h>
#include <omp.h>

#define N 6


int main(int argc, char** argv)
{
	int partial_sum, total_sum, tab[] = {1, 2, 3, 4, 5, 6};

	#pragma omp parallel private(partial_sum) shared(total_sum)
	{
		partial_sum = 0;
		total_sum = 0;

		#pragma omp parallel for
		for(int i = 0; i < N; i++)
			{
				partial_sum += tab[i];
			}

		#pragma omp critical
		{
			total_sum += partial_sum;
		}
	}

	printf("Somme total est: %d\n", total_sum);
	return 0;
}
