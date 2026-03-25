#!/usr/bin/env python3
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

# 32x32 픽셀 아트 - 여백을 확보한 현대적 카메라 아이콘
B,C,D,L,R,X,W,G = 'B','C','D','L','R','X','W','G'

grid32 = [
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 0
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 1
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 2
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 3
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 4
    [B,B,B,B,B,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,B,B,B,B,B,B],  # 5
    [B,B,B,B,B,D,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,D,B,B,B,B,B,B],  # 6
    [B,B,B,B,B,D,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 7
    [B,B,B,B,B,D,C,W,D,D,D,D,D,D,D,D,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 8
    [B,B,B,B,B,D,C,W,D,L,L,L,L,L,L,D,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 9
    [B,B,B,B,B,D,C,W,D,L,R,R,R,L,L,D,W,W,X,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 10
    [B,B,B,B,B,D,C,W,D,L,R,W,R,L,L,D,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 11
    [B,B,B,B,B,D,C,W,D,L,R,R,R,L,L,D,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 12
    [B,B,B,B,B,D,C,W,D,L,L,L,L,L,L,D,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 13
    [B,B,B,B,B,D,C,W,D,D,D,D,D,D,D,D,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 14
    [B,B,B,B,B,D,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 15
    [B,B,B,B,B,D,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,D,B,B,B,B,B,B,B],  # 16
    [B,B,B,B,B,D,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,D,B,B,B,B,B,B,B],  # 17
    [B,B,B,B,B,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,B,B,B,B,B,B,B],  # 18
    [B,B,B,B,B,B,B,B,D,C,C,C,C,B,B,B,B,B,B,B,B,B,C,C,C,D,B,B,B,B,B,B],  # 19
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 20
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 21
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 22
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 23
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 24
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 25
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 26
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 27
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 28
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 29
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 30
    [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B],  # 31
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
print("✓ 새 아이콘 생성 완료")
print("  - icon-192.png 생성")
print("  - icon-512.png 생성")
