from collections import defaultdict, deque

class FriendNetwork:
    def __init__(self):
        self.network = defaultdict(set)

    def add_friendship(self, person1, person2):
        self.network[person1].add(person2)
        self.network[person2].add(person1)

    def find_common_friends(self, person1, person2):
        friends1 = self.network.get(person1, set())
        friends2 = self.network.get(person2, set())
        return friends1.intersection(friends2)

    def nth_connection(self, start, end, n):
        if start not in self.network or end not in self.network:
            return -1
        
        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            current_person, depth = queue.popleft()
            if depth == n:
                if current_person == end:
                    return n
                continue
            
            for friend in self.network[current_person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, depth + 1))
        
        return -1

def main():
    network = FriendNetwork()
    
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Bob", "Janice")
    network.add_friendship("Alice", "Charlie")
    network.add_friendship("Charlie", "David")
    network.add_friendship("Janice", "Eve")

    common_friends = network.find_common_friends("Alice", "Bob")
    print(f"Common friends of Alice and Bob: {common_friends}")

    connection_1 = network.nth_connection("Alice", "Janice", 2)
    print(f"Connection between Alice and Janice: {connection_1}")

    connection_2 = network.nth_connection("Alice", "Bob", 1)
    print(f"Connection between Alice and Bob: {connection_2}")

if __name__ == "__main__":
    main()
