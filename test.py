import unittest
from main import *


class TestDejkstra(unittest.TestCase):

	def setUp(self):
		self.dejkstra_obj = Dejkstra()
		self.graph = [
						[ (2, 10) ],
						[ (2, 40), (3, 100) ],
						[ (0, 10), (3, 80), (1, 40) ],
						[ (2, 80), (4, 50), (1, 100) ],
						[ (3, 50), (5, 20) ],
						[ (4, 20) ]
					]

	def test_init_graph_vars(self):
		sys_maxsize = sys.maxsize
		self.dejkstra_obj.init_graph_vars(self.graph, 0)
		self.assertEqual(self.dejkstra_obj.vertex_distance, 
							[0, sys_maxsize, sys_maxsize, sys_maxsize, sys_maxsize, sys_maxsize])
		self.assertEqual(self.dejkstra_obj.parent_vertexes_idxes, [None, None, None, None, None, None])
	
	def test_relax_edge(self):
		sys_maxsize = sys.maxsize
		self.dejkstra_obj.vertex_distance = [0, sys_maxsize, sys_maxsize, sys_maxsize, sys_maxsize, sys_maxsize]
		self.dejkstra_obj.parent_vertexes_idxes = [None, None, None, None, None, None]
		self.dejkstra_obj.relax_edge(3, 4, 50)
		self.assertEqual(self.dejkstra_obj.vertex_distance, [0, sys_maxsize, sys_maxsize, 50, sys_maxsize, sys_maxsize])
		self.assertEqual(self.dejkstra_obj.parent_vertexes_idxes, [None, None, None, 4, None, None])
			
	def test_dejkstra(self):
		vertex_distance = self.dejkstra_obj.dejkstra(self.graph, 2) 
		self.assertEqual(vertex_distance, [10, 40, 0, 80, 130, 150])	
		vertex_distance = self.dejkstra_obj.dejkstra(self.graph, 3) 
		self.assertEqual(vertex_distance, [90, 100, 80, 0, 50, 70])	
		vertex_distance = self.dejkstra_obj.dejkstra(self.graph, 4) 
		self.assertEqual(vertex_distance, [140, 150, 130, 50, 0, 20])	

	def test_input_data(self):
		graph, routers_idxes, clients_idxes = input_data('io/test/test_in.in')
		self.assertEqual(clients_idxes, set([0, 1, 5]))
		self.assertEqual(routers_idxes, set([2, 3, 4]))
		self.assertEqual(graph, self.graph)

	def test_output_data(self):
		result = 15
		file_path = 'io/test/test_out.out'
		output_data(file_path, result)
		with open(file_path, 'r') as file:
			assert_result = int(file.readline())
		self.assertEqual(assert_result, result)

	def test_main(self):
		file_in = 'io/in/gamsrv_1.in'
		result = main(file_in)
		self.assertEqual(result, 100)
		file_in = 'io/in/gamsrv_2.in'
		result = main(file_in)
		self.assertEqual(result, 10)
		file_in = 'io/in/gamsrv_3.in'
		result = main(file_in)
		self.assertEqual(result, 1000000000)
		file_in = 'io/test/test_main_1.in'
		result = main(file_in)
		self.assertEqual(result, 40)
		file_in = 'io/test/test_main_2.in'
		result = main(file_in)
		self.assertEqual(result, 20)
		file_in = 'io/test/test_main_3.in'
		result = main(file_in)
		self.assertEqual(result, 30)

if __name__ == "__main__":
	unittest.main()