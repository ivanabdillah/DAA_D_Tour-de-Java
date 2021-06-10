import random
import sys

GRAPH = {\
            'Pacitan': {'Blitar': 174, 'Madiun': 108},
            'Magetan': {'Madiun': 28},
            'Madiun': {'Magetan': 28, 'Pacitan': 108, 'Bojonegoro': 112},
            'Bojonegoro': {'Madiun': 112, 'Lamongan': 66},
            'Lamongan': {'Bojonegoro': 66, 'Surabaya': 46},
            'Surabaya': {'Lamongan': 46, 'Sidoarjo': 26, 'Bangkalan': 43},
            'Sidoarjo': {'Surabaya': 26, 'Jombang': 90, 'Malang': 71, 'Pasuruan': 47},
            'Jombang': {'Sidoarjo': 90, 'Kediri': 35},
            'Kediri': {'Jombang': 35, 'Blitar': 98},
            'Blitar': {'Pacitan': 174, 'Kediri': 98, 'Malang': 78},
            'Malang': {'Blitar': 78, 'Sidoarjo': 71},
            'Pasuruan': {'Sidoarjo': 47, 'Probolinggo': 47},
            'Probolinggo': {'Pasuruan': 47, 'Bondowoso': 97},
            'Bondowoso': {'Probolinggo': 97, 'Jember': 35, 'Banyuwangi': 97},
            'Jember': {'Bondowoso': 35},
            'Banyuwangi': {'Bondowoso': 97},
            'Sumenep': {'Bangkalan': 139},
            'Bangkalan': {'Sumenep': 139, 'Surabaya': 43}
        }

def dfs_paths(source, destination, path=None):
    """All possible paths from source to destination using depth-first search
    source: Source city name
    destination: Destination city name
    path: Current path (Default value = None)
    yields: All possible paths from start to its destination
    """
    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(GRAPH[source].keys()) - set(path):
        yield from dfs_paths(next_node, destination, path + [next_node])

def closest(source, destination):
    """
    Cheapest path from source to destination using uniform cost search
    :param source: Source city name
    :param destination: Destination city name
    :returns: Cost and path for cheapest traversal
    """
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))
                

def main():
    print("\nList of Cities in East Java:")

    p = open("Listtown.txt", "r")
    print(p.read())
    print("\n")

    cities = open('horizoncity.txt').readlines()
    city = cities[0]
    words = city.split()
    source = random.choice(words)
    goal = random.choice(words)

    if source == goal:
        print("Generate random origin city same to destination city!")
        sys.exit(1)

    count = 0
    paths = dfs_paths(source, goal)
    cost, closest_path = closest(source, goal)

    for path in paths:
        count+=1

    print("How many ways are there from " + source + " to " + goal + " ?", end=' ')

    ans1 = int(input("\nNumber of ways = "))

    points = 0

    if ans1 == count:
        print ('Congratulations your answer is correct!', end='\n')
        points += 1

    else:
        print('Wrong Answer!', end='\n')
        print("The correct answer is ", count, "ways")

    print("\nClosest path from " + source + " to " + goal + " ?", end ='\n') 

    d = " -> ".join(closest_path)
    ans2 = input('The closest path is = ')

    if ans2 == d:
        print ('Congratulations your answer is correct!', end='\n')
        points += 1

    else:
        print('Wrong Answer!', end='\n')
        print('The correct answer is ')
        print(' -> '.join(city for city in closest_path))

    print('\nHow far is it ?')
    ans3 = int(input("distance = "))

    if ans3 == cost:
        print ('\nCongratulations your answer is correct!', end='\n')
        points += 1

    else:
        print('\nWrong Answer!', end='\n')
        print("\nThe correct answer is ", cost, "km\n")

    if points == 1:
        print("\nYour score is 50")

    elif points == 2:
        print("\nYour score is 75")

    elif points == 3:
        print("\nYour score is 100, Congratulations!")

    elif points == 0:
        print("\nDon't give up, Please try again")

    print("\nSo, from the game above, it can be concluded that the fastest possible paths that can be passed are : ")
    paths = dfs_paths(source, goal)
    hitung = 0

    for path in paths:
        print("\n")
        hitung+=1
        print(hitung, ".")
        print(' -> '.join(city for city in path))

    print("\n")
    print("The number of paths that can be taken are : ", count, "paths")
    print("The closest path is : ",( ' -> '.join(city for city in closest_path)))
    print("The distance is ",cost, "km\n")
    
if __name__ == '__main__':
    main()
