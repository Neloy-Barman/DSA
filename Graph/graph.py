class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):
        if node in self.adjacentList.keys():
            return
        self.numberOfNodes += 1
        self.adjacentList[node] = []
        return self

    def addEdge(self, node1, node2):
        if node1 and node2 not in self.adjacentList.keys():
            return
        if node2 in self.adjacentList[node1]:
            return 
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return self

    def showConnections(self):
        nodes = self.adjacentList.keys()

        for node in nodes:
            temp = ""
            for edge in self.adjacentList[node]:
                temp += f"{edge} "
            print(f"{node} --> {temp}")
        return self

def main():
    graph = Graph()

    graph.addVertex('0')
    graph.addVertex('1')
    graph.addVertex('2')
    graph.addVertex('3')
    graph.addVertex('4')
    graph.addVertex('5')
    graph.addVertex('6')

    graph.addEdge('3', '1')
    graph.addEdge('3', '4')
    graph.addEdge('4', '2')
    graph.addEdge('4', '5')
    graph.addEdge('1', '2')
    graph.addEdge('1', '0')
    graph.addEdge('0', '2')
    graph.addEdge('6', '5')

    graph.showConnections()


if __name__ == "__main__":
    main()