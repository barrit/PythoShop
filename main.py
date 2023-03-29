import sys
import modules.extract as extract
import modules.plot as plot
import modules.render as render

name = 'spaceinvader'

def main(args):
    if len(args) != 3:
        print('Use 2 arguments: e(xtract), p(lot), r(ender) and the name of the object')
        return
    if args[1] == 'e':
        extract.extract(args[2])
    if args[1] == 'p':
        plot.plot(args[2])
    if args[1] == 'r':
        render.render(args[2])
    
if __name__ == '__main__':
    main(sys.argv)