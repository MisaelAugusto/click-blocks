import pygame
from pygame.locals import *
from random import *

pygame.init()
pygame.display.set_caption("1_Joguinho")

screen = pygame.display.set_mode((600, 500), 0, 32)

pygame.font.init()

pygame.mixer.pre_init(44100, 32, 2, 4096)

# Fonts
font = pygame.font.get_default_font()
font_game = pygame.font.SysFont(font, 45)
font_exit = pygame.font.SysFont(font, 45)
font_play = pygame.font.SysFont(font, 70)
font_options = pygame.font.SysFont(font, 55)

Back_text = font_exit.render("Back", 1, (255, 255, 255))

Back_text_position_X = 495
Back_text_position_Y = 450

# Clock
clock = pygame.time.Clock()

# Colors
Background_Color = Color(0, 0, 0)

# Sounds
time_bonus_sound = pygame.mixer.Sound("./assets/sounds/1.ogg")
click_sound = pygame.mixer.Sound("./assets/sounds/2.ogg")
seconds_sound = pygame.mixer.Sound("./assets/sounds/3.ogg")
test_sound = pygame.mixer.Sound("./assets/sounds/4.ogg")
main_sound = pygame.mixer.Sound("./assets/sounds/main.ogg")

# Images
Block_pink = pygame.image.load("./assets/images/Block_Pink.png")
Block_blue = pygame.image.load("./assets/images/Block_Blue.png")
Timer_aux = pygame.image.load("./assets/images/Time_aux.png")
Selected_block = pygame.image.load("./assets/images/selected.png")
Unselected_block = pygame.image.load("./assets/images/unselected.png")
Timer_bonus = pygame.image.load("./assets/images/timer_bonus.png")
Time_bonus_aux = pygame.image.load("./assets/images/Time_bonus_aux.png")

# Extra
Block_colors_list = [Block_blue, Block_pink]
i = randint(0, 1)
Block = Block_colors_list[i]

scores = []
Start_2 = True

def Game_Over(score, scores):
	Start_2 = True

	scores.append(score)
	scores = sorted(scores)

	if len(scores) > 10:
		scores.pop(0)

	highscore = str(scores[-1])
	High_Score_Number = font_options.render(highscore, 1, (255, 255, 255))

	The_End = font_play.render("Game Over!", 1, (255, 255, 255))

	Your_Score_Text = font_options.render("Your Score:", 1, (255, 255, 255))

	High_Score_Text = font_options.render("HighScore:", 1, (255, 255, 255))

	score = str(score)
	Score_Number = font_options.render(score, 1, (255, 255, 255))

	screen.fill(Background_Color)
	screen.blit(The_End, (145, 90))

	screen.blit(Your_Score_Text, (165, 250))
	screen.blit(Score_Number, (380, 250))

	screen.blit(High_Score_Text, (165, 300))
	screen.blit(High_Score_Number, (380, 300))

	screen.blit(Back_text, (Back_text_position_X, Back_text_position_Y))

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		mouse_position = pygame.mouse.get_pos()
		click_mouse = pygame.mouse.get_pressed()

		if Back_text_position_X < mouse_position[0] < 565 and Back_text_position_Y < mouse_position[1] < 480 and click_mouse[0]:
			Menu(Block, Start_2)

		pygame.display.update()

def Sort_Position(position_X, position_Y):
	while True:
		position_Bonus_X = randint(10, 490)
		position_Bonus_Y = randint(50, 390)
		if position_Bonus_X != position_X and position_Bonus_Y != position_Y:
			break

	return position_Bonus_X, position_Bonus_Y

def Sort_Bonus():
	number = randint(0, 20)
	if number == 1:
		return True
	else:
		return False

def Game(Block):
	main_sound.stop()
	Start_2 = True
	start = False
	screen.fill(Background_Color)

	score = 0

	Score_text = font_game.render("Score:", 1, (255, 255, 255))
	Score_number = font_game.render("0", 1, (255, 255, 255))

	screen.blit(Score_text, (10, 10))
	screen.blit(Score_number, (110, 12))

	time = 60

	Timer_text = font_game.render("Time:", 1, (255, 255, 255))
	Timer_number = font_game.render("60", 1, (255, 255, 255))
	Timer_Bonus = font_game.render("+5s", 1, (255, 255, 255))

	screen.blit(Timer_text, (445, 10))
	screen.blit(Timer_number, (530, 12))

	position_Block_X = 240
	position_Block_Y = 200

	screen.blit(Block, (position_Block_X, position_Block_Y))

	screen.blit(Back_text, (Back_text_position_X, Back_text_position_Y))

	n = 0
	time_bonus = 0
	Bonus = False
	Bonus_2 = True
	Bonus_3 = False
	Time_s = True

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		mouse_position = pygame.mouse.get_pos()
		click_mouse = pygame.mouse.get_pressed()

		seconds = pygame.time.get_ticks() / 1000
		n += 1

		if n % 33 == 0:
			time -= 1
			if Bonus_3:
				time_bonus += 1

		if time == 0:
			test_sound.play()
			Game_Over(score, scores)

		if n % 33 == 0 and time <= 10 and Time_s:
			seconds_sound.play()
			Time_s = False
		elif n % 33 == 0 and time > 10:
			seconds_sound.stop()
			Time_s = True

		time_str = str(time)
		Timer_number = font_game.render(time_str, 1, (255, 255, 255))

		screen.blit(Timer_aux, (530, 12))
		screen.blit(Timer_number, (530, 12))

		score_str = str(score)
		Score_number = font_game.render(score_str, 1, (255, 255, 255))

		position_X = randint(10, 395)
		position_Y = randint(50, 350)

		if Bonus:
			if position_Bonus_X < mouse_position[0] < (position_Bonus_X + 50) and position_Bonus_Y < mouse_position[1] < (position_Bonus_Y + 50) and click_mouse[0]:
				time += 5
				time_bonus_sound.play()
				screen.blit(Time_bonus_aux , (position_Bonus_X, position_Bonus_Y))
				Bonus = False
				Bonus_2 = True
				Bonus_3 = False

		if Bonus_3:
			screen.blit(Timer_Bonus, (position_Bonus_X, position_Bonus_Y))

		if time_bonus == 3:
			screen.blit(Time_bonus_aux , (position_Bonus_X, position_Bonus_Y))
			Bonus = False
			Bonus_2 = True
			Bonus_3 = False
			time_bonus = 0

		if position_Block_X < mouse_position[0] < (position_Block_X + 100) and position_Block_Y < mouse_position[1] < (position_Block_Y + 100) and click_mouse[0]:
			click_sound.play()
			score += 1
			position_Block_X = position_X
			position_Block_Y = position_Y
			screen.fill(Background_Color)
			screen.blit(Score_text, (10, 10))
			screen.blit(Score_number, (110, 12))
			screen.blit(Timer_text, (445, 10))

			Sort = Sort_Bonus()

			if Sort and Bonus_2:
				position_Bonus_X, position_Bonus_Y = Sort_Position(position_X, position_Y)
				screen.blit(Timer_Bonus, (position_Bonus_X, position_Bonus_Y))
				Bonus = True
				Bonus_2 = False
				Bonus_3 = True

		if Back_text_position_X < mouse_position[0] < 565 and Back_text_position_Y < mouse_position[1] < 480 and click_mouse[0]:
			Menu(Block, Start_2)

		screen.blit(Back_text, (Back_text_position_X, Back_text_position_Y))

		screen.blit(Block, (position_Block_X, position_Block_Y))

		pygame.display.update()
		time_passed = clock.tick(30)

def Credits():
	Start_2 = False

	screen.fill(Background_Color)

	screen.blit(Back_text, (Back_text_position_X, Back_text_position_Y))

	font_credits = pygame.font.SysFont(font, 50)

	Credits_text_1 = font_credits.render("A Game By", 1, (255, 255, 255))
	Credits_text_2 = font_credits.render("Misael Augusto", 1, (255, 255, 255))
	Credits_text_3 = font_credits.render("(C)opyright 2017", 1, (255, 255, 255))

	screen.blit(Credits_text_1, (200, 170))
	screen.blit(Credits_text_2, (160, 210))
	screen.blit(Credits_text_3, (150, 250))

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		mouse_position = pygame.mouse.get_pos()
		click_mouse = pygame.mouse.get_pressed()

		if Back_text_position_X < mouse_position[0] < 565 and Back_text_position_Y < mouse_position[1] < 480 and click_mouse[0]:
			Menu(Block, Start_2)

		pygame.display.update()

def Options():
	start = False
	Start_2 = False

	screen.fill(Background_Color)

	Select_text = font_options.render("Select your Block Color", 1, (255, 255, 255))

	Color_Blue_text = font_exit.render("Blue", 1, (255, 255, 255))
	Color_Pink_text = font_exit.render("Pink", 1, (255, 255, 255))

	screen.blit(Select_text, (90, 60))

	screen.blit(Color_Blue_text, (125, 180))
	screen.blit(Block_blue, (108, 220))

	screen.blit(Color_Pink_text, (400, 180))
	screen.blit(Block_pink, (383, 220))

	screen.blit(Back_text, (Back_text_position_X, Back_text_position_Y))

	color_b = True
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		mouse_position = pygame.mouse.get_pos()
		click_mouse = pygame.mouse.get_pressed()

		if 108 < mouse_position[0] < 208 and 220 < mouse_position[1] < 320 and click_mouse[0]:
			Block = Block_blue
			screen.blit(Selected_block, (100, 211))
			screen.blit(Unselected_block, (375, 211))
			color_b = False
		elif 383 < mouse_position[0] < 483 and 220 < mouse_position[1] < 320 and click_mouse[0]:
			Block = Block_pink
			screen.blit(Selected_block, (375, 211))
			screen.blit(Unselected_block, (100, 211))
			color_b = False

		if Back_text_position_X < mouse_position[0] < 565 and Back_text_position_Y < mouse_position[1] < 480 and click_mouse[0]:
			if color_b:
				Block_colors_list = [Block_blue, Block_pink]
				i = randint(0, 1)
				Block = Block_colors_list[i]

			Menu(Block, Start_2)

		pygame.display.update()

def Menu(Block, Start_2):
	if Start_2:
		main_sound.play()
		Start_2 = False

	Play_text = font_play.render("Play", 1, (255, 255, 255))

	Options_text = font_options.render("Options", 1, (255, 255, 255))

	Credits_text = font_options.render("Credits", 1, (255, 255, 255))

	Exit_text = font_exit.render("Exit", 1, (255, 255, 255))

	screen.fill(Background_Color)
	screen.blit(Play_text, (248, 150))
	screen.blit(Options_text, (220, 210))
	screen.blit(Credits_text, (230, 260))
	screen.blit(Exit_text, (270, 310))

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		mouse_position = pygame.mouse.get_pos()
		click_mouse = pygame.mouse.get_pressed()

		start = True

		if 248 < mouse_position[0] < 350 and 150 < mouse_position[1] < 200 and click_mouse[0] and start:
			Game(Block)
		elif 220 < mouse_position[0] < 372 and 210 < mouse_position[1] < 250 and click_mouse[0] and start:
			Options()
		elif 230 < mouse_position[0] < 370 and 260 < mouse_position[1] < 300 and click_mouse[0] and start:
			Credits()
		elif 270 < mouse_position[0] < 330 and 310 < mouse_position[1] < 340 and click_mouse[0] and start:
			exit()

		pygame.display.update()

Menu(Block, Start_2)
