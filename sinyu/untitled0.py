# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:36:39 2023

@author: jamppo
"""
import pygame
import random

def fn_fight():
    pygame.init()
    
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    back = pygame.image.load("back.png")
    player = pygame.image.load("man_0.png")
    
    g = pygame.image.load("g.png")
    o = pygame.image.load("o.png")
    
    x = 100
    y = 210
    
    abc = []
    tx = "/"
    dd = False
    
    ss = ["aaa","www","sss"]
    
    aa = random.choice(ss)
    
    running = True
    while running:
      # df = clock.tick(20)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
            if event.type == pygame.KEYDOWN:
                print(abc)
                if event.key == pygame.K_p: 
                    running = False
                    
                if event.key == pygame.K_w:
                    abc.append("w")
                    
                    
                if event.key == pygame.K_s:
                    abc.append("s")
                    
                    
                if event.key == pygame.K_a:
                    abc.append("a")
                
                  
                if event.key == pygame.K_d:
                    abc.append("d")
                if event.key == pygame.K_b:
                    abc.append("b")
                if event.key == pygame.K_g:
                    abc.append("g")
                if event.key == pygame.K_o:
                    abc.append("o")
                if event.key == pygame.K_c:
                    abc.append("c")
                if event.key == pygame.K_k:
                    abc.append("k")
                 
               
                    
                if event.key == pygame.K_SPACE:
                    print(aa)
                # 캐릭터 움직임     
                    for i in range(len(abc)):
                        tx += abc[i]
                    abc.clear()    
                    print(tx)
                    if tx == "/ww" :
                        print("웅횽ㄹㄴ")
                        
                    elif tx == "/back" :
                        x -= 40
                        print(x,y)
                    elif tx == "/go":
                        dd = True
                        x += 30
                        print(x,y)
                        screen.blit(g,(20,200))
                        screen.blit(o,(60,200))
                        
               # 적이 내는 텍스트         
                    elif tx == "/"+aa :
                        print("ㅇㅇ")
                        aa = random.choice(ss)
                    tx = "/"                        
                        
         
        
        screen.blit(back,(0,0))
        if dd == True :      
            screen.blit(g,(20,200))
            screen.blit(o,(60,200))
        screen.blit(player,(x,y))
        
        pygame.display.update()
    
    pygame.quit()

fn_fight()