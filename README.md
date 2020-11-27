# programing_part_3 lab_3 - "Gamsrv"
### main.py

Ініціалізуємо змінні:
```python
graph, routers_idxes, clients_idxes = input_data(file_in)
dejkstra_obj = Dejkstra()
distances_to_further_client = []
```
Для кожного з претендентів на сервер обраховуємо список дистанцій до всіх вузлів графу:
```python
for router_idx in routers_idxes:
    distances_list = dejkstra_obj.dejkstra(graph, router_idx)
    # set distance to routers 0, therefore other 
    # distances are distances only to clients
    for router_idx in routers_idxes:
        distances_list[router_idx] = 0
```
шукаємо відстань до найдальшого клієнта та добавляємо у відповідний список:
```python
    distance_to_further_client= 0
	for distance in distances_list:
		if distance_to_further_client < distance:
			distance_to_further_client = distance
    distances_to_further_client.append(distance_to_further_client)
```
Знаходимо найкоротшу дистанцію:
```python
min_distance = distances_to_further_client[0]
for distance in distances_to_further_client:
	if min_distance > distance:
		min_distance = distance

return min_distance
```
### io_data.py
Ініціалізуємо змінні:

```python
def input_data(file_name):
    graph = []
    routers_idxes = set()
    with open(file_name, 'r') as file:
        vetex_num, edge_num = file.readline().split()
 
        for idx in range(int(vetex_num)):
            graph.append([])
            routers_idxes.add(idx)
```
Створюємо множину з індексами клієнтів:
```python
        clients_str = file.readline().split()
        clients_idxes = set(int(client) - 1 for client in clients_str)
```
Приводимо до кінцевої форми множину з індексами роутерів за допомогою віднімання множин:
```python
        routers_idxes.difference_update(clients_idxes)
```
Заповнюємо граф:
```python
        for line in file.readlines():
            start_node, end_node, weight = line.split()
            graph[int(start_node) - 1].append((int(end_node) - 1, int(weight)))
            graph[int(end_node) - 1].append((int(start_node) - 1, int(weight)))

    return graph, routers_idxes, clients_idxes
```
У вхідному файлі нумерація вершин починається з 1, тому, добавляючи запис в граф, віднімаємо одиницю для коректного зберігання індексів вершин.

## Installation
Copy repository with command:                                                         
`git clone https://github.com/smallpoxlviv/programing_part_3_lab_3.git`
or another method.                        
To run script, enter this command in root directory: `python main.py`      
To run unit tests, enter this command in root directory: `python test.py`
###  
[Instagam](https://www.instagram.com/logic_bomb.exe/)