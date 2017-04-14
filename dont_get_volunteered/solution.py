import math, collections, sys

def breadth_first_search(graph, src, destination): 
	visited, queue = set(), collections.deque([src])
	fl = []
	pred = []
	for i in range(len(graph)):
		fl.append(False)
		pred.append(-1)
	while queue: #while there are still unvisited nodes 
		vertex = queue.popleft() #pop a node off the queue 
		for neighbour in graph[vertex]: # for each neighbor of the vertex
			#print(neighbour)
			neighbour = int(neighbour)
			if fl[neighbour] is False:
				fl[neighbour] = True
				pred[neighbour] = vertex
			if neighbour == destination:
				return pred
			if neighbour not in visited:
				visited.add(neighbour) 
				queue.append(neighbour)

def get_coords(num):
	row = math.floor(num/8)
	col = num%8
	return (row, col)

def get_val(coords):
	val = 8*coords[0]
	val += coords[1]
	return val

# Determines if a node falls in our board of dim [8][8]
# TO BE TESTED
def is_valid(coord):
	row = coord[0]
	col = coord[1]

	if row < 0 or row > 7:
		return False
	if col < 0 or col > 7:
		return False
	return True

def construct_adjacency_list():
	# TL, UL, TR, UR, DL, BL, DR, BR
	possible_moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1, -2), (1, 2), (2, -1), (2,1)]
	# Calculate viable moves of dist 1 for all cells in the game board 1-63
	matrix = []
	valid_moves = dict()
	for j in range(64):
		curr = get_coords(j)
		valids = []
		for i in range(len(possible_moves)): # Try every possible move on each cell.
			row_adjust = possible_moves[i][0]
			col_adjust = possible_moves[i][1]
			new = (curr[0] + row_adjust, curr[1] + col_adjust)
			if is_valid(new):
				valids.append(get_val(new))
		valid_moves[j] = valids
	return valid_moves


def answer(src, dest):
	if src == dest:
		return 0
	src_coord = get_coords(src)
	dest_coord = get_coords(dest)
	adjacency_list = construct_adjacency_list() # dict with cell # : [cells 1 move away]
	pred = breadth_first_search(adjacency_list, src, dest)
	steps = 0
	index = dest
	while True:
		steps += 1
		if pred[index] == src:
			return steps
		index = pred[index]

print(answer(int(sys.argv[1]),int(sys.argv[2])))
'''
def make_matrix():
    matrix = [[10,17],[16,18,11],[8,12,17,19],[9,13,18,20],[10,14,19,21],[11,15,20,22],[12,21,23],[13,22],//
    			[2,18,25],[3,24,26,19],[0,4,16,20,25,27],[1,5,17,21,26,28],[2,6,18,22,27,29],[3,7,19,23,28,30]//
    			[1,10,26,33],[0,2,11,27,32,34],[1,3,8,12,24,28,33,35],[]



-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
'''