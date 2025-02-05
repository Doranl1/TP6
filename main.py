import arcade
from enum import Enum


class State(Enum):
    ROUND_DONE = 0
    GAME_OVER = 1
    NOT_STARTED = 2
    ROUND_ACTIVE = 3


class Choice(Enum):
    NONE = 0
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class MyGame(arcade.Window):
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        super().__init__(self.window_width, self.window_height, "Jeu de Game")
        self.player_choice = Choice.NONE
        self.bot_choice = None
        self.move_x = 0
        self.move_y = 0

        self.game_state = None

        self.box_x = 100
        self.box_y = 150

        self.cursor_position = 1

        self.cursor_left = self.box_x - 30
        self.cursor_right = self.box_x + 30
        self.cursor_top = self.box_y + 30
        self.cursor_bottom = self.box_y - 30
        self.cursor_color = arcade.color.RED

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

        arcade.draw.draw_lrbt_rectangle_outline(self.cursor_left - 90,
                                                self.cursor_right - 90,
                                                self.cursor_bottom,
                                                self.cursor_top,
                                                self.cursor_color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_update(self, delta_time: float):
        self.cursor_left = (self.box_x - 30) + (90 * self.cursor_position)
        self.cursor_right = (self.box_x + 30) + (90 * self.cursor_position)
        print(f"{self.cursor_position}")

        if self.cursor_position == 1:
            self.player_choice = Choice.ROCK
            print(f"{self.player_choice}\n{self.cursor_position}")

        elif self.cursor_position == 2:
            self.player_choice = Choice.PAPER
            print(f"{self.player_choice}\n{self.cursor_position}")

        elif self.cursor_position == 3:
            self.player_choice = Choice.SCISSOR
            print(f"{self.player_choice}\n{self.cursor_position}")

        if self.game_state == State.ROUND_ACTIVE:
            self.cursor_color = arcade.color.WHITE

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.game_state = State.ROUND_ACTIVE
        if self.game_state == State.ROUND_ACTIVE:
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.cursor_position -= 1
                if self.cursor_position < 1:
                    self.cursor_position = 1

            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.cursor_position += 1
                if self.cursor_position > 3:
                    self.cursor_position = 3

            else:
                pass

    def on_key_release(self, key: int, modifiers: int):
        # if key == arcade.key.LEFT:
        #     self.move_left = not self.move_left
        #
        # elif key == arcade.key.RIGHT:
        #     self.move_right = not self.move_right
        #
        # elif key == arcade.key.UP:
        #     self.move_up = not self.move_up
        #
        # elif key == arcade.key.DOWN:
        #     self.move_down = not self.move_down
        pass


def main():
    MyGame()
    arcade.run()


main()
