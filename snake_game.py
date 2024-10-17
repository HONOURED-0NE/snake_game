from turtle import Screen, Turtle
import time
import random
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20  
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
ALIGNMENT = "center" 
FONT = ("Courier", 18, "normal")

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write((f"Score: {self.score} High score:{self.high_score}"), align = ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

#    def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align = ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Detect snake colission with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
#Detect collision with wall
    if snake.head.xcor() > 290 or  -290 > snake.head.xcor() or snake.head.ycor() > 290 or  -290 > snake.head.ycor():
        scoreboard.reset()
        snake.reset()
#Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

















































































screen.exitonclick()