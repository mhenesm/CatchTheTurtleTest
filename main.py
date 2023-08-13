import turtle
import random

# Oyun ekranı
play_board = turtle.Screen()
play_board.title(" Kaplumbağayı  Yakala")
play_board.bgcolor("green")

# kaplumbağa tasarımı
catch_turtle = turtle.Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("light blue")
catch_turtle.shapesize(5, 5, 10)
catch_turtle.penup()
catch_turtle.hideturtle()
# zamanlayıcı kalem ayarları
timer_pen = turtle.Turtle()
timer_pen.penup()
timer_pen.hideturtle()
timer_pen.goto(0, 300)
timer_pen.color("white")

# zamanlayıcı kalem ayarları
catch_pen = turtle.Turtle()
catch_pen.penup()
catch_pen.hideturtle()
catch_pen.goto(0, 200)
catch_pen.color("white")

countdown = 30
catch = 0
def on_turtle_click(x, y):
    if countdown > 0:
        global catch
        catch_pen.clear()
        catch_pen.write("Skor:  " + str(catch), align="center", font=("Arial", 48, "normal"))
        catch += 1
# Geri sayıcıyı gösteren işlev
def show_countdown():
    global countdown
    timer_pen.clear()  # Önceki yazıyı temizle
    if countdown > 0:
        timer_pen.write("Time:  " + str(countdown), align="center", font=("Arial", 48, "normal"))
        countdown -= 1
        turtle.ontimer(show_countdown, 1000)  # 1 saniye bekleyip tekrar çağır
    else:
        timer_pen.write("KAPLUMBAĞALAR KAÇTIIIIIIIII!", align="center", font=("Arial", 48, "normal"))

show_countdown()
def hide_turtle():
    catch_turtle.hideturtle()
    play_board.ontimer(show_turtle, 800)  # Kaplumbağayı tekrar göster
    catch_turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
def show_turtle():
    if countdown > 0:
        catch_turtle.showturtle()
        play_board.ontimer(hide_turtle, 800)  # Kaplumbağayı gizle

show_turtle()
if countdown > 0 :
    show_turtle()
    # İlk çağrıyı yap (2 saniye sonra)
    catch_turtle.onclick(on_turtle_click)

turtle.done()
