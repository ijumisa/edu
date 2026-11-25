import random
import sys
import pygame
#初期化
pygame.init()
yoko,tate = 600,500
FPS = 60 #何枚の絵を表示するか
screen = pygame.display.set_mode((yoko,tate))
pygame.display.set_capsiton("モグラたたき") #表示される文字
clock = pygame.time.clock() #時間
font = pygame.font.SysFont("msgothic", 28) #文字
#色決め　（赤、緑、青）
BG =COLOR =(120,190,90)#背景　草地
HOLE = COLOR = (60,40,20)#穴
MOLE = COLOR = (150,95,45)#モグラ
HIT = COLOR = (220,70,70)#叩かれたとき
TEXT = COLOR = (255,255,255)#文字
#穴の座標　3*3のマス目
holes =[] #穴の座標カードを9枚入れるためのケース
for  tate_ind in range(3):
    for yoko_ind in range(3):
        X = 130+yoko_ind*170
        y = 150+tate_ind*115
        holse.append((x,y))

HOLE_RADIUS =38
MOKE_RADIUS =30
#モグラの状態 Noneは不在　dictは出現中
active_mole=None
spawa_cooldown = 0.8 #次のモグラが出るまでの待ち時間（秒）

score=0 #初期化してる
time_left=30.0 #制限時間

running=True
while running
dt=clock.tick(FPS)/1000.0 #画面の更新スピードを一定に保つ＋何ミリ秒たったか教える
#イベント処理
for event in pygame event.get():#イベントのリストを取り出す
if event.typ


