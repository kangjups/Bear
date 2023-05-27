# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:14:42 2023

@author: angel
"""

import pygame 
import random
# Head, body, tail
class cls_card:
    def __init__(self,img,name,energy,damage,head,body,tail):
        self.img = pygame.image.load(img)
        self.name = name
        self.energy = energy
        self.damage = damage
                
        
        self.head = head
        self.body = body
        self.tail = tail
        
        self.count = 0
        self.card_time = 0
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        
        self.font = pygame.font.SysFont(None,30)
     
    def time(self):
        self.count += 1
        if self.count >= 60 :
            self.card_time += 1
            self.count = 0
            
    def screen(self,screen):
        screen.blit(self.font.render(str(self.card_time),True,self.BLACK),(self.x,self.y))



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
    
    card_sword = cls_card("소드 타격.png","card_sword",3,4,"red","red","red")
    card_defending = cls_card("수비.png","card_sword",3,4,"red","red","green")
    card_arrow = cls_card("애로우.png","card_sword",3,4,"red","green","green")
    card_search = cls_card("탐색.png","card_sword",3,4,"red","green","red")
    card_bomb = cls_card("폭탄 펑!.png","card_sword",3,4,"red","green","yellow")
    
    #all_cards = ["card_sword","card_defending","card_arrow","card_search","card_bomb"]
   # my_cards = ["card_sword","card_defending","card_arrow","card_search"]
    
    card_1 =  card_sword
    card_2 = card_defending
    card_3 = card_arrow
    card_4 = card_search
    
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
                        return position,card_1,card_2,card_3,card_4
                        
                if event.key == pygame.K_d: 
                    boxs[position] = '-'
                    position += 1
                    if position >= len(boxs):
                        position -= 1 
                        
                    else :
                        pygame.quit()
                        return position,card_1,card_2,card_3,card_4
                        
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
        
    def re_img(self,img):
        self.img = pygame.image.load(img)
        
    def screen(self,screen):
        screen.blit(self.img,(self.x,self.y))
        screen.blit(self.hp_img,(self.x+80,self.y+170))
        screen.blit(self.name_img,(self.x+20,self.y+170))
        
    def hp_change(self,hp):
        self.hp -= hp
        self.hp_img = self.font.render(str(self.hp),True,self.BLACK)
        
class cls_text_create:
    def __init__(self,name,text,x,y):
        
        self.RED = (255,0,0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.font = pygame.font.SysFont(None,45)
        
        self.name = name
        self.text = text
        self.text_img = self.font.render(str(self.text),True,self.BLACK)
    
        self.x = x
        self.y = y
            
    def screen(self,screen):
        screen.blit(self.text_img,(self.x,self.y))
    
    def text_change(self,text):
        #self.text_img = self.font.render(self.name + str(self.text),True,self.BLACK)
        self.text_img = self.font.render(str(self.text),True,self.BLACK)

def fn_fight(hp,energy,ex,gold,card_1,card_2,card_3,card_4):
    pygame.init()
    screen_width =800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    back = pygame.image.load("back.png")
    
    player = cls_character("man_0.png","ban",280,300,hp,20)
    woulf = cls_character("nemo_0.png","nemo",580,300,100,10)
    
    ba = pygame.image.load("ba.png")
    ba_x = 50
    ba_y = 300
    
    ex = cls_text_create("Ex :",ex,110,23)
    gold = cls_text_create("gold :",gold,280,23)
    energy = cls_text_create("energy :",energy,50,ba_y + 170)
    max_energy = cls_text_create("energy :",energy,50,ba_y + 170)    
    
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
    
    red_ball = pygame.image.load("red_ball.png")
    blue_ball = pygame.image.load("blue_ball.png")
    green_ball = pygame.image.load("green_ball.png")
    
    balls = []
    
    
    Time = 0
    t = 0
    ball_time = 0
    
    running = True
    while running:
        
        t += 1 
        if t >= 460 :
            Time += 0
            if energy.text < 4:    
                energy.text += 1
                energy.text_change(energy.text)
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
                        balls.append("green")
                        green_position = random.randint(ba_x + 8 ,ba_x + 100)
                        
                    elif sword == sword_down and sword_x_pos + 25 >= yellow_position and sword_x_pos + 25  <= yellow_position + 50:
                        #balls.append(1)
                        yellow_position = random.randint(ba_x + 8 ,ba_x + 100)
                        
                    elif sword == sword_left and sword_y_pos + 25 >= red_position and sword_y_pos + 25  <= red_position + 50:
                        #woulf.hp_change(player.damage)
                        balls.append("red")
                        red_position = random.randint(ba_y + 8 ,ba_y + 100)
                        
                    elif sword == sword_right and sword_y_pos + 25 >= blue_position and sword_y_pos + 25  <= blue_position + 50:
                        balls.append("blue")
                        blue_position = random.randint(ba_y + 8 ,ba_y + 100)
                    
                    else :
                        print("스킬 실패")
                        balls.clear()
                        
                   
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
        
        if len(balls) >= 3:
            player.re_img("man_1.png")
            #ball_time += 1
            
            #if ball_time >= 25:
            print("마지카 매법")
            
            if balls[0] == card_1.head and balls[1] == card_1.body and balls[2] == card_1.tail and energy.text > card_1.energy:                  
                energy.text -= card_1.energy
                woulf.hp_change(player.damage+card_1.damage)
                
            elif balls[0] == card_2.head and balls[1] == card_2.body and balls[2] == card_2.tail and energy.text > card_2.energy :                  
                energy.text -= card_2.energy
                woulf.hp_change(player.damage+card_2.damage)
                
            elif balls[0] == card_3.head and balls[1] == card_3.body and balls[2] == card_3.tail and energy.text > card_3.energy :                  
                energy.text -= card_3.energy
                woulf.hp_change(player.damage+card_3.damage)
                
            elif balls[0] == card_4.head and balls[1] == card_4.body and balls[2] == card_4.tail and energy.text > card_4.energy :                  
                energy.text -= card_4.energy
                woulf.hp_change(player.damage+card_4.damage)
                
            player.re_img("man_0.png")
            balls.clear()
               # ball_time = 0
                
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
        energy.screen(screen)
        gold.screen(screen)
        ex.screen(screen)
        
        screen.blit(ba,(ba_x,ba_y))
        
        for i in range(len(balls)):
            
            if balls[i] == "green" :
                screen.blit(green_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
                
            if balls[i] == "blue" :
                screen.blit(blue_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
                
            if balls[i] == "red" :
                screen.blit(red_ball,(ba_x + 20 + (i*40) ,ba_y + 105))
                   
                
        screen.blit(green,(green_position, ba_y + 2))
        screen.blit(yellow,(yellow_position, ba_y + 140))
        screen.blit(red,(ba_x + 2, red_position))
        screen.blit(blue,(ba_x + 140, blue_position))
        
        screen.blit(sword,(sword_x_pos,sword_y_pos))
        
        screen.blit(card_1.img,(29,600))
        screen.blit(card_2.img,(229,600))
        screen.blit(card_3.img,(429,600))
        screen.blit(card_4.img,(629,600))
        
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
            
    inv = {"energy" : 1,"gold" : 0,"ex" : 0}
    hp = 100
    gold = 0
    ex = 0
    print(position,"0")
    # 루프
    while running:
       
        position,card_1,card_2,card_3,card_4 = fn_main(floor,position,hp,inv["ex"],inv["gold"])
       
        
        if position == None :
            break
        if boxs[position] == 'enemy':
            gold,ex,hp = fn_fight(hp,inv["energy"],inv["ex"],inv["gold"],card_1,card_2,card_3,card_4)
            
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
    
    
    
    
    
    
    
    