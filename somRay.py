import ray



@ray.remote
def somme(tab):
	som = 0
	for i in range(len(tab)):
		som += tab[i]

	return som

tab = [1, 2, 3, 4, 5, 6]

result = somme.remote(tab)
results = ray.get(result)
print(results)