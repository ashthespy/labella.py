
CATEGORY_10 = [
        '#1f77b4',
        '#ff7f0e',
        '#2ca02c',
        '#d62728',
        '#9467bd',
        '#8c564b',
        '#e377c2',
        '#7f7f7f',
        '#bcbd22',
        '#17becf',
        ]

CATEGORY_20 = [
        '#1f77b4',
        '#aec7e8',
        '#ff7f0e',
        '#ffbb78',
        '#2ca02c',
        '#98df8a',
        '#d62728',
        '#ff9896',
        '#9467bd',
        '#c5b0d5',
        '#8c564b',
        '#c49c94',
        '#e377c2',
        '#f7b6d2',
        '#7f7f7f',
        '#c7c7c7',
        '#bcbd22',
        '#dbdb8d',
        '#17becf',
        '#9edae5',
        ]

def color_code(i, colorscale=CATEGORY_10):
    return colorscale[i%len(colorscale)]

def hex2dec(s):
    return int(s, 16)

def hex2rgb(code):
    if code[0:1] == '#':
        code = code[1:]
    rgb = (hex2dec(code[:2]), hex2dec(code[2:4]), hex2dec(code[4:6]))
    return rgb

def hex2rgbstr(code):
    rgb = hex2rgb(code)
    rgbstr = ', '.join([str(x) for x in rgb])
    return 'rgb(%s)' % rgbstr

