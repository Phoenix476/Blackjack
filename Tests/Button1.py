from pgu import gui

app = gui.Desktop()
t = gui.Table()

t.tr()
t.td(gui.Label('Write a, b and c'), colspan=2)
t.tr()


# def cb():
#
# a_inp = gui.Input('')
# a_inp.connect('activate', cb)
# t.td(gui.Label('a'))
# t.td(a_inp)

t.tr()
b_inp = gui.Input('')
t.td(b_inp)


def cb():
    print('Hello!')
b = gui.Button('Long')
b.connect(gui.CLICK, cb)

t.tr()
t.td(b, colspan=1)
t.tr()


def cb():
    print('Buy')
b2 = gui.Button('Buy')
b2.connect(gui.CLICK, cb)
t.td(b2, colspan=1)
app.run(t)
