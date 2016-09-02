def initial_position():
	return 4

def primitive(pos):
	if pos == 0:
		return "LOSE"
	return "UNDETERMINED"

def gen_moves(pos):
	return [-1, -2][:pos]

def do_move(pos, move):
	return pos + move

def solve():
	def get_next_moves(pos):
		moves = gen_moves(pos)
		return [do_move(pos, move) for move in moves]

	solution = {}
	curr = initial_position()
	queue = [curr]
	queue = get_next_moves(curr) + queue

	def get_solution_from_children(position):
		children = get_next_moves(position)
		if all(child in solution.keys() for child in children):
			if any(solution[child] == "LOSE" for child in children):
				return "WIN"
			return "LOSE"
		return "UNDETERMINED"

	while queue:
		curr = queue.pop(0)
		if not (curr in solution.keys()):
			prim = primitive(curr)
			children_sol = get_solution_from_children(curr)
			if prim != "UNDETERMINED":
				solution[curr] = prim
			elif children_sol != "UNDETERMINED":
				solution[curr] = children_sol
			else:
				queue = get_next_moves(curr) + [curr] + queue
	return solution

print solve()