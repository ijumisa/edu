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


