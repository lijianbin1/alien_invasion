import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion(object):
    """管理员游戏资源和行为类"""

    def __init__(self):
        """初始化游戏并创建界面"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_high))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏，当点击退出后退出"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """响应按钮和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #飞船向右移动
                    self.ship.rect.x += 40

    def _update_screen(self):
        """更新屏幕图像，并让其可见"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()