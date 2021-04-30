import random as r
import curses as c

s = c.initscr()
c.curs_set(0)
sh, sw = s.getmaxyx()
w = c.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)
#w.border()
w.box()
s_y = sw//4
s_x = sh//2
snake = [
[s_y , s_x],
[s_y , s_x-1],
[s_y , s_x-2]
]
food = [sh//2 , sw//2]
w.addch(int(food[0]),int(food[1]), c.ACS_PI)
key = c.KEY_RIGHT
while True:
    n_k = w.getch()
    key = key if n_k == -1 else n_k
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        c.endwin()
        quit()
    n_h = [snake[0][0], snake[0][1]]
    if key == c.KEY_DOWN:
        n_h[0] += 1
    elif key == c.KEY_UP:
        n_h[0] -= 1
    if key == c.KEY_LEFT:
        n_h[1] -= 1
    if key == c.KEY_RIGHT:
        n_h[1] += 1
    snake.insert(0, n_h)
    #count =0
    if snake[0]==food:
        c.beep()
        #count +=1
        food  = None
        while food is None:
            nf = [
            r.randint(1,sh-1),
            r.randint(1,sw-1)
            ]
            food  =nf if nf not in snake else None
        w.addch(int(food[0]),int(food[1]), c.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]),int(tail[1]),' ')
    w.addch(int(snake[0][0]),int(snake[0][1]),c.ACS_CKBOARD)
#print("score :",count)
