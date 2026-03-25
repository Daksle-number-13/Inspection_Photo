from PIL import Image

# 한국 전통 단청 팔레트
COLORS = {
    'B': (27,  42,  94),    # 남청색 배경 (청기와)
    'C': (210, 165, 60),    # 단청 금색 (카메라 몸체)
    'D': (100, 75,  20),    # 진한 금색 (그림자/테두리)
    'L': (58,  140, 128),   # 청자 녹청 (렌즈)
    'R': (140, 210, 200),   # 청자 연청 (렌즈 반사)
    'X': (185, 35,  35),    # 단청 빨강 (포인트)
    'W': (250, 243, 210),   # 한지 미색 (내부 밝은 면)
    'G': (180, 140, 45),    # 중간 금색
}

# 32x32 픽셀 아트 (배율 적용 시 선명함)
grid = [
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBXXXBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBXXXXX BBBBBBBBBBBBBBBBBBBBBBB",
    "BDDDDDDDDDDDDDDDDDDDDDDDDDDDDBB",
    "BDCCCCCCCCCCCCCCCCCCCCCCCCCCCCDB",
    "BDCWWWWWWWWWWWWWWWWWWWWWWWWWCDB",
    "BDCWDDDDDDDDDDWWWWWWWWWWWWWWCDB",
    "BDCWDLLLLLLLLDDWWWWXWWWWWWWWCDB",
    "BDCWDLRRRRRLLDDWWWWWWWWWWWWWCDB",
    "BDCWDLRWWRRLLDDWWWWWWWWWWWWWCDB",
    "BDCWDLRRRRRLLDWWWWWWWWWWWWWWCDB",
    "BDCWDLLLLLLLLDDWWWWWWWWWWWWWCDB",
    "BDCWDDDDDDDDDDWWWWWWWWWWWWWWCDB",
    "BDCWWWWWWWWWWWWWWWWWWWWWWWWWCDB",
    "BDCWWWWWWWWWWWWWWWWWWWWWWWWWCDB",
    "BDCCCCCCCCCCCCCCCCCCCCCCCCCCCCDB",
    "BDDDDDDDDDDDDDDDDDDDDDDDDDDDDBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
]

# 더 정밀한 32x32 그리드로 재설계
B,C,D,L,R,X,W,G = 'B','C','D','L','R','X','W','G'

grid32 = [
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,X,X,X,X,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,X,C,C,X,X,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,X,X,X,X,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,B],
    [B,D,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,D,B],
    [B,D,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,D,D,D,D,D,D,D,D,D,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,L,L,L,L,L,L,L,D,D,W,W,W,X,X,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,L,R,R,R,R,L,L,D,W,W,W,W,X,X,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,L,R,W,R,R,L,L,D,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,L,R,R,R,L,L,L,D,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,L,L,L,L,L,L,L,D,D,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,D,D,D,D,D,D,D,D,D,D,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B],
    [B,D,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,D,B],
    [B,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,B],
    [B,B,B,B,D,C,C,C,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,C,C,C,D,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],
]

def make_icon(size):
    SCALE = size // 32
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    for y, row in enumerate(grid32):
        for x, key in enumerate(row):
            color = COLORS[key] + (255,)
            for dy in range(SCALE):
                for dx in range(SCALE):
                    img.putpixel((x * SCALE + dx, y * SCALE + dy), color)
    return img

make_icon(192).save('/home/user/inspection-photo/icon-192.png')
make_icon(512).save('/home/user/inspection-photo/icon-512.png')
print("done")
