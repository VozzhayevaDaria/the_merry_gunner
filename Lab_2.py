from math import *


def to_radians(angle):
    return angle * (pi / 180)


def len_vector(Ax, Ay, Ax_O, Ay_O):
    return ((Ax - Ax_O) ** 2 + (Ay - Ay_O) ** 2) ** 0.5


def angle_between_vectors(Ax, Ay, Ax_O, Ay_O, Bx, By, Bx_O, By_O):
    cos_alpha = ((Ax - Ax_O) * (Bx - Bx_O) + (Ay - Ay_O) * (By - By_O)) / (
                len_vector(Ax, Ay, Ax_O, Ay_O) * len_vector(Bx, By, Bx_O, By_O))
    #print(cos_alpha)
    if cos_alpha > 1 : return 0
    if cos_alpha < -1: return pi
    return acos(cos_alpha)


with open('input.txt', 'r') as f:
    Vx, Vy = map(float, f.readline().split())
    Ax, Ay = map(float, f.readline().split())
    Mx, My = map(float, f.readline().split())
    Wx, Wy = map(float, f.readline().split())

angle_A_W = angle_between_vectors(Ax, Ay, 0, 0, Wx, Wy, Vx, Vy)
flag = 0
if to_radians(30) <= abs(angle_A_W) <= to_radians(150):
    flag = 1

if flag:
    if abs(angle_between_vectors(-Ay, Ax, 0, 0, Wx, Wy, 0, 0)) < (pi / 2):
        print(angle_between_vectors(-Ay, Ax, 0, 0, Wx, Wy, Vx, Vy))
        flag = 1
    else:
        flag = -1

betta = 90 - angle_A_W * (180 / pi)

mast_corner = acos(1 / ((Mx ** 2 + My ** 2 + 1) ** 0.5)) * (pi / 180)

phrase = '0000'
with open('output.txt', 'w') as f:
    f.write(str(flag) + '\n')
    if flag != 0:
        f.write(str(betta) + '\n')
        f.write(str(mast_corner) + '\n')
        f.write(phrase)
