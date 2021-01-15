from typing import List, Any, Union

from vertex import Vertex
from queue import Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, key):
        return self.vertices[key]

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            v1 = Vertex(f)
            self.vertices[f] = v1
        if t not in self.vertices:
            v2 = Vertex(t)
            self.vertices[t] = v2
        self.vertices[f].addNeighbor(self.vertices[t], cost)
        self.vertices[t].addNeighbor(self.vertices[f], cost)

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = set()
        for name, vertex in self.vertices.items():
            for nbr in vertex.connectedTo:
                edges.add((name, nbr.id, vertex.getWeight(nbr)))
        return list(edges)

    def bfs(self, start):
        fila = Queue()
        fila.put(start)
        visitado = [start]
        while fila.qsize() > 0:
            vert = fila.get()
            for nbr in self.vertices[vert].getConnections():
                if nbr.id not in visitado:
                    visitado.append(nbr.id)
                    fila.put(nbr.id)
        return visitado

    def dfs(self, start):
        pilha = [start]
        visit = [start]
        while pilha:
            inversa = sorted(pilha)
            pilha.pop()
            vertic = inversa.pop()
            for nbr in self.vertices[vertic].getConnections():
                print(nbr.id)
                if nbr.id not in visit:
                    pilha.append(nbr.id)
            visit.append(vertic)
        return visit

    def dijkstra(self, start, maxD=1e309):

        prev = []
        dist = []
        marcados = []  # não visitados
        analisador = start

        for vert in self.vertices.keys():
            marcados.append(vert)#coloca todos para serem visitados
            prev[vert] = None
            dist[vert] = maxD

        dist[analisador] = 0
        marcados.remove(analisador)

        while marcados:

            for vSearch in self.vertices.keys():
                if dist[vSearch] < maxD:
                    analisador = vSearch
                    marcados.pop(vSearch)

            for vizinho in self.vertices[analisador].getConnections():
                totalCost = dist[analisador] + self.vertices[vizinho].getEdges()
                if totalCost < dist[vizinho]:
                    dist[vizinho] = totalCost
                    prev[vizinho] = analisador
        print(dist)