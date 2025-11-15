from UDGraph import UDGraph
from Profiles import users

# create graph object
user_graph = UDGraph()

# add all users as vertices
for user in users:
    user_graph.addVertex(user)

# add "follows" relationships (directed edges)
# user0 = Tan Jing Ming (follows everyone)
for i in range(1, 8):
    user_graph.addEdge(users[0], users[i])

# user1 = Sofia Ahmad (follows 3 people)
user_graph.addEdge(users[1], users[0])  # follows Tan Jing Ming
user_graph.addEdge(users[1], users[4])  # follows Thanu Raj
user_graph.addEdge(users[1], users[7])  # follows David Chuah

# user2 = JY Lim (follows no one)
# (no edges added)

# user3 = Ethan Koh Yi Ming (follows 2 people)
user_graph.addEdge(users[3], users[0])  # follows Tan Jing Ming
user_graph.addEdge(users[3], users[5])  # follows Helen Lee Jia Rong

# user4 = Thanu Raj (follows 5 people)
user_graph.addEdge(users[4], users[0])  # follows Tan Jing Ming
user_graph.addEdge(users[4], users[1])  # follows Sofia Ahmad
user_graph.addEdge(users[4], users[3])  # follows Ethan Koh Yi Ming
user_graph.addEdge(users[4], users[5])  # follows Helen Lee Jia Rong
user_graph.addEdge(users[4], users[7])  # follows David Chuah

# user5 = Helen Lee Jia Rong (follows 1 person)
user_graph.addEdge(users[5], users[6])  # follows Robert Lim

# user6 = Robert Lim (follows 4 people)
user_graph.addEdge(users[6], users[0])  # follows Tan Jing Ming
user_graph.addEdge(users[6], users[1])  # follows Sofia Ahmad
user_graph.addEdge(users[6], users[2])  # follows JY Lim
user_graph.addEdge(users[6], users[4])  # follows Thanu Raj

# user7 = David Chuah (follows 2 people)
user_graph.addEdge(users[7], users[0])  # follows Tan Jing Ming
user_graph.addEdge(users[7], users[3])  # follows Ethan Koh Yi Ming

if __name__ == "__main__":
    # print each user and who they follow
    for user in users:
        outgoing = user_graph.listOutgoingAdjacentVertex(user)
        print(f"{user.name} follows:")
        if outgoing:
            for u in outgoing:
                print(f"  - {u.name}")
        else:
            print("  - No one")
        print('-' * 40)
