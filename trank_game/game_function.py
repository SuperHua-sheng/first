import pygame
import sys
from bullet import Bullet
from  food import Food
def check_events(ai_settings,screen,trank,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.K_q:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #右移动
            if event.key == pygame.K_RIGHT:
                trank.moving_right = True
            #左移动
            elif event.key == pygame.K_LEFT:
                trank.moving_left = True
            #下移动
            elif event.key == pygame.K_DOWN:
                trank.moving_down = True
            #上移动
            elif event.key == pygame.K_UP:
                trank.moving_up = True
            elif event.key==pygame.K_SPACE:
                if len(bullets)<ai_settings.bullets_allowed:
                    new_bullet=Bullet(ai_settings,screen,trank)
                    bullets.add(new_bullet)
        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                trank.moving_right = False
            elif event.key == pygame.K_LEFT:
                trank.moving_left=False
            elif event.key == pygame.K_DOWN:
                trank.moving_down=False
            elif event.key == pygame.K_UP:
                trank.moving_up=False

def update_screen(ai_settings,screen,trank,foods,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    trank.blitme()
    foods.draw(screen)
    #显示新屏幕
    pygame.display.flip()

def update_bullets(foods,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, foods, True, True)

def get_number_foods_x(ai_settings,food_width):
    available_space_x = ai_settings.screen_width - 3 * food_width
    number_foods_x = int(available_space_x / (3 * food_width))
    return number_foods_x

def create_food(ai_settings,screen,foods,food_number):
    food = Food(ai_settings, screen)
    food_width=food.rect.width
    food.x=food_width+3*food_width*food_number
    food.rect.x=food.x
    foods.add(food)

def create_fleet(ai_settings,screen,foods):
    food=Food(ai_settings,screen)
    number_foods_x=get_number_foods_x(ai_settings,food.rect.width)
    for food_number in range(number_foods_x):
        create_food(ai_settings,screen,foods,food_number)
def check_fleet(ai_settings,foods):
    for food in foods.sprites():
        if food.check():
            change_fleet_direction(ai_settings,foods)
            break
def change_fleet_direction(ai_settings,foods):
    for food in foods.sprites():
        food.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_foods(ai_settings,foods):
    check_fleet(ai_settings,foods)
    foods.update()


