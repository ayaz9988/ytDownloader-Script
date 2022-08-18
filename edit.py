#!/usr/bin/env python3
import curses, sys

def main(stdscr):
    scr = curses.initscr()
    scr.nodelay(1)
    curses.noecho()
    curses.raw()
    scr.keypad(1)
    buf = []
    src = 'noname.txt'
    Row, Col = scr.getmaxyx()
    x, y, curR, curC = [0] * 4
    if len(sys.argv) == 2:
        src = sys.argv[1]
    try:
        with open(sys.argv[1]) as f:
            cont = f.read().split('\n')
            cont = cont[:-1] if len(cont) > 1 else cont
            for row in cont:
                b.append([
                    ord(c) for c in row
                ])
    except:
        buf.append([])
    if len(sys.argv) == 1:
        buf.append([])

    while True:
        scr.move(0, 0)
        if curR < y:
            y = curR

        if curR >= y + Row:
            y = curR - Row + 1

        if curC < x:
            x = curC

        if curC >= x + Col:
            x = curC - Col + 1

        for row in range(Row):
            brow = row + y
            for col in range(Col):
                bcol = col + x
                try:
                    src.addch(row, col, buf[brow][bcol])
                except:
                    pass
            scr.clrtoeol()
            try:
                s.addch('\n')
            except:
                pass
        curses.curs_set(0)
        scr.move(curR - y, curC - x)
        curses.curs_set(1)
        scr.refresh()
        ch = -1
        while (ch == -1): 
            ch = scr.getch()
            if ch != ((ch) & 0x1f) and ch < 128:
                buf[curR].insert(curC, ch)
                curC += 1
            
            elif chr(ch) in ['\n', '\r']:
                line = buf[curR][curC:]
                buf[curR][:curC]
                curR += 1
                curC = 0
                buf.insert(curR, [] + line)
            
            elif ch in [8, 263]:
                if curC:
                    curC -= 1
                    del buf[curR][curC]
                elif curR:
                    line = buf[curR][curC:]
                    del buf[curR]
                    curR -= 1
                    curC = len(buf[curR])
                    buf[curR] += 1

            elif ch == curses.KEY_LEFT:
                if curC != 0:
                    curC -= 1
                elif curR > 0:
                    curR -= 1
                    curC = len(buf[curR])

            elif ch == curses.KEY_RIGHT:
                if curC < len(buf[curR]):
                    curC += 1
                elif curR < len(buf) - 1:
                    r += 1
                    curC = 0
            elif ch == curses.KEY_UP and curR != 0:
                r -= 1
            elif ch == curses.KEY_DOWN and curR < len(buf) - 1:
                r += 1

            row = buf[curR] if curR < len(buf) else None
            rowlen = len(row) if row is not None else 0
            if col > rowlen:
                curC = rowlen

            if ch == (ord('q') & 0x1f):
                sys.exit()
            
            elif ch == (ord('s') & 0x1f):
                cont = ''
                for line in buf:
                    cont += ''.join([chr(c) for c in line]) + '\n'
                with open(src, 'w') as f:
                    f.write(cont)

curses.wrapper(main)
