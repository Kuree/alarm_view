css_string = ""
for i in range(128):
    css = "" 
    for j in range(7):
        if ((i & ( 1 << j)) >> j) == 1:
            css +=  "#clock .digits div.d{0:07b} .d{1},\n".format(i, 7 - j)
    if len(css) > 0:
        css = css[:-2]
        css += "{\nopacity:0;\n}\n\n";
        css_string += css

with open("static/clock.css", "w+") as f:
    f.write(css_string)
