import turtle
import random
import math


class Vertex:
  def __init__(self, number, pos_x, pos_y):
    self.number = number
    self.pos_x = pos_x
    self.pos_y = pos_y


def main():
  seed = 4416
  n3 = 1
  n4 = 6
  N = 11

  directed_graph_matrix = generateMatrix(n3, n4, N, seed)
  undirected_graph_matrix = doUndir(directed_graph_matrix)
  position = createPositions(undirected_graph_matrix)
  degree_of_vertex = getDegreeOfVertex(undirected_graph_matrix)

  checkForUniformity(degree_of_vertex)
  findFinalVertices(degree_of_vertex)
  findIsolatedVertices(degree_of_vertex)

  drawVertices(position)
  drawLines(position, undirected_graph_matrix)
  drawCurvedLines(position, undirected_graph_matrix)
  drawCircles(position, undirected_graph_matrix)


def generateMatrix(n3, n4, N, seed):
  random.seed(seed)
  adj_matrix = [[random.random() * 2.0 for _ in range(N)] for _ in range(N)]
  k = 1.0 - n3 * 0.01 - n4 * 0.01 - 0.3

  for i in range(N):
    for j in range(N):
      adj_matrix[i][j] *= k
      adj_matrix[i][j] = 0 if adj_matrix[i][j] < 1.0 else 1

  return adj_matrix


def doUndir(adj_matrix):
  n = len(adj_matrix)
  undirected_adj_matrix = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if adj_matrix[i][j] == 1:
        undirected_adj_matrix[i][j] = 1
        undirected_adj_matrix[j][i] = 1

  print("\nМатриця суміжності ненапрямленого графа:")
  for row in undirected_adj_matrix:
    print(row)

  return undirected_adj_matrix


def createPositions(undirected_graph_matrix):
  n = len(undirected_graph_matrix)
  vertices = []
  center_x = 0
  center_y = 0
  radius = 300

  for i in range(1, n):
    angle = i * (2 * math.pi / (n - 1))
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertices.append(Vertex(i, x, y))

  central_vertex = Vertex(n, center_x, center_y)
  vertices.append(central_vertex)

  return vertices


def drawVertices(vertices):
  turtle.speed(0)
  turtle.penup()
  radius = 20

  for vertex in vertices:
    x, y = vertex.pos_x, vertex.pos_y
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(vertex.number, align="center")


def drawLines(vertices, undirected_graph_matrix):
  turtle.speed(0)
  turtle.penup()
  n = len(vertices)
  radius = 20

  for i in range(n):
    for j in range(i + 1, n):
      if i != j and undirected_graph_matrix[i][j] == 1 and abs(vertices[i].number - vertices[j].number) != 5:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y

        angle = math.atan2(y2 - y1, x2 - x1)
        x1 += math.cos(angle) * radius
        y1 += math.sin(angle) * radius
        x2 -= math.cos(angle) * radius
        y2 -= math.sin(angle) * radius

        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)


def drawCurvedLines(vertices, undirected_graph_matrix):
  turtle.speed(0)
  turtle.penup()
  n = len(vertices)
  radius = 20

  for i in range(n):
    for j in range(i + 1, n):
      if i != j and undirected_graph_matrix[i][j] == 1 and abs(vertices[i].number - vertices[j].number) == 5:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y

        angle = math.atan2(y2 - y1, x2 - x1)
        x1 += math.cos(angle) * radius
        y1 += math.sin(angle) * radius
        x2 -= math.cos(angle) * radius
        y2 -= math.sin(angle) * radius

        turtle.penup()
        turtle.goto(x1, y1)
        turtle.setheading(math.degrees(angle))
        turtle.pendown()

        distance = turtle.distance(x2, y2)
        degrees = math.pi * 2
        b = distance / 2 / math.cos(math.radians(degrees))

        turtle.right(degrees)
        turtle.forward(b)
        turtle.setheading(turtle.towards(x2, y2))
        turtle.goto(x2, y2)
        turtle.penup()


def drawCircles(vertices, undirected_graph_matrix):
  turtle.speed(0)
  turtle.penup()
  n = len(vertices)
  radius = 10

  for i in range(n):
    if undirected_graph_matrix[i][i] == 1:
      x, y = vertices[i].pos_x, vertices[i].pos_y
      turtle.goto(x + math.pi / 2.8 * radius, y + math.pi / 2 * radius)
      turtle.pendown()
      turtle.circle(radius)
      turtle.penup()

  turtle.hideturtle()
  turtle.done()


def getDegreeOfVertex(adjacency_matrix):
  num_vertices = len(adjacency_matrix)
  edges = {}

  for i in range(1, num_vertices + 1):
    edges[i] = sum(adjacency_matrix[i - 1])

  print("Степені вершин:", edges)
  return edges


def checkForUniformity(degree_of_vertex):
  edges_counts = list(degree_of_vertex.values())

  if len(set(edges_counts)) == 1:
    print("Граф однорідний. Степінь однорідності:", edges_counts[0])
  else:
    print("Граф не є однорідним")


def findFinalVertices(degree_of_vertex):
  vertices_with_one_edge = [v for v, deg in degree_of_vertex.items() if deg == 1]

  if vertices_with_one_edge:
    print("Висячі вершини:", vertices_with_one_edge)
  else:
    print("Немає висячих вершин")


def findIsolatedVertices(degree_of_vertex):
  vertices_without_edges = [v for v, deg in degree_of_vertex.items() if deg == 0]

  if vertices_without_edges:
    print("Ізольовані вершини:", vertices_without_edges)
  else:
    print("Немає ізольованих вершин")


main()
