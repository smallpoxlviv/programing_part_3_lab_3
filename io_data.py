import sys


def input_data(file_name):
    graph = []
    routers_idxes = set()

    try:
        with open(file_name, 'r') as file:
            vetex_num, edge_num = file.readline().split()
 
            for idx in range(int(vetex_num)):
                graph.append([])
                routers_idxes.add(idx)

            clients_str = file.readline().split()
            clients_idxes = set(int(client) - 1 for client in clients_str)
            routers_idxes.difference_update(clients_idxes)

            for line in file.readlines():
                start_node, end_node, weight = line.split()
                graph[int(start_node) - 1].append((int(end_node) - 1, int(weight)))
                graph[int(end_node) - 1].append((int(start_node) - 1, int(weight)))

        return graph, routers_idxes, clients_idxes
    except (FileNotFoundError):
        sys.exit(f'file "{file_name}" not found')
    except:
        sys.exit(f'check data in "{file_name}"')

def output_data(file_name, output):
    with open(file_name,'w') as file:
        file.write(str(output))
        