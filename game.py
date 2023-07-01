import pygame #pygame 모듈 불러오기
from pygame.locals import * #pygame 모듈에 정의된 모든 요소 직접 참조 가능
import sys # sys 모듈 불러오기 (파이썬 인터프리터와 관련된 기능 제공)
import random # randomo 모듈 불러오기 (난수 생성과 관련된 함수 제공)
import time # time 모듈 불러오기 (시간과 관련된 함수 제공)
from PIL import Image #Pillow에서 Image 불러오기 (이미지 처리와 조작)

pygame.display.set_caption("졸업시켜주세요! 교수님") # 게임 이름

baseSpeed = 5 # 캐릭터 기본 스피드

is_music_paused = False  # 음악 일시정지 상태를 나타내는 변수

padWidth = 640  # 게임 화면 너비
padHeight = 720 # 게임 화면 높이

itemImage = ['item/beer.png', 'item/soju.png'] # 목숨 아이템 (소주, 맥주)
speedImage = ['item/coffee.png', 'item/drink.png'] # 속도 증가 아이템 (커피, 맥주)
gradeImage = ['grade/C.png','grade/F.png'] # C, F 학점
plusImage = ['grade/A.png', 'grade/B.png'] # A, B 학점
plusImage2 = ['grade/A.png', 'grade/B.png'] # A, B 학점 2개
slowImage = ['supplies/homework.png']
moneyImage = ['item/scholarship.png'] # 보너스 스코어 아이템 (장학금)

itemImages = [] # 목숨 아이템 이미지 조절
for img_path in itemImage: #itemImage 리스트에 있는 이미지 반복문 실행
    img = pygame.image.load(img_path) #img_path에 지정된 이미지 파일 불러오기
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    itemImages.append(img) # 해상도 높인 이미지를 itemImages에 추가

speedImages = [] # 속도 증가 아이템 이미지 조절
for img_path in speedImage:
    img = pygame.image.load(img_path)
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    speedImages.append(img)    

gradeImages = [] # C, F 학점 이미지 조절
for img_path in gradeImage:
    img = pygame.image.load(img_path)
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    gradeImages.append(img)

plusImages = [] # A, B 학점 이미지 조절
for img_path in plusImage:
    img = pygame.image.load(img_path)
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    plusImages.append(img)

plusImages2 = [] # A, B 학점2 이미지 조절
for img_path in plusImage2:
    img = pygame.image.load(img_path)
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    plusImages2.append(img)

moneyImages = [] # 목숨 아이템 이미지 조절
for img_path in moneyImage:
    img = pygame.image.load(img_path)
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    moneyImages.append(img)

slowImages = [] # 과제 아이템 이미지 조절
for img_path in slowImage:
    img = pygame.image.load(img_path)
    img = pygame.transform.smoothscale(img, (70, 70))  # 이미지 해상도 높이기
    slowImages.append(img)

def writeScore(count): # 점수 표시 기능
    global gamePad
    font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 20)
    text = font.render('스코어: ' + str(count), True, (0, 0, 0))
    gamePad.blit(text, (10, 10)) # (10, 10) 좌표에 출력

def writePassed(count): # 목숨 표시 기능
    global gamePad
    font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 20)
    text = font.render('목숨: ' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (550, 10))

def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 80)
    text = textfont.render(text, True, (0, 0, 0))
    textpos = text.get_rect() # 텍스트 위치와 크기 지정
    textpos.center = (padWidth/2, padHeight/2) # 정중앙에 출력
    gamePad.blit(text, textpos) # 화면에 출력
    pygame.display.update()
    
def helpPage(): # 도움말 페이지
    pygame.mixer.music.pause()  # 음악 일시정지

    pause_screen = pygame.display.set_mode((padWidth, padHeight))  # 게임 시작 화면 이미지
    background_image = pygame.image.load('background/help_page.jpg')
    screen_rect = pause_screen.get_rect()

    pygame.font.init()
    back_font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 30)

    back_button = back_font.render("뒤로가기", True, (0, 0, 0))
    back_button_rect = back_button.get_rect()
    back_button_rect.center = (550, 685)

    # 마우스 커서 기본 설정
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
            # 마우스 커서 모양 변화 설정
            if back_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) # 버튼에 갖다 대면 손가락으로 바뀐다.
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) # 그 외에는 기본형으로 바뀐다.

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if back_button_rect.collidepoint(event.pos): # 뒤로가기 버튼을 누르면
                    return "resume"  # "resume" 값을 반환하여 게임으로 돌아감

        pause_screen.blit(background_image, screen_rect)
        pause_screen.blit(back_button, back_button_rect)
        pygame.display.update()

def gameOver(): # 게임 오버 메시지 출력 
    global gamePad
    writeMessage('졸업 실패!')
    pygame.mixer.init()
    sound = pygame.mixer.Sound("bgm/gameover_sound.mp3")
    sound.play()
    time.sleep(2) # 2.5초 후에 게임 꺼짐

def drawObject(obj, x, y):
    # obj는 그릴 객체(이미지 or 텍스트), (x,y)는 해당 위치를 나타낸다.
    global gamePad
    gamePad.blit(obj, (x, y))

def game_start(): # 게임 시작 화면

    # 크레딧 화면 표시
    show_credits()

    start_screen = pygame.display.set_mode((padWidth, padHeight))  # 게임 시작 화면 이미지
    background_image = pygame.image.load('background/start_screen.jpg')
    screen_rect = start_screen.get_rect()

    pygame.font.init()  # 폰트
    start_font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 30)
    copyright_font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 10)

    start_button = start_font.render("개강하기", True, (0, 0, 0))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (padWidth // 2 + 10, padHeight // 2 + 190)

    quit_button = start_font.render("자퇴하기", True, (0, 0, 0))
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.center = (padWidth // 2, padHeight // 2 + 270)

    # 저작권 표기
    copyright_text = copyright_font.render("Copyright © 2023 Please graduate me, Professor! All rights reserved.", True, (0, 0, 0))
    copyright_text_rect = copyright_text.get_rect()
    copyright_text_rect.center = (padWidth // 2, padHeight - 10)

    # 마우스 커서 기본 설정
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # 깜빡이는 버튼 상태 변수 추가
    start_button_flashing = False
    quit_button_flashing = False
    start_button_flash_counter = 0
    quit_button_flash_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 마우스 커서 모양 변화 설정
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # 시작 버튼에 갖다 대면 손가락으로 바뀐다.
                start_button_flashing = True  # 시작 버튼 깜빡이는 상태로 설정
            else:
                start_button_flashing = False  # 시작 버튼 깜빡이는 상태 해제

            if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # 종료 버튼에 갖다 대면 손가락으로 바뀐다.
                quit_button_flashing = True  # 종료 버튼 깜빡이는 상태로 설정
            else:
                quit_button_flashing = False  # 종료 버튼 깜빡이는 상태 해제

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):  # 시작 버튼을 누르면
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # 마우스 커서가 기본형으로 돌아옴
                    return

                elif quit_button_rect.collidepoint(event.pos):  # 종료 버튼을 누르면
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # 마우스 커서가 기본형으로 돌아옴
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("bgm/exit.mp3")
                    sound.play()
                    pygame.quit()
                    sys.exit()

        # 버튼 깜빡이는 로직 추가
        if start_button_flashing:
            start_button_flash_counter += 1
            if start_button_flash_counter <= 600:  # 600프레임 동안 보여준 후
                start_screen.blit(background_image, screen_rect)  # 화면에 이미지 출력
                start_screen.blit(start_button, start_button_rect)
                start_screen.blit(quit_button, quit_button_rect)
                start_screen.blit(copyright_text, copyright_text_rect)
                pygame.display.update()
            elif start_button_flash_counter <= 800:  # 다음 800프레임 동안은 버튼 없이 화면만 출력
                start_screen.blit(background_image, screen_rect)
                start_screen.blit(quit_button, quit_button_rect)
                start_screen.blit(copyright_text, copyright_text_rect)
                pygame.display.update()
            else:  # 버튼 깜빡이는 상태 초기화
                start_button_flash_counter = 0
                
        elif quit_button_flashing:
            quit_button_flash_counter += 1
            if quit_button_flash_counter <= 600:  # 30프레임 동안 보여준 후
                start_screen.blit(background_image, screen_rect)  # 화면에 이미지 출력
                start_screen.blit(quit_button, quit_button_rect)
                start_screen.blit(start_button, start_button_rect)
                start_screen.blit(copyright_text, copyright_text_rect)
                pygame.display.update()
            elif quit_button_flash_counter <= 800:  # 다음 30프레임 동안은 버튼 없이 화면만 출력
                start_screen.blit(background_image, screen_rect)
                start_screen.blit(start_button, start_button_rect)
                start_screen.blit(copyright_text, copyright_text_rect)
                pygame.display.update()
            else:  # 버튼 깜빡이는 상태 초기화
                quit_button_flash_counter = 0
        else:
            start_screen.blit(background_image, screen_rect)  # 화면에 이미지 출력
            start_screen.blit(start_button, start_button_rect)
            start_screen.blit(quit_button, quit_button_rect)
            start_screen.blit(copyright_text, copyright_text_rect)
            pygame.display.update()

def game_pause(): # 게임 일시정지 화면
    pygame.mixer.music.pause()  # 게임 플레이 배경음악 일시정지

    paused_theme.play(-1)  # paused_theme 반복 재생

    paused_screen = pygame.display.set_mode((padWidth, padHeight))  # 게임 시작 화면 이미지
    background_image = pygame.image.load('background/paused_menu.jpg')
    screen_rect = paused_screen.get_rect()


    pygame.font.init()
    start_font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 30)

    resume_button = start_font.render("수업 마저듣기", True, (0, 0, 0))
    resume_button_rect = resume_button.get_rect()
    resume_button_rect.center = (padWidth // 2, padHeight // 2 - 100)

    restart_button = start_font.render("재수강하기", True, (0, 0, 0))
    restart_button_rect = restart_button.get_rect()
    restart_button_rect.center = (padWidth // 2, padHeight // 2 - 30)

    help_button = start_font.render("도움말", True, (0, 0, 0))
    help_button_rect = help_button.get_rect()
    help_button_rect.center = (padWidth // 2, padHeight // 2 + 40)

    quit_button = start_font.render("자퇴하기", True, (0, 0, 0))
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.center = (padWidth // 2, padHeight // 2 + 110)

    # 마우스 커서 기본 설정
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
            # 마우스 커서 모양 변화 설정
            if resume_button_rect.collidepoint(pygame.mouse.get_pos()) \
            or quit_button_rect.collidepoint(pygame.mouse.get_pos()) \
            or help_button_rect.collidepoint(pygame.mouse.get_pos()) \
            or restart_button_rect.collidepoint(pygame.mouse.get_pos()):
                
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) # 버튼에 갖다 대면 손가락으로 바뀐다.
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) # 그 외에는 기본형으로 바뀐다.

            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button_rect.collidepoint(event.pos):  # 마저 수업듣기 버튼을 누르면
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/click.mp3")
                    sound.play()
                    paused_theme.stop()  # paused_theme 노래 중지
                    pygame.mixer.music.unpause()  # 게임 플레이 배경음악 재개
                    return "resume"  # "resume" 값을 반환하여 게임으로 돌아감
                
                elif restart_button_rect.collidepoint(event.pos): # 재시작 버튼을 누르면
                    paused_theme.stop()  # paused_theme 노래 중지
                    runGame()  # 게임 재시작
                elif help_button_rect.collidepoint(event.pos): # 도움말 버튼을 누르면
                    helpPage()
                elif quit_button_rect.collidepoint(event.pos): # 종료 버튼을 누르면
                    return "quit"  # "quit" 값을 반환하여 게임 종료

        paused_screen.blit(background_image, screen_rect)
        paused_screen.blit(resume_button, resume_button_rect)
        paused_screen.blit(restart_button, restart_button_rect)
        paused_screen.blit(help_button, help_button_rect)
        paused_screen.blit(quit_button, quit_button_rect)
        pygame.display.update()

def game_end(): # 게임 오버 화면
    start_screen = pygame.display.set_mode((padWidth, padHeight))
    background_image = ['gameover/gameover_1.jpg', 'gameover/gameover_2.jpg', 'gameover/gameover_3.jpg']
    background_image_path = random.choice(background_image)
    background_image = pygame.image.load(background_image_path)
    screen_rect = start_screen.get_rect()

    pygame.font.init()
    start_font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 30)

    start_button = start_font.render("재수강하기", True, (0, 0, 0))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (padWidth // 2, padHeight // 2 + 190)

    quit_button = start_font.render("자퇴하기", True, (0, 0, 0))
    quit_button_rect = quit_button.get_rect()
    quit_button_rect.center = (padWidth // 2, padHeight // 2 + 270)

    # 마우스 커서 기본 설정
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.mixer.init()  # 믹서 초기화

    # 배경 음악 로드 및 재생
    pygame.mixer.music.load("bgm/gameover_music.mp3")
    pygame.mixer.music.set_volume(0.5)  # 볼륨을 절반으로 설정
    pygame.mixer.music.play(-1)  # -1을 전달하여 반복 재생


    # 깜빡이는 버튼 상태 변수 추가
    start_button_flashing = False
    quit_button_flashing = False
    start_button_flash_counter = 0
    quit_button_flash_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
            # 마우스 커서 모양 변화 설정
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # 시작 버튼에 갖다 대면 손가락으로 바뀐다.
                start_button_flashing = True  # 시작 버튼 깜빡이는 상태로 설정
            else:
                start_button_flashing = False  # 시작 버튼 깜빡이는 상태 해제

            if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # 종료 버튼에 갖다 대면 손가락으로 바뀐다.
                quit_button_flashing = True  # 종료 버튼 깜빡이는 상태로 설정
            else:
                quit_button_flashing = False  # 종료 버튼 깜빡이는 상태 해제

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):  # 재수강 버튼을 누르면
                    runGame()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # 마우스 커서가 기본형으로 돌아옴
                    

                elif quit_button_rect.collidepoint(event.pos):  # 종료 버튼을 누르면
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # 마우스 커서가 기본형으로 돌아옴
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("bgm/exit.mp3")
                    sound.play()
                    pygame.quit()
                    sys.exit()

        # 버튼 깜빡이는 로직 추가
        if start_button_flashing:
            start_button_flash_counter += 1
            if start_button_flash_counter <= 600:  # 600프레임 동안 보여준 후
                start_screen.blit(background_image, screen_rect)  # 화면에 이미지 출력
                start_screen.blit(start_button, start_button_rect)
                start_screen.blit(quit_button, quit_button_rect)
                pygame.display.update()
            elif start_button_flash_counter <= 800:  # 다음 800프레임 동안은 버튼 없이 화면만 출력
                start_screen.blit(background_image, screen_rect)
                start_screen.blit(quit_button, quit_button_rect)
                pygame.display.update()
            else:  # 버튼 깜빡이는 상태 초기화
                start_button_flash_counter = 0
                
        elif quit_button_flashing:
            quit_button_flash_counter += 1
            if quit_button_flash_counter <= 600:  # 30프레임 동안 보여준 후
                start_screen.blit(background_image, screen_rect)  # 화면에 이미지 출력
                start_screen.blit(quit_button, quit_button_rect)
                start_screen.blit(start_button, start_button_rect)
                pygame.display.update()
            elif quit_button_flash_counter <= 800:  # 다음 30프레임 동안은 버튼 없이 화면만 출력
                start_screen.blit(background_image, screen_rect)
                start_screen.blit(start_button, start_button_rect)
                pygame.display.update()
            else:  # 버튼 깜빡이는 상태 초기화
                quit_button_flash_counter = 0
        else:
            start_screen.blit(background_image, screen_rect)  # 화면에 이미지 출력
            start_screen.blit(start_button, start_button_rect)
            start_screen.blit(quit_button, quit_button_rect)
            pygame.display.update()

def show_credits(): # 크레딧 화면 표시
    credits_screen = pygame.display.set_mode((padWidth, padHeight))
    credits_image = pygame.Surface((padWidth, padHeight))  # 화면 크기와 동일한 Surface 생성
    credits_image.fill((255, 255, 255))  # 흰색으로 채우기
    screen_rect = credits_screen.get_rect()

    pygame.font.init()
    present_font = pygame.font.Font("NEXON Lv1 Gothic OTF Bold.woff", 40)

    # "Made by 장우영" 글씨
    name_button = present_font.render("Made by 장우영", True, (0, 0, 0))
    name_button_rect = name_button.get_rect()
    name_button_rect.center = (padWidth // 2, padHeight // 2 - 250)

    # 내 사진 해상도 높이기
    img = Image.open("myimage.jpg")
    new_size = (200, 200)  # 원하는 해상도로 크기 조정
    resized_img = img.resize(new_size, resample=Image.BICUBIC)
    resized_img.save("resized_myimage.jpg")

    # 내 사진
    myimage_image = pygame.image.load("resized_myimage.jpg")
    myimage_rect = myimage_image.get_rect()
    myimage_rect.center = (padWidth // 2, padHeight // 2 - 90)

    # "Present by" 글씨
    present_button = present_font.render("Present by", True, (0, 0, 0))
    present_button_rect = present_button.get_rect()
    present_button_rect.center = (padWidth // 2, padHeight // 2 + 90)

    # 남서울 로고
    nsu_image = pygame.image.load("남서울로고.png")
    nsu_rect = nsu_image.get_rect()
    nsu_rect.center = (padWidth // 2, padHeight // 2 + 230)  # 이미지 위치 설정

    # 게임 시작 브금
    pygame.mixer.init()  # 믹서 초기화
    pygame.mixer.music.load("bgm/start_music.mp3")
    pygame.mixer.music.play(-1)  # -1을 전달하여 반복 재생

    # 크레딧 화면을 표시할 시간 (초)
    display_time = 5.8
    start_time = time.time()  # 크레딧 화면 시작 시간

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # 마우스 클릭 시 함수 종료하여 크레딧 화면 스킵

        current_time = time.time()  # 현재 시간
        elapsed_time = current_time - start_time  # 경과 시간

        if elapsed_time >= display_time:
            return  # 경과 시간이 표시 시간을 초과하면 함수 종료하여 게임 시작 화면으로 전환

        credits_screen.blit(credits_image, screen_rect)

        # 알파 값을 조절하여 투명도 설정
        # 5.8초 동안 서서히 사라지게 설정
        alpha = int((1 - elapsed_time / display_time) * 255)
        name_button.set_alpha(alpha)
        present_button.set_alpha(alpha)
        myimage_image.set_alpha(alpha)
        nsu_image.set_alpha(alpha)

        credits_screen.blit(credits_image, screen_rect)
        credits_screen.blit(myimage_image, myimage_rect)
        credits_screen.blit(name_button, name_button_rect)
        credits_screen.blit(present_button, present_button_rect)
        credits_screen.blit(nsu_image, nsu_rect)
        pygame.display.update()
        
game_start() 

def initGame(): # 게임 초기화
    global paused_theme, gamePad, clock, background, background2, student, student_die, student_throw, student_hurt, pen, eraser, book, pencil, boom
    pygame.init()
    
    # 게임 초기화 과정에서 paused_theme 로드
    paused_theme = pygame.mixer.Sound("bgm/paused_theme.mp3")
    paused_theme.set_volume(0.5)  # 볼륨을 절반으로 설정

    gamePad = pygame.display.set_mode((padWidth, padHeight)) # 게임 화면 선언
    pygame.display.set_caption('졸업시켜주세요 교수님!') # 게임 웹페이지 이름
    background = pygame.image.load('background/background_pic.jpg') # 게임 배경 화면 선언
    background2 = pygame.image.load('background/background_pic2.jpg') # 높은 스코어일 때 게임 배경 화면 선언

    # 학생 캐릭터
    img_student = Image.open("student/student.png")  # 캐릭터 이미지 불러오기
    new_size = (150, 150) # 새로운 이미지 크기 지정
    resized_img_student = img_student.resize(new_size, resample=Image.BICUBIC)  # 해상도 높이기
    resized_img_student.save("student/resized_student.png") # 새로운 이미지 저장
    student = pygame.image.load('student/resized_student.png') # 게임 캐릭터

    # 게임오버 될 때 학생 캐릭터 이미지
    img_student_die = Image.open("student/student_die.png")  # 캐릭터 이미지 불러오기
    resized_img_student_die = img_student_die.resize(new_size, resample=Image.BICUBIC)  # 해상도 높이기
    resized_img_student_die.save("student/resized_student_die.png") # 새로운 이미지 저장
    student_die = pygame.image.load('student/resized_student_die.png') # 게임 캐릭터

    # 학생이 학용품을 던질 때 사용할 이미지
    img_student_throw = Image.open("student/student_throw.png") # 캐릭터 이미지 불러오기
    resized_img_student_throw = img_student_throw.resize(new_size, resample=Image.BICUBIC) # 해상도 높이기 
    resized_img_student_throw.save("student/resized_student_throw.png") # 새로운 이미지 저장
    student_throw = pygame.image.load('student/resized_student_throw.png') # 던지는 모션

    # 학생이 학점에 맞았을 때 사용할 이미지
    # 구현 실패 / 계속 수정해보기
    img_student_hurt = Image.open("student/student_hurt.png") # 캐릭터 이미지 불러오기
    resized_img_student_hurt = img_student_hurt.resize(new_size, resample=Image.BICUBIC) # 해상도 높이기 
    resized_img_student_hurt.save("student/resized_student_hurt.png") # 새로운 이미지 저장
    student_hurt = pygame.image.load('student/resized_student_hurt.png') # 던지는 모션

    # 학용품 이미지(연필, 볼펜, 지우개, 전공책) 불러오기
    pencil = pygame.transform.scale(pygame.image.load("supplies/pencil.png"), (50, 50)) # 연필 이미지
    pen = pygame.transform.scale(pygame.image.load("supplies/pen.png"), (50, 50)) # 볼펜 이미지
    eraser = pygame.transform.scale(pygame.image.load("supplies/eraser.png"), (30, 30)) # 지우개 이미지
    book = pygame.transform.scale(pygame.image.load("supplies/book.png"), (50, 50)) # 전공책 이미지

    # 학용품으로 격추시켰을 때 폭발 이미지
    img_boom = Image.open("item/boom.png") # 캐릭터 이미지 불러오기
    boom_size = (80, 80)  # 크기 설정
    resized_img_boom = img_boom.resize(boom_size, resample=Image.BICUBIC) # 해상도 높이기 
    resized_img_boom.save("item/boom.png") # 새로운 이미지 저장
    boom = pygame.image.load('item/boom.png') # 던지는 모션

    clock = pygame.time.Clock() # 게임 시간

    # 키 입력 반복을 활성화
    # 딜레이 값이 0이면, 사용자가 키를 누르고 있어도 초기 입력은 딱 한 번.
    pygame.key.set_repeat(0, 1)  # 딜레이 0ms, 간격 10ms


def runGame(): # 게임 작동 시
    global gamePad, clock, background, background2, student_die, student_throw, student_hurt, pen, eraser, book, pencil, boom

    pygame.mixer.init()  # 믹서 초기화

    background = pygame.image.load('background/background_pic.jpg') # 게임 배경 화면 선언
    background2 = pygame.image.load('background/background_pic2.jpg') # 높은 스코어일 때 게임 배경 화면 선언

    is_music_paused = False  # 음악 일시정지 여부

    # 게임 플레이 브금
    pygame.mixer.music.load("bgm/game_music.mp3")
    pygame.mixer.music.set_volume(0.5)  # 볼륨을 절반으로 설정
    pygame.mixer.music.play(-1)  # -1을 전달하여 반복 재생

    studentSize = student.get_rect().size
    studentWidth = studentSize[0]
    studentHeight = studentSize[1]

    x = padWidth * 0.4 # 게임 캐릭터 x좌표
    y = padHeight * 0.75 #게임 캐릭터 y좌표
    studentX = 0 # 캐릭터는 안 움직인다.

    suppliesXY = []

    # 목숨 아이템 랜덤 생성
    item = random.choice(itemImages)
    itemSize = item.get_rect().size # 아이템 크기
    itemWidth = itemSize[0]
    itemHeight = itemSize[1]

    # 속도 증가 아이템 랜덤 생성
    speed = random.choice(speedImages)
    speedSize = speed.get_rect().size # 아이템 크기
    speedWidth = speedSize[0]
    speedHeight = speedSize[1]

    # C, F학점 아이템 랜덤 생성
    grade = random.choice(gradeImages)
    gradeSize = grade.get_rect().size # 아이템 크기
    gradeWidth = gradeSize[0]
    gradeHeight = gradeSize[1]

    # A, B 학점 아이템 랜덤 생성
    plus = random.choice(plusImages)
    plusSize = plus.get_rect().size # 아이템 크기
    plusWidth = plusSize[0]
    plusHeight = plusSize[1]

    # A, B 학점2 아이템 랜덤 생성
    plus2 = random.choice(plusImages2)
    plus2Size = plus2.get_rect().size # 아이템 크기
    plus2Width = plus2Size[0]
    plus2Height = plus2Size[1]

    # 목숨 아이템 랜덤 생성
    money = random.choice(moneyImages)
    moneySize = money.get_rect().size # 아이템 크기
    moneyWidth = moneySize[0]
    moneyHeight = moneySize[1]

    # 목숨 아이템 초기 위치 설정
    if itemWidth >= padWidth: # itemWidth가 padWidth 보다 크거나 같을 때
        itemX = 5 # 아이템 가로 위치 설정
    else:
        itemX = random.randrange(0, padWidth - itemWidth) # 0부터 padWidth - itemWidth 사이의 랜덤 값을 itemX에 대입
        itemY = 0 # 아이템 세로 위치 설정
        itemSpeed = 2 # 떨어지는 속도

    # 속도 증가 아이템 초기 위치 설정
    if speedWidth >= padWidth:
        speedX = 5
    else:
        speedX = random.randrange(0, padWidth - speedWidth)
        speedY = 0
        speedSpeed = 5

    # C, F학점 초기 위치 설정
    if gradeWidth >= padWidth:
        gradeX = 5
    else:
        gradeX = random.randrange(0, padWidth - gradeWidth)
        gradeY = 0
        gradeSpeed = 5

    # A, B학점 초기 위치 설정
    if plusWidth >= padWidth:
        plusX = 5
    else:
        plusX = random.randrange(0, padWidth - plusWidth)
    plusY = 0
    plusSpeed = 5

    # A, B학점2 초기 위치 설정
    if plus2Width >= padWidth:
        plus2X = 5
    else:
        plus2X = random.randrange(0, padWidth - plus2Width)
    plus2Y = 0
    plus2Speed = 5

    # 목숨 아이템 초기 위치 설정
    if moneyWidth >= padWidth:
        moneyX = 5
    else:
        moneyX = random.randrange(0, padWidth - moneyWidth)
        moneyY = 0
        moneySpeed = 1 

    actionSpeed = 3

    # 학용품에 학점이 맞았을 경우 True
    collision_detected = False  # 충돌 감지 플래그
    isShot = False # 격추시켰을 때의 함수 상태 off
    shotCount = 0 # 스코어 = 0
    gradePassed = 3 # 캐릭터의 목숨이 3개로 시작
    throwing = False # 던지고 있는 상태 off
    onGame = False # 게임 작동 상태 off

    while not onGame: # 게임이 작동되면?
        for event in pygame.event.get(): # 모든 이벤트 호출
            if event.type in [pygame.QUIT]: # 종료 상태면? -> 시스템 종료
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]: # 키보드를 눌렀을 때
                if event.key == pygame.K_LEFT: # 키보드 좌 방향 눌렀을 때
                    studentX -= baseSpeed + actionSpeed

                elif event.key == pygame.K_RIGHT: # 키보드 우 방향 눌렀을 때
                    studentX += baseSpeed + actionSpeed

                elif event.key == pygame.K_SPACE: # 스페이스 바 눌렀을 때
                    img = random.choice([pen, eraser, book, pencil]) # 학용품 (랜덤으로)
                    suppliesX = x + studentWidth/2 # 캐릭터 중앙에서 발사
                    suppliesY = (140 + y) - studentHeight # 캐릭터 머리 위에서 발사
                    suppliesXY.append([suppliesX, suppliesY, img]) # 캐릭터와 이미지 출력
                    throwing = True  # False에서 True로 변환

                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/throw_effect.mp3")
                    sound.play()

                elif event.key == pygame.K_ESCAPE: # esc를 눌렀을 때
                    paused = True # 일시정지 작동
                    while paused: # 일시정지 때의 상태
                        result = game_pause()
                        if result == "resume":
                            paused = False # False가 되면서 다시 게임 작동
                            if is_music_paused:
                                pygame.mixer.music.unpause()  # 일시정지된 음악 재생
                                
                            pygame.time.wait(100)  # CPU 사용량을 줄이기 위한 대기 시간

                        elif result == "quit":
                            pygame.quit()
                            sys.exit()

            if event.type == pygame.KEYUP: # 키보드를 땠을 때
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 키보드 좌, 우 방향을 뗐을 때
                    studentX = 0 # 캐릭터는 안 움직인다.

                elif event.key == pygame.K_SPACE:
                    throwing = False  # 던지기 False로 변경

                elif event.key == pygame.K_ESCAPE:
                    paused = True # 일시정지 작동 
                    studentX = 0 # 캐릭터는 안 움직인다.

        drawObject(background, 0, 0) # 배경 화면 이미지 생성

        x += studentX # 캐릭터 이동 방향 좌표
        if x < 0:
            x = 0
        elif x > padWidth - studentWidth:
            x = padWidth - studentWidth

        # 충돌이 감지 되었을 경우
        if not collision_detected:
            # 학생이 C, F 학점과 부딪혔는지 체크
            if y < gradeY + gradeHeight:
                if (gradeX > x and gradeX < x + studentWidth) or (gradeX + gradeWidth > x and gradeX + gradeWidth < x + studentWidth):
                    collision_detected = True
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/hit.mp3")
                    sound.play()
                    gradePassed -= 1  # 딱 한 번만 1 감소
                    actionSpeed -= 2  # 이동 속도 2 감소
                    gradeX = random.randrange(0, padWidth - gradeWidth)
                    gradeY = 0
        
        # 충돌이 감지되지 않았을 경우
        if collision_detected:
            # 충돌 해제 여부 체크
            if y >= gradeY + gradeHeight:
                collision_detected = False  # 충돌 해제


        # 충돌이 감지 되었을 경우
        if not collision_detected:
            # 학생이 A, B 학점과 부딪혔는지 체크
            if y < plusY + plusHeight:
                if (plusX > x and plusX < x + studentWidth) or (plusX + plusWidth > x and plusX + plusWidth < x + studentWidth):
                    collision_detected = True  # 충돌이 감지되면 플래그 설정
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/item_effect.mp3")
                    sound.play()
                    shotCount += 300 # 300점 추가
                    plusX = random.randrange(0, padWidth - plusWidth)
                    plusY = 0
                    plus = random.choice(plusImages)
                    plus = pygame.transform.scale(plus, (70, 70)) # 이미지 크기 수정
                    plusSize = plus.get_rect().size
                    plusWidth = plusSize[0]
                    plusHeight = plusSize[1]
                    # 학점 이미지 삭제하는 기능 추가하기

        # 충돌이 감지되지 않았을 경우
        if collision_detected:
            # 충돌 해제 여부 체크
            if y >= plusY + plusHeight:
                collision_detected = False  # 충돌 해제

        # 충돌이 감지 되었을 경우
        if not collision_detected:
            # 학생이 A, B 학점과 부딪혔는지 체크
            if y < plus2Y + plus2Height:
                if (plus2X > x and plus2X < x + studentWidth) or (plus2X + plusWidth > x and plus2X + plus2Width < x + studentWidth):
                    collision_detected = True  # 충돌이 감지되면 플래그 설정
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/item_effect.mp3")
                    sound.play()
                    shotCount += 300 # 300점 추가
                    plus2X = random.randrange(0, padWidth - plusWidth)
                    plus2Y = 0
                    plus2 = random.choice(plusImages2)
                    plus2 = pygame.transform.scale(plus, (70, 70)) # 이미지 크기 수정
                    plus2Size = plus.get_rect().size
                    plus2Width = plus2Size[0]
                    plus2Height = plus2Size[1]
                    # 학점 이미지 삭제하는 기능 추가하기

        # 충돌이 감지되지 않았을 경우
        if collision_detected:
            # 충돌 해제 여부 체크
            if y >= plus2Y + plus2Height:
                collision_detected = False  # 충돌 해제

        # 충돌이 감지 되었을 경우
        if not collision_detected:
            # 학생이 목숨 증가 아이템과 부딪혔는지 체크
            if y < itemY + itemHeight:
                if (itemX > x and itemX < x + studentWidth) or (itemX + itemWidth > x and itemX + itemWidth < x + studentWidth):
                    collision_detected = True  # 충돌이 감지되면 플래그 설정
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/drink2_sound.mp3")
                    sound.play()
                    gradePassed += 1
                    itemX = -itemWidth  # 화면 왼쪽으로 이동하여 사라지도록 설정
                    itemY = -itemHeight  # 화면 위로 이동하여 사라지도록 설정
                    speed_respawn_time = pygame.time.get_ticks() + 10000 # 10초 후에 재생성되도록 설정

        # 충돌이 감지되지 않았을 경우
        if collision_detected:
            # 충돌 해제 여부 체크
            if pygame.time.get_ticks() >= speed_respawn_time:  # 아이템 재생성 시간이 지났는지 확인
                collision_detected = False
                itemX = random.randrange(0, padWidth - itemWidth)
                itemY = 0

        # 충돌이 감지 되었을 경우
        if not collision_detected:
            # 학생이 속도 증가 아이템과 부딪혔는지 체크
            if y < speedY + speedHeight:
                if (speedX > x and speedX < x + studentWidth) or (speedX + speedWidth > x and speedX + speedWidth < x + studentWidth):
                    collision_detected = True  # 충돌이 감지되면 플래그 설정
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/drink_sound.mp3")
                    sound.play()
                    if actionSpeed < 8: # 이동 속도는 최대 8
                        actionSpeed += 4 # 이동 속도 4 증가
                    speedX = -speedWidth  # 화면 왼쪽으로 이동하여 사라지도록 설정
                    speedY = -speedHeight  # 화면 위로 이동하여 사라지도록 설정
                    speed_respawn_time = pygame.time.get_ticks() + 10000 # 10초 후에 재생성되도록 설정

        # 충돌이 감지되지 않았을 경우
        if collision_detected:
            # 충돌 해제 여부 체크
            if pygame.time.get_ticks() >= speed_respawn_time:  # 아이템 재생성 시간이 지났는지 확인
                collision_detected = False
                speedX = random.randrange(0, padWidth - speedWidth)
                speedY = 0

        # 충돌이 감지 되었을 경우
        if not collision_detected:
            # 학생이 장학금과 부딪혔는지 체크
            if y < moneyY + moneyHeight:
                if (moneyX > x and moneyX < x + studentWidth) or (moneyX + moneyWidth > x and moneyX + moneyWidth < x + studentWidth):
                    collision_detected = True
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("sound/money_sound.mp3")
                    sound.play()
                    shotCount += 700 # 스코어 +700
                    moneyX = -moneyWidth  # 화면 왼쪽으로 이동하여 사라지도록 설정
                    moneyY = -moneyHeight  # 화면 위로 이동하여 사라지도록 설정
                    speed_respawn_time = pygame.time.get_ticks() + 10000 # 10초 후에 재생성되도록 설정

        # 충돌이 감지되지 않았을 경우
        if collision_detected:
            # 충돌 해제 여부 체크
            if pygame.time.get_ticks() >= speed_respawn_time:  # 장학금 재생성 시간이 지났는지 확인
                collision_detected = False
                moneyX = random.randrange(0, padWidth - moneyWidth)
                moneyY = 0
                     
        # 충돌이 감지 되었을 경우
        if not collision_detected:
            if throwing: # 던지는 함수 True이면?
                drawObject(student_throw, x, y)  # 던지는 이미지 출력
            else:
                if gradePassed == 0: # 목숨이 0개가 되면?
                    drawObject(student_die, x, y)  # 기절하는 이미지 출력
                else:
                    drawObject(student, x, y)  # 기본 이미지 표시

        if gradePassed == 0: # 목숨이 0개이면
            gameOver() # 게임 오버 문구 표시
            game_end() # 게임 오버 화면으로 변환

        # 학용품 발사 화면에 그리기
        if len(suppliesXY) != 0:
            for supply in suppliesXY:
                supply[1] -= 10    # 학용품의 y좌표 -10 (위로 이동)

                # 학용품이 학점을 맞추었을 경우
                if supply[1] < gradeY:
                    if gradeX < supply[0] < gradeX + gradeWidth:
                        isShot = True # 학용품으로 낮은 학점을 격추시켰을 때
                        suppliesXY.remove(supply) # 발사한 학용품 삭제
                        shotCount += 100 # 스코어 100 추가
                        break

                if supply[1] <= 0: # 학용품이 화면 밖을 벗어나면
                    suppliesXY.remove(supply) # 발사한 학용품 삭제

            for supply in suppliesXY:
                drawObject(supply[2], supply[0], supply[1])
            
        writeScore(shotCount) # 스코어 기록

        itemY += itemSpeed # 목숨 증가 아이템이 아래로 움직임

        speedY += speedSpeed # 속도 증가 아이템이 아래로 움직임

        gradeY += gradeSpeed # C, F 학점 아이템이 아래로 움직임

        plusY += plusSpeed # A, B 학점 아이템이 아래로 움직임

        plus2Y += plus2Speed # A, B 학점 아이템이 아래로 움직임

        moneyY += moneySpeed # 장학금 아이텡이 아래로 움직임

        # 목숨 아이템이 아래로 떨어진 경우
        if itemY > padHeight:
            # 새로운 아이템 (랜덤)
            item = random.choice(itemImages)
            item = pygame.transform.scale(item, (70, 70)) # 이미지 크기 수정
            itemSize = item.get_rect().size
            itemWidth = itemSize[0]
            itemHeight = itemSize[1]
            
            if itemWidth >= padWidth:
                itemX = 0
            else:
                itemX = random.randrange(0, padWidth - itemWidth)
            itemY = 0

        # 속도 증가 아이템이 아래로 떨어진 경우
        if speedY > padHeight:
            # 새로운 아이템 (랜덤)
            speed = random.choice(speedImages)
            speed = pygame.transform.scale(speed, (70, 70)) # 이미지 크기 수정
            speedSize = speed.get_rect().size
            speedWidth = speedSize[0]
            speedHeight = speedSize[1]
            
            if speedWidth >= padWidth:
                speedX = 0
            else:
                speedX = random.randrange(0, padWidth - speedWidth)
                speedY = 0

        # C, F학점이 아래로 떨어진 경우
        if gradeY > padHeight:
            # 새로운 아이템 (랜덤)
            grade = random.choice(gradeImages)
            grade = pygame.transform.scale(grade, (70, 70)) # 이미지 크기 수정
            gradeSize = grade.get_rect().size
            gradeWidth = gradeSize[0]
            gradeHeight = gradeSize[1]
            pygame.mixer.init()
            sound = pygame.mixer.Sound("sound/hit.mp3")
            sound.play()
            gradePassed -= 1 # C, F 학점 놓치면 목숨 -1 차감
            actionSpeed -= 2  # 이동 속도 2 감소
            
            if gradeWidth >= padWidth:
                gradeX = 0
            else:
                gradeX = random.randrange(0, padWidth - gradeWidth)
                gradeY = 0

        writePassed(gradePassed) # 목숨 기록

        # A, B학점이 아래로 떨어진 경우
        if plusY > padHeight:
            # 새로운 아이템 (랜덤)
            plus = random.choice(plusImages)
            plus = pygame.transform.scale(plus, (70, 70)) # 이미지 크기 수정
            plusSize = plus.get_rect().size
            plusWidth = plusSize[0]
            plusHeight = plusSize[1]
            
            if plusWidth >= padWidth:
                plusX = 0
            else:
                plusX = random.randrange(0, padWidth - plusWidth)
            plusY = 0

        # A, B학점2이 아래로 떨어진 경우
        if plus2Y > padHeight:
            # 새로운 아이템 (랜덤)
            plus2 = random.choice(plusImages2)
            plus2 = pygame.transform.scale(plus2, (70, 70)) # 이미지 크기 수정
            plus2Size = plus2.get_rect().size
            plus2Width = plus2Size[0]
            plus2Height = plus2Size[1]
            
            if plus2Width >= padWidth:
                plus2X = 0
            else:
                plus2X = random.randrange(0, padWidth - plus2Width)
            plus2Y = 0

        # 목숨 아이템이 아래로 떨어진 경우
        if moneyY > padHeight:
            # 새로운 아이템 (랜덤)
            money = random.choice(moneyImages)
            money = pygame.transform.scale(money, (70, 70)) # 이미지 크기 수정
            moneySize = money.get_rect().size
            moneyWidth = moneySize[0]
            moneyHeight = moneySize[1]
            
            if moneyWidth >= padWidth:
                moneyX = 0
            else:
                moneyX = random.randrange(0, padWidth - moneyWidth)
                moneyY = 0

        if isShot:
            # 학점 폭발
            pygame.mixer.init()
            sound = pygame.mixer.Sound("sound/boom4.mp3") # 맞췄을 때 효과음
            sound.play()

            drawObject(boom, gradeX, gradeY) # 폭발 이미지 불러오기
            pygame.display.update()
            isShot = False

            boom_time = pygame.time.get_ticks()  # 폭발 이미지가 나타난 시간 저장

            # 새로운 학점 (랜덤)
            grade = random.choice(gradeImages)
            grade = pygame.transform.scale(grade, (70, 70)) # 이미지 크기 수정
            gradeSize = grade.get_rect().size
            gradeWidth = gradeSize[0]
            gradeHeight = gradeSize[1]
            gradeX = random.randrange(0, padWidth - gradeWidth)
            gradeY = -100

            if pygame.time.get_ticks() - boom_time >= 2000:  # 폭발 이미지가 화면에 보여진 후 2초가 지나면
                # 폭발 이미지 삭제
                drawObject(background, gradeX, gradeY)
                pygame.display.update()

        # 점수에 따른 낙하 속도 증가
        if shotCount % 1500 == 0:  # shotCount가 1500의 배수인 경우
            gradeSpeed += 0.02  # 속도 증가

        if shotCount >= 2000: # 스코어가 5000이면
            background = background2 # 배경화면이 전환

        if actionSpeed >= 10: # 이동속도는 최대 10
            actionSpeed = 10

        drawObject(item, itemX, itemY) # 아이템 그리기

        drawObject(speed, speedX, speedY) # 아이템 그리기
        
        drawObject(grade, gradeX, gradeY) # C, F 학점 그리기 

        drawObject(plus, plusX, plusY) # A, B 학점 그리기

        drawObject(plus2, plus2X, plus2Y) # A, B 학점2 그리기

        drawObject(money, moneyX, moneyY) # A, B 학점 그리기


        pygame.display.update()

        clock.tick(60)

    pygame.quit()

initGame()
runGame()