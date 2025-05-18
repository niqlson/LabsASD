import turtle
import random
import math
import time


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
  position = createPositions(directed_graph_matrix)
  countOutgoingEdges(directed_graph_matrix)
  countIncomingEdges(directed_graph_matrix)
  findPathsOfLengthTwo(directed_graph_matrix)
  findPathsOfLengthThree(directed_graph_matrix)
  reachability_matrix = generateReachabilityMatrix(directed_graph_matrix)
  strong_connectivity_matrix = generateStrongConnectivityMatrix(reachability_matrix)
  components_of_strong_connectivity = getComponentsOfStrongConnectivity(strong_connectivity_matrix)
  condensation_matrix = generateAdjacencyMatrixOfCondensationGraph(directed_graph_matrix, components_of_strong_connectivity)
  positions_of_condensation_graph = createPositions(condensation_matrix)
  drawVertices(position)
  drawArrows1(position, directed_graph_matrix)
  drawArrows2(position, directed_graph_matrix)
  drawCurvedArrows1(position, directed_graph_matrix)
  drawCurvedArrows2(position, directed_graph_matrix)
  drawCirclesWithArrows(position, directed_graph_matrix)
  turtle.hideturtle()
  time.sleep(5)
  turtle.reset()
  drawVertices(positions_of_condensation_graph)
  drawArrows2(positions_of_condensation_graph, condensation_matrix)
  turtle.hideturtle()
  turtle.done()


def generateMatrix(n3, n4, N, seed):
  random.seed(seed)
  adj_matrix = [[random.random() * 2.0 for _ in range(N)] for _ in range(N)]
  k = 1.0 - n3 * 0.005 - n4 * 0.005 - 0.27
  for i in range(N):
    for j in range(N):
      adj_matrix[i][j] *= k
      adj_matrix[i][j] = 0 if adj_matrix[i][j] < 1.0 else 1
  print("Матриця суміжності напрямленого графа:")
  for row in adj_matrix:
    print(row)
  return adj_matrix
  

def createPositions(matrix):
  n = len(matrix)
  vertices = []
  center_x = 0
  center_y = 0
  radius = 300

  for i in range(1, n):
    angle = i * (2 * math.pi / (n-1))
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertex = Vertex(i, x, y)
    vertices.append(vertex)

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


def drawArrows1(vertices, directed_graph_matrix):
  turtle.speed(0)
  turtle.penup()

  n = len(vertices)
  radius = 20
  arrow_size = 10

  for i in range(n):
    for j in range(i + 1, n):
      if i != j and abs(vertices[i].number - vertices[j].number) != 5 and directed_graph_matrix[i][j] == 1:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y

        x1 += math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y1 += math.sin(math.atan2(y2 - y1, x2 - x1)) * radius
        x2 -= math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y2 -= math.sin(math.atan2(y2 - y1, x2 - x1)) * radius

        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))

        turtle.goto(x1, y1)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.goto(x2, y2)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.pendown()
        turtle.right(150)
        turtle.forward(arrow_size)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.left(300)
        turtle.pendown()
        turtle.forward(arrow_size)
        turtle.penup()


def drawArrows2(vertices, directed_graph_matrix):
  turtle.speed(0)
  turtle.penup()

  n = len(vertices)
  radius = 20
  arrow_size = 10

  for i in range(n):
    for j in range(i):
      if i != j and abs(vertices[i].number - vertices[j].number) != 5 and directed_graph_matrix[i][j] == 1 and directed_graph_matrix[j][i] != 1:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y

        x1 += math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y1 += math.sin(math.atan2(y2 - y1, x2 - x1)) * radius
        x2 -= math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y2 -= math.sin(math.atan2(y2 - y1, x2 - x1)) * radius

        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))

        turtle.goto(x1, y1)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.goto(x2, y2)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.pendown()
        turtle.right(150)
        turtle.forward(arrow_size)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.left(300)
        turtle.pendown()
        turtle.forward(arrow_size)
        turtle.penup()


def drawCurvedArrows1(vertices, directed_graph_matrix):
  turtle.speed(0)
  turtle.penup()

  n = len(vertices)
  radius = 20
  arrow_size = 10

  for i in range(n):
    for j in range(i):
      if directed_graph_matrix[i][j] == 1 and directed_graph_matrix[j][i] == 1 and abs(vertices[i].number - vertices[j].number) != 5:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y
        x1 += math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y1 += math.sin(math.atan2(y2 - y1, x2 - x1)) * radius
        x2 -= math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y2 -= math.sin(math.atan2(y2 - y1, x2 - x1)) * radius

        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))

        turtle.penup()
        turtle.goto(x1, y1)
        turtle.setheading(angle)
        turtle.pendown()
        distance = turtle.distance(x2, y2)
        degrees = 10
        b = distance / 2 / math.cos(math.radians(degrees))
        turtle.left(degrees)
        turtle.forward(b)
        turtle.setheading(turtle.towards(x2, y2))
        turtle.goto(x2, y2)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.pendown()
        turtle.right(150)
        turtle.forward(arrow_size)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.left(300)
        turtle.pendown()
        turtle.forward(arrow_size)
        turtle.penup()


def drawCurvedArrows2(vertices, directed_graph_matrix):
  turtle.speed(0)
  turtle.penup()

  n = len(vertices)
  radius = 20
  arrow_size = 10

  for i in range(n):
    for j in range(n):
      if directed_graph_matrix[i][j] == 1 and abs(vertices[i].number - vertices[j].number) == 5:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y
        x1 += math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y1 += math.sin(math.atan2(y2 - y1, x2 - x1)) * radius
        x2 -= math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y2 -= math.sin(math.atan2(y2 - y1, x2 - x1)) * radius

        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))

        turtle.penup()
        turtle.goto(x1, y1)
        turtle.setheading(angle)
        turtle.pendown()
        distance = turtle.distance(x2, y2)
        degrees = 2 * math.pi
        b = distance / 2 / math.cos(math.radians(degrees))
        turtle.right(degrees)
        turtle.forward(b)
        turtle.setheading(turtle.towards(x2, y2))
        turtle.goto(x2, y2)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.pendown()
        turtle.right(150)
        turtle.forward(arrow_size)
        turtle.penup()
        turtle.goto(x2, y2)
        turtle.left(300)
        turtle.pendown()
        turtle.forward(arrow_size)
        turtle.right(300)
        turtle.penup()


def drawCirclesWithArrows(vertices, directed_graph_matrix):
  turtle.speed(0)
  turtle.penup()

  n = len(vertices)
  radius = 10
  for i in range(n):
    if directed_graph_matrix[i][i] == 1:
      x, y = vertices[i].pos_x, vertices[i].pos_y
      turtle.goto(x + math.pi / 1.8 * radius, y + math.pi / 1.8 * radius)
      turtle.pendown()
      turtle.circle(radius)
      turtle.penup()
      turtle.goto(x + math.pi / 1.6 * radius - math.pi, y + math.pi / 1.9 * radius - 1.4 * math.pi)
      turtle.pendown()
      turtle.right(55)
      turtle.backward(10)
      turtle.penup()
      turtle.goto(x + math.pi / 1.6 * radius - math.pi, y + math.pi / 1.9 * radius - 1.4 * math.pi)
      turtle.left(90)
      turtle.pendown()
      turtle.backward(10)
      turtle.right(35)
      turtle.penup()


def countOutgoingEdges(adjacency_matrix):
  num_vertices = len(adjacency_matrix)
  outgoing_edges = {}

  for i in range(1, num_vertices + 1):
    outgoing_edges[i] = sum(adjacency_matrix[i - 1])

  print("Напівстепені виходу вершин:", outgoing_edges)
  return outgoing_edges


def countIncomingEdges(adjacency_matrix):
  num_vertices = len(adjacency_matrix)
  transposed_matrix = [[adjacency_matrix[j][i] for j in range(num_vertices)] for i in range(num_vertices)]

  incoming_edges = {}

  for i in range(1, num_vertices + 1):
        incoming_edges[i] = sum(transposed_matrix[i - 1])

  print("Напівстепені заходу вершин:", incoming_edges)
  return incoming_edges


def matrixMultiply(matrix1, matrix2):
  result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
          result[i][j] += matrix1[i][k] * matrix2[k][j]

  return result


def matrixSum(matrix1, matrix2):
  result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]

  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result[i][j] = matrix1[i][j] + matrix2[i][j]

  return result


def transposeMatrix(matrix):
  n = len(matrix)
  transposedMatrix = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      transposedMatrix[j][i] = matrix[i][j]

  return transposedMatrix


def multiplyMatricesElementByElement(matrix1, matrix2):
  n = len(matrix1)
  result = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      result[i][j] = matrix1[i][j] * matrix2[i][j]

  return result


def findPathsOfLengthTwo(adjacency_matrix):
  square_matrix = matrixMultiply(adjacency_matrix, adjacency_matrix)
  numbers = len(square_matrix)
  print("Шляхи довжиною 2:")
  for i in range(numbers):
    for j in range(numbers):
      if square_matrix[i][j]:
        for e in range(numbers):
          if adjacency_matrix[i][e] and adjacency_matrix[e][j]:
            print(f"{i + 1}-{e + 1}-{j + 1}")


def findPathsOfLengthThree(adjacency_matrix):
  cube_matrix = matrixMultiply(matrixMultiply(adjacency_matrix, adjacency_matrix), adjacency_matrix)
  numbers = len(cube_matrix)
  print("Шляхи довжиною 3:")
  for i in range(numbers):
    for j in range(numbers):
      if cube_matrix[i][j]:
        for k in range(numbers):
          for m in range(numbers):
            if adjacency_matrix[i][k] and adjacency_matrix[k][m] and adjacency_matrix[m][j]:
              print(f"{i + 1}-{k + 1}-{m + 1}-{j + 1}")


def generateReachabilityMatrix(directed_graph_matrix):
  n = len(directed_graph_matrix)
  previous_degree = directed_graph_matrix
  unit_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
  reachability_matrix = matrixSum(unit_matrix, previous_degree)

  for _ in range(n - 2):
    previous_degree = matrixMultiply(previous_degree, directed_graph_matrix)
    reachability_matrix = matrixSum(reachability_matrix, previous_degree)

  for i in range(n):
    for j in range(n):
      if reachability_matrix[i][j] >= 1:
        reachability_matrix[i][j] = 1
      else:
        reachability_matrix[i][j] = 0

  print("Матриця досяжності:")
  for row in reachability_matrix:
    print(row)

  return reachability_matrix


def generateStrongConnectivityMatrix(reachability_matrix):
  transposed_reachability_matrix = transposeMatrix(reachability_matrix)
  strong_connectivity_matrix = multiplyMatricesElementByElement(reachability_matrix, transposed_reachability_matrix)

  print("Матриця сильної зв'язності:")
  for row in strong_connectivity_matrix:
    print(row)

  return strong_connectivity_matrix


def getComponentsOfStrongConnectivity(strong_connectivity_matrix):
  def depthFirstSearch(vertex):
    nonlocal component
    visited[vertex] = True
    component.append(vertex)
    for neighbor in range(1, len(strong_connectivity_matrix) + 1):
      if strong_connectivity_matrix[vertex - 1][neighbor - 1] == 1 and not visited[neighbor]:
        depthFirstSearch(neighbor)

  n = len(strong_connectivity_matrix)
  visited = [False] * (n + 1)
  components = []

  print("Компоненти сильної зв'язності:")
  for vertex in range(1, n + 1):
    if not visited[vertex]:
      component = []
      depthFirstSearch(vertex)
      components.append(component)
      print(f"{component}")

  return components


def generateAdjacencyMatrixOfCondensationGraph(graph_adjacency_matrix, components):
  num_scc = len(components)
  condensation_matrix = [[0] * num_scc for _ in range(num_scc)]

  for i in range(len(graph_adjacency_matrix)):
    for j in range(len(graph_adjacency_matrix[0])):
      if graph_adjacency_matrix[i][j] == 1:
        scc_i = next(index for index, scc in enumerate(components) if i + 1 in scc)
        scc_j = next(index for index, scc in enumerate(components) if j + 1 in scc)
        if scc_i != scc_j:
          condensation_matrix[scc_i][scc_j] = 1

  print("Матриця суміжності графа конденсації:")
  for row in condensation_matrix:
    print(row)

  return condensation_matrix


main()
