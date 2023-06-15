from tkinter import *
from PIL import ImageTk, Image
import random

# main window object
root = Tk()

# Title of GUI window
root.title('Rock Paper Scissor')

# Size of window
root.geometry('800x680')

# Creating canvas
canvas = Canvas(root, width=800, height=680)
canvas.grid(row=0, column=0)

# Creating labels on GUI window
label1 = Label(root, text='Player', font=('Algerian', 25))
label2 = Label(root, text='Computer', font=('Algerian', 25))
label3 = Label(root, text='Vs', font=('Algerian', 40))

# Placing all the labels on window
label1.place(x=80, y=20)
label2.place(x=560, y=20)
label3.place(x=370, y=230)

# Default image
default_img_raw = Image.open("images/default.png")
default_img_raw = default_img_raw.resize((300, 300))
# Flipping image from left to right for cpu choice
default_img_cpu = default_img_raw.transpose(Image.FLIP_LEFT_RIGHT)
# Loading images to put on canvas
default_img = ImageTk.PhotoImage(default_img_raw)
default_img_cpu = ImageTk.PhotoImage(default_img_cpu)

# Rock image
rock_img_raw = Image.open("images/rock.png")
rock_img_raw = rock_img_raw.resize((300, 300))
# Flipping image from left to right for cpu choice
rock_img_cpu = rock_img_raw.transpose(Image.FLIP_LEFT_RIGHT)
# Loading images to put on canvas
rock_img = ImageTk.PhotoImage(rock_img_raw)
rock_img_cpu = ImageTk.PhotoImage(rock_img_cpu)

# Paper image
paper_img_raw = Image.open("images/paper.png")
paper_img_raw = paper_img_raw.resize((300, 300))
# Flipping image from left to right for cpu choice
paper_img_cpu = paper_img_raw.transpose(Image.FLIP_LEFT_RIGHT)
# Loading images to put on canvas
paper_img = ImageTk.PhotoImage(paper_img_raw)
paper_img_cpu = ImageTk.PhotoImage(paper_img_cpu)

# Scissors image
scissors_img_raw = Image.open("images/scissors.png")
scissors_img_raw = scissors_img_raw.resize((300, 300))
# Flipping image from left to right for cpu choice
scissors_img_cpu = scissors_img_raw.transpose(Image.FLIP_LEFT_RIGHT)
# Loading images to put on canvas
scissors_img = ImageTk.PhotoImage(scissors_img_raw)
scissors_img_cpu = ImageTk.PhotoImage(scissors_img_cpu)

# Scoring
player_score = 0
cpu_score = 0
score_txt = StringVar()
score_txt.set(str(player_score) + "-" + str(cpu_score))
score_label = Label(root, textvariable=score_txt, font=('Algerian', 50)).place(x=350, y=400)

# game function
def game(player):
    global player_score, cpu_score, score_txt
    
    # clear previous choices
    clear()
    
    # cpu choices
    select = [1,2,3]
    
    # randomly select option for computer
    computer = random.choice(select)
    
    # remove default images
    canvas.delete("default")
    
    # Setting image for player on canvas
    match player:
        case 1:
            # Rock
            canvas.create_image(0, 100, anchor=NW, image=rock_img, tag='player_choice')
        case 2:
            # Paper
            canvas.create_image(0, 100, anchor=NW, image=paper_img, tag='player_choice')
        case 3:
            # Scissors
            canvas.create_image(0, 100, anchor=NW, image=scissors_img, tag='player_choice')

    # Setting image for cpu on canvas
    match computer:
        case 1:
            # Rock
            canvas.create_image(500, 100, anchor=NW, image=rock_img_cpu, tag='cpu_choice')
        case 2:
            # Paper
            canvas.create_image(500, 100, anchor=NW, image=paper_img_cpu, tag='cpu_choice')
        case 3:
            # Scissors
            canvas.create_image(500, 100, anchor=NW, image=scissors_img_cpu, tag='cpu_choice')

    # Get match result
    # Draw
    if player == computer:
        res = 'Draw'
    # Player win
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        player_score += 1
        res = 'You won'
    # CPU win
    else:
        cpu_score += 1
        res = 'Computer won'
    
    score_txt.set(str(player_score) + "-" + str(cpu_score))
        
    # Display result
    canvas.create_text(390, 620, text='Result:- ' + res, fill="black", font=('Algerian', 25), tag='result')

# Clear function
def clear():
    canvas.delete('result')
    canvas.delete('player_choice')
    canvas.delete('cpu_choice')

# Reset function
def reset():
    global player_score, cpu_score, score_txt
    # reset scores
    player_score = 0
    cpu_score = 0
    score_txt.set(str(player_score) + "-" + str(cpu_score))
    
    # remove result & choices from canvas
    canvas.delete('result')
    canvas.delete('player_choice')
    canvas.delete('cpu_choice')
    
    # display default image
    canvas.create_image(0, 100, anchor=NW, image=default_img, tag='default')
    canvas.create_image(500, 100, anchor=NW, image=default_img_cpu, tag='default')

# Selection buttons/images
# Rock button
rock_img_raw = rock_img_raw.resize((100, 100))
rock_img_choice = ImageTk.PhotoImage(rock_img_raw)
# rock_img_label = Label(image=rock_img_choice)
rock_btn = Button(root, image=rock_img_choice, command=lambda: game(1), borderwidth=5)
rock_btn.place(x=35, y=487)

# Paper
paper_img_raw = paper_img_raw.resize((100, 100))
paper_img_choice = ImageTk.PhotoImage(paper_img_raw)
# paper_img_label = Label(image=paper_img_choice)
paper_btn = Button(root, image=paper_img_choice, command=lambda: game(2), borderwidth=5)
paper_btn.place(x=140, y=487)

# Scissors
scissors_img_raw = scissors_img_raw.resize((100, 100))
scissors_img_choice = ImageTk.PhotoImage(scissors_img_raw)
# scissors_img_label = Label(image=scissors_img_choice)
scissors_btn = Button(root, image=scissors_img_choice, command=lambda: game(3), borderwidth=5)
scissors_btn.place(x=250, y=487)

# reset button
reset_btn = Button(root, text="RESET", font=('Times', 10, 'bold'), width=10, command=reset).place(x=370, y=28)

# display default image
canvas.create_image(0, 100, anchor=NW, image=default_img, tag='default')
canvas.create_image(500, 100, anchor=NW, image=default_img_cpu, tag='default')

root.mainloop()