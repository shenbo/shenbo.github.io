#%% 找出 `oh-my-posh` 用到的特殊字符
import os, re

def get_posh_symbols(root):
    # 找到所有配置文件
    files = []
    # - 默认配置文件
    default_file = os.path.join(root, 'defaults.ps1') 
    files.append(default_file)
    
    # - 主题配置文件
    themes_dir = os.path.join(root, 'Themes')
    for parent, dirnames, filenames in os.walk(themes_dir):
        for filename in filenames:
            filedir = os.path.join(parent, filename)
            files.append(filedir)
    print('All config files:\n ', '\n  '.join(files))

    # 找到所有可能的 powerline 字符
    symbols = []
    for file in files:
        with open(file, 'r', encoding='utf8') as f:
            res = f.read(50000)
            chars = re.findall("0x[0-9A-F]{4}", res)
            symbols.extend(chars)
    # - 去掉重复的，排序
    symbols = sorted(list(set(symbols)))
    # - 打印
    for i in symbols:
        print(f'{  i:8s} {chr(int(i, base=16)):4s}')
    
    return symbols

posh_root = r'C:\Users\shenbo\scoop\apps\oh-my-posh\current'
posh_symbols = get_posh_symbols(posh_root)


#%% 显示 powerline 字符
from PIL import  Image,ImageDraw,ImageFont

ttf = r"C:\Users\shenbo\AppData\Local\Microsoft\Windows\Fonts\JetBrainsMono-Regular.ttf"
ttfont = ImageFont.truetype(ttf, 16)

dict = {'0x00BB': 'Right-Pointing Double Angle Quotation Mark',
        '0x2191': 'Upwards Arrow',
        '0x2193': 'Downwards Arrow',
        '0x2262': 'Not Identical To',
        '0x2263': 'Strictly Equivalent To',
        '0x250C': 'Box Drawings Light Down And Right',
        '0x2514': 'Box Drawings Light Up And Right',
        '0x25B6': 'Black Right-Pointing Triangle',
        '0x25F7': 'White Circle With Upper Right Quadrant',
        '0x26A1': 'High Voltage Sign',
        '0x276F': 'Heavy Right-Pointing Angle Quotation Mark Ornament',
        '0x279C': 'Heavy Round-Tipped Rightwards Arrow',
        '0x2A2F': 'Vector Or Cross Product',
        '0xE0A0': 'Version Control Branch',
        '0xE0A1': 'LN (line) Symbol',
        '0xE0A2': 'Closed Padlock',
        '0xE0B0': 'Rightwards Black Arrowhead',
        '0xE0B1': 'Rightwards Arrowhead',
        '0xE0B2': 'Leftwards Black Arrowhead',
        '0xE0B3': 'Leftwards Arrowhead',
        '0xE606': 'Python Logo',
        '0xF09B': 'Github Logo',
        '0xF171': 'Bitbucket Logo',
        '0xF296': 'GitLab Logo',
        '0x0000': '',
        '0x27E9': 'Mathematical Right Angle Bracket',
        '0x2260': 'Not Equal To',
        '0x2261': 'Identical To',
        '0x2717': 'BALLOT X'
        }

def show_posh_fonts():    
    im = Image.new('RGBA', (600, 600), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    txt = '\n'.join([f'{i} {chr(int(i, base=16))} {dict[i]}' for i in dict])
    print(txt)

    draw.text((5,5), txt, fill=(0,0,0), font=ttfont)
    im.show()

show_posh_fonts()


#%% 打印所有 unicode 字符
from PIL import  Image, ImageDraw, ImageFont

ttfont = ImageFont.truetype(ttf, 16)

def show_all_fonts(list):
    im = Image.new('RGBA', (1600, 800), (255, 255, 255))
    
    for st, x, y in list:
        txt = ''
        for i in range(st, st + 0x0100):
            if i % 16 == 0:
                txt += f'\n {hex(i):6s} '
            txt += f'{chr(i):2s}'
        print(txt)

        draw = ImageDraw.Draw(im)
        draw.text((x, y+20), txt, fill=(0,0,0), font=ttfont)
    im.show()

list = [[0x2100, 0, 0],
        [0x2200, 400, 0],
        [0x2300, 800, 0],
        [0x2400, 1200, 0],
        [0x2500, 0, 400],
        [0x2600, 400, 400],
        [0x2700, 800, 400],
        [0xE000, 1200, 400],
]

show_all_fonts(list)
