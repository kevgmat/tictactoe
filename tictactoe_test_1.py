# a = 1
# b = 2
# c = 1
# d = 2
# e = 1
# f = 4
# g = 5
# h = 6
# i = 1
#
# game = [[a,b,c],
#         [d,e,f],
#         [g,h,i]]
#
# case_1 = (a==b==c)
# case_2 = (d==e==f)
# case_3 = (g==h==i)
# case_4 = (a==d==g)
# case_5 = (b==e==h)
# case_6 = (c==f==i)
# case_7 = (a==e==i)
# case_8 = (c==e==g)
#
# if case_1 or case_2 or case_3 or case_4 or case_5 or case_6 or case_7 or case_8:
#         print("won")
# else:
#         print("lost")
#
# import random
#
# value = random.randint(0,1)
#





import pygame
import random
import time

pygame.init()

display = pygame.display.set_mode((600,600))
display.fill((255, 255, 255))

value = random.randint(0,1)
#0 = x
#1 = o
if value == 0:
        a = "o`"
else:
        a = "x"
print("its turn of ", a)
# while not done:
black = pygame.Color((0,0,0))
pygame.draw.line(display , black,(200,0),(200, 600), width = 2)
pygame.draw.line(display, black, (400,0),(400, 600), width = 2)
pygame.draw.line(display, black, (0, 200),(600, 200), width = 2)
pygame.draw.line(display, black, (0, 400),(6000, 400), width = 2)
pygame.display.update()


a_box = pygame.Rect(0,0, 200,200)
b_box = pygame.Rect(200,0,200,200)
c_box = pygame.Rect(400,0,200,200)
d_box = pygame.Rect(0,200,200,200)
e_box = pygame.Rect(200,200,200,200)
f_box = pygame.Rect(400,200,200,200)
g_box = pygame.Rect(0,400,200,200)
h_box = pygame.Rect(200,400,200,200)
i_box = pygame.Rect(400,400,200,200)

def message(msg, color, width_location, height_location):
        mesg = pygame.font.SysFont("ariel", 300).render(msg, True, color)
        display.blit(mesg, (width_location+40, height_location))
        pygame.display.update()
a = -1
b = -2
c = -3
d = -4
e = -5
f = -6
g = -7
h = -8
i = -9

game = [[a,b,c],
        [d,e,f],
        [g,h,i]]
done = False
while not done:
        for event in pygame.event.get():
                mousepos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                        pygame.quit()
                        done = True
                # print(mousepos)
                x = mousepos[0]
                y = mousepos[1]
                if 0<=x<=200 and 0<=y<=200:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if a_box.collidepoint(event.pos):
                                        if value%2 ==0 :
                                                message("o",black,0,0)
                                                game[0][0] = "o"
                                        else:
                                                message("x",black,0,0)
                                                game[0][0] = "x"
                                value+=1
                elif 200<=x<=400 and 0<=y<=200:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if b_box.collidepoint(event.pos):
                                        if value%2 ==0 :
                                                message("o",black,200,0)
                                                game[0][1] = "o"
                                        else:
                                                message("x",black,200,0)
                                                game[0][1] = "x"
                                value +=1
                elif 400<=x<=600 and 0<=y<=200:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if c_box.collidepoint(event.pos):
                                        if value%2 ==0 :
                                                message("o",black,400,0)
                                                game[0][2] = "o"
                                        else:
                                                message("x",black,400,0)
                                                game[0][2] = "x"
                                value +=1
                elif 0<=x<=200 and 200<=y<=400:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if d_box.collidepoint(event.pos):
                                        if value%2 ==0 :
                                                message("o",black,0,200)
                                                game[1][0] = "o"
                                        else:
                                                message("x",black,0,200)
                                                game[1][0] = "x"
                                value +=1
                elif 200<=x<=400 and 200<=y<=400:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if e_box.collidepoint(event.pos):
                                        if value%2 ==0 :
                                                message("o",black,200,200)
                                                game[1][1] = "o"
                                        else:
                                                message("x",black,200,200)
                                                game[1][1] = "x"
                                value +=1
                elif 400<=x<=600 and 200<=y<=400:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if f_box.collidepoint(event.pos):
                                        if value % 2 == 0:
                                                message("o", black, 400, 200)
                                                game[1][2] = "o"
                                        else:
                                                message("x", black, 400, 200)
                                                game[1][2] = "x"
                                value += 1
                elif 0<=x<=200 and 400<=y<=600:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if g_box.collidepoint(event.pos):
                                        if value % 2 == 0:
                                                message("o", black, 0, 400)
                                                game[2][0] = "o"
                                        else:
                                                message("x", black, 0, 400)
                                                game[2][0] = "x"
                                value += 1
                elif 200<=x<=400 and 400<=y<=600:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if h_box.collidepoint(event.pos):
                                        if value%2 ==0 :
                                                message("o",black,200,400)
                                                game[2][1] = "o"
                                        else:
                                                message("x",black,200,400)
                                                game[2][1] = "x"
                                value +=1
                elif 400<=x<=600 and 400<=y<=600:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if i_box.collidepoint(event.pos):
                                        if value % 2 == 0:
                                                message("o", black, 400, 400)
                                                game[2][2] = "o"
                                        else:
                                                message("x", black, 400, 400)
                                                game[2][2] = "x"

                                value += 1
                a=game[0][0]
                b=game[0][1]
                c=game[0][2]
                d=game[1][0]
                e=game[1][1]
                f=game[1][2]
                g=game[2][0]
                h=game[2][1]
                i=game[2][2]

                case_1 = (a==b==c)
                case_2 = (d==e==f)
                case_3 = (g==h==i)
                case_4 = (a==d==g)
                case_5 = (b==e==h)
                case_6 = (c==f==i)
                case_7 = (a==e==i)
                case_8 = (c==e==g)

                if case_1 or case_2 or case_3 or case_4 or case_5 or case_6 or case_7 or case_8:
                        print("won")
                        done = True
                else:
                        print("lost")

        # game = [[a,b,c],
        #         [d,e,f],
        #         [g,h,i]]

if value%2==0:
        print("x won")
elif value%2 != 0:
        print("o won")
time.sleep(3)

