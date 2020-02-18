from collections import deque

queue = deque(["Eric", "John", "Michael"])
print('queue', queue)
queue.append("Terry")                       # Terry arrives
queue.append("Graham")                      # Graham arrives
print('after append Terry and Graham', queue)
queue.popleft()                             # The first to arrive now leaves
queue.popleft()                             # The second to arrive now leaves
print('after popleft twice', queue)         # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])       # New queue