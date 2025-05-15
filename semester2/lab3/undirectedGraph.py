
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
  drawVertices(position)
  drawLines(position, undirected_graph_matrix)
  drawCurvedLines(position, undirected_graph_matrix)
  drawCircles(position, undirected_graph_matrix)

def generateMatrix(n3, n4, N, seed):
  random.seed(seed)
  adj_matrix = [[random.random() * 2.0 for _ in range(N)] for _ in range(N)]
  k = 1.0 - n3 * 0.02 - n4 * 0.005 - 0.25
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
  vertices = []
  center_x = 0
  center_y = 0
  radius = 300
  n = len(undirected_graph_matrix)

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

def drawLines(vertices, undirected_graph_matrix):
  turtle.speed(0)
  turtle.penup()

  n = len(vertices)
  radius = 20
  for i in range(n):
    for j in range(i+1, n): # верхній трикутник матриці
      if i != j and undirected_graph_matrix[i][j] == 1 and abs(vertices[i].number - vertices[j].number) != 5:
        x1, y1 = vertices[i].pos_x, vertices[i].pos_y
        x2, y2 = vertices[j].pos_x, vertices[j].pos_y
        x1 += math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y1 += math.sin(math.atan2(y2 - y1, x2 - x1)) * radius
        x2 -= math.cos(math.atan2(y2 - y1, x2 - x1)) * radius
        y2 -= math.sin(math.atan2(y2 - y1, x2 - x1)) * radius

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
    for j in range(i+1, n): # верхній трикутник матриці
      if i != j and undirected_graph_matrix[i][j] == 1 and abs(vertices[i].number - vertices[j].number) == 5:
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
  for i in range(n): # головна діагональ
    if undirected_graph_matrix[i][i] == 1:
      x, y = vertices[i].pos_x, vertices[i].pos_y
      turtle.goto(x + math.pi / 2 * radius, y + math.pi / 2 * radius)
      turtle.pendown()
      turtle.circle(radius)
      turtle.penup()
  turtle.hideturtle()
  turtle.done()

main()
