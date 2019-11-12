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
        self.bullet_width = 3
        # 子弹长度
        self.bullet_height = 15
        # 子弹颜色（深灰色）
        self.bullet_color = 60, 60, 60
        # 限制未消失的子弹为3颗
        self.bullet_allowed = 3


