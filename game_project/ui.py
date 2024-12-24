import pygame
from game_project.settings import *


class UI:
    def __init__(self):

        self.top_surf = pygame.Surface((WIDTH,HEIGHT/8))
        
        self.btm_surf = pygame.Surface((WIDTH,HEIGHT/6))
        


    def top_texts(self,state,direction,moneys):
        state_txt = get_font(16).render(f"State:{state}",True,BLACK)
        self.top_surf.blit(state_txt,(22,16))
        dir_txt = get_font(16).render(f"Direction:{direction}",True,BLACK)
        self.top_surf.blit(dir_txt,(22,32))

        money = get_font(16).render(f"$:{moneys}",True,BLACK)
        self.top_surf.blit(money,(WIDTH - 64,16))



    def conditional_texts(self,text):
        txt = get_font(16).render(f"{text}",True,WHITE)
        rect = txt.get_rect(center=(WIDTH/2,32))
        
        self.top_surf.blit(txt,(rect))
    def btm_conditional_texts(self,text):
        txt = get_font(16).render(f"{text}",True,WHITE)
        rect = txt.get_rect(center=(36,32))
        
        self.btm_surf.blit(txt,(rect))
    def btm_texts(self,bullets,reload_timer):
        bullet_count = get_font(24).render(f"{bullets}/6",True,BLACK)
        self.btm_surf.blit(bullet_count,(32,32)) 
        if reload_timer > 0:
            reload_text = get_font(24).render("Reloading...", True, RED)
            self.btm_surf.blit(reload_text, (100, 32))

    def draw(self,enabled,surf,state,direction,bullets,reload_timer,moneys):
        surf.blit(self.top_surf,(0,0))
        self.top_surf.fill(GREY)

        surf.blit(self.btm_surf,(0,HEIGHT-HEIGHT/6))
        
        self.btm_surf.fill(GREY)
        if enabled:
            self.top_texts(state,direction,moneys)
            self.btm_texts(bullets,reload_timer)
        

        