import os
FPS = 40
SCREENSIZE = (640, 640)

SKIER_IMAGE_PATHS = [
    os.path.join(os.getcwd(), 'Skier/resources/images/skier_forward.png'),    
    os.path.join(os.getcwd(), 'Skier/resources/images/skier_right1.png'),
    os.path.join(os.getcwd(), 'Skier/resources/images/skier_right2.png'),
    os.path.join(os.getcwd(), 'Skier/resources/images/skier_left2.png'),
    os.path.join(os.getcwd(), 'Skier/resources/images/skier_left1.png'),
    os.path.join(os.getcwd(), 'Skier/resources/images/skier_fall.png')
    ]

OBSTACLE_PATHS = {
    'tree': os.path.join(os.getcwd(), 'Skier/resources/images/tree.png'),
    'flag': os.path.join(os.getcwd(), 'Skier/resources/images/flag.png')
}

AUDIO_PATHS = {
    'bgm': os.path.join(os.getcwd(), 'Skier/resources/music/bgm.mp3'),
    'get': os.path.join(os.getcwd(), 'Skier/resources/music/get.wav'),
    'loss': os.path.join(os.getcwd(), 'Skier/resources/music/shit.mp3')
}

#BGMPATH = os.path.join(os.getcwd(), 'Skier/resources/music/bgm.mp3')
#FLAGBGM = os.path.join(os.getcwd(), 'Skier/resources/music/get.wav')
FONTPATH = os.path.join(os.getcwd(), 'Skier/resources/font/FZSTK.TTF')