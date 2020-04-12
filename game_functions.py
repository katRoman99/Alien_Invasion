import sys

import pygame

from bullet import Bullet
from alien import Alien

def update_bullets(bullets):
    ''' 
    Update position of the bullets on the screen and those outside
    of the screen.
    '''

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    ''' Create a new bullet and add it to the group of bullets '''
    if(len(bullets) < ai_settings.bullets_allowed):
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    ''' Response to the events generated by keyboard/ mouse input '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def debug_aliens(aliens, screen):
    for alien in aliens:
        pygame.draw.rect(screen, (200, 200, 200), alien.rect)

def get_number_aliens_x(ai_settings, alien_width):
    ''' Determine the number of aliens in a row on the screen '''
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y/ (2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    ''' Create an alien and put it in a fleet '''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x_pos = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x_pos
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    ''' Create the whole fleet of aliens '''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.image.get_rect().height, ship.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    ''' Invoke proper action when an alien reaches the edge of the screen '''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    ''' Move the whole fleet down and change the direction in which it moves '''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    ''' Update the position of all aliens in the fleet '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def update_screen(ai_settings, screen, ship, aliens, bullets):
    ''' Update images displayed on the screen and move to the next screen '''
    # Refresh the screen for each new iteration of the game loop
    screen.blit(ai_settings.bg_image, screen.get_rect())

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # debug_aliens(aliens, screen)

    # Displaye the last modified screen
    pygame.display.flip()