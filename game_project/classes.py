import pygame

from game_project.settings import *



class SpeechBubble(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("game_project/img/npc/talk.png")
        self.rect = self.image.get_rect(topleft=(x,y))
    def draw(self,surf):
        surf.blit(self.image,self.rect)
      

class MoneyBag(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        barrel = pygame.image.load("game_project/img/moneybag.png")

        self.image = barrel
        self.rect = self.image.get_rect(topleft=(pos))
        self.amount = 5
class Home(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("game_project/img/HOME.png")
        self.rect = self.image.get_rect(topleft=(pos))
        x = self.rect.x
        y = self.rect.y 
        self.hitbox = pygame.Surface((96,80))
        self.hitbox_rect = self.hitbox.get_rect(topleft=(x,y+58))
    def custom_draw(self,surf,dt):

        surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)
class Sheriff_Building(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("game_project/img/sheriff.png")
        self.rect = self.image.get_rect(topleft=(pos))
        x = self.rect.x
        y = self.rect.y 
        self.hitbox = pygame.Surface((96,83))
        self.hitbox_rect = self.hitbox.get_rect(topleft=(x,y+38))
    def custom_draw(self,surf,dt):

        surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)
class Tree(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("game_project/img/TREE.png")
        self.rect = self.image.get_rect(topleft=(pos))
        x = self.rect.x
        y = self.rect.y 
        self.hitbox = pygame.Surface((33,19))
        self.hitbox_rect = self.hitbox.get_rect(topleft=(x+15,y+76))
    def custom_draw(self,surf,dt):

        surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)
class Wagon(pygame.sprite.Sprite):
    def __init__(self, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("game_project/img/wagon.png")
        self.rect = self.image.get_rect(topleft=(pos))
        x = self.rect.x
        y = self.rect.y 
        self.hitbox = pygame.Surface((60,20))
        self.hitbox_rect = self.hitbox.get_rect(topleft=(x,y+24))
    def custom_draw(self,surf,dt):

        surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)

class Barrel(pygame.sprite.Sprite):
    
    def __init__(self, pos,groups):
        super().__init__(groups)
        barrel = pygame.image.load("game_project/img/barrel.png")

       

        self.original_position = (pos)  # Store the barrel's original position
        self.image = barrel
        self.rect = self.image.get_rect(topleft=self.original_position)
        x = self.rect.x
        y = self.rect.y 
        self.hitbox = pygame.Surface((16,8))
        self.hitbox_rect = self.hitbox.get_rect(topleft=(x,y+13))

        # Load explosion animation frames from sprite sheet
        xplode = pygame.image.load("game_project/img/xplode.png")
        self.frames = self.load_explosion_frames(xplode)
        self.current_frame = 0

        self.state = "idle"  # "idle" or "exploding"
        self.explosion_time = 0.5
        self.explosion_timer = 0
        self.animation_speed = 0.1
        self.time_since_last_frame = 0

        # Offset for the explosion frames
        self.explosion_offset = (-15, -25)  # Example: Adjust as needed

    def load_explosion_frames(self, sprite_sheet):
        """Extract frames from the sprite sheet."""
        temp_list = []
        for i in range(8):  # Assuming 8 frames in the animation
            frame = sprite_sheet.subsurface(pygame.Rect(i * 50, 0, 50, 55))
            temp_list.append(frame)
        return temp_list

    def trigger_explosion(self):
        """Trigger the explosion animation."""
        if self.state == "idle":
            self.state = "exploding"
            self.explosion_timer = 0
            self.current_frame = 0

    def animate(self, dt):
        """Handle the animation of the explosion."""
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_speed:
            self.time_since_last_frame = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
                # Adjust position using the explosion offset
                self.rect.topleft = (
                    self.original_position[0] + self.explosion_offset[0],
                    self.original_position[1] + self.explosion_offset[1],
                )
            else:
                self.kill()  # Remove sprite when the animation is done

    def update(self, dt):



        """Update the barrel's state."""
        if self.state == "exploding":
            self.explosion_timer += dt
            self.animate(dt)
    def custom_draw(self,surf,dt):

        surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)

class FENCE(pygame.sprite.Sprite):
    def __init__(self,dir,pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load(f"game_project/img/FENCE/{dir}.png")
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox_rect = self.rect
    def draw(self,surf):
        surf.blit(self.image,(self.rect))
class Rock(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        
        self.image = pygame.image.load(f"game_project/img/rock.png")
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox_rect = self.rect
    def draw(self,surf):
        surf.blit(self.image,(self.rect))



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=3, lifespan=2000):
        super().__init__()
        """
        Initialize a bullet.
        :param x: Initial x-coordinate of the bullet.
        :param y: Initial y-coordinate of the bullet.
        :param direction: Direction of the bullet ("up", "down", "left", "right").
        :param speed: Speed of the bullet (pixels/second).
        :param lifespan: Lifespan of the bullet in milliseconds.
        """
        self.image = pygame.Surface((5,5))
        #self.image.fill("Green")
        self.rect = pygame.Rect(x, y, 5, 5)  # A small square for the bullet
        self.direction = direction
        self.speed = speed
        self.lifespan = lifespan
        self.timer = 0
        self.velocity = 0

    def collision(self):
        if self.rect.x < 100:
            self.remove() 


    def update(self, dt):
        

        self.dx =0
        self.dy = 0
        """
        Update the bullet's position and lifespan.
        :param dt: Time elapsed since the last update (ms).
        """
        # Update position based on velocity
        # Set velocity based on direction
        if self.direction == "Up":
            
            self.dy = -self.speed
        elif self.direction == "Down":
            self.dy = self.speed
        elif self.direction == "Left":
            self.dx = -self.speed
        elif self.direction == "Right":
            self.dx = self.speed

        
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        # Update lifespan timer
        self.timer += dt

    def is_alive(self):
        """Check if the bullet is still within its lifespan."""
        return self.timer < self.lifespan

    def draw(self, screen):
        """Draw the bullet."""
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen, RED, self.rect)  # Golden yellow bullet

class PLAYER(pygame.sprite.Sprite):
    def __init__(self,speed,pos,groups):
        super().__init__(groups)
        self.Bank_Handler()
        self.groups = groups
        


        self.alive = True
        self.dead = False
        self.death_start_time = 0
        self.death_duration = 1400
        self.health = 100
        self.hit = False
        self.hit_start_time = 0
        self.hit_time = 420
        self.gun_equipped = True
        self.shooting = False
        self.reloading = False
        self.max_bullets = 6
        self.bullets_remaining = self.max_bullets
        self.reload_time = 2000
        self.reload_timer = 0  

        self.bullets = []
        self.attack_start_time = 0
        self.attack_duration = 666
        self.fire_rate = 555
        self.last_shot_time = 0
        self.speed = speed
        

        
        
        self.State_Management()
        self.Img_Loader()
        
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox_surf = pygame.Surface((16,32))
        self.hitbox_surf.fill("DarkRed")
        self.hitbox_rect = self.hitbox_surf.get_rect(topleft=(self.rect.x+15,self.rect.y+10))
        self.hb_surf = pygame.Surface((16,8))
        self.hb_surf.fill("DarkGreen")
        self.hb_rect = self.hb_surf.get_rect(topleft=(self.rect.x+15,self.rect.y+34))





        self.hitbox = pygame.Rect(self.rect.x+16,self.rect.y+12,16,32)

    def State_Management(self):
        self.state = "Idle"
        self.states = {
            "Idle": 1,
            "Walk": 2,
            "Shoot": 3,
            "Hit": 4,
            "Dead": 5,
            "FullyDead": 6,
        }
        self.direction = "Right"
        self.directions = ['Right', 'Left', 'Up', 'Down']
        self.flip = False
    def Img_Loader(self):
        front_sheet = pygame.image.load("game_project/img/Front.png")
        back_sheet = pygame.image.load("game_project/img/Back.png")
        side_sheet = pygame.image.load("game_project/img/Side.png")
        dead_sheet = pygame.image.load("game_project/img/Dead.png")
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks() 
        frame_width = 48
        frame_height = 44
        scale = 1
        # Front Idle Action (0)
        temp_list = []
        for i in range(6):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)
        # Front Walk Action (1)
        temp_list = []
        for i in range(8):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,44, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Front Shoot Action (2)
        temp_list = []
        for i in range(6):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,88, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)

        # Side Idle Action (3)
        temp_list = []
        for i in range(6):
                frame = side_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)
        # Side Walk Action (4)
        temp_list = []
        for i in range(8):
                frame = side_sheet.subsurface(pygame.Rect(i * frame_width,44, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Side Shoot Action (5)
        temp_list = []
        for i in range(6):
                frame = side_sheet.subsurface(pygame.Rect(i * frame_width,88, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)       
        
        # Back Idle Action (6)
        temp_list = []
        for i in range(6):
                frame = back_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)
        # Back Walk Action (7)
        temp_list = []
        for i in range(8):
                frame = back_sheet.subsurface(pygame.Rect(i * frame_width,44, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Back Shoot Action (8)
        temp_list = []
        for i in range(6):
                frame = back_sheet.subsurface(pygame.Rect(i * frame_width,88, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)      
        # Hit Action (9)
        temp_list = []
        for i in range(1):
                frame = dead_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Dying Action (10)
        temp_list = []
        for i in range(14):
                frame = dead_sheet.subsurface(pygame.Rect(i * frame_width,44, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)  
        self.image = self.animation_list[self.action][self.frame_index]
       # DEAD Action (11)
        temp_list = []
        for i in range(1):
                frame = dead_sheet.subsurface(pygame.Rect(13 * frame_width,44, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)  
        self.image = self.animation_list[self.action][self.frame_index]         
    def Bank_Handler(self):
        self.total_money = 0       
    def QuickDraw(self):
        
        if not self.shooting and self.bullets_remaining > 0 and self.gun_equipped:
            
            self.shooting = True
            self.shoot()

            self.state = "Shoot"
            
            
            self.attack_start_time = pygame.time.get_ticks()
            #
            
    def YouShotMe(self):
        if not self.hit:
            self.hit = True
            self.hit_start_time = pygame.time.get_ticks()
            self.state = "Hit"
            self.health -=100          
    def hit_timer(self):
        current_time = pygame.time.get_ticks()
        if self.hit:
            if current_time - self.hit_start_time >= self.hit_time:
                self.hit = False
                self.state = "Idle"            
    def shoot_timer(self):
        current_time = pygame.time.get_ticks()
        
        if self.shooting:
            if current_time - self.attack_start_time >= self.attack_duration:
                self.shooting = False
                self.state = "Idle"
    def shoot(self):
        #self.QuickDraw()
        
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_shot_time > self.fire_rate) and self.bullets_remaining > 0:
        
            """Fire a bullet in the current facing direction."""
            if self.direction == "Up":
                bullet_x = self.hitbox_rect.centerx
                bullet_y = self.hitbox_rect.top - 10
            elif self.direction == "Down":
                bullet_x = self.hitbox_rect.centerx
                bullet_y = self.hitbox_rect.bottom + 10
            elif self.direction == "Left":
                bullet_x = self.hitbox_rect.left - 10
                bullet_y = self.hitbox_rect.centery
            elif self.direction == "Right":
                bullet_x = self.hitbox_rect.right + 10
                bullet_y = self.hitbox_rect.centery
        # Create a new bullet and add it to the list
            self.new_bullet = Bullet(bullet_x, bullet_y, self.direction)
            self.bullets.append(self.new_bullet)
            
  
            # Update bullet count and shot time
            self.bullets_remaining -= 1
            self.last_shot_time = current_time
    def reload(self):
        current_time = pygame.time.get_ticks()
        """
        Reload bullets after a reload timer finishes.
        :param current_time: The current time in milliseconds.
        """
        if self.bullets_remaining == 0 and self.reload_timer == 0 and self.reloading:
            # Start the reload timer
            self.reload_timer = current_time
        elif self.reload_timer > 0 and current_time - self.reload_timer >= self.reload_time:
            # Reload bullets once the timer completes
            self.bullets_remaining = self.max_bullets
            self.reload_timer = 0  # Reset the reload timer
            self.reloading = False
    def death_timer(self):
        if not self.dead:

            self.dead = True
            #print("Dying")
            self.death_start_time = pygame.time.get_ticks()
            self.state = "Dead"      
    def Final_Will_and_Test(self):
        current_time = pygame.time.get_ticks()
        if self.dead:
            if current_time - self.death_start_time >= self.death_duration:
                print("Fully Dead")
                self.state = "FullyDead"
                self.update_action(11)
    def update(self, dt):

        self.inputs() 
        self.update_animation(dt)
        
        self.direction_animation()
        
        
        
        
        for bullet in self.bullets:
            bullet.update(dt)
                 
    def update_animation(self,dt):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    def update_action(self,new_action):
        #check if action is different from previous
        if new_action != self.action:
            self.action = new_action
        #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    def direction_animation(self):
        if self.alive:
            
            
            if self.hit:
                self.update_action(9)
                
            elif self.direction == "Right" or self.direction == "Left":
                if self.state == "Shoot":
                    self.update_action(5)
                    #print("Shoot")
                     
                elif self.state == "Walk":
                    self.update_action(4)
                else:
                    self.update_action(3)
            elif self.direction == "Down":
                if self.state == "Shoot":
                    self.update_action(2)
                elif self.state == "Walk":
                    self.update_action(1)
                else:
                    self.update_action(0)
            elif self.direction == "Up":
                if self.state == "Shoot":
                    self.update_action(8)
                elif self.state == "Walk":

                    self.update_action(7)
                else:
                    self.update_action(6)
            #else:
                #self.state == "Idle"
        else:
            if not self.alive:
                
                self.update_action(10)
                self.death_timer()              
    def Screen_Collision(self):
        if self.hitbox_rect.right + self.dx > WIDTH:
            self.dx = 0
        if self.hitbox_rect.left + self.dx < 0:
            self.dx = 0
        if self.hitbox_rect.top + self.dy < 0:
            self.dy = 0
        if self.hitbox_rect.bottom + self.dy > HEIGHT:
            self.dy = 0         
    def Barrel_Collision(self,sprites):
        offset = 16
        y_offset_up = 8
        y_offset_down = 2
        hb_offset = 24
        for barrel in sprites:
            if self.hb_rect.colliderect(barrel.hitbox_rect):
                #print("Collision w/ barrel")
                if self.dx > 0:
                    self.rect.right  = barrel.rect.left+offset     
                    self.hitbox_rect.right = barrel.rect.left 
                    self.hb_rect.right = barrel.rect.left
                elif self.dx < 0:
                    self.rect.left  = barrel.rect.right-offset     
                    self.hitbox_rect.left = barrel.rect.right
                    self.hb_rect.left = barrel.rect.right

                elif self.dy > 0:  
                    self.rect.bottom  = barrel.rect.top+6
                    self.hitbox_rect.bottom = barrel.rect.top+4
                    self.hb_rect.bottom = barrel.rect.top+4
                elif self.dy < 0:
                    self.rect.top  = barrel.rect.bottom-32
                    self.hitbox_rect.top = barrel.rect.bottom -24
                    self.hb_rect.top  = barrel.rect.bottom

    def Obs_Collision(self,obs):
        offset = 16
        y_offset_up = 8
        y_offset_down = -2
        hb_offset = 24
        for obstacle in obs:
            if self.hb_rect.colliderect(obstacle.hitbox_rect):
                if self.dx > 0:
                    self.rect.right  = obstacle.rect.left+offset     
                    self.hitbox_rect.right = obstacle.rect.left 
                    self.hb_rect.right = obstacle.rect.left
                elif self.dx < 0:
                    self.rect.left  = obstacle.rect.right-offset     
                    self.hitbox_rect.left = obstacle.rect.right
                    self.hb_rect.left = obstacle.rect.right


                elif self.dy > 0:  
                    self.rect.bottom  = obstacle.hitbox_rect.top-y_offset_down     
                    self.hitbox_rect.bottom = obstacle.hitbox_rect.top 
                    self.hb_rect.bottom = obstacle.hitbox_rect.top
                elif self.dy < 0:
                    self.rect.top  = obstacle.rect.bottom-32   
                    self.hitbox_rect.top = obstacle.rect.bottom -24
                    self.hb_rect.top = obstacle.rect.bottom
    def MoneyBag_Collision(self,money):
        for moneybag in money:
            if self.hitbox_rect.colliderect(moneybag.rect):
                self.total_money += moneybag.amount
                moneybag.kill()
    def inputs(self):
        if self.health <= 0:
            self.alive = False
            
            
            
            
        self.dx = 0
        self.dy = 0
        if self.state == "Walk":
            if self.direction == "Left":
                self.dx = -self.speed
            elif self.direction == "Right":
                self.dx = self.speed
            else:
                self.dx = 0

            if self.direction == "Up":
                self.dy = -self.speed
            elif self.direction == "Down":
                self.dy = self.speed
            else:
                self.dy = 0
            

        #self.Screen_Collision()
        
        
        
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.hitbox_rect.x += self.dx
        self.hitbox_rect.y += self.dy
        self.hb_rect.x += self.dx
        self.hb_rect.y += self.dy
        
        
        
        self.shoot_timer()
        self.reload()
        self.hit_timer()
        self.Final_Will_and_Test()
        
            
    def custom_draw(self,surf,dt):
        

        if self.direction == "Left":
            

            
            surf.blit(pygame.transform.flip(self.image,True,False),self.rect)
        else:
            surf.blit(self.image,self.rect)


        for bullet in self.bullets:
            bullet.draw(surf)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        #pygame.draw.rect(surf,BLUE,self.rect,1,1)        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)
        #pygame.draw.rect(surf,"DarkGreen",self.hb_rect,1,1)
       


class CACTUS(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.alive = True
        self.dead = False
        self.death_start_time = 0
        self.death_duration = 1000
        self.health = 100
        self.hit = False
        self.hit_start_time = 0
        self.hit_time = 420
        self.shooting = False
        self.reloading = False
        self.max_bullets = 6
        self.bullets_remaining = self.max_bullets
        self.reload_time = 2000
        self.reload_timer = 0  

        self.bullets = []
        self.attack_start_time = 0
        self.attack_duration = 666
        self.fire_rate = 555
        self.last_shot_time = 0
        

        
        
        self.State_Management()
        self.Img_Loader()
        
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox_surf = pygame.Surface((16,32))
        self.hitbox_surf.fill("DarkRed")
        self.hitbox_rect = self.hitbox_surf.get_rect(topleft=(self.rect.x+15,self.rect.y+10))
        self.hb_surf = pygame.Surface((16,8))
        self.hb_surf.fill("DarkGreen")
        self.hb_rect = self.hb_surf.get_rect(topleft=(self.rect.x+15,self.rect.y+34))





        self.hitbox = pygame.Rect(self.rect.x+16,self.rect.y+12,16,32)

    def State_Management(self):
        self.state = "Idle"
        self.states = {
            "Idle": 1,
            "Walk": 2,
            "Shoot": 3,
            "Hit": 4,
            "Dead": 5,
            "FullyDead": 6,
        }
        self.direction = "Right"
        self.directions = ['Right', 'Left', 'Up', 'Down']
        self.flip = False
    def Img_Loader(self):
        front_sheet = pygame.image.load("game_project/img/Cactus/front.png")
        back_sheet = pygame.image.load("game_project/img/Cactus/back.png")
        side_sheet = pygame.image.load("game_project/img/Cactus/side.png")
        dead_sheet = pygame.image.load("game_project/img/Cactus/xplode.png")
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks() 
        frame_width = 40
        frame_height = 40
        scale = 1
        # Front Idle Action (0)
        temp_list = []
        for i in range(4):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)
        # Front Walk Action (1)
        temp_list = []
        for i in range(10):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,40, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Front Shoot Action (2)
        temp_list = []
        for i in range(11):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,84, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
        # Hit Action (3)
        temp_list = []
        for i in range(1):
                frame = front_sheet.subsurface(pygame.Rect(i * frame_width,120, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)


        # Back Idle Action (4)
        temp_list = []
        for i in range(4):
                frame = back_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)
        # Back Walk Action (5)
        temp_list = []
        for i in range(10):
                frame = back_sheet.subsurface(pygame.Rect(i * frame_width,40, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Back Shoot Action (6)
        temp_list = []
        for i in range(11):
                frame = back_sheet.subsurface(pygame.Rect(i * frame_width,84, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)

        # Side Idle Action (7)
        temp_list = []
        for i in range(4):
                frame = side_sheet.subsurface(pygame.Rect(i * frame_width,0, frame_width, frame_height))
                temp_list.append(frame)
        self.animation_list.append(temp_list)
        # Side Walk Action (8)
        temp_list = []
        for i in range(9):
                frame = side_sheet.subsurface(pygame.Rect(i * frame_width,40, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)
       # Side Shoot Action (9)
        temp_list = []
        for i in range(11):
                frame = side_sheet.subsurface(pygame.Rect(i * frame_width,84, frame_width, frame_height))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)        

        #Xplode Action (10)
        temp_list = []
        for i in range(8):
                frame = dead_sheet.subsurface(pygame.Rect(i * 50, 0, 50, 55))
                temp_list.append(frame)  
        self.animation_list.append(temp_list)          







        self.image = self.animation_list[self.action][self.frame_index]         
 
    def QuickDraw(self):
        if not self.shooting and self.bullets_remaining > 0:
            self.shooting = True
            self.attack_start_time = pygame.time.get_ticks()
            self.state = "Shoot"
    def YouShotMe(self):
        if not self.hit:
            self.hit = True
            self.hit_start_time = pygame.time.get_ticks()
            self.state = "Hit"
            self.health -=10          
    def hit_timer(self):
        current_time = pygame.time.get_ticks()
        if self.hit:
            if current_time - self.hit_start_time >= self.hit_time:
                self.hit = False
                self.state = "Idle"            
    def shoot_timer(self):
        current_time = pygame.time.get_ticks()
        if self.shooting:
            if current_time - self.attack_start_time >= self.attack_duration:
                self.shooting = False
                self.state = "Idle"
    def shoot(self):
        
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_shot_time > self.fire_rate) and self.bullets_remaining > 0:
        
            """Fire a bullet in the current facing direction."""
            if self.direction == "Up":
                bullet_x = self.hitbox_rect.centerx
                bullet_y = self.hitbox_rect.top - 10
            elif self.direction == "Down":
                bullet_x = self.hitbox_rect.centerx
                bullet_y = self.hitbox_rect.bottom + 10
            elif self.direction == "Left":
                bullet_x = self.hitbox_rect.left - 10
                bullet_y = self.hitbox_rect.centery
            elif self.direction == "Right":
                bullet_x = self.hitbox_rect.right + 10
                bullet_y = self.hitbox_rect.centery
        # Create a new bullet and add it to the list
            self.new_bullet = Bullet(bullet_x, bullet_y, self.direction)
            self.bullets.append(self.new_bullet)
  
            # Update bullet count and shot time
            self.bullets_remaining -= 1
            self.last_shot_time = current_time
    def reload(self):
        current_time = pygame.time.get_ticks()
        """
        Reload bullets after a reload timer finishes.
        :param current_time: The current time in milliseconds.
        """
        if self.bullets_remaining == 0 and self.reload_timer == 0 and self.reloading:
            # Start the reload timer
            self.reload_timer = current_time
        elif self.reload_timer > 0 and current_time - self.reload_timer >= self.reload_time:
            # Reload bullets once the timer completes
            self.bullets_remaining = self.max_bullets
            self.reload_timer = 0  # Reset the reload timer
            self.reloading = False
    def death_timer(self):
        if not self.dead:

            self.dead = True
            #print("Dying")
            self.death_start_time = pygame.time.get_ticks()
            self.state = "Dead"      
    def Final_Will_and_Test(self):
        current_time = pygame.time.get_ticks()
        if self.dead:
            if current_time - self.death_start_time >= self.death_duration:
                print("Fully Dead")
                self.state = "FullyDead"
                
                


    def update(self, dt):
        self.update_animation(dt)
        for bullet in self.bullets:
            bullet.update(dt)
        self.inputs()  
        if self.state == "FullyDead":
            self.kill()        
    def update_animation(self,dt):
        ANIMATION_COOLDOWN = 125
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    def update_action(self,new_action):
        #check if action is different from previous
        if new_action != self.action:
            self.action = new_action
        #update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    def direction_animation(self):
        if self.alive:
            
            
            if self.hit:
                self.update_action(3)
                
            elif self.direction == "Right" or self.direction == "Left":
                if self.state == "Shoot":
                    self.update_action(9)
                     
                elif self.state == "Walk":
                    self.update_action(8)
                else:
                    self.update_action(7)

            elif self.direction == "Down":
                if self.state == "Shoot":
                    self.update_action(2)
                elif self.state == "Walk":
                    self.update_action(1)
                else:
                    self.update_action(0)
            elif self.direction == "Up":

                if self.state == "Shoot":
                    self.update_action(6)
                elif self.state == "Walk":
                    self.update_action(5)
                else:
                    self.update_action(4)
            #else:
                #self.state == "Idle"
        else:
            if not self.alive:
                
                self.death_timer()  
                self.update_action(10)            
    def Screen_Collision(self):
        if self.hitbox_rect.right + self.dx > WIDTH:
            self.dx = 0
        if self.hitbox_rect.left + self.dx < 0:
            self.dx = 0
        if self.hitbox_rect.top + self.dy < 0:
            self.dy = 0
        if self.hitbox_rect.bottom + self.dy > HEIGHT:
            self.dy = 0         
    def Barrel_Collision(self,sprites):
        offset = 16
        y_offset_up = 8
        y_offset_down = -2
        hb_offset = 24
        for barrel in sprites:
            if self.hitbox_rect.colliderect(barrel.rect):
                #print("Collision w/ barrel")
                if self.dx > 0:
                    self.rect.right  = barrel.rect.left+offset     
                    self.hitbox_rect.right = barrel.rect.left 
                    self.hb_rect.right = barrel.rect.left
                elif self.dx < 0:
                    self.rect.left  = barrel.rect.right-offset     
                    self.hitbox_rect.left = barrel.rect.right
                    self.hb_rect.left = barrel.rect.right

                elif self.dy > 0:  
                    self.rect.bottom  = barrel.rect.top-y_offset_down     
                    self.hitbox_rect.bottom = barrel.rect.top 
                    self.hb_rect.bottom = barrel.rect.top
                elif self.dy < 0:
                    self.rect.top  = barrel.rect.bottom-y_offset_up     
                    self.hitbox_rect.top = barrel.rect.bottom 
                    self.hb_rect.top  = barrel.rect.bottom+ hb_offset

    def Obs_Collision(self,obs):
        offset = 16
        y_offset_up = 8
        y_offset_down = -2
        hb_offset = 24
        for obstacle in obs:
            if self.hitbox_rect.colliderect(obstacle.hitbox_rect):
                if self.dx > 0:
                    self.rect.right  = obstacle.rect.left+offset     
                    self.hitbox_rect.right = obstacle.rect.left 
                    self.hb_rect.right = obstacle.rect.left
                elif self.dx < 0:
                    self.rect.left  = obstacle.rect.right-offset     
                    self.hitbox_rect.left = obstacle.rect.right
                    self.hb_rect.left = obstacle.rect.right


                elif self.dy > 0:  
                    self.rect.bottom  = obstacle.hitbox_rect.top-y_offset_down     
                    self.hitbox_rect.bottom = obstacle.hitbox_rect.top 
                    self.hb_rect.bottom = obstacle.hitbox_rect.top
                elif self.dy < 0:
                    self.rect.top  = obstacle.rect.bottom-y_offset_up     
                    self.hitbox_rect.top = obstacle.rect.bottom 
                    self.hb_rect.top = obstacle.rect.bottom+ hb_offset

    def inputs(self):
        if self.health <= 0:
            self.alive = False
            
            
            
            
        self.dx = 0
        self.dy = 0
        self.speed = 3
        if self.state == "Walk":
            if self.direction == "Left":
                self.dx = -self.speed
            elif self.direction == "Right":
                self.dx = self.speed
            else:
                self.dx = 0

            if self.direction == "Up":
                self.dy = -self.speed
            elif self.direction == "Down":
                self.dy = self.speed
                
            else:
                self.dy = 0
            

        #self.Screen_Collision()
        
        
        
        self.rect.x += self.dx
        self.hitbox_rect.x += self.dx
        self.hitbox_rect.y += self.dy
        self.hb_rect.x += self.dx
        self.hb_rect.y += self.dy
        self.rect.y += self.dy
        self.direction_animation()
        self.shoot_timer()
        self.reload()
        self.hit_timer()
        self.Final_Will_and_Test()
        
            
    def custom_draw(self,surf,dt):
        for bullet in self.bullets:
            bullet.draw(surf)

        if self.direction == "Left":
            

            
            surf.blit(pygame.transform.flip(self.image,True,False),self.rect)
        else:
            surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)
        #pygame.draw.rect(surf,"DarkGreen",self.hb_rect,1,1)
       
        
class NPC(pygame.sprite.Sprite):
    def __init__(self,char, pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load(f"game_project/img/{char}/front.png")
        self.rect = self.image.get_rect(topleft=(pos))
        x = self.rect.x
        y = self.rect.y 
        self.hitbox = pygame.Surface((24,12))
        self.hitbox_rect = self.hitbox.get_rect(topleft=(x+6,y+24))
    def custom_draw(self,surf,dt):

        surf.blit(self.image,self.rect)
        #surf.blit(self.hitbox_surf,self.hitbox_rect)
        
        #pygame.draw.rect(surf,RED,self.hitbox_rect,1,1)         
        

class PerspectiveGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()


    def draw(self, surface):
        sorted_sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.bottom)

        for sprite in sorted_sprites:
            if hasattr(sprite, "custom_draw"):
                sprite.custom_draw(surface, sprite.rect)
            else:
                surface.blit(sprite.image, sprite.rect)

    def update(self, dt):
    
        for sprite in self.sprites():
            sprite.update(dt)
