import turtle as t
import pandas as pd

screen = t.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
screen.title('U.S. States Game')
t.shape(image)

game_data = pd.read_csv('50_states.csv')

game_is_on = True
score = 0
guessed = []
while game_is_on:
    answer_state = t.textinput(title=f'{score}/50 Guess the state', prompt="Enter a state's name: ").title()
    state_list = game_data['state'].to_list()

    if answer_state == 'Exit':
        missing_states = [state for state in state_list if state not in guessed]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        game_is_on = False

    if answer_state in state_list:
        guessed.append(answer_state)
        score += 1
        turt = t.Turtle()
        turt.hideturtle()
        turt.penup()
        turt.goto(int(game_data[game_data['state'] == answer_state].x), int(game_data[game_data['state'] == answer_state].y))
        turt.write(answer_state)
        if score == 50:
            game_is_on = False
    else:
        pass


screen.exitonclick()