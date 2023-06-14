import pygame
import random
import pygame.mixer
import sys

# Define the screen size
screen_width = 800
screen_height = 600

# Initialize Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define any necessary fonts
font = pygame.font.SysFont(None, 40)

# Define any necessary colors
white = (255, 255, 255)
screen.fill("light blue")
# Define any necessary images
bg_image1 = pygame.image.load("Game.img/start_btn.png")
bg_rect1 = bg_image1.get_rect(topleft=(255, 60))
bg_image2 = pygame.image.load("Game.img/exit_btn.png")
bg_rect2 = bg_image2.get_rect(topleft=(278, 280))
bg_image3 = pygame.image.load("Game.img/bird1.png")
bg_rect3 = bg_image3.get_rect(topleft=(0, 0))


def game_intro1():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and bg_rect1.collidepoint(mouse_pos):
            return
        if pygame.mouse.get_pressed()[0] and bg_rect2.collidepoint(mouse_pos):
            pygame.quit()
            
            
        screen.blit(bg_image1, bg_rect1)
        screen.blit(bg_image2, bg_rect2)

        pygame.display.flip()
game_intro1()

screen_width = 800
screen_height = 600

# Initialize Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define any necessary fonts
font = pygame.font.SysFont(None, 40)

# Define any necessary colors
white = (255, 255, 255)
screen.fill("light blue")
# Define any necessary images
bg_image2 = pygame.image.load("Game.img/exit_btn.png")
bg_rect2 = bg_image2.get_rect(topleft=(278, 280))


def game_intro2():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and bg_rect1.collidepoint(mouse_pos):
            return
        if pygame.mouse.get_pressed()[0] and bg_rect2.collidepoint(mouse_pos):
            pygame.quit()
            
            
        screen.blit(bg_image2, bg_rect2)

        pygame.display.flip()
import pygame
pygame.init()
pygame.mixer.music.load('Game.img\SpotifyMate.com - Angry Birds Theme - Ari Pulkkinen.mp3')
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)
nonlimit_gap = 1
max_gap = 436
score = 0


clock = pygame.time.Clock()

font = pygame.font.SysFont("Comic Sans",50)

color_col = ((255,225,255))

fps = 60
screen_width = 864
screen_height = 736
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird "BETA"')
ground_scroll = 0
scroll_speed = 4
flying = True
game_over = False
pipe_idk = 1500
pipe_end = pygame.time.get_ticks() - pipe_idk
pipe_gap = 200
score = 0
scorecont = 0
start_button = pygame.image.load('Game.img/menu_start_button.png')
pass_pipe = False


restart_button = pygame.image.load("Game.img/restart.png")
bg = pygame.image.load("Game.img/sky.png")
ground = pygame.image.load("Game.img/ground.png")

def draw_text(text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
def create_pipe():
    # Import the random module if necessary
    import random
    gap_size = random.randint(nonlimit_gap, max_gap)
    bottom_pipe = Pipe(screen_width, int(screen_height / 2) - gap_size // 3, -1)
    top_pipe = Pipe(screen_width, int(screen_height / 2) - gap_size // 5, 1)
    pipe_group.add(bottom_pipe)
    pipe_group.add(top_pipe)
    pipe_group.draw(screen)

class Button2():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self):

		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check if mouse is over the button
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action             
def reset_game():
    pipe_group.empty()
    create_pipe()
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f"Game.img/bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.position = position
        
        
        
        
    def update(self):
        global game_over, flying
        if flying == True:
            #gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
            if self.rect.top < 864:
                self.rect.y += int(self.vel)
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -8.7
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        
        # Check if the bird has collided with the bottom of the screen
        
        
        if self.rect.bottom >= screen_height:
            try:
                pass
            except:
                pass
            
        if self.rect.top >= screen_height:
            flying = True
            try:
                pass
            except:
                pass
            # Define the screen size

        
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y ,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Game.img/pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False,True)
            self.rect.bottomleft = (x,y - int(pipe_gap / 2))
        if position == -1:
            self.rect.topleft = (x,y - int(pipe_gap / -1.2))   
            
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.colliderect(flappy.rect):
            flying = False
            try:
                score = 0
            except:
                    pass
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self):

		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check if mouse is over the button
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action        
            
bottom_pipe = Pipe(screen_width, int(screen_height / 5), -1)
top_pipe = Pipe(screen_width, int(screen_height / 5), 1)
pipe_group = pygame.sprite.Group()
pipe_group.add(bottom_pipe)
pipe_group.add(top_pipe)
flappy = Bird(100, int(screen_height / 2),0)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)


# Create initial objects and add them to groups
flappy = Bird(100, int(screen_height / 2), 0)
bird_group.add(flappy)
bottom_pipe = Pipe(screen_width, int(screen_height / 5), -1)
top_pipe = Pipe(screen_width, int(screen_height / 5), 1)
pipe_group.add(bottom_pipe)
pipe_group.add(top_pipe)

#restart button something

new_button2_image = pygame.transform.scale(bg_image2, (239, 132))
button = Button(screen_width // 2 - 50, screen_height // 2 - 100, restart_button)
button2 = Button2(625, 596, new_button2_image)

run = True

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update the game objects
    bird_group.update()
    pipe_group.update()
    # Check for collisions between the bird and the pipes
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        game_over = True
        game_over = True
    


    # Add new pipes when necessary
    if pipe_group.sprites() and pipe_group.sprites()[0].rect.right < 0:
        pipe_group.empty()
        gap_size = random.randint(nonlimit_gap, max_gap)
        bottom_pipe = Pipe(screen_width, int(screen_height / 2) - gap_size // 5, -1)
        top_pipe = Pipe(screen_width, int(screen_height / 2) - gap_size // 5, 1)
        pipe_group.add(bottom_pipe)
        pipe_group.add(top_pipe)


    # Draw game objects to screen
    screen.blit(bg, (0, 0))
    screen.blit(ground, (ground_scroll, 625))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    
	#check the score
    if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                    and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                    and pass_pipe == False:
                    pass_pipe = True
                if pass_pipe == True:
                    if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                        score += 1
                        pass_pipe = False


    draw_text(str(score), font, color_col, int(screen_width / 2), 20)
    
    # Draw the reset button if game_over is True
    


    if game_over == True:
        game_over = False
        flying = False
        if flying == False:
            score = 0
            scroll_speed = 0
            

            
        if button.draw():
            flying = True
            scroll_speed = 4
            score = reset_game()
    if button2.draw():
        game_intro2()
        flying = False
        score = reset_game()
    
    pygame.display.flip()

