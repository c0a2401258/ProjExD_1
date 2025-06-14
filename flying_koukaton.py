import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #Surface生成
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect() #こうかとんのRect
    kk_rct.center = 300, 200 #こうかとん中心座標
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0]) #1枚目
        screen.blit(bg_img2, [-x+1600, 0]) #2枚目
        screen.blit(bg_img, [-x+3200, 0]) #3枚目
        screen.blit(kk_img, kk_rct) #こうかとん表示
        kk_lst = pg.key.get_pressed() #キーの押下状態の取得
        
        a = -1 
        b = 0
        if kk_lst[pg.K_UP]: #上移動
            b = -1
        if kk_lst[pg.K_DOWN]: #下移動
            b = 1
        if kk_lst[pg.K_RIGHT]: #右移動
            a = 1
            b = 0
        kk_rct.move_ip((a, b))
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()