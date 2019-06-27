from chiplotle import *

plotter = instantiate_plotters()[0]

#plotter.select_pen(1)
print("wasd move, q/e pen u/d, . to quit.")

#inchar = input()
while True:
    inchar = raw_input()
    
    if inchar == 'w':
        plotter.write(hpgl.PR([(0,100)]))
    elif inchar == 'a':
        plotter.write(hpgl.PR([(-100,0)]))
    elif inchar == 's':
        plotter.write(hpgl.PR([(0,-100)]))
    elif inchar == 'd':
        plotter.write(hpgl.PR([(100,0)]))
    elif inchar == 'q':
        plotter.write(hpgl.PU([]))
    elif inchar == 'e':
        plotter.write(hpgl.PD([]))
    elif inchar == '.':
        break
                      

#plotter.write(hpgl.PD(coords))

#plotter.select_pen(0)