import pygame 
import random
import time
from datetime import datetime
#1 게임 초기화
pygame.init()

#2 게임창 옵션 설정
size = [450,800]
screen = pygame.display.set_mode(size)

title = "Bum Game"
pygame.display.set_caption(title)

bgimg = pygame.image.load("/Users/bumlee/Desktop/bggg.png")

#event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(bgimg, (0, 0))
    pygame.display.update()
    pygame.display.flip()



#3 게임 내 필요한 설정
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self,address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else :
             self.img = pygame.image.load(address)
             self.dx, self.dy = self.img.get_size()
    def change_size(self, dx, dy):
        self.img = pygame.transform.scale(self.img,(dx,dy))
        self.dx, self.dy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x,self.y))

# a.x-b.dx <= b.x <= a.x+a.dx
# a.y-b.dy <= b.y <= a.y+a.dy
        

def crash(a, b):
    if (a.x-b.dx <+ b.x) and (b.x <= a.x+a.dx):
        if (a.y-b.dy <= b.y) and (b.y <= a.y+a.dy):
            return True
        else : return False
    else :
        return False

  
dd = obj()
dd.put_img("/Users/bumlee/Desktop/dd1.png")        
dd.change_size(100,100)
dd.x = round(size[0]/2- dd.dx/2)
dd.y = size[1] -dd.dy- 45
dd.move = 6  #움직이는 속도

left_go = False
right_go = False
space_go = False

m_list = []
a_list = []

    #class 이전 코드 (dd = pygame.image.load("/Users/bumlee/Desktop/dd1.png").convert_alpha()
        #dd = pygame.transform.scale(dd,(70,90))
        #dd_dx, dd_dy = dd.get_size()
        #dd_x = round(size[0]/2- dd_dx/2)
        #dd_y = size[1] -dd_dy- 45

black = (0,0,0)
white = (255,255,255)
k = 0

GO = 0
바이러스처치 = 0
바이러스놓친개수ㅠㅠ = 0

#4-0 대기화면
SB = 0
while SB == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    SB = 1
    font = pygame.font.Font("/Users/bumlee/Desktop/textt/textfont/BM Hanna Pro/texttt.otf", 25)
    text = font.render("스페이스바를 눌러 게임을 시작하세요!", True,(0,0,0))
    screen.blit(text, (40,round(size[1]/2-50)))
    pygame.display.flip()

#4 메인 이벤트

start_time = datetime.now()
SB = 0
while SB == 0:
    #왼4 오3
    #4-1 FPS 설정
    clock.tick(60)

    #4-2 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                    space_go = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                    space_go = False
            
                
    #4-3 입력, 시간에 따른 변화
    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())
    
    if left_go == True:
        dd.x -= dd.move
        if dd.x <= 0:
            dd.x = 0
    elif right_go == True:
        dd.x += dd.move
        if dd.x >= size[0] - dd.dx:
            dd.x = size[0] - dd.dx
    
    
    
    if space_go == True and k % 10 == 0:
        mm = obj()
        mm.put_img("/Users/bumlee/Desktop/ddd.png")        
        mm.change_size(80,90)
        mm.x = round(dd.x + dd.dx/2 - mm.dx/2)
        mm.y = dd.y - mm.dy - 10
        mm.move = 8  #움직이는 속도
        m_list.append(mm)
        
    k += 1  
    d_list = []   
    for i in range(len(m_list)):
       m = m_list[i]
       m.y -= m.move
       if m.y <= -m. dy:
           d_list.append(i)
    for d in d_list:
        del m_list[d]
    
    
    if random.random() > 0.91:
        aa= obj()
        aa.put_img("/Users/bumlee/Desktop/aaaa.png")
        aa.change_size(60,60)
        aa.x = random.randrange(0, size[0]-aa.dx-round(dd.dx/2))
        aa.y = 10
        aa.move = 7
        a_list.append(aa)
    
    d_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]:
           d_list.append(i)
    for d in d_list:
        del a_list[d]
        바이러스놓친개수ㅠㅠ+=1
        
    dm_list = []
    da_list = []
    for i in range(len(m_list)):
        for j in range(len(a_list)):
            m = m_list[i]
            a = a_list[j]
            if crash(m,a) == True :
                dm_list.append(i)
                da_list.append(j)
                
    dm_list = list(set(dm_list))
    da_list = list(set(da_list)) 
    
    for dm in dm_list:
        del m_list[dm]
    for da in da_list:
        del a_list[da]
        바이러스처치+=1 
        
        
        
    for i in range(len(a_list)):
        a = a_list[i] 
        if crash(a,dd) == True:
            SB = 1
            GO = 1        
   
    #4-4 그리기
    screen.fill(black)
    dd.show()
    for m in m_list:
        m.show()
    
    for a in a_list:
        a.show()
        
    font = pygame.font.Font("/Users/bumlee/Desktop/textt/textfont/BM Hanna Pro/texttt.otf", 20)
    text_kill = font.render("바이러스처치! : {} 놓친바이러스ㅠ: {}".format(바이러스처치, 바이러스놓친개수ㅠㅠ), True,(255,255,0))
    screen.blit(text_kill, (10,5))
    
    text_time = font.render("time : {}".format(delta_time), True,(255,255,255))
    screen.blit(text_time, (size[0]-100, 5))
    #4-5 업데이트
    pygame.display.flip()
   
    
#5 게임 종료
while GO == 1:
    clock.tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GO = 0
    font = pygame.font.Font("/Users/bumlee/Desktop/textt/textfont/BM Hanna Pro/texttt.otf", 40)
    text = font.render("GAME OVER", True,(255,0,0))
    screen.blit(text, (120,round(size[1]/2-50)))
    pygame.display.flip()
    

pygame.quit()   