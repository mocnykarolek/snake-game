from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.distance = 0
        self.segments = []
        self.len_of_snake = 3
        self.snake_body()
        self.head = self.segments[0]

    def snake_body(self):
        for turtle in range(self.len_of_snake):
            turtle = Turtle()
            turtle.penup()
            turtle.speed("fastest")
            turtle.color("white")
            turtle.shape("square")
            turtle.backward(self.distance)
            self.distance += 20
            self.segments.append(turtle)
    def extend(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.color("white")
        new_segment.shape("square")

                # Umieść nowy segment na pozycji ostatniego segmentu węża
        last_segment = self.segments[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        
        self.segments.append(new_segment)
        self.len_of_snake += 1




    def forward(self, distance):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()

            self.segments[seg].goto(x, y)

        self.head.forward(distance)

    def up(self):
        if not self.segments[0].heading() == DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if not self.segments[0].heading() == UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if not self.segments[0].heading() == RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if not self.segments[0].heading() == LEFT:
            self.segments[0].setheading(RIGHT)
