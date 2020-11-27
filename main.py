from io_data import *
from dejkstra import Dejkstra


def main(file_in):
	graph, routers_idxes, clients_idxes = input_data(file_in)
	dejkstra_obj = Dejkstra()

	distances_to_further_client = []
	for router_idx in routers_idxes:
		distances_list = dejkstra_obj.dejkstra(graph, router_idx)
		if distances_list is None:
			return None
		# set distance to routers 0, therefore other 
		# distances are distances only to clients
		for router_idx in routers_idxes:
			distances_list[router_idx] = 0

		distance_to_further_client = 0
		for distance in distances_list:
			if distance_to_further_client < distance:
				distance_to_further_client = distance
		distances_to_further_client.append(distance_to_further_client)

	min_distance = distances_to_further_client[0]
	for distance in distances_to_further_client:
		if min_distance > distance:
			min_distance = distance

	return min_distance


if __name__ == "__main__":
	file_in_1 = 'io/in/gamsrv_1.in'
	file_in_2 = 'io/in/gamsrv_2.in'
	file_in_3 = 'io/in/gamsrv_3.in'
	file_out_1 = file_in_1.replace('in', 'out')
	file_out_2 = file_in_2.replace('in', 'out')
	file_out_3 = file_in_3.replace('in', 'out')

	result_1 = main(file_in_1)
	result_2 = main(file_in_2)
	result_3 = main(file_in_3)

	print(f'result from 1 example: {result_1}')
	print(f'result from 2 example: {result_2}')
	print(f'result from 3 example: {result_3}')

	output_data(file_out_1, str(result_1))
	output_data(file_out_2, str(result_2))
	output_data(file_out_3, str(result_3))
	