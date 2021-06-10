import random
import sys

def terdekat(source, destination):
    """Cheapest path from source to destination using uniform cost search
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
    print("Daftar Kota di Jawa Timur : ")
    p = open("Listtown.txt", "r")
    print(p.read())
    print("\n")
    cities = open('horizoncity.txt').readlines()
    city = cities[0]
    words = city.split()
    source = random.choice(words)
    goal = random.choice(words)
    if source == goal:
        print("Generate random mengambil asal kota dan tujuan kota yang sama!")
        sys.exit(1)
    count = 0
    paths = dfs_paths(source, goal)
    cost, jalur_terdekat = terdekat(source, goal)
    for path in paths:
        count+=1
    print("Ada berapa cara dari " + source + " ke " + goal + " ?", end=' ')
    ans1 = int(input("\nJumlah cara = "))
    benar = 0
    if ans1 == count:
        print ('Selamat jawaban Anda benar!', end='\n')
        benar += 1
    else:
        print('Jawaban Anda salah!', end='\n')
        print("Jawaban yang benar adalah", count, "cara")
    print("\nJalur terdekat dari " + source + " ke " + goal + " ?", end ='\n') 
    d = " -> ".join(jalur_terdekat)
    ans2 = input('Jalur terdekat adalah = ')
    if ans2 == d:
        print ('Selamat jawaban Anda benar!', end='\n')
        benar += 1
    else:
        print('Jawaban Anda salah!', end='\n')
        print('Jawaban yang benar adalah ')
        print(' -> '.join(city for city in jalur_terdekat))
    print('\nBerapa jaraknya ?')
    ans3 = int(input("Jarak = "))
    if ans3 == cost:
        print ('\nSelamat Jawaban Anda benar!', end='\n')
        benar += 1
    else:
        print('\nJawaban Anda salah!', end='\n')
        print("\nJawaban yang benar adalah", cost, "km\n")
    if benar == 1:
        print("\nNilai anda adalah 50 ")
    elif benar == 2:
        print("\nNilai anda adalah 75 ")
    elif benar == 3:
        print("\nNilai anda adalah 100, Selamat anda benar semua!")
    elif benar == 0:
        print("\nDibaca mapnya lagi yaaa")
    print("\nJadi, dari quiz game di atas dapat disimpulkan bahwa kemungkinan jalur yang dapat dilalui adalah :")
    paths = dfs_paths(source, goal)
    hitung = 0
    for path in paths:
        print("\n")
        hitung+=1
        print(hitung, ".")
        print(' -> '.join(city for city in path))
    print("\n")
    print("Jumlah jalur yang bisa ditempuh adalah:", count, "jalur")
    print("Jalur yang terdekat adalah:",( ' -> '.join(city for city in jalur_terdekat)))
    print("Dengan jarak",cost, "km\n")
    
if __name__ == '__main__':
    main()
