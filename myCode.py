import time


class Graph:
    def __init__(self, vertices):
        self._V = vertices

    def printStepByStepSolution(self, Line, matrix):
        print(Line)
        for r in matrix:
            print(r)
            time.sleep(0.5)
        time.sleep(1)

    def printEdgesOfTheGraph(self, Line, edges):
        print(Line, edges)

    def solveTransitive(self, edges):
        Line = "Here are the Edges of the Graph Before Solving The Transitive Closure using Warshall's Method"
        print(Line, edges)
        time.sleep(1)
        Line = "Make Matrix with Dimensions of V*V and fill it by 0"
        Mat = [[0 for _ in range(self._V)] for _ in range(self._V)]
        self.printStepByStepSolution(Line, Mat)
        Line = "In the Position of each edge, Put 1 in that position"
        for i in range(len(Mat)):
            for j in range(len(Mat[i])):
                if (i + 1, j + 1) in edges:
                    Mat[i][j] = 1
        self.printStepByStepSolution(Line, Mat)
        for k in range(self._V):
            print(f"    We now should select row {k+1} and column {k+1}")
            time.sleep(1)
            for r in range(self._V):
                for c in range(self._V):
                    if Mat[r][c]:
                        print(
                            f"    Since the {r+1}th and {c+1}th element is 1, we leave it as it is"
                        )
                        time.sleep(0.5)
                    else:
                        print(
                            f"    Since the {r+1}th and {c+1}th element is 0, we have two options:"
                        )
                        time.sleep(0.5)
                        print(
                            f"    1. If the element in {k+1}th row and {c+1}th column is 1 and element in {r+1}th row {k+1}th column is 1, we change the current element to 1"
                        )
                        print(f"    2. Else keep the current element as it is")
                        time.sleep(1)
                        if Mat[k][c] and Mat[r][k]:
                            print("     Here we are going to choose the first option")
                            time.sleep(0.5)
                            Mat[r][c] = 1
                        else:
                            print("     We are going to choose the second option")
                            time.sleep(0.5)
            Line = f"   After the {k+1} trial, here is our Matrix"
            self.printStepByStepSolution(Line, Mat)
            time.sleep(1)
        Line = "Our final Edges are"
        newEdges = []
        for i in range(self._V):
            for j in range(self._V):
                if Mat[i][j] == 1:
                    newEdges.append((i + 1, j + 1))
        self.printEdgesOfTheGraph(Line, newEdges)
        time.sleep(1)


g = Graph(4)
edges = {(2, 1), (2, 3), (3, 1), (3, 4), (4, 1), (4, 3)}
g.solveTransitive(edges)
