import pygame
import time
import random
pygame.init()
gd_width=1200
gd_height=600
gd=pygame.display.set_mode((gd_width,gd_height))
pygame.display.set_caption("Snake")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,155,0)
img=pygame.image.load('snakehead.png')
appleimg=pygame.image.load('apple.png')
clock=pygame.time.Clock()
at=25
block_size=20
FPS=10
direction="left"
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)

def pause():
	paused=True
	while paused:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_c:
					paused=False
				elif event.key==pygame.K_q:
					pygame.quit()
					quit()
		gd.fill(white)
		msg_to_gd("Paused",black,-100,"large")
		msg_to_gd("Press C to continue or Q to quit",
					black,25)
		pygame.display.update()
		clock.tick(5)
def score(score):
	text=smallfont.render("Score: "+str(score),True,red)
	gd.blit(text,[0,0])
def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_s:
					intro=False
				elif event.key==pygame.K_q:
					pygame.quit()
					quit()
		
		gd.fill(white)
		icon=pygame.image.load('icon.png')
		gd.blit(icon,[20,20])
		msg_to_gd("Welcome to Snakiee",green,-120,"large")
		msg_to_gd("Objective to eat apples",black,-30)
		msg_to_gd("More apples the longer you get",black,10)
		msg_to_gd("If you run intor yourself and out of boundaries",black,70)
		msg_to_gd("Precc S to start or Q to quit",black,100)
		msg_to_gd("Press P to pause the game..!",black,150)
		pygame.display.update()
		clock.tick(100)
def snake(block_size,snakelist):
	if direction=="right":
		head=pygame.transform.rotate(img,270)
	if direction=="left":
		head=pygame.transform.rotate(img,90)
	if direction=="up":
		head=img
	if direction=="down":
		head=pygame.transform.rotate(img,180)
	gd.blit(head,(snakelist[-1][0],snakelist[-1][1]))
	for XnY in snakelist[:-1]:
		pygame.draw.rect(gd,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
	if size=="small":
		textSurface=smallfont.render(text,True,color)
	elif size=="medium":
		textSurface=medfont.render(text,True,color)
	elif size=="large":
		textSurface=largefont.render(text,True,color)
	return textSurface, textSurface.get_rect()
			
def msg_to_gd(msg,color,y_displace=0,size="small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center=(gd_width/2),(gd_height/2)+y_displace
	gd.blit(textSurf, textRect)
def g_loop():
	global direction
	direction='right'
	lead_x=gd_width/2
	lead_y=gd_height/2
	lead_x_change=0
	lead_y_change=0
	snakelist=[]
	snakelength=1
	rapple_x=round(random.randrange(0,gd_width-at))#/10.0)*10.0
	rapple_y=round(random.randrange(0,gd_height-at))#/10.0)*10.0
	ge=False
	go=False
	while not ge:
		while go == True:
			gd.fill(white)
			msg_to_gd("Game over..!",red,y_displace=-50,size="large")
			msg_to_gd("S to play again an Q to quit",black,50,size="medium")
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					ge=True
					go=False
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_q:
						ge=True
						go=False
					if event.key==pygame.K_s:
						g_loop()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				ge=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					direction="right"
					lead_x_change = block_size
					lead_y_change=0
				elif event.key==pygame.K_LEFT:
					direction="left"
					lead_x_change = -block_size
					lead_y_change=0
				elif event.key==pygame.K_UP:
					direction="up"
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key==pygame.K_DOWN:
					direction="down"
					lead_y_change = block_size
					lead_x_change =0
				elif event.key==pygame.K_p:
					pause()
		if lead_x >= gd_width or lead_x <= 0 or lead_y >= gd_height or lead_y <= 0:
			go=True

		lead_x += lead_x_change
		lead_y += lead_y_change
		
		gd.fill(white)
		
		#pygame.draw.rect(gd,green,[rapple_x,rapple_y,at,at])
		gd.blit(appleimg,(rapple_x,rapple_y))
		gd.blit(appleimg,(100,0))
		snakehead=[]
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)
		if len(snakelist)>snakelength:
			del snakelist[0]
		for eachseg in snakelist[:-1]:
			if eachseg==snakehead:
				go=True
		snake(block_size,snakelist)
		score(snakelength-1)
		pygame.display.update()
#		if lead_x == rapple_x and lead_y == rapple_y:
#			rapple_x=round(random.randrange(0,gd_width-block_size)/10.0)*10.0
#			rapple_y=round(random.randrange(0,gd_height-block_size)/10.0)*10.0
#			snakelength += 1

#		if lead_x >= rapple_x and lead_x <= rapple_x + at:
#			if lead_y >= rapple_y and lead_y <= rapple_y +at:
#				rapple_x=round(random.randrange(0,gd_width-block_size))#/10.0)*10.0
#				rapple_y=round(random.randrange(0,gd_height-block_size))#/10.0)*10.0
#				snakelength += 1
		if lead_x > rapple_x and lead_x < rapple_x + at or lead_x + block_size > rapple_x and lead_x+block_size < rapple_x + at:
			if lead_y > rapple_y and lead_y < rapple_y + at or lead_y + block_size > rapple_y and lead_y+block_size < rapple_y + at:
				rapple_x=round(random.randrange(0,gd_width-at))#/10.0)*10.0
				rapple_y=round(random.randrange(0,gd_height-at))#/10.0)*10.0
				snakelength += 1
		clock.tick(FPS)
	pygame.quit()
	quit()
game_intro()
g_loop()
