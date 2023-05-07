# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:14:42 2023

@author: angel
"""

import pygame 
import random

def fn_start():
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    #pygame.display.set_caption("school")
    background = pygame.image.load("back_ground_0.png")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    
            if event.type == pygame.MOUSEMOTION:
                pass
            
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
                if event.button == 1:  # 마우스 왼쪽 클릭시
                    x_p, y_p = pygame.mouse.get_pos()    
                    if x_p > 200 and x_p < 600 and y_p > 340 and y_p < 390:
                        pygame.quit()    
                        return True
                    if x_p > 200 and x_p < 600 and y_p > 450 and y_p < 500:
                        print("setting")
                    if x_p > 200 and x_p < 600 and y_p > 540 and y_p <610:
                        pygame.quit()    
                        return False
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            
        screen.blit(background,(0,0))
        pygame.display.update()
         
    pygame.quit()

def fn_main(floor,position,hp,ex,gold): # 플레이어의 초기 x,y 위치 / 층 수 / 리스트 속 플레이어 위치
    
    pygame.init() # 게임 초기화
    
    # 게임 화면 크기  
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # 이미지 불러오기 
    back = pygame.image.load("back_ground_1.png") # 바탕화면
    event_ = pygame.image.load("event.png") # 이벤트 
    enemy = pygame.image.load("enemy.png") # 적 
    bose = pygame.image.load("bose.png") # 보스
    
    player = pygame.image.load("player.png") # 플레이어
    boxs[position] = 'player'
    
    hp = cls_text_create("Hp :",hp,100,20)
    ex = cls_text_create("Ex :",ex,200,20)
    gold = cls_text_create("gold :",gold,300,20)
    stage = cls_text_create("stage :",1,400,20)
    
    # 루프
    running = True
    while running:
        # 키보드를 누루는 이벤트가 발생했을 때 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    running = False
                
                if event.key == pygame.K_w:
                    boxs[position] = '-'
                    position += 7
                    if position >= len(boxs):
                        position -= 7 
                        
                    else :
                        pygame.quit()
                        return position
                        
                if event.key == pygame.K_d: 
                    boxs[position] = '-'
                    position += 1
                    if position >= len(boxs):
                        position -= 1 
                        
                    else :
                        pygame.quit()
                        return position
                        
          #  if event.type == pygame.MOUSEBUTTONDOWN: # 마우스의 어떤 버튼을 눌렀을때
              #  if event.button == 1:  # 마우스 왼쪽 클릭시
                 #   x, y = pygame.mouse.get_pos()
                    
          #  if event.type == pygame.MOUSEBUTTONUP:
           #     pass
            
        # 이미지 그리기 
        screen.blit(back,(0,0)) # 바탕화면
        hp.screen(screen)
        ex.screen(screen)
        gold.screen(screen)
        stage.screen(screen)
        # 박스들 
        for i in range(len(boxs)):
            if i == floor:
                floor += 7
            if i < floor :
                a = 80*(i-(floor-7)) + 120  # 길이 
                b = 800-(80*(floor/7)) -120 # 높이 
             
                if boxs[i] == 'enemy':
                    screen.blit(enemy,(a,b))
                    
                elif boxs[i] == 'event_':
                    screen.blit(event_,(a,b))
                    
                elif boxs[i] == 'bose':
                    screen.blit(bose,(a,b))
                    
                elif boxs[i] == 'player':
                    screen.blit(player,(a,b))
                    
            if i == len(boxs)-1:
                floor = 7
        
        # 업데이트
        pygame.display.update()
        
    # 초기화
    pygame.quit()                                                                    
    


class cls_character:
    def __init__(self,img,name,x,y,hp,damage):
        self.img = pygame.image.load(img)
        self.name = name
        self.x , self.y = x,y
        #self.max_hp = max_hp
        self.hp = hp
        self.damage = damage
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,30)
        self.hp_img = self.font.render(str(self.hp),True,self.BLACK)
        self.name_img = self.font.render(str(self.name),True,self.BLACK)
        
    def screen(self,screen):
        screen.blit(self.img,(self.x,self.y))
        screen.blit(self.hp_img,(self.x+80,self.y+315))
        screen.blit(self.name_img,(self.x+20,self.y+315))
        
    def hp_change(self,hp):
        self.hp -= hp
        self.hp_img = self.font.render(str(self.hp),True,self.BLACK)
        
class cls_text_create:
    def __init__(self,name,text,x,y):
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.font = pygame.font.SysFont(None,30)
        
        self.name = name
        self.text = text
        self.text_img = self.font.render(self.name + str(self.text),True,self.BLACK)
    
        self.x = x
        self.y = y
        
        
    def screen(self,screen):
        screen.blit(self.text_img,(self.x,self.y))
        

def fn_fight(hp,ex,gold):
    pygame.init()
    screen_width =800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    back = pygame.image.load("back_ground_2.png")
    
    player = cls_character("game_player.png","ban",50,150,hp,20)
    woulf = cls_character("cat.png","woulf",550,150,100,10)
    
    ex = cls_text_create("Ex :",ex,100,20)
    gold = cls_text_create("gold :",gold,200,20)
    
    ba = pygame.image.load("ba.png")
    ba_x = 75
    ba_y = 575
    
    sword_up = pygame.image.load("sword.png")
    sword_down = pygame.image.load("sword_down.png")
    sword_left = pygame.image.load("sword_left.png")
    sword_right = pygame.image.load("sword_right.png")
    
    sword = sword_up
    
    sword_x_pos = ba_x
    sword_y_pos = ba_y - 12
    sword_speed = 3
    
    green =  pygame.image.load("green.png")
    green_position = random.randint(ba_x + 8 ,ba_x + 100)
    
    yellow =  pygame.image.load("yellow.png")
    yellow_position = random.randint(ba_x + 8 ,ba_x + 100)
    
    red =  pygame.image.load("red.png")
    red_position = random.randint(ba_y + 8 ,ba_y + 100)
    
    blue =  pygame.image.load("blue.png")
    blue_position = random.randint(ba_y + 8 ,ba_y + 100)
    
    
    Time = 0
    t = 0
    
    running = True
    while running:
        
        t += 1 
        if t >= 60 :
            Time += 1
            t = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    running = False
                    
                if event.key == pygame.K_w:
                    sword = sword_up
                    sword_x_pos = ba_x
                    sword_y_pos = ba_y - 12
                    
                    
                if event.key == pygame.K_s:
                    sword = sword_down
                    sword_x_pos = ba_x
                    sword_y_pos = ba_y + 100 + 12
                    
                if event.key == pygame.K_a:
                    sword = sword_left
                    sword_x_pos = ba_x - 12
                    sword_y_pos = ba_y
                    
                    
                if event.key == pygame.K_d:
                    sword = sword_right
                    sword_x_pos = ba_x + 100 + 12
                    sword_y_pos = ba_y 
                    
                    
                if event.key == pygame.K_SPACE:
                    if sword == sword_up and sword_x_pos + 25 >= green_position and sword_x_pos + 25  <= green_position + 50:
                        woulf.hp_change(player.damage)
                        green_position = random.randint(ba_x + 8 ,ba_x + 100)
                        
                    if sword == sword_down and sword_x_pos + 25 >= yellow_position and sword_x_pos + 25  <= yellow_position + 50:
                        woulf.hp_change(player.damage)
                        yellow_position = random.randint(ba_x + 8 ,ba_x + 100)
                        
                    if sword == sword_left and sword_y_pos + 25 >= red_position and sword_y_pos + 25  <= red_position + 50:
                        woulf.hp_change(player.damage)
                        red_position = random.randint(ba_y + 8 ,ba_y + 100)
                        
                    if sword == sword_right and sword_y_pos + 25 >= blue_position and sword_y_pos + 25  <= blue_position + 50:
                        woulf.hp_change(player.damage)
                        blue_position = random.randint(ba_y + 8 ,ba_y + 100)
    
                   
        if sword == sword_up or sword == sword_down:
            sword_x_pos += sword_speed
            
            if sword_x_pos + 25 >= ba_x + 150 :
                sword_speed = -sword_speed
            if sword_x_pos + 25 <= ba_x:
                
                sword_speed = -1*sword_speed
                
        if sword == sword_left or sword == sword_right:
            sword_y_pos += sword_speed
            
            if sword_y_pos + 25 >= ba_y + 150 :
                sword_speed = -sword_speed
                
            if sword_y_pos + 25 <= ba_y:
                sword_speed = -1*sword_speed
        
        if Time >= 5:
            Time = 0 
            player.hp_change(woulf.damage)
        
        if woulf.hp <= 0 :
            pygame.quit()
            return random.randint(3,6),random.randint(4,8), player.hp
        
        if player.hp <= 0 :
            pygame.quit()
            return random.randint(3,6),random.randint(4,8), player.hp
        
        screen.blit(back,(0,0))
        
        player.screen(screen)
        woulf.screen(screen)
        gold.screen(screen)
        ex.screen(screen)
        
        screen.blit(ba,(ba_x,ba_y))
        
        screen.blit(green,(green_position, ba_y + 2))
        screen.blit(yellow,(yellow_position, ba_y + 140))
        screen.blit(red,(ba_x + 2, red_position))
        screen.blit(blue,(ba_x + 140, blue_position))
        
        screen.blit(sword,(sword_x_pos,sword_y_pos))

        pygame.display.update()
    
    pygame.quit()
   
if __name__ == "__main__":
    running = fn_start()
    
    # 박스리스트
    boxs = ['-'] * 49
    
    # 층,리스트 속 플레이어 위치
    
    floor = 7
    position = 0
    
    # 박스리스트 채우기
    for i in range(len(boxs)):
        boxs[0] = 'player' 
        boxs[len(boxs)-1] = 'bose'
        if boxs[i] == '-' :
            boxs[i] = random.choice(['enemy','event_'])
            
    inv = {"gold" : 0,"ex" : 0}
    hp = 100
    gold = 0
    ex = 0
    print(position,"0")
    # 루프
    while running:
        print(position,"1")
        position = fn_main(floor,position,hp,inv["ex"],inv["gold"])
        print(position,"2")
        
        if position == None :
            break
        if boxs[position] == 'enemy':
            gold,ex,hp = fn_fight(hp,inv["ex"],inv["gold"])
            
            inv["gold"] += gold
            inv["ex"] += ex
            
        elif boxs[position] == 'event_':
            e = random.randint(0,1)
            
            if e == 0:
                print("악마가 나타나 당신에게 말을 겁니다... 넌 무엇을 위해 싸우지? : ")
                e = int(input("정의를 위해 싸운다(0)/욕망을 위해 싸운다(1)"))
                if e == 0:
                    print("악마는 당신의 대답을 마음에 들어하지 않습니다... 악마에게 공격을 당하여 -5의 피해를 입습니다")
                    hp -= 5
                if e == 1:
                    print("악마는 당신의 대답을 마음에 들어 합니다... 악마가 당시에게 돈을 줍니다")
                    inv["gold"] += 5
                    
            if e == 1:
                print("아무 일도 없습니다")
        elif boxs[position] == 'bose':
            print("업데이트 준비중 입니다")
        
        
        if hp <= 0:
                break       
                print("게임 오버")
    
    
    
    
    
    
    
    
    