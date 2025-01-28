import arcade
from enum import Enum


class State(Enum):
    ROUND_DONE = 0
    GAME_OVER = 1
    NOT_STARTED = 2
    ROUND_ACTIVE = 3


class PlayerChoice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    MENU = 4


class MyGame(arcade.Window):
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        super().__init__(self.window_width, self.window_height, "Jeu de Game")
        self.player_choice = None
        self.bot_choice = None
        self.move_x = 0
        self.move_y = 0
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        self.box_x = 100
        self.box_y = 150

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.GRAY)
        arcade.draw_text("Roche, Papier, Ciseaux",
                         100,
                         self.window_height - 90,
                         arcade.color.DARK_RED,
                         50)
        arcade.draw_text("Appuyer sur une image pour faire une attaque!",
                         85,
                         self.window_height - 125,
                         arcade.color.LIGHT_BLUE,
                         25)
        for x in range(0, 3):
            arcade.draw.draw_lrbt_rectangle_outline((self.box_x - 30) + 90 * x,
                                                    (self.box_x + 30) + 90 * x,
                                                    self.box_y - 30,
                                                    self.box_y + 30,
                                                    arcade.color.RED)

        arcade.draw.draw_lrbt_rectangle_outline((self.box_x - 30) + 90,
                                                (self.box_x + 30) + 90,
                                                self.box_y - 30,
                                                self.box_y + 30,
                                                arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_update(self, delta_time: float):
        if self.move_left:
            self.move_x = self.box_x - 30 + 90 * self.player_choice

        if self.move_right:
            self.move_x = self.box_x - 30 + 90 * self.player_choice

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.move_left = not self.move_left

        elif key == arcade.key.RIGHT:
            self.move_right = not self.move_right

        else:
            pass

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.move_left = not self.move_left

        elif key == arcade.key.RIGHT:
            self.move_right = not self.move_right

        elif key == arcade.key.UP:
            self.move_up = not self.move_up

        elif key == arcade.key.DOWN:
            self.move_down = not self.move_down


def main():
    MyGame()
    arcade.run()


main()
