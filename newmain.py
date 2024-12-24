import pygame, sys
from game_project.teststate import *
from game_project.ui import *
from game_project.settings import *
from game_project.classes import *
from game_project.cam import *




class Init_Game:
    def __init__(self,enable,clock,screen):
        self.ENABLED = enable
        self.CLOCK = clock
        self.dt = self.CLOCK.tick(FPS)
        self.SCREEN = screen

        self.ui = UI()
        self.bgcanvas = pygame.Surface((WIDTH*2,WIDTH))   
        
        
        self.CLICK = False
        self.NumJoysticks = pygame.joystick.get_count()  
        if self.NumJoysticks > 0:
            self.joystick = pygame.joystick.Joystick(0)
        else:
            self.joystick = None
        self.TS = Tutorial(self.ENABLED,self.CLOCK,self.SCREEN)
        


        self.DevMode = False     

        self.Start_Tutorial = False
        self.collision_check = False
    def Constant_Texts(self):
        txt=get_font(32).render("Game State", True, WHITE)
        rect = txt.get_rect(center=(WIDTH/2,32))
        self.SCREEN.blit(txt,rect)
    def Cam_Init(self):
        self.cam = Camera(self.player)
        follow = Follow(self.cam,self.player)
        self.cam.setmethod(follow)
        self.cam.scroll()
    def BG_Init(self):
        self.SCREEN.fill(BLACK)
        self.SCREEN.blit(self.bgcanvas,(0 - self.cam.offset.x,60 - self.cam.offset.y))
        self.bgcanvas.fill(FLOOR_YELLOW)
    def ViewPort_Manager(self):
        self.Cam_Init()
        
        self.BG_Init()
        self.Sprite_Draw()
        #self.Constant_Texts()
    def Load_CSV(self):
        self.level_data = {
            "bound": LOAD_CSV(f'game_project/lvl_data/lvl.csv'),



        }
        for style,data in self.level_data.items():
            for row_index, row in enumerate(data):
                for col_index, col in enumerate(row):
                    if style == "bound" :
                        x = col_index * TILE
                        y = row_index * TILE
                        if col == '7':
                            FENCE("NE",(x,y),[self.perspective_group,self.obs])
                        elif col == '6':
                            FENCE("NW",(x,y),[self.perspective_group,self.obs])
                        elif col == '8':
                            FENCE("SE",(x,y),[self.perspective_group,self.obs])
                        elif col == '9':
                            FENCE("SW",(x,y),[self.perspective_group,self.obs])
                        elif col == '5':
                            FENCE("W",(x,y),[self.perspective_group,self.obs])
                        elif col == '4':
                            FENCE("E",(x,y),[self.perspective_group,self.obs])
                        elif col == '3':
                            FENCE("N",(x,y),[self.perspective_group,self.obs])
                        elif col == '2':
                            FENCE("S",(x,y),[self.perspective_group,self.obs])
                        elif col == '11':
                            FENCE("L",(x,y),[self.perspective_group,self.obs])
                        elif col == '12':
                            FENCE("FR",(x,y),[self.perspective_group,self.obs])
                        elif col == '13':
                            FENCE("FL",(x,y),[self.perspective_group,self.obs])
                        elif col == '10':
                            FENCE("F",(x,y),[self.perspective_group,self.obs])
                        elif col == '14':
                            FENCE("gate",(x,y),[self.perspective_group,self.fence_group])
                        elif col == '77':
                            Rock((x,y),[self.perspective_group,self.obs])

                        elif col == '66':
                            Barrel((x,y),[self.perspective_group,self.barrels])
                        elif col == '55':
                            MoneyBag((x,y),[self.perspective_group,self.money])
                        
                        


                        elif col == '100':
                            Sheriff_Building((x,y),[self.perspective_group,self.obs])
                        elif col == '96':
                            Home((x,y),[self.perspective_group,self.obs])
                            
                        elif col == '101':
                            Tree((x,y),[self.perspective_group,self.obs])




                        elif col == '111':
                            Wagon((x,y),[self.perspective_group,self.obs])
                        elif col == '23':
                            self.player = PLAYER(3,(x,y),[self.perspective_group])
                        elif col == '33':
                            self.cactus = CACTUS((x,y),[self.perspective_group])
                        elif col == '45':
                            self.npc = NPC("npc",(x,y),[self.perspective_group,self.obs])                
    def Initialize_Sprites(self):
        self.perspective_group = PerspectiveGroup()
        self.obs = pygame.sprite.Group()
        self.barrels = pygame.sprite.Group()   
        self.money = pygame.sprite.Group()
        self.fence_group = pygame.sprite.Group()
    def Sprite_Update(self):
        
        for bullet in self.player.bullets:          
            for barrel in self.barrels:
                if bullet.rect.colliderect(barrel.rect):
                    barrel.state = "exploding"
                    try:
                        self.player.bullets.remove(bullet)
                    except ValueError:
                        pass
            if bullet.rect.x < 0:
                self.player.bullets.remove(bullet)
            elif bullet.rect.x > 1280:
                self.player.bullets.remove(bullet)
            elif bullet.rect.y < 0:
                self.player.bullets.remove(bullet)
            elif bullet.rect.y > 640:
                self.player.bullets.remove(bullet)
            for sprite in self.obs:
                if bullet.rect.colliderect(sprite.rect):
                    print("Bullet collision w/ PG")
                    try:
                        self.player.bullets.remove(bullet)
                    except ValueError:
                        pass
                        #print(f"Bullet {bullet} not found in the list. It may have already been removed.")
                    

        self.fence_group.update()
        self.perspective_group.update(self.dt) # Perspective Group -> Displaying everything w/ Y-Axis Perspective
        self.player.Barrel_Collision(self.barrels) # Explosive Group  -> still an obstacle but can be shot
        self.player.MoneyBag_Collision(self.money) # Collectable Group -> not an obstacle?
        self.player.Obs_Collision(self.obs) # Obstacle Group -> only an obstacle: buildings, fence, trees, etc
    def Tutorial_Events(self):
            
        if self.player.rect.colliderect(self.npc.rect):
            self.collision_check = True
            sb = SpeechBubble(self.npc.rect.x+12,self.npc.rect.y-30)
            sb.draw(self.bgcanvas)
            txt = get_font(10).render("Howdy",True,BLACK)
            self.bgcanvas.blit(txt,(sb.rect.x + 6,sb.rect.y+4))
            txt = get_font(10).render("Partner",True,BLACK)
            self.bgcanvas.blit(txt,(sb.rect.x + 16,sb.rect.y+14))

            if self.NumJoysticks > 0:

                self.ui.conditional_texts("Click 'B' to Start Tutorial")
            else:
                if self.NumJoysticks < 1:
                    
                    self.ui.conditional_texts("Click Enter to Start Tutorial")

            if self.Start_Tutorial:
                self.TS.run()
    def Sprite_Draw(self):
            if self.DevMode:
                for sprite in self.perspective_group:
                    pygame.draw.rect(self.bgcanvas,(RED),sprite.rect,1,1)
                    pygame.draw.rect(self.bgcanvas,(GREEN),sprite.hitbox_rect,1,1)

                pygame.draw.line(self.bgcanvas,("Purple"),(WIDTH,0),(WIDTH,WIDTH))
                pygame.draw.line(self.bgcanvas,("Orange"),(0,WIDTH/2),(WIDTH*2,WIDTH/2))

            self.perspective_group.draw(self.bgcanvas)
            self.fence_group.draw(self.bgcanvas)
            self.Tutorial_Events()
            self.ui.draw(self.DevMode,self.SCREEN,self.player.state,
                         self.player.direction,
                         self.player.bullets_remaining,
                         self.player.reload_timer,
                         self.player.total_money)
    def Event_Handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.ENABLED = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
                    #self.player.state == "Shoot"
                    self.player.QuickDraw()
            elif self.joystick != None and  (self.joystick.get_button(0) ):
                self.player.QuickDraw()     


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i and self.DevMode == False:
                    self.DevMode = True
                elif event.key == pygame.K_i and self.DevMode == True:
                    self.DevMode = False

                elif event.key == pygame.K_RETURN and self.collision_check == True:
                    self.Start_Tutorial = True
                elif event.key == pygame.K_r :
                    self.player.reloading = True




                
                elif event.key == pygame.K_RIGHT:
                    self.player.direction = "Right"
                    self.player.state = "Walk"
                elif event.key == pygame.K_RIGHT:
                    self.player.direction = "Right"
                    self.player.state = "Walk"
                elif event.key == pygame.K_LEFT:
                    self.player.direction = "Left"
                    self.player.state = "Walk"
                elif event.key == pygame.K_UP:
                    self.player.direction = "Up"
                    self.player.state = "Walk"
                elif event.key == pygame.K_DOWN:
                    self.player.direction = "Down"
                    self.player.state = "Walk"    
                elif event.key == pygame.K_x:
                    self.player.alive = False
                elif event.key == pygame.K_a:
                    self.player.alive = True
                elif event.key == pygame.K_h:
                    self.player.YouShotMe()

                elif event.key == pygame.K_p:
                    self.paused = True
                    self.PAUSED()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player.state = "Idle"
                elif event.key == pygame.K_RIGHT:
                    self.player.state = "Idle"
                elif event.key == pygame.K_LEFT:
                    self.player.state = "Idle"
                elif event.key == pygame.K_UP:
                    self.player.state = "Idle"
                            
            
            elif event.type == pygame.JOYBUTTONDOWN:
                if self.joystick.get_button(1) and self.player.bullets_remaining <= 0:
                    self.player.reloading = True
                elif self.joystick.get_button(1) and self.collision_check == True:
                    self.Start_Tutorial = True


                if self.joystick.get_button(4):
                    if not self.DevMode:
                        self.DevMode = True
                    else:
                        self.DevMode = False
                



            elif event.type == pygame.JOYAXISMOTION:
                
                horiz_move = self.joystick.get_axis(0)
                vert_move = self.joystick.get_axis(1)
                left_move = self.joystick.get_axis(14)
                right_move = self.joystick.get_axis(15)
                up_move = self.joystick.get_axis(12)
                down_move = self.joystick.get_axis(13)
                if abs(left_move) >= -1.000 and horiz_move <= -0.5:
                    self.player.direction = "Left"
                    self.player.state = "Walk"
                elif abs(right_move) >= -1.000 and horiz_move >= 0.5:
                    self.player.direction = "Right"
                    self.player.state = "Walk"
                
                elif abs(up_move) >= -1.000 and vert_move <= -0.5:
                    self.player.direction = "Up"
                    self.player.state = "Walk"
                elif abs(down_move) >= -1.000 and vert_move >= 0.5:
                    self.player.direction = "Down"
                    self.player.state = "Walk"
                else:
                    self.player.state = "Idle"    
    def run(self):
        self.Initialize_Sprites()
        self.Load_CSV()
        
        while self.ENABLED:
            self.Event_Handler()
            self.Sprite_Update()
            
            
            
            self.ViewPort_Manager()

            pygame.display.flip()
            self.CLOCK.tick(FPS)
            

class Game_Engine:
    def __init__(self):
        pygame.init()
        
        self.ENABLED = True
        
        self.CLOCK = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(RES)
        # Icon & Display Window Name
        self.CLICK = False

        self.menu_active = False

        self.MENU = Init_Game(self.ENABLED,self.CLOCK,self.SCREEN)
    def Init_Joystick(self):
        pygame.joystick.init()
        self.JoyRect = pygame.Rect(WIDTH-128,32,32,32)
        
        self.NumJoysticks = pygame.joystick.get_count()
        if self.NumJoysticks > 0:
            self.Joystick = pygame.joystick.Joystick(0)
            #print("Joystick Initialized")
            self.joy_col = "Green"  
        else:
            if self.NumJoysticks < 1:
                self.Joystick = None
                self.joy_col = "Red"
    def Indicate_Controls(self):
        pygame.draw.rect(self.SCREEN,self.joy_col,self.JoyRect,0,2)
        pygame.draw.rect(self.SCREEN,BLACK,self.JoyRect,2,2)
    def Conditional_Texts(self):
        if self.NumJoysticks > 0:
            txt = "Press 'Start' to Play"
        else:
            txt = "Click 'SpaceBar' to Play"
        text = get_font(24).render(f"{txt}",True,WHITE)
        rect = text.get_rect(center=(WIDTH/2,HEIGHT-64))
        self.SCREEN.blit(text,(rect))
    def Constant_Texts(self):
        menutxt=get_font(32).render("Init Screen", True, WHITE)
        rect = menutxt.get_rect(center=(WIDTH/2,32))
        self.SCREEN.blit(menutxt,rect)

    def ViewPort_Manager(self):
        self.SCREEN.fill("DarkBlue")
  
        self.Conditional_Texts()
        self.Constant_Texts()
        self.Indicate_Controls()

    def Event_Handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.ENABLED = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.NumJoysticks < 1:
                    if event.key == pygame.K_SPACE:
                        self.MENU.run()
            elif event.type == pygame.JOYBUTTONDOWN:
                if self.NumJoysticks > 0:
                    if event.button == 6:
                        self.MENU.run()

    def Event_Loop(self):
        
        while self.ENABLED:
            self.Init_Joystick()
            self.Event_Handler()
            self.ViewPort_Manager()
            pygame.display.flip()
            self.CLOCK.tick(FPS)



if __name__ == "__main__":
    main = Game_Engine()
    main.Event_Loop()
