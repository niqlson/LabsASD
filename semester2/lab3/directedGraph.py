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
  position = createPositions(directed_graph_matrix)
  drawVertices(position)
  drawArrows1(position, directed_graph_matrix)
  drawArrows2(position, directed_graph_matrix)
  drawCurvedArrows1(position, directed_graph_matrix)
  drawCurvedArrows2(position, directed_graph_matrix)
  drawCirclesWithArrows(position, directed_graph_matrix)

def generateMatrix(n3, n4, N, seed):
  random.seed(seed)
  adj_matrix = [[random.random() * 2.0 for _ in range(N)] for _ in range(N)]
  k = 1.0 - n3 * 0.02 - n4 * 0.005 - 0.25
  for i in range(N):
    for j in range(N):
      adj_matrix[i][j] *= k
      adj_matrix[i][j] = 0 if adj_matrix[i][j] < 1.0 else 1
  print("Матриця суміжності напрямленого графа:")
  for row in adj_matrix:
    print(row)

  return adj_matrix

def createPositions(directed_graph_matrix):
  vertices = []
  center_x = 0
  center_y = 0
  radius = 300
  n = len(directed_graph_matrix)

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
    for j in range(i + 1, n): # верхній трикутник матриці
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
    for j in range(i): # нижній трикутник матриці
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
    for j in range(i): # нижній трикутник матриці
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
    for j in range(n): # повна матриця
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
  for i in range(n): # головна діагональ
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

  turtle.hideturtle()
  turtle.done()

main()
