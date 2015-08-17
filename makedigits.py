from PIL import Image, ImageDraw

segments = [
 ((0,  0),   (200,0)),
 ((200,0),   (200,250)),
 ((200,250), (200,500)),
 ((0,  500), (200,500)),
 ((0,  500), (0,250)),
 ((0,  250), (0,0)),
 ((0,  250), (200,250))]

w = 30
# fill values are rgb color codes
fills = {'0': "#CC0000", '1': "#404040"}

padamt = 50

def pad(pts, amt = padamt // 2 ):
    a = []
    for p in pts:
        a += (p[0]+amt, p[1]+amt)
    return a
def mkimg(v):
    im = Image.new("RGB", (200+padamt,500+padamt))
    draw = ImageDraw.Draw(im)
    
    # this is for active low displays!      

    # draw all off first
    for i in range(7):
        draw.line(pad(segments[i]), width=w, fill=fills['1'] )
    # then turn on, to make it look nicer
    for i in range(7):
        assert v[i] in '01', "Segment value must be one of 0 or 1."
        if v[i] == '0':
            draw.line(pad(segments[i]), width=w, fill=fills[v[i]] )            

    im.save('static/' + v + '.png')

for i in range(128):
    value = "{:07b}".format(i)
    
    mkimg(value)