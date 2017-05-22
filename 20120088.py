n, m, v = input().split()
n, m, v = [int(n), int(m), int(v)]

graph = {}
for i in range(1, n+1):
    graph[i] = {}

for i in range(m):
    a, b = input().split()
    a, b = [int(a), int(b)]
    graph[b][a] = True
    graph[a][b] = True

class Queue():
    def __init__(self):
        self.__queue = []
    def enqueue(self, data):
        self.__queue.append(data)
    def dequeue(self):
        return self.__queue.pop(0)
    def __len__(self):
        return len(self.__queue)

def dfs(pos):
    result = [pos]
    checkGo[pos - 1] = 'y'
    for i in range(1, n+1):
        if i in graph[pos] and checkGo[i - 1] == 'n':
            result = result + dfs(i)
    return result

def bfs(start):
    queue = Queue()
    queue.enqueue(start)
    checkGo[start - 1] = 'y'
    result = []
    while len(queue):
        out = queue.dequeue()
        result.append(out)
        for i in range(1, n+1):
            if i in graph[out] and checkGo[i - 1] == 'n':
                queue.enqueue(i)
                checkGo[i - 1] = 'y'
    return result

checkGo = list('n' * n)
print(*dfs(v), sep = ' ')
checkGo = list('n' * n)
print(*bfs(v), sep = ' ')