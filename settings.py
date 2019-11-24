class Settings():
    def __init__(self):
        # 游戏画面的宽
        self.screen_width = 1028
        # 游戏画面的高
        self.screen_height = 750
        # 游戏画面的初始颜色
        self.bg_color = (255, 255, 255)
        # 飞船速度的设置
        self.ship_speed_factor = 1.5
        # 子弹速度
        self.bullet_speed_factor = 1
        # 子弹宽度
        self.bullet_width = 3000
        # 子弹长度
        self.bullet_height = 15
        # 子弹颜色（深灰色）
        self.bullet_color = 60, 60, 60
        # 限制未消失的子弹为3颗
        self.bullet_allowed = 3
        # 外星人设置
        self.alien_speed_factor = 0.5
        # 外星人触碰到边界下移的距离
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1


