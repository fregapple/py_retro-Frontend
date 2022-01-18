from pygame.constants import K_ESCAPE, KEYDOWN, VIDEORESIZE
import pygame_gui, pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE
from .display import *
from collections import deque

class DirectoryDialog(pygame_gui.windows.ui_file_dialog.UIFileDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.allow_picking_directories = False

    def update_current_file_list(self):
        super().update_current_file_list()

        self.current_file_list = [item for item in self.current_file_list if item[1] == '#directory_list_item']



def loop():
    def open_file_dialog():
        global file_dialog    

        rect = pygame.Rect((0,0), (200, 50))
        rect.center = screen.get_rect().center

        file_dialog = pygame_gui.windows.ui_file_dialog.UIFileDialog(rect=rect, manager=manager, allow_picking_directories=True)
    pygame.init()

    screen = Window().displayScreen
    manager = pygame_gui.UIManager((Window().res))

    rect = pygame.Rect((0,0), (200, 50))
    rect.center = screen.get_rect().center

    time_delta_stack = deque([])
    button_directory = pygame_gui.elements.UIButton(relative_rect=rect, text = 'Select Default Cores', manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick() / 1000.0  
        time_delta_stack.append(time_delta)
        if len(time_delta_stack) > 2000:
            time_delta_stack.popleft()

                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_running = False

            if event.type == VIDEORESIZE:
                pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
                Window.resize()
                Images().__call__()
                manager.draw_ui(screen)
                Window().refresh()

            if event.type == pygame.USEREVENT:

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_directory:
                        open_file_dialog()

            if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                if event.ui_element == file_dialog:
                    print('Selected:', event.text)

            manager.process_events(event)

        
        manager.update(time_delta)

        screen.fill(Colors().black)
        manager.draw_ui(screen)
        pygame.display.update()
