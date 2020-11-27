import sys
from queue import PriorityQueue


class Dejkstra:

	def init_graph_vars(self, graph: list, start_vertex_idx: int):
		self.vertex_distance = []
		self.parent_vertexes_idxes = []

		for vertex in graph: 
			self.vertex_distance.append(sys.maxsize)
			self.parent_vertexes_idxes.append(None)
		self.vertex_distance[start_vertex_idx] = 0


	def dejkstra(self, graph: list, start_vertex_idx: int):
		self.init_graph_vars(graph, start_vertex_idx)

		available_vertexes_queue_idxes = PriorityQueue()
		available_vertexes_queue_idxes.put((0, start_vertex_idx))

		while not available_vertexes_queue_idxes.empty():
			parent_idx = available_vertexes_queue_idxes.get()[1]

			for child_distance_tuple in graph[parent_idx]:
				child_idx = child_distance_tuple[0]
				distance = self.vertex_distance[parent_idx] + child_distance_tuple[1]

				if self.vertex_distance[child_idx] > distance:
					self.relax_edge(child_idx, parent_idx, distance)
					available_vertexes_queue_idxes.put((distance, child_idx))

		for distance in self.vertex_distance:
			if distance == sys.maxsize:
				return None

		return self.vertex_distance


	def relax_edge(self, child_idx, parent_idx, distance):
			self.parent_vertexes_idxes[child_idx] = parent_idx
			self.vertex_distance[child_idx] = distance

