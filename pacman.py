import os, sys, random, math
import pygame, os
from pygame.locals import *
if not pygame.font: print 'Required fonts not found'
if not pygame.mixer: print 'Sound is not working'
#The mapping of objects on the grid
gridmap =              [[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                       [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                       [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                       [37,38,38,38,38,38,38,38,38,38,38,38,38,49,47,38,38,38,38,38,38,38,38,38,38,38,38,39],
                       [34,15,15,15,15,15,15,15,15,15,15,15,15,26,24,15,15,15,15,15,15,15,15,15,15,15,15,36],
                       [34,15,27,22,22,29,15,27,22,22,22,29,15,26,24,15,27,22,22,22,29,15,27,22,22,29,15,36],
                       [34,16,26,10,10,24,15,26,10,10,10,24,15,26,24,15,26,10,10,10,24,15,26,10,10,24,16,36],
                       [34,15,21,28,28,23,15,21,28,28,28,23,15,21,23,15,21,28,28,28,23,15,21,28,28,23,15,36],
                       [34,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,36],
                       [34,15,27,22,22,29,15,27,29,15,27,22,22,22,22,22,22,29,15,27,29,15,27,22,22,29,15,36],
                       [34,15,21,28,28,23,15,26,24,15,21,28,28,29,27,28,28,23,15,26,24,15,21,28,28,23,15,36],
                       [34,15,15,15,15,15,15,26,24,15,15,15,15,26,24,15,15,15,15,26,24,15,15,15,15,15,15,36],
                       [31,32,32,32,32,29,15,26,21,22,22,29,10,26,24,10,27,22,22,23,24,15,27,32,32,32,32,33],
                       [10,10,10,10,10,34,15,26,27,28,28,23,10,21,23,10,21,28,28,29,24,15,36,10,10,10,10,10],
                       [10,10,10,10,10,34,15,26,24,10,10,10,10,10,10,10,10,10,10,26,24,15,36,10,10,10,10,10],
                       [10,10,10,10,10,34,15,26,24,10,57,32,32,25,25,32,32,59,10,26,24,15,36,10,10,10,10,10],
                       [38,38,38,38,38,23,15,21,23,10,36,10,10,10,10,10,10,34,10,21,23,15,21,38,38,38,38,38],
                       [17,17,17,17,17,17,15,10,10,10,36,10,10,10,10,10,10,34,10,10,10,15,17,17,17,17,17,17],
                       [32,32,32,32,32,29,15,27,29,10,36,10,10,10,10,10,10,34,10,27,29,15,27,32,32,32,32,32],
                       [10,10,10,10,10,34,15,26,24,10,51,38,38,38,38,38,38,53,10,26,24,15,36,10,10,10,10,10],
                       [10,10,10,10,10,34,15,26,24,10,10,10,10,10,10,10,10,10,10,26,24,15,36,10,10,10,10,10],
                       [10,10,10,10,10,34,15,26,24,10,27,22,22,22,22,22,22,29,10,26,24,15,36,10,10,10,10,10],
                       [37,38,38,38,38,23,15,21,23,10,21,28,28,29,27,28,28,23,10,21,23,15,21,38,38,38,38,39],
                       [34,15,15,15,15,15,15,15,15,15,15,15,15,26,24,15,15,15,15,15,15,15,15,15,15,15,15,36],
                       [34,15,27,22,22,29,15,27,22,22,22,29,15,26,24,15,27,22,22,22,29,15,27,22,22,29,15,36],
                       [34,15,21,22,29,24,15,21,28,28,28,23,15,21,23,15,21,28,28,28,23,15,26,27,22,23,15,36],
                       [34,16,15,15,26,24,15,15,15,15,15,15,15,10,10,15,15,15,15,15,15,15,26,24,15,15,16,36],
                       [41,22,29,15,26,24,15,27,29,15,27,22,22,22,22,22,22,29,15,27,29,15,26,24,15,27,22,43],
                       [44,28,23,15,21,23,15,26,24,15,21,28,28,29,27,28,28,23,15,26,24,15,21,23,15,21,28,46],
                       [34,15,15,15,15,15,15,26,24,15,15,15,15,26,24,15,15,15,15,26,24,15,15,15,15,15,15,36],
                       [34,15,27,22,22,22,22,23,21,22,22,29,15,26,24,15,27,22,22,23,21,22,22,22,22,29,15,36],
                       [34,15,21,28,28,28,28,28,28,28,28,23,15,21,23,15,21,28,28,28,28,28,28,28,28,23,15,36],
                       [34,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,36],
                       [31,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,33],
                       [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                       [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]]
class PacmanMain(object):
    """The main menu and the game

    """
    def __init__(self):
        """Initialize pygame modules and some variables
        """
        self.point = []
        pygame.init()
        pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=4096)
        self.screen = pygame.display.set_mode((336,432))
        self._font = pygame.font.Font(None, 12)
        self.startfont = pygame.font.Font(None, 20)
        self.players = 1
        pygame.display.set_caption('Pacman')
        self.livesimage = pygame.image.load(os.path.join('Data','pac16.bmp'))
        self.livesimage = self.livesimage.convert()
        self.livesimagerect = self.livesimage.get_rect()
        self.fruit1 = pygame.image.load(os.path.join('Data','fruit1.bmp'))
        self.fruit1 = self.fruit1.convert()
        self.fruitrect = self.fruit1.get_rect(topleft = (288,408))
        self.bclear = pygame.Surface((768,24))
        self.bclear = self.bclear.convert()
        self.bclear.fill((0,0,0))
        self.row = 0 # Number of consecutive ghosts eaten after eating one big pellet
        self._pelletsblink = 0
        self._pelletsdelay = 0
        highscorefile = open(os.path.join('Data','highscore.txt'), 'U')
        self.highscore = int(highscorefile.read())
        highscorefile.close()
        self.nnumx = 336/(336/28)
        self.nnumy = 432/(432/len(gridmap))
        self.pelletseaten = 0
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
    def Menu(self):
        """The top method for the game's menu

        """
        #Setting the fonts for the various text on the menu
        self.selectfont = pygame.font.SysFont("arial", 16)
        self.fullscreenfont = pygame.font.SysFont("calibri", 14)
        self.selectedfont = pygame.font.SysFont('arial', 16, bold=True)
        self.titlefont = pygame.font.SysFont("calibri", 40, bold = True)
        self.menu = 0 #Which option in the menu is been selected
        #Title animation variables
        self._menutitledelay = 0
        self._menutitleframe = 0
        self.menudirect = 1
        #Sprites animation variables
        self.menuspritesdelay = 0
        self.menuspritesframe = 0
        self.menuspritesframecount = 0
        self.MenuLoad()
        self.fullscreen = False
        pygame.key.set_repeat(200,500)
        while True:
            for ourevent in pygame.event.get():
                if ourevent.type == QUIT:
                    sys.exit()
                if ourevent.type == KEYDOWN:
                    #Executing what the player has selected
                    if ourevent.key == K_RETURN:
                        if self.menu == 0:
                            self.players = 1
                            self.MainLoop()
                        elif self.menu == 1:
                            self.players = 2
                            self.MainLoop()
                        elif self.menu == 2:
                            if self.fullscreen == False:
                                self.screen = pygame.display.set_mode((336,432), pygame.FULLSCREEN)
                                self.fullscreen = True
                            else:
                                self.screen = pygame.display.set_mode((336,432))
                                self.fullscreen = False
                        elif self.menu == 3:
                            sys.exit()
                    if ourevent.key == K_DOWN and self.menu < 3:
                        self.menu += 1
                    if ourevent.key == K_UP and self.menu > 0:
                        self.menu -= 1
            self.firstplayermenu = self.selectfont.render("1 Player", 1, (255,255,255))
            self.secondplayermenu = self.selectfont.render("2 Players", 1, (255,255,255))
            self.fullscreenselect = self.selectfont.render("Fullscreen", 1, (255,255,255))
            if self.fullscreen == True:
                self.fullscreenchoose = self.fullscreenfont.render("On", 1, (255,255,255))
            else:
                self.fullscreenchoose = self.fullscreenfont.render("Off", 1, (255,255,255))
            self.quitmenu = self.selectfont.render("Quit", 1, (255,255,255))
            if self.menu == 0:
                self.firstplayermenu = self.selectedfont.render("1 Player", 1, (255,255,255))
            elif self.menu == 1:
                self.secondplayermenu = self.selectedfont.render("2 Players", 1, (255,255,255))
            elif self.menu == 2:
                self.fullscreenselect = self.selectedfont.render("Fullscreen", 1, (255,255,255))
            elif self.menu == 3:
                self.quitmenu = self.selectedfont.render("Quit", 1, (255,255,255))
            self.MenuAnim()
            self.MenuDisplay()
    def MenuLoad(self):
        """Load up all the sprites that are to be used in the menu screen

        """
        self.spritesx = -1  #Determine which direction the sprites are travelling
        self.pacman = Pacman((150,150))
        self.blinky = Blinky()
        self.blinky.direction = 'LEFT'
        self.blinky.rect.center = (180,150)
        self.pinky = Pinky()
        self.pinky.rect.center = (210,150)
        self.pinky.direction = 'LEFT'
        self.clyde = Clyde()
        self.clyde.rect.center = (240,150)
        self.clyde.direction = 'LEFT'
        self.inky = Inky()
        self.inky.rect.center = (270,150)
        self.inky.direction = 'LEFT'
        self.ghostssprites = pygame.sprite.RenderUpdates()
        self.ghostssprites.add(self.blinky)
        self.ghostssprites.add(self.pinky)
        self.ghostssprites.add(self.clyde)
        self.ghostssprites.add(self.inky)
    def MenuAnim(self):
        """Animating objects in the menu

        """
        if self._menutitledelay <= pygame.time.get_ticks():
            if self._menutitleframe == 51:
                self.menudirect = -1
            elif self._menutitleframe == 0:
                self.menudirect = 1
            self.title = self.titlefont.render("Pacman", 1, (204+self._menutitleframe,204+self._menutitleframe,5*self._menutitleframe))
            self._menutitleframe += self.menudirect
            self._menutitledelay = pygame.time.get_ticks() + 16
        if self.menuspritesdelay <= pygame.time.get_ticks():
            self.pacman.moveanim(pygame.time.get_ticks())
            self.pacman.rect.move_ip(self.spritesx,0)
            self.menuspritesdelay = pygame.time.get_ticks() + 12
            for g in self.ghostssprites:
                g.rect.move_ip(self.spritesx,0)
                if g.weak == False:
                    g.moveanim()
                else:
                    g.image = Ghosts.images[self.menuspritesframe]
                if self.inky.rect.right == 0:
                    g.weak = True
                    self.pacman.key = K_RIGHT
                    g.direction = 'RIGHT'
                    self.spritesx = 1
                elif self.pacman.rect.left == 350:
                    g.weak = False
                    self.pacman.key = K_LEFT
                    g.direction = 'LEFT'
                    self.spritesx = -1
            if self.menuspritesframecount == 5:
                self.menuspritesframecount = -1
                self.menuspritesframe = 1 - self.menuspritesframe
            self.menuspritesframecount += 1
    def MenuDisplay(self):
        """Refresh what's on the menu screen

        """
        self.screen.blit(self.background, [0,0])
        self.screen.blit(self.firstplayermenu, [130,252])
        self.screen.blit(self.secondplayermenu, [130,280])
        self.screen.blit(self.fullscreenselect, [130,308])
        self.screen.blit(self.fullscreenchoose, [201,312])
        self.screen.blit(self.quitmenu, [130,336])
        self.screen.blit(self.title, [105,30])
        self.screen.blit(self.pacman.image, self.pacman.rect)
        self.ghostssprites.draw(self.screen)
        pygame.display.update()
    def Win(self):
        """Reset the variables and restarting the game when the player wins

        """
        for pac in self.pacman:
            pac.image = Pacman.images[4]
        pygame.time.delay(200)
        self.UpdateDisplay()
        for s in self.backsound1:
            s.stop()
        self.death = 0
        self.gpellets = 0
        self.pinky.updatepelletcount(self.gpellets)
        self.inky.updatepelletcount(self.gpellets)
        self.clyde.updatepelletcount(self.gpellets)
        self.createcounterbug = False
        self.screen.blit(self.background, [0,0])
        self.loadMisc()
        self.loadWallsPellets()
        self.RefreshMisc()
        pygame.mixer.Sound(os.path.join('Data','Sounds','start.wav')).play()
        self.screen.blit(self.starttext, [144, 240])
        pygame.display.update()
        pygame.time.delay(2500)
        self.loadSprites()
        pygame.display.update()
        pygame.time.delay(2500)
        self.backsoundchange = True
        self.BackSound()
        self.screen.blit(self.startclear, [144, 240])
        self.pellettime = pygame.time.get_ticks()
    def GameOverMed(self):
        """Return to the main menu when the player has no lives left

        """
        highscorefile = open('highscore.txt', 'w')
        highscorefile.write(str(self.highscore))
        highscorefile.close()
        self.gameover = True
        self.menu = 0
        self.MenuLoad()
        pygame.key.set_repeat(200,500)
    def DeathMed(self):
        """Reset the position of the sprites and minus one life

        """
        if self.lives == 0:
            self.GameOverMed()
            return
        self.death = 1
        self.lives -= 1
        self.gpellets = 0
        self.pinky.updatepelletcount(self.gpellets)
        self.inky.updatepelletcount(self.gpellets)
        self.clyde.updatepelletcount(self.gpellets)
        self.createcounterbug = False
        self.screen.blit(self.background, [0,0])
        self.loadMisc()
        self.RefreshMisc()
        pygame.mixer.Sound(os.path.join('Data','Sounds','start.wav')).play()
        self.screen.blit(self.starttext, [144, 240])
        pygame.display.update()
        pygame.time.delay(2500)
        self.loadSprites()
        pygame.display.update()
        pygame.time.delay(2500)
        self.screen.blit(self.startclear, [144, 240])
        self.backsoundchange = True
        self.BackSound()
        self.pellettime = pygame.time.get_ticks()
    def loadStuff(self):
        """Load things such as text and any miscellaneous images when starting the game

        """
        for i in range(4):
            self.point.append(pygame.image.load(os.path.join('Data','point' + str(i) +'.bmp')))
            self.point[i] = self.point[i].convert()
            self.point[i].set_colorkey((0,0,0))
        self.p1score = self._font.render("1UP", 0, (255,255,255))
        self.p1scorerect = self.p1score.get_rect(topleft =(48,0))
        self.p2score = self._font.render("2UP", 0, (255,255,255))
        self.p2scorerect = self.p2score.get_rect(topleft =(294,0))
        self.p1clear = pygame.Surface(self.p1score.get_size())
        self.p1clear = self.p1clear.convert()
        self.p1clear.fill((0,0,0))
        self.p2clear = pygame.Surface(self.p2score.get_size())
        self.p2clear = self.p2clear.convert()
        self.p2clear.fill((0,0,0))
        self.bxclear = pygame.Surface((20,20))
        self.bxclear = self.bxclear.convert()
        self.bxclear.fill((0,0,0))
        self.pscore1 = self._font.render("00", 1, (255,255,255))
        self.pscore1rect = self.pscore1.get_rect(topleft =(54,12))
        self.pscore2 = self._font.render("00", 1, (255,255,255))
        self.pscore2rect = self.pscore2.get_rect(topleft =(300,12))
        self.phigh = self._font.render(str(self.highscore), 1, (255,255,255))
        self.phighrect = self.phigh.get_rect(topleft =(164,12))
        self.pclear = pygame.Surface((768,12))
        self.pclear = self.pclear.convert()
        self.pclear.fill((0,0,0))
        self.highscoretitle = self._font.render("HIGH SCORE", 1, (255,255,255))
        self.highscoretitlerect = self.highscoretitle.get_rect(topleft =(140,0))
        self.starttext = self.startfont.render("READY!", 1, (255,255,0))
        self.startclear = pygame.Surface(self.starttext.get_size())
        self.startclear = self.startclear.convert()
        self.startclear.fill((0,0,0))
    def MainLoop(self):
        """Initialize the sprites, sounds, variables and any other miscellenous things then enter the main game loop
        """
        pygame.key.set_repeat(2,15)
        self.screen.blit(self.background, [0,0])
        self.lives = 2
        self.death = 0
        self.gpellets = 0
        self.score1 = 0
        self.score2 = 0
        self.bonus = None
        self.gameover = False
        self.createcounterbug = False   #Purposely create a variable to simulate a bug that occurs in the original Pacman
        self.loadStuff()
        self.loadMisc()
        self.loadWallsPellets()
        self.loadSounds()
        self.screen.blit(self.starttext, [144, 240])
        pygame.display.update()
        pygame.mixer.Sound(os.path.join('Data','Sounds','start.wav')).play()
        pygame.time.delay(2500)
        self.loadSprites()
        pygame.display.update()
        pygame.time.delay(2500)
        self.screen.blit(self.startclear, [144, 240])
        self.pellettime = pygame.time.get_ticks()
        #The main loop of the game
        while self.gameover == False:
            for ourevent in pygame.event.get():
                if ourevent.type == QUIT:
                    sys.exit()
                elif ourevent.type == KEYDOWN:
                    if ourevent.key == K_ESCAPE:
                        for s in self.backsound1:
                            s.stop()
                        self.GameOverMed()
                        return
                    for p in self.pacman:
                        if p.player == 1:
                            if ((ourevent.key == K_RIGHT)
                            or (ourevent.key == K_LEFT)
                            or (ourevent.key == K_UP)
                            or (ourevent.key == K_DOWN)):
                                p.move(ourevent.key)
                        elif p.player == 2:
                            if (ourevent.key == K_h):
                                p.move(K_RIGHT)
                            elif (ourevent.key == K_f):
                                p.move(K_LEFT)
                            elif (ourevent.key == K_t):
                                p.move(K_UP)
                            elif (ourevent.key == K_g):
                                p.move(K_DOWN)
            self.BackSound()
            self.blinky.updatepacman(self.pacman)   #Update positions of target for the ghosts
            self.pinky.updatepacman(self.pacman)
            self.inky.updatepacman(self.pacman)
            self.clyde.updatepacman(self.pacman)
            self.blinky.ghostcheck(self.clyde.incage)
            self.inky.ghostcheck(self.pinky.incage)
            self.inky.blinkyposition(self.blinky.rect.center)
            self.clyde.ghostcheck(self.inky.incage)
            self.pinky.pellettimecheck(pygame.time.get_ticks() - self.pellettime) #Check for the amount of time elapsed between eating a pellet
            self.inky.pellettimecheck(pygame.time.get_ticks() - self.pellettime)
            self.clyde.pellettimecheck(pygame.time.get_ticks() - self.pellettime)
            self.blinky.update(pygame.time.get_ticks())
            self.pinky.update(pygame.time.get_ticks())
            self.inky.update(pygame.time.get_ticks())
            self.clyde.update(pygame.time.get_ticks())
            self.pacman.update(pygame.time.get_ticks())
            self.BonusCheck()
            if self.score1 > self.highscore:
                self.highscore = self.score1
                self.phigh = self._font.render(str(self.highscore), 1, (255,255,255))
            elif self.score2 > self.highscore:
                self.highscore = self.score2
                self.phigh = self._font.render(str(self.highscore), 1, (255,255,255))
            self.UpdateDisplay()
            self.Pelletscollision()
            self.Bigpelletscollision()
            self.Ghostcollision()
    def BonusCheck(self):
        """Check if the player has collided with any bonus items and if so increase score

        """
        if self.pelletseaten == 70 or self.pelletseaten == 170:
            self.bonus = Bonus()
            self.bonustime = pygame.time.get_ticks() + 9500
        if self.bonus is not None and self.bonustime <= pygame.time.get_ticks():
            self.screen.blit(self.bxclear, self.bonus.rect)
            self.bonus = None
        elif self.bonus is not None and self.bonus.image != self.point[0]:
            for pac in self.pacman:
                if self.bonus.rect.center[1]/12 == pac.squarey and (self.bonus.rect.center[0]/12) == pac.squarex:
                    self.bonus.image = self.point[0]
                    self.bonussound.play()
                    if pac.player == 1:
                        self.score1 +=  200
                    elif pac.player == 2:
                        self.score2 +=  200
                    self.UpdateDisplay()
                    self.screen.blit(self.bxclear, self.bonus.rect)
                    self.bonustime = pygame.time.get_ticks()+1000
    def loadMisc(self):
        """Initialize miscellneous things

        """
        self.screen.blit(self.bclear, [0,410]) #Clear the amount of lives the player has and the bonus of each level
        for i in range(self.lives):
            self.livesimagerect.topleft = (24+(20*i), 410)
            self.screen.blit(self.livesimage, self.livesimagerect)
        self.screen.blit(self.fruit1, self.fruitrect)
        self.screen.blit(self.highscoretitle,self.highscoretitlerect)
        self.screen.blit(self.p1score,self.p1scorerect)
        self.screen.blit(self.p2score,self.p2scorerect)
        self.screen.blit(self.pscore1, self.pscore1rect)
        self.screen.blit(self.pscore2, self.pscore2rect)

    def loadSounds(self):
        """Initialize the sounds by preloading them into memory

        """
        self.backsound1 = []
        self.backsoundnum = 0
        self.backsoundchange = True
        self.pacmaneatsounddelay = 0
        self.pacmaneat1 = pygame.mixer.Sound(os.path.join('Data','Sounds','eat1.wav'))
        self.pacmaneat2 = pygame.mixer.Sound(os.path.join('Data','Sounds','eat2.wav'))
        self.deathsound = pygame.mixer.Sound(os.path.join('Data','Sounds','death.wav'))
        self.bonussound = pygame.mixer.Sound(os.path.join('Data','Sounds','bonus.wav'))
        self.pacmandeathsound = pygame.mixer.Sound(os.path.join('Data','Sounds','deathsound.wav'))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','siren1.wav')))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','siren2.wav')))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','siren3.wav')))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','siren4.wav')))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','siren5.wav')))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','bigpellet1.wav')))
        self.backsound1.append(pygame.mixer.Sound(os.path.join('Data','Sounds','hit1.wav')))
        self.pacmaneat = 0
        self.eatdelaystop = 0
    def loadSprites(self):
        """Initialize the sprites

        """
        self.pacman = pygame.sprite.RenderUpdates() #Group sprite used as it allows for the addition of a multiplayer feature
        self.pacman.add(Pacman((168,318),1))
        if self.players == 2:
            self.pacman.add(Pacman((168,246),2))
        if self.death == 0:
            self.blinky = Blinky()
            self.pinky = Pinky()
            self.clyde = Clyde()
            self.inky = Inky()
        elif self.death == 1:
            self.blinky = Blinky(1)
            self.pinky = Pinky(1)
            self.clyde = Clyde(1)
            self.inky = Inky(1)
        self.ghostssprites = pygame.sprite.RenderUpdates()
        self.ghostssprites.add(self.blinky)
        self.ghostssprites.add(self.pinky)
        self.ghostssprites.add(self.clyde)
        self.ghostssprites.add(self.inky)
        self.pacman.draw(self.screen)
        self.ghostssprites.draw(self.screen)
    def loadWallsPellets(self):
        """Mapping out the walls and pellets onto the grid

        """
        self.walls = pygame.sprite.Group()
        self.refreshwalls = pygame.sprite.RenderUpdates()
        self.pellets = pygame.sprite.RenderUpdates()
        self.bigpellets = pygame.sprite.RenderUpdates()
        xoffset = 0
        yoffset = 0
        #Adding items to the grid
        for y in range(self.nnumy):
            for x in range(self.nnumx):
                if gridmap[y][x] == 15:
                    self.pellets.add(Pellets([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))]))
                elif gridmap[y][x] == 16:
                    self.bigpellets.add(BigPellets([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))]))
                elif gridmap[y][x] == 38:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],10))
                elif gridmap[y][x] == 37:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],1))
                elif gridmap[y][x] == 39:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],0))
                elif gridmap[y][x] == 32:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],12))
                elif gridmap[y][x] == 31:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],5))
                elif gridmap[y][x] == 33:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],4))
                elif gridmap[y][x] == 34:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],3))
                elif gridmap[y][x] == 36:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],2))
                elif gridmap[y][x] == 47:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],41))
                elif gridmap[y][x] == 49:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],42))
                elif gridmap[y][x] == 41:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],7))
                elif gridmap[y][x] == 43:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],6))
                elif gridmap[y][x] == 44:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],9))
                elif gridmap[y][x] == 46:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],8))
                elif gridmap[y][x] == 26:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],24))
                elif gridmap[y][x] == 24:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],23))
                elif gridmap[y][x] == 27:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],38))
                elif gridmap[y][x] == 29:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],37))
                elif gridmap[y][x] == 21:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],26))
                elif gridmap[y][x] == 23:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],25))
                elif gridmap[y][x] == 28:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],20))
                elif gridmap[y][x] == 22:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],14))
                elif gridmap[y][x] == 25:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],43))
                elif gridmap[y][x] == 59:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],27))
                elif gridmap[y][x] == 57:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],28))
                elif gridmap[y][x] == 51:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],30))
                elif gridmap[y][x] == 53:
                    self.walls.add(Walls([(xoffset+x*(336/28)),(yoffset+y*(432/len(gridmap)))],29))
        for w in self.walls.sprites():
            self.screen.blit(w.image, w.rect)
            #Adding walls that are required to be further refreshed into this list
            if w.id == 43:
                self.refreshwalls.add(w) 
        self.pellets.draw(self.screen)
        self.bigpellets.draw(self.screen)
    def RefreshMisc(self):
        """Refresh the walls and pellets

        """
        for w in self.walls.sprites():
            self.screen.blit(w.image, w.rect)
        self.pellets.draw(self.screen)
        self.bigpellets.draw(self.screen)
    def UpdateDisplay(self):
        """Update sprite locations on the screen

        """
        if self._pelletsdelay < pygame.time.get_ticks():
            self._pelletsblink = 1 - self._pelletsblink
            self._pelletsdelay = pygame.time.get_ticks() + 250
        if self._pelletsblink == 0:
            self.bigpellets.clear(self.screen, self.background)
            self.screen.blit(self.p1clear,self.p1scorerect)
            self.screen.blit(self.p2clear,self.p2scorerect)
        elif self._pelletsblink == 1:
            self.bigpellets.draw(self.screen)
            self.screen.blit(self.p1score,self.p1scorerect)
            self.screen.blit(self.p2score,self.p2scorerect)
        self.screen.blit(self.pclear, self.pscore1rect)
        self.screen.blit(self.pscore1, self.pscore1rect)
        self.screen.blit(self.pscore2, self.pscore2rect)
        self.screen.blit(self.phigh, self.phighrect)
        if self.bonus is not None:
            self.screen.blit(self.bonus.image, self.bonus.rect)
        self.refreshwalls.draw(self.screen)
        self.pacman.clear(self.screen, self.background)
        self.ghostssprites.clear(self.screen, self.background)
        self.pellets.draw(self.screen)
        self.pacman.draw(self.screen)
        self.ghostssprites.draw(self.screen)
        pygame.display.update()
    def BackSound(self):
        """Play background music/sounds

        """
        if (self.CheckWeak() == False and self.backsoundnum == 5) or (self.CheckHit() == False and self.backsoundnum == 6):
            self.backsoundchange = True
        if self.pelletseaten == 1 or self.pelletseaten == 48 or self.pelletseaten == 96 or self.pelletseaten == 144 or self.pelletseaten == 192:
            self.backsoundchange = True
        if self.pelletseaten >=0:
            self.backsoundnum = 0
        if self.pelletseaten >=48:
            self.backsoundnum = 1
        if self.pelletseaten >=96:
            self.backsoundnum = 2
        if self.pelletseaten >=144:
            self.backsoundnum = 3
        if self.pelletseaten >=192:
            self.backsoundnum = 4
        if self.CheckWeak() == True:
            self.backsoundnum = 5
        if self.CheckHit() == True:
            self.backsoundnum = 6
        if self.backsoundchange == True:
            for s in self.backsound1:       #Stop all music that's currently playing
                s.stop()
            self.backsound1[self.backsoundnum].play(loops=-1)  #play selected music
            self.backsoundchange = False
    def CheckHit(self):
        """Check if a ghost has been eaten by pacman and if so change background music

        """
        for g in self.ghostssprites:
            if g.hit == True:
                self.backsoundchange = True
                return True
        return False
    def CheckWeak(self):
        """Check if Pacman has eaten a big pellet and if so change background music

        """
        for g in self.ghostssprites:
            if g.weak == True:
                self.backsoundchange = True
                return True
        return False
    def PacSound(self, time):
        """Play sounds produced by pacman when eating pellets
        time - pygame.time.get_ticks()

        """
        if self.pacmaneatsounddelay < time:
            if self.pacmaneat == 0:
                self.pacmaneat2.stop()
                self.pacmaneat1.play()
            else:
                self.pacmaneat1.stop()
                self.pacmaneat2.play()
            self.pacmaneat = 1 - self.pacmaneat #Change pellet eating sound
            self.pacmaneatsounddelay = time + 115
    def Pelletscollision(self):
        """Handling pellets collision

        """
        for pac in self.pacman:
            for p in self.pellets:
                if p.rect.center[1]/12 == pac.squarey and (p.rect.center[0]/12) == pac.squarex:
                    p.kill()
                    if pac.player == 1:
                        self.score1 +=  10
                        self.pscore1 = self._font.render(str(self.score1), 1, (255,255,255))
                    elif pac.player == 2:
                        self.score2 +=  10
                        self.pscore2 = self._font.render(str(self.score2), 1, (255,255,255))
                    #Count the number of pellets pacman has eaten
                    self.pelletseaten +=1
                    #Number of pellets used for the ghost exit house counter after death
                    if self.gpellets == 32 and self.clyde.incage == False:
                        self.createcounterbug = True
                    self.gpellets += 1
                    if self.createcounterbug == True:
                        self.gpellets = 0
                    self.pellettime = pygame.time.get_ticks()
                    self.blinky.updatepelletcount(self.pelletseaten)
                    self.pinky.updatepelletcount(self.gpellets)
                    self.inky.updatepelletcount(self.gpellets)
                    self.clyde.updatepelletcount(self.gpellets)
                    self.blinky.adjustspeed()
                    self.PacSound(pygame.time.get_ticks())
                    self.CheckWin()
    def Bigpelletscollision(self):
        """Checking if pacman is on top of a big pellet and adjust game mechanics accordingly

        """
        for pac in self.pacman:
            for p in self.bigpellets:
                if p.rect.center[1]/12 == pac.squarey and (p.rect.center[0]/12) == pac.squarex:
                    p.kill()
                    if pac.player == 1:
                        self.score1 +=  50
                        self.pscore1 = self._font.render(str(self.score1), 1, (255,255,255))
                    elif pac.player == 2:
                        self.score2 +=  50
                        self.pscore2 = self._font.render(str(self.score2), 1, (255,255,255))
                    self.row = 0
                    self.PacSound(pygame.time.get_ticks())
                    self.CheckWin()
                    self.blinky.bigpellets(pygame.time.get_ticks())
                    self.pinky.bigpellets(pygame.time.get_ticks())
                    self.inky.bigpellets(pygame.time.get_ticks())
                    self.clyde.bigpellets(pygame.time.get_ticks())
    def CheckWin(self):
        """Check if all the pellets have been eaten

        """
        if len(self.bigpellets)+len(self.pellets) <= 0:
            self.Win()
    def Ghostcollision(self):
        """Handling collisions with ghosts

        """
        for pac in self.pacman:
            for g in self.ghostssprites:
                if g.rect.center[1]/12 == pac.squarey and (g.rect.center[0]/12) == pac.squarex:
                    if g.weak == True:
                        if g.hit == False:
                            self.row += 1
                            pac.image = self.bxclear
                            if pac.player == 1:
                                self.score1 += 200*2**(self.row-1)
                                self.pscore1 = self._font.render(str(self.score1), 1, (255,255,255))
                            elif pac.player == 2:
                                self.score2 += 200*2**(self.row-1)
                                self.pscore2 = self._font.render(str(self.score2), 1, (255,255,255))
                            g.image = self.point[self.row-1]
                            self.UpdateDisplay()
                            pygame.time.delay(500)
                            g.hit = True
                            g.weak = False
                            g.oppdirect()
                    elif g.weak == False and g.hit == False and len(self.pacman) == 2:
                        frame = 5
                        while frame <= 15:
                            pac.deathanim(frame)
                            self.UpdateDisplay()
                            frame+= 1
                            pygame.time.delay(200)
                        pac.kill()
                    elif g.weak == False and g.hit == False and len(self.pacman) <= 1:
                        #stop BackGround music
                        for s in self.backsound1:
                            s.stop()
                        pygame.time.delay(500)
                        self.deathsound.play()
                        self.screen.blit(self.bxclear, [158,236])
                        self.ghostssprites.clear(self.screen, self.background)
                        self.ghostssprites = pygame.sprite.RenderUpdates()
                        self.UpdateDisplay()
                        frame = 5
                        while frame <= 15:
                            pac.deathanim(frame)
                            self.UpdateDisplay()
                            frame+= 1
                            pygame.time.delay(200)
                        self.pacmandeathsound.play(loops=1)
                        pygame.time.delay(400)
                        pac.kill()
                        self.DeathMed()
                        
class Ghosts(pygame.sprite.Sprite):
    """Creating the top level ghost class which accounts for all the enemies in the game

    """
    imagesloaded = False
    images = []
    def __init__(self, death):
        pygame.sprite.Sprite.__init__(self)
        self.pacman = pygame.sprite.RenderUpdates()
        self.pacman.add(Pacman((168,318)))
        if Ghosts.imagesloaded == False:        #Preload the images to reduce cpu usage in game
            Ghosts.imagesloaded = True
            for i in range(12):
                im = pygame.image.load(os.path.join('Data','sghost' + str(i) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Ghosts.images.append(im)
        self.pelletsnum = 0
        self.weak = False
        self.ghostcage = True
        self.delaytime = 0
        self.initspeed = 16
        self.speed = 16
        self.weakframanim = 0
        self.moveanimframe = 0
        self.moveanimdelay = 0
        self.scatter = True
        self.pcheck = False     #Cage exit pellet timer
        self.scattercount = 1
        self.death = death
        self.scatterchasetime = pygame.time.get_ticks()+2500
        self.weakanimdelay = 0
        self.weakframe = 0
        self.hit = False
    def scatterchase(self):
        """Updates the scatter and chase timer and puts the ghosts in either scatter mode or chase mode accordingly

        """
        if (self.scatterchasetime+7000) <= pygame.time.get_ticks() and self.scatter == True and self.scattercount <= 2:
            self.scatter = False
            self.scatterchasetime = pygame.time.get_ticks()
        elif (self.scatterchasetime+5000) <= pygame.time.get_ticks() and self.scatter == True and self.scattercount > 2:
            self.scatter = False
            self.scatterchasetime = pygame.time.get_ticks()
        elif self.scatter == False and (self.scatterchasetime+20000) <= pygame.time.get_ticks() and self.scattercount <=4:
            self.scatter = True
            self.oppdirect()
            self.scattercount += 1
            self.scatterchasetime = pygame.time.get_ticks()
    def bigpellets(self, time):
        """Adjusts the properties of the ghosts accordingly when a big pellet has been eaten
        time - pygame.time.get_ticks()
        """
        if self.weak == True:       #Check if two big pellets were eaten before the previous big pellet's effects were over and adjust scatter chase time accordingly
            self.scatterchasetime -= 7000 - (pygame.time.get_ticks()-self.weaktimestart)
        self.weak = True
        self.scatterchasetime += 7000
        self.pcheck = False
        self.weaktimestart = time
        self.oppdirect()
        self.weakanim()
    def weakanim(self):
        """Animations for when a big pellet is eaten

        """
        if pygame.time.get_ticks() - self.weaktimestart < 4000:
            self.weakframanim = 0
        elif pygame.time.get_ticks() - self.weaktimestart >= 4000:
            if self.weakanimdelay < pygame.time.get_ticks():
                if self.weakframe == 1:
                    self.weakframanim = 2
                else:
                    self.weakframanim = 0
                self.weakframe = 1-self.weakframe
                self.weakanimdelay = pygame.time.get_ticks()+200
        if pygame.time.get_ticks() - self.weaktimestart >= 6000:
            self.weak = False
            self.moveanim()
        if self.moveanimdelay <= pygame.time.get_ticks():
            self.moveanimframe = 1-self.moveanimframe
            self.moveanimdelay = pygame.time.get_ticks()+100
        self.image = Ghosts.images[self.weakframanim+self.moveanimframe]
    def ongrid(self):
        """Check if the ghost's current position is a valid place to make a turn

        """
        if (self.rect.topleft[0]%12 == 9) and (self.rect.topleft[1]%12 == 8):
            return True
        return False
    def intunnel(self):
        """Checks if the ghosts are in the tunnel if so their speed is halved

        """
        if self.rect[0]/12 <= -1 or self.rect[0]/12 >=27:
            self.speed = self.initspeed*2
            return True
        elif gridmap[self.rect.center[1]/12][self.rect.center[0]/12] == 17:
            self.speed = self.initspeed*2
            return True
        else:
            self.speed = self.initspeed
            return False
    def move(self):
        """Move the ghosts

        """
        if self.direction == 'LEFT':
            self.rect.move_ip(-1,0)
        elif self.direction == 'RIGHT':
            self.rect.move_ip(1,0)
        elif self.direction == 'UP':
            self.rect.move_ip(0,-1)
        elif self.direction == 'DOWN':
            self.rect.move_ip(0,1)
    def tunnelcheck(self):
        """Teleport ghosts when they reach the end of the tunnel

        """
        if self.rect[0] == -27:
            self.rect[0] = 344
        elif self.rect[0] == 345:
            self.rect[0] = -26
    def collision(self):
        """Check to see if the ghost will collide with any of the walls

        """
        rectcheck = self.rect
        rectcheckx = self.rect[0]/12
        rectchecky = self.rect[1]/12
        if self.direction == 'LEFT':
            rectcheckx = (rectcheck.center[0]-8)/12
            rectchecky = (rectcheck.center[1])/12
        if self.direction == 'RIGHT':
            rectcheckx = (rectcheck.center[0]+5)/12
            rectchecky = (rectcheck.center[1])/12
        if self.direction == 'UP':
            rectcheckx = (rectcheck.center[0])/12
            rectchecky = (rectcheck.center[1]-11)/12
        if self.direction == 'DOWN':
            rectcheckx = (rectcheck.center[0])/12
            rectchecky = (rectcheck.center[1]+10)/12
        if gridmap[rectchecky][rectcheckx] < 20:
            return False
        return True
    def ghostcheck(self, check):
        """Checks if the given ghost is inside the cage

        """
        self.ghostcage = check
    def moveupdown(self):
        """Force the ghosts to move up and down

        """
        if self.direction == ('LEFT' or 'RIGHT'):
            self.direction = 'UP'
            self.nextturn = 'UP'
        if self.collision() == False:
            self.move()
        elif self.collision() == True:
            if self.direction == 'UP':
                self.direction = 'DOWN'
            elif self.direction == 'DOWN':
                self.direction = 'UP'
    def pickturn(self):
        """Decides which direction the ghost should take next

        """
        if self.weak == False or self.hit == True:
            self.nextturn = self.checkdirection((self.rect.center[0]/12,self.rect.center[1]/12))
        elif self.weak == True:
            self.nextturn = self.randomturn((self.rect.center[0]/12,self.rect.center[1]/12))
    def randomturn(self, gridloc):
        """Make a random turn
        gridloc - rect of the ghost
        """
        turn = random.randint(0,3)
        if self.rect.center[0]/12 <= -1:
            self.tunnelcheck()
            return self.direction
        if self.rect.center[0]/12 >= 27:
            self.tunnelcheck()
            return self.direction
        if turn == 0:
            if gridmap[gridloc[1]][gridloc[0]-1] < 20 and self.direction != 'RIGHT':
                return 'LEFT'
            else:
                return self.randomturn(gridloc)
        elif turn == 1:
            if gridmap[gridloc[1]-1][gridloc[0]] < 20 and self.direction != 'DOWN':
                return 'UP'
            else:
                return self.randomturn(gridloc)
        elif turn == 2:
            if gridmap[gridloc[1]][gridloc[0]+1] < 20 and self.direction != 'LEFT':
                return 'RIGHT'
            else:
                return self.randomturn(gridloc)
        elif turn == 3:
            if gridmap[gridloc[1]+1][gridloc[0]] < 20 and self.direction != 'UP':
                return 'DOWN'
            else:
                return self.randomturn(gridloc)
    def checkdirection(self, gridloc):
        """Calculates distance from the target for the ghost to know which turn to take next
        gridloc - rect of the ghost
        """
        dtopac = 999
        turn = None
        for p in self.pacman:
            if self.rect.center[0]/12 <= -1:
                self.tunnelcheck()
                return self.direction
            if self.rect.center[0]/12 >= 27:
                self.tunnelcheck()
                return self.direction
            if (abs((p.squarex - gridloc[0]))+abs((p.squarey - (gridloc[1]-1)))) < dtopac and self.direction != 'DOWN':
                if gridmap[gridloc[1]-1][gridloc[0]] < 20:
                    dtopac = (abs((p.squarex - gridloc[0]))+abs((p.squarey - (gridloc[1]-1))))
                    turn = 'UP'
            if (abs((p.squarex - (gridloc[0]-1)))+abs((p.squarey - gridloc[1]))) < dtopac and self.direction != 'RIGHT':
                if gridmap[gridloc[1]][gridloc[0]-1] < 20:
                    dtopac = (abs((p.squarex - (gridloc[0]-1)))+abs((p.squarey - gridloc[1])))
                    turn = 'LEFT'
            if (abs((p.squarex - gridloc[0]))+abs((p.squarey - (gridloc[1]+1)))) < dtopac and self.direction != 'UP':
                if gridmap[gridloc[1]+1][gridloc[0]] < 20:
                    dtopac = (abs((p.squarex - gridloc[0]))+abs((p.squarey - (gridloc[1]+1))))
                    turn = 'DOWN'
            if (abs((p.squarex - (gridloc[0]+1)))+abs((p.squarey - gridloc[1]))) < dtopac and self.direction != 'LEFT':
                if gridmap[gridloc[1]][gridloc[0]+1] < 20:
                    dtopac = (abs((p.squarex - (gridloc[0]+1)))+abs((p.squarey - gridloc[1])))
                    turn = 'RIGHT'
        return turn
    def updatepacman(self, pacman):
        """Updates target location
        pacman - the pacman sprite the player is controlling
        """
        self.pacman = pacman
        if self.hit == True:
            self.pacman = pygame.sprite.RenderUpdates()
            self.pacman.add(Pacman((168,174)))
        elif self.scatter == True:
            self.pacman = pygame.sprite.RenderUpdates()
            self.pacman.add(Pacman((self.scatterrect)))
    def oppdirect(self):
        """Reverse the ghost's current facing position

        """
        if self.direction == 'UP':
            self.nextturn = 'DOWN'
        elif self.direction == 'DOWN':
            self.nextturn = 'UP'
        elif self.direction == 'LEFT':
            self.nextturn = 'RIGHT'
        elif self.direction == 'RIGHT':
            self.nextturn = 'LEFT'
    def updatepelletcount(self, pellets):
        """Update the number of pellets eaten
        pellets - number of pellets eaten
        """
        self.pelletsnum = pellets
    def pellettimecheck(self, time):
        """Update the amount of time elapsed between eating a pellet
        time - pygame.time.get_ticks()
        """
        self.ptime = time
    def moveanim(self):
        """Animate the ghosts when they are moving

        """
        if self.hit == False:
            if self.direction == 'LEFT':
                self.image = self.images[4+self.moveanimframe]
            elif self.direction == 'UP':
                self.image = self.images[6+self.moveanimframe]
            elif self.direction == 'DOWN':
                self.image = self.images[2+self.moveanimframe]
            elif self.direction == 'RIGHT':
                self.image = self.images[0+self.moveanimframe]
        if self.hit == True:
            if self.direction == 'LEFT':
                self.image = Ghosts.images[8+self.moveanimframe]
            elif self.direction == 'UP':
                self.image = Ghosts.images[10+self.moveanimframe]
            elif self.direction == 'DOWN':
                self.image = Ghosts.images[6+self.moveanimframe]
            elif self.direction == 'RIGHT':
                self.image = Ghosts.images[4+self.moveanimframe]
        if self.moveanimdelay <= pygame.time.get_ticks():
            self.moveanimframe = 1-self.moveanimframe
            self.moveanimdelay = pygame.time.get_ticks()+100
class Blinky(Ghosts):
    """The red ghost
    time - pygame.time.get_ticks()

    """
    imagesloaded = False
    images = []
    def __init__(self,death=0):
        Ghosts.__init__(self,death)
        if Blinky.imagesloaded == False:
            Blinky.imagesloaded = True
            for i in range(8):
                im = pygame.image.load(os.path.join('Data','rghost' + str(i) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Blinky.images.append(im)
        self.image = Blinky.images[4]
        self.rect = self.image.get_rect()
        self.rect.center = (168,174)
        self.incage = False
        self.scatterrect = (306,96)
        self.direction = 'LEFT'
        self.nextturn = 'LEFT'
    def update(self,time):
        """Update the Blinky's position and other properties

        """
        self.scatterchase()
        if self.incage == True and self.delaytime < time:
            self.exitproc()
            self.delaytime = time+20
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
        if self.delaytime < time and self.incage == False:
            self.direction = self.nextturn
            self.inprocess()
            self.move()
            if self.ongrid() == True:
                self.pickturn()
                self.intunnel()
            if self.hit == True:
                self.delaytime = time+self.speed/4
            elif self.weak == True:
                self.delaytime = time+self.speed*2
            else:
                self.delaytime = time+self.speed
    def adjustspeed(self):
        """Adjust the speed of Blinky accordingly

        """
        if self.ghostcage == False and (240 - self.pelletsnum) <= 20 and (240 - self.pelletsnum) >10 :
            self.initspeed = 12
            self.speed = 12
        elif self.ghostcage == False and (240 - self.pelletsnum) <= 10:
            self.initspeed = 11
            self.speed = 11
        elif self.ghostcage == True and self.intunnel() == False:
            self.initspeed = 16
            self.speed = 16
    def exitproc(self):
        """Process executed when exiting the cage

        """
        if self.rect.center != (168,174):
            self.direction ='UP'
            self.move()
        elif self.rect.center == (168,174):
            self.pickturn()
            self.incage = False
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
    def inprocess(self):
        """Process executed when going into the cage

        """
        if self.rect.center == (168,174) and self.hit == True:
            if self.rect.center != (168,209):
                self.direction = 'DOWN'
                self.nextturn = 'DOWN'
        elif self.rect.center == (168,209) and self.hit == True:
            self.hit = False
            self.incage = True
    def updatepacman(self, pacman):
        """Blinky's own target location method to prevent him from going to his corner when scatter mode occurs when his speed has increased

        """
        self.pacman = pacman
        if self.hit == True:
            self.pacman = pygame.sprite.RenderUpdates()
            self.pacman.add(Pacman((168,174)))
        elif self.scatter == True and self.initspeed >= 16:
            self.pacman = pygame.sprite.RenderUpdates()
            self.pacman.add(Pacman((self.scatterrect)))
class Pinky(Ghosts):
    """The pink ghost
    time - pygame.time.get_ticks()

    """
    imagesloaded = False
    images = []
    def __init__(self,death=0):
        Ghosts.__init__(self,death)
        if Pinky.imagesloaded == False:
            Pinky.imagesloaded = True
            for i in range(8):
                im = pygame.image.load(os.path.join('Data','pghost' + str(i) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Pinky.images.append(im)
        self.image = Pinky.images[2]
        self.incage = True
        self.rect = self.image.get_rect()
        self.rect.center = (168,210)
        if self.death == 0:     #Check to see if pacman has died once
            self.owndotcount = 0
        else:
            self.owndotcount = 7
        self.scatterrect = (72,6)
        self.ptime = 0
        self.pelletimer = 4000
        self.direction = 'LEFT'
        self.nextturn = 'LEFT'
    def update(self,time):
        """Update Pinky's position and various other properties

        """
        self.scatterchase()
        if self.incage == True:
            self.pelletimecheck()
        if self.incage == True and self.exitcheck() == True and self.delaytime < time:
            self.exitproc()
            self.delaytime = time+20
        if self.delaytime < time and self.exitcheck() == False and self.incage == True:
            self.moveupdown()
            self.delaytime = time+self.speed
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
        if self.delaytime < time and self.incage == False:
            self.direction = self.nextturn
            self.inprocess()
            self.move()
            if self.ongrid() == True:
                if self.hit == 0 and self.weak == 0:
                    self.ownturn()
                else:
                    self.pickturn()
                self.intunnel()
            if self.hit == True:
                self.delaytime = time+self.speed/4
            elif self.weak == True:
                self.delaytime = time+self.speed*2
            else:
                self.delaytime = time+self.speed
    def exitproc(self):
        if self.rect.center != (168,174):
            self.direction ='UP'
            self.move()
        elif self.rect.center == (168,174):
            self.pickturn()
            self.incage = False
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
    def pelletimecheck(self):
        """Check if the time passed between eating pellets has exceeded

        """
        if self.ptime >= 4000:
            self.pcheck = True
    def exitcheck(self):
        if self.pelletsnum >= self.owndotcount or self.pcheck:
            return True
        return False
    def inprocess(self):
        if self.rect.center == (168,174) and self.hit == True:
            if self.rect.center != (168,209):
                self.direction = 'DOWN'
                self.nextturn = 'DOWN'
        elif self.rect.center == (168,209) and self.hit == True:
            self.hit = False
            self.incage = True
    def ownturn(self):
        """Decides which turn Pinky would take at an intersection by calculating the closest path to a target position.
            Target position is the direction Pacman is facing plus 4 squares in that direction with the exception of Pacman
            facing up.

        """
        dtopac = 999
        gridloc = (self.rect.center[0]/12, self.rect.center[1]/12)
        for p in self.pacman:
            if self.rect.center[0]/12 <= -1:
                self.tunnelcheck()
                self.nextturn = self.direction
                return
            if self.rect.center[0]/12 >= 27:
                self.tunnelcheck()
                self.nextturn = self.direction
                return
            #Check which direction pacman is facing and assign appropriate square of target
            if p.key == K_LEFT:
                px = p.squarex - 4
                py = p.squarey
            elif p.key == K_RIGHT:
                px = p.squarex + 4
                py = p.squarey
            elif p.key == K_UP:
                px = p.squarex - 4
                py = p.squarey - 4
            elif p.key == K_DOWN:
                px = p.squarex
                py = p.squarey + 4
            if px < 0:
                px = 0
            elif px > 28:
                px = 28
            if py < 0:
                py = 0
            elif py > 36:
                py = 36
            if (abs((px - gridloc[0]))+abs((py - (gridloc[1]-1)))) < dtopac and self.direction != 'DOWN':
                if gridmap[gridloc[1]-1][gridloc[0]] < 20:
                    dtopac = (abs((px - gridloc[0]))+abs((py - (gridloc[1]-1))))
                    self.nextturn = 'UP'
            if (abs((px - (gridloc[0]-1)))+abs((py - gridloc[1]))) < dtopac and self.direction != 'RIGHT':
                if gridmap[gridloc[1]][gridloc[0]-1] < 20:
                    dtopac = (abs((px - (gridloc[0]-1)))+abs((py - gridloc[1])))
                    self.nextturn = 'LEFT'
            if (abs((px - gridloc[0]))+abs((py - (gridloc[1]+1)))) < dtopac and self.direction != 'UP':
                if gridmap[gridloc[1]+1][gridloc[0]] < 20:
                    dtopac = (abs((px - gridloc[0]))+abs((py - (gridloc[1]+1))))
                    self.nextturn = 'DOWN'
            if (abs((px - (gridloc[0]+1)))+abs((py - gridloc[1]))) < dtopac and self.direction != 'LEFT':
                if gridmap[gridloc[1]][gridloc[0]+1] < 20:
                    dtopac = (abs((px - (gridloc[0]+1)))+abs((py - gridloc[1])))
                    self.nextturn = 'RIGHT'
class Inky(Ghosts):
    """The blue ghost
    time - pygame.time.get_ticks()

    """
    imagesloaded = False
    images = []
    def __init__(self,death=0):
        Ghosts.__init__(self,death)
        if Inky.imagesloaded == False:
            Inky.imagesloaded = True
            for i in range(8):
                im = pygame.image.load(os.path.join('Data','bghost' + str(i) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Inky.images.append(im)
        self.image = Inky.images[6]
        self.rect = self.image.get_rect()
        self.rect.center = (144,210)
        self.incage = True
        if self.death == 0:
            self.owndotcount = 30
        else:
            self.owndotcount = 17
        self.blinky = (168, 174)
        self.scatterrect = (330,414)
        self.inprocesscheck = False
        self.ptime = 0
        self.ptimeminus = 0
        self.pelletimer = 4000
        self.direction = 'LEFT'
        self.nextturn = 'LEFT'
    def update(self,time):
        """Update Inky's position and various other properties

        """
        self.scatterchase()
        if self.incage == True:
            self.pelletimecheck()
        if self.delaytime < time and self.exitcheck() == False and self.incage == True:
            self.moveupdown()
            self.delaytime = time+self.speed
        if self.incage == True and self.exitcheck() == True and self.delaytime < time:
            self.exitproc()
            self.delaytime = time+20
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
        if self.delaytime < time and self.incage == False:
            self.direction = self.nextturn
            self.inprocess()
            self.move()
            if self.ongrid() == True:
                if self.hit == False and self.weak == False and self.scatter == False:
                    self.ownturn()
                else:
                    self.pickturn()
                self.intunnel()
            if self.hit == True:
                self.delaytime = time+self.speed/4
            elif self.weak == True:
                self.delaytime = time+self.speed*2
            else:
                self.delaytime = time+self.speed
    def exitproc(self):
        if self.rect.center != (168,174):
            self.direction ='UP'
            if self.rect.center[0] != 168:
                self.direction = 'RIGHT'
            self.move()
        elif self.rect.center == (168,174):
            self.pickturn()
            self.incage = False
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
    def exitcheck(self):
        if self.pelletsnum >= self.owndotcount:
            return True
        if self.pcheck:
            return True
        return False
    def ghostcheck(self, check):
        """Check if Pinky's in the cage

        """
        if self.ghostcage == True and check == False:
            self.ptimeminus = self.ptime
        self.ghostcage = check
        if self.ptime - self.ptimeminus < 0:
            self.ptimeminus = 0
    def updatepelletcount(self, pelletsnum):
        if self.ghostcage == False and self.death == 0:
            self.pelletsnum += 1
        else:
            self.pelletsnum = pelletsnum
    def pelletimecheck(self):
        if self.ptime - self.ptimeminus >= self.pelletimer and self.ghostcage == False:
            self.pcheck = True
    def inprocess(self):
        if self.rect.center == (168,174) and self.hit == True:
            self.inprocesscheck = True
            if self.rect.center[1] !=210:
                    self.direction = 'DOWN'
                    self.nextturn = 'DOWN'
        if self.rect.center[0] !=143 and self.rect.center[1] == 210 and self.inprocesscheck == True and self.hit == True:
                self.direction = 'LEFT'
        elif self.rect.center == (143,210) and self.hit == True:
            self.hit = False
            self.incage = True
            self.inprocesscheck = False
    def blinkyposition(self,blinky):
        self.blinky = blinky
    def ownturn(self):
        """Decides which turn Inky would take at an intersection by calculating the closest path to the target position.
            The target position is two times the eucludian distance from two spaces ahead of the direction the player is facing minus the current position of Blinky

        """
        dtopac = 999
        gridloc = (self.rect.center[0]/12, self.rect.center[1]/12)
        for p in self.pacman:
            if self.rect.center[0]/12 <= -1:
                self.tunnelcheck()
                self.nextturn = self.direction
                return
            if self.rect.center[0]/12 >= 27:
                self.tunnelcheck()
                self.nextturn = self.direction
                return
            #Check which direction pacman is facing and assign appropriate square of target
            if p.key == K_LEFT:
                px = p.squarex - 2
                py = p.squarey
            elif p.key == K_RIGHT:
                px = p.squarex + 2
                py = p.squarey
            elif p.key == K_UP:
                px = p.squarex - 2
                py = p.squarey - 2
            elif p.key == K_DOWN:
                px = p.squarex
                py = p.squarey + 2
            px = px + abs(self.blinky[0]/12 - px)
            py = py + abs(self.blinky[1]/12 - py)
            if px < 0:
                px = 0
            elif px > 28:
                px = 28
            if py < 0:
                py = 0
            elif py > 36:
                py = 36
            if (abs((px - gridloc[0]))+abs((py - (gridloc[1]-1)))) < dtopac and self.direction != 'DOWN':
                if gridmap[gridloc[1]-1][gridloc[0]] < 20:
                    dtopac = (abs((px - gridloc[0]))+abs((py - (gridloc[1]-1))))
                    self.nextturn = 'UP'
            if (abs((px - (gridloc[0]-1)))+abs((py - gridloc[1]))) < dtopac and self.direction != 'RIGHT':
                if gridmap[gridloc[1]][gridloc[0]-1] < 20:
                    dtopac = (abs((px - (gridloc[0]-1)))+abs((py - gridloc[1])))
                    self.nextturn = 'LEFT'
            if (abs((px - gridloc[0]))+abs((py - (gridloc[1]+1)))) < dtopac and self.direction != 'UP':
                if gridmap[gridloc[1]+1][gridloc[0]] < 20:
                    dtopac = (abs((px - gridloc[0]))+abs((py - (gridloc[1]+1))))
                    self.nextturn = 'DOWN'
            if (abs((px - (gridloc[0]+1)))+abs((py - gridloc[1]))) < dtopac and self.direction != 'LEFT':
                if gridmap[gridloc[1]][gridloc[0]+1] < 20:
                    dtopac = (abs((px - (gridloc[0]+1)))+abs((py - gridloc[1])))
                    self.nextturn = 'RIGHT'
class Clyde(Ghosts):
    """The orange ghost
    time - pygame.time.get_ticks()

    """
    imagesloaded = False
    images = []
    def __init__(self,death=0):
        Ghosts.__init__(self,death)
        if Clyde.imagesloaded == False:
            Clyde.imagesloaded = True
            for i in range(8):
                im = pygame.image.load(os.path.join('Data','oghost' + str(i) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Clyde.images.append(im)
        self.image = Clyde.images[6]
        self.rect = self.image.get_rect()
        self.rect.center = (192,210)
        self.incage = True
        self.inprocesscheck = False
        if self.death == 0:
            self.owndotcount = 60
        else:
            self.owndotcount = 32
        self.ptimeminus = 0
        self.pelletimer = 4000
        self.ptime = 0
        self.scatterrect = (6,414)
        self.direction = 'LEFT'
        self.nextturn = 'LEFT'
    def update(self,time):
        """Update Clyde's position and various other properties

        """
        self.scatterchase()
        if self.incage == True:
            self.pelletimecheck()
        if self.delaytime < time and self.exitcheck() == False and self.incage == True:
            self.moveupdown()
            self.delaytime = time+self.speed
        if self.incage == True and self.exitcheck() == True and self.delaytime < time:
            self.exitproc()
            self.delaytime = time+20
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
        if self.delaytime < time and self.incage == False:
            self.direction = self.nextturn
            self.inprocess()
            self.move()
            if self.ongrid() == True:
                self.pickturn()
                self.intunnel()
            if self.hit == True:
                self.delaytime = time+self.speed/4
            elif self.weak == True:
                self.delaytime = time+self.speed*2
            else:
                self.delaytime = time+self.speed
    def exitproc(self):
        if self.rect.center != (168,174):
            self.direction ='UP'
            if self.rect.center[0] != 168:
                self.direction = 'LEFT'
            self.move()
        elif self.rect.center == (168,174):
            self.pickturn()
            self.incage = False
        if self.weak == False:
            self.moveanim()
        elif self.weak == True:
            self.weakanim()
    def ghostcheck(self, check):
        """Check if Inky's in the cage

        """
        if self.ghostcage == True and check == False:
            self.ptimeminus = self.ptime
        self.ghostcage = check
        if self.ptime - self.ptimeminus < 0:
            self.ptimeminus = 0
    def exitcheck(self):
        """Check to see if Clyde can exit the cage

        """
        if self.pelletsnum >= self.owndotcount:
            return True
        if self.pcheck == True and self.ghostcage == False:
            return True
        return False
    def pelletimecheck(self):
        if self.ptime - self.ptimeminus >= self.pelletimer and self.ghostcage == False:
            self.pcheck = True
    def inprocess(self):
        if self.rect.center == (168,174) and self.hit == True:
            self.inprocesscheck = True
            if self.rect.center[1] !=210:
                    self.direction = 'DOWN'
                    self.nextturn = 'DOWN'
        if self.rect.center[0] !=191 and self.rect.center[1] == 210 and self.inprocesscheck == True and self.hit == True:
                self.direction = 'RIGHT'
        elif self.rect.center == (191,210) and self.hit == True:
            self.hit = False
            self.incage = True
            self.inprocesscheck = False
    def pickturn(self):
        """Decides which direction the ghost should take next based on pacman's current euclidean distance from Clyde

        """
        if self.weak == False and self.hit == False:
            for pac in self.pacman:
                x = self.rect.center[0]/12 - pac.squarex
                y = self.rect.center[1]/12 - pac.squarey
                if math.sqrt(x*x + y*y) < 8:
                    self.pacman = pygame.sprite.RenderUpdates()
                    self.pacman.add(Pacman((self.scatterrect)))
            self.nextturn = self.checkdirection((self.rect.center[0]/12,self.rect.center[1]/12))
        elif self.hit == True:
            self.nextturn = self.checkdirection((self.rect.center[0]/12,self.rect.center[1]/12))
        elif self.weak == True:
            self.nextturn = self.randomturn((self.rect.center[0]/12,self.rect.center[1]/12))
class Pellets(pygame.sprite.Sprite):
    """Pellets

    """
    image = None
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        if Pellets.image == None:
            Pellets.image = pygame.image.load(os.path.join('Data','pellet0.bmp'))
            Pellets.image = Pellets.image.convert(Pellets.image)
            Pellets.image.set_colorkey((0,0,0))
        self.image = Pellets.image
        self.rect = self.image.get_rect()
        self.rect.topleft = rect
class Walls(pygame.sprite.Sprite):
    """The wall sprites
    Constructor: Location(tuple(interger,interger)), Walltype(interger)
    
    """
    imagesloaded = False
    images = []
    def __init__(self, rect, wallnumber):
        pygame.sprite.Sprite.__init__(self)
        self.id = wallnumber
        if Walls.imagesloaded == False:
            Walls.imagesloaded = True
            for i in range(44):
                im = pygame.image.load(os.path.join('Data','wall' + str(i) +'.bmp'))
                im = im.convert(im)
                Walls.images.append(im)
        for i in range(44):
            if wallnumber == i:
               self.image = Walls.images[i] 
        self.rect = self.image.get_rect()
        self.rect.topleft = rect
class BigPellets(pygame.sprite.Sprite):
    """The four large pellets

    """
    image = None
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        if BigPellets.image == None:
            BigPellets.image = pygame.image.load(os.path.join('Data','pellet4.bmp'))
            BigPellets.image = BigPellets.image.convert(BigPellets.image)
            BigPellets.image.set_colorkey((0,0,0))
        self.image = BigPellets.image
        self.rect = self.image.get_rect()
        self.rect.topleft = rect

class Pacman(pygame.sprite.Sprite):
    """Pacman

    """
    imagesloaded = False
    images = []
    def __init__(self, rect, player=1):
        pygame.sprite.Sprite.__init__(self)
        if Pacman.imagesloaded == False:
            Pacman.imagesloaded = True
            for i in range(20):
                im = pygame.image.load(os.path.join('Data','pac' + str(i) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Pacman.images.append(im)
        self.image = Pacman.images[4]
        self.rect = self.image.get_rect()
        self.rect.center = (rect)
        self.start = 1 #Check if pacman has just been created
        self.player = player
        self.dead = False
        self.x = 0
        self.y = 0
        self.squarex = self.rect.center[0]/12
        self.squarey = self.rect.center[1]/12
        self.frame = 0
        self.framedelay = 0
        #move pacman towards a predetermined destination when starting
        if player == 1:
            self.key = K_LEFT
            self.move(K_LEFT)
        elif player == 2:
            self.key = K_RIGHT
            self.move(K_RIGHT)
        self.delaytime = 0
    def collision(self):
        """Check to see if the direction that the player intends to move towards is valid

        """
        if self.dead == True:
            return True
        rectcheck = self.rect
        rectcheckx = self.rect.center[0]/12
        rectchecky = self.rect.center[1]/12
        if self.key == K_LEFT:
            rectcheckx = (rectcheck.center[0]-8)/12
            rectchecky = (rectcheck.center[1])/12
        if self.key == K_RIGHT:
            rectcheckx = (rectcheck.center[0]+5)/12
            rectchecky = (rectcheck.center[1])/12
        if self.key == K_UP:
            rectcheckx = (rectcheck.center[0])/12
            rectchecky = (rectcheck.center[1]-7)/12
        if self.key == K_DOWN:
            rectcheckx = (rectcheck.center[0])/12
            rectchecky = (rectcheck.center[1]+6)/12
        if rectcheckx >= 28 or rectcheckx <= -1:
            self.tunnelcheck()
            if self.key == K_UP or self.key == K_DOWN:
                return True
            return False
        elif gridmap[rectchecky][rectcheckx] < 20:
            return False
        return True
    def tunnelcheck(self):
        """Teleports the player when he reaches the end of the tunnel

        """
        if self.rect[0] == -27:
            self.rect[0] = 344
        elif self.rect[0] == 345:
            self.rect[0] = -26
    def moveanim(self,time):
        """Pacman's animations when moving

        """
        if self.framedelay < time:  
            if self.key == K_LEFT:
                if self.frame == 0:
                    self.image = Pacman.images[18]
                    self.frame = 1
                elif self.frame == 1:
                    self.image = Pacman.images[16]
                    self.frame = 0
            elif self.key == K_RIGHT:
                if self.frame == 0:
                    self.image = Pacman.images[0]
                    self.frame = 1
                elif self.frame == 1:
                    self.image = Pacman.images[2]
                    self.frame = 0
            elif self.key == K_UP:
                if self.frame == 0:
                    self.image = Pacman.images[17]
                    self.frame = 1
                elif self.frame == 1:
                    self.image = Pacman.images[19]
                    self.frame = 0
            elif self.key == K_DOWN:
                if self.frame == 0:
                    self.image = Pacman.images[3]
                    self.frame = 1
                elif self.frame == 1:
                    self.image = Pacman.images[1]
                    self.frame = 0
            self.framedelay = time+50
    def move(self, key):
        """Move Pacman

        """
        oldkey = self.key
        if key == K_LEFT:
            self.key = K_LEFT
            if self.collision() == False and self.ongrid():
                    self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]+8-self.rect.topleft[1]%12)
                    self.x = -1
                    self.y = 0
            else:
                self.key = oldkey
        elif key == K_RIGHT:
            self.key = K_RIGHT
            if self.collision() == False and self.ongrid():
                    self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]+8-self.rect.topleft[1]%12)
                    self.x = 1
                    self.y = 0
            else:
                self.key = oldkey
        elif key == K_UP:
            self.key = K_UP
            if self.collision() == False and self.ongrid():
                    self.rect.topleft = (self.rect.topleft[0]+9-self.rect.topleft[0]%12, self.rect.topleft[1])
                    self.x = 0
                    self.y = -1
            else:
                self.key = oldkey
        elif key == K_DOWN:
            self.key = K_DOWN
            if self.collision() == False and self.ongrid():
                    self.rect.topleft = (self.rect.topleft[0]+9-self.rect.topleft[0]%12, self.rect.topleft[1])
                    self.x = 0
                    self.y = 1
            else:
                self.key = oldkey
    def ongrid(self):
        """Checks to see if pacman is at a valid coordinate to turn without crashing into walls

        """
        if self.start == 1:
            self.start = 0
            return True
        elif (self.rect.topleft[1]%12 >= 3 and self.rect.topleft[1]%12 <= 13) and (self.rect.topleft[0]%12 >= 4 and self.rect.topleft[0]%12 <= 14):
            return True
        return False
    def deathanim(self, frame):
        """Animation of when pacman dies

        """
        self.dead = True
        self.image = Pacman.images[frame]
        #Delay for 6 frames in 60 frames per second 
    def update(self, time):
        """Update the position of pacman

        """
        self.squarex = self.rect.center[0]/12
        self.squarey = self.rect.center[1]/12
        if self.delaytime < time:
            if self.collision() == False:
                self.moveanim(pygame.time.get_ticks())
                self.rect.move_ip(self.x,self.y)
                self.delaytime = time+12
            else:
                self.x = 0
                self.y = 0
class Bonus(pygame.sprite.Sprite):
    """The bonus's sprites

    """
    imagesloaded = False
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if Bonus.imagesloaded == False:
            Bonus.imagesloaded = True
            for i in range(8):
                im = pygame.image.load(os.path.join('Data','fruit' + str(i+1) +'.bmp'))
                im = im.convert(im)
                im.set_colorkey((0,0,0))
                Bonus.images.append(im)
        self.image = Bonus.images[0]
        self.rect = self.image.get_rect(center = (168,246))
        
InGame = PacmanMain()
InGame.Menu()
