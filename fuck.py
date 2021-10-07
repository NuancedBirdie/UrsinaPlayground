from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
global player

player = FirstPersonController( y=0, origin_y=-.5) #set first person player

def update():

	visibletext()

	rutabaga()

	coordinates()

	if held_keys['shift']:
		thirdperson()

	if held_keys['r']:
		player.y = 5
		player.x = 0
		player.z = 0	

def thirdperson():
	if held_keys['shift']:
		player = FirstPersonController(model='cube', collider='mesh')
		camera.z = -5
		player.y = 5
		player.x = 0
		player.z = 0

def coordinates(): #displays area player is in based on olayer.x

	coordinates = str(player.x)

	if player.x < 2.35 and player.x > -2.12:
		area.text = "Area 1"
		ominous.texture = "omin"

	#default values for info text and ominous color and texture
	if player.x < -5.24 and player.x > -9.31:
		area.text = "Area 2"
		ominous.color = color.white
		ominous.texture = "omin2" 

	if player.grounded == False:
		area.text = "Jump!"

def playerreset(): 	#resets player if fallen 
	if player.y < -2:
		player.y = 5
		player.x = 0
		player.z = 0	

def visibletext(): #makes the text visible upon 'e' press
	if held_keys['e']:
		area.visible = True

	else:
		area.visible = False

def rutabaga(): #mutes upon 'm' press and unmute upon 'n'8
	if held_keys['m']:
		a.volume = 0

	if held_keys['n']:
		a.volume = 20
		a.pitch = 2
		a.balance = 1

def windowsetup(): #sets up the game window
	window.title = 'Fucking About'
	window.borderless = False
	window.fullscreen = False
	window.exit_button.visible = False
	window.fps_counter.enabled = False

windowsetup()

#sets up text on UI layer
Text.size = 0.05
Text.default_resolution = 1080 * Text.size
area = Text(text="           ")
area.x = -0.105
area.y = -0.35
area.background = True
area.visible = False

a = Audio('salad', pitch=1, loop=True, autoplay=True, volume=1) #WELCOME TO POST HELL

ominous = Entity(model='sphere', color=color.white, scale=(1,1,1), texture="omin", texture_scale=(1,1), collider='box', position=(0,3,3)) #set the ominous figure

area_1 = Entity(model='plane', color=color.white, scale=(5,1,5), texture="brick", texture_scale=(3,3), collider='box', position=(0,0,0)) #set the floor entity

area_2 = Entity(model='plane', color=color.white, scale=(5,1,5), texture="brick", texture_scale=(3,3), collider='box', position=(-7,1,0)) #set floor2

sky = Entity(model='sky_dome', color=color.white, scale=(20,20,20), texture="sky") #set the sky

app.run()