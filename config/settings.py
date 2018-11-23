class Settings():
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (199,188,218)

        self.player_limit = 3
        self.levelup = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.difficulty = 1
        self.count = 0

    def increase_level(self):
        self.difficulty += self.levelup