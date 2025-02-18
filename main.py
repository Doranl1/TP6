import arcade
import random

from game_state import State
from attack_animation import AttackType, AttackAnimation


class MyGame(arcade.Window):
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        super().__init__(self.window_width, self.window_height, f"Jeu de Game")
        self.player_choice = None
        self.player_point = 0
        self.bot_choice = None
        self.bot_point = 0
        self.move_x = 0
        self.move_y = 0

        self.round_state = f"tie"

        self.game_state = State.NOT_STARTED

        self.box_x = 100
        self.box_y = 150

        self.cursor_position = 1

        self.cursor_left = self.box_x - 50
        self.cursor_right = self.box_x + 50
        self.cursor_top = self.box_y + 50
        self.cursor_bottom = self.box_y - 50
        self.cursor_color = arcade.color.BRICK_RED

        self.image_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.paper_list = arcade.SpriteList()
        self.scissor_list = arcade.SpriteList()

        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock.center_x = 100
        self.rock.center_y = 150
        self.rock_list.append(self.rock)

        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.center_x = 230
        self.paper.center_y = 154
        self.paper_list.append(self.paper)

        self.scissor = AttackAnimation(AttackType.SCISSOR)
        self.scissor.center_x = 345
        self.scissor.center_y = 154
        self.scissor_list.append(self.scissor)

        self.face = arcade.Sprite("assets/faceBeard.png", scale=0.3)
        self.face.center_x = 225
        self.face.center_y = 300

        self.compy = arcade.Sprite("assets/compy.png", scale=1.5)
        self.compy.center_x = 620
        self.compy.center_y = 300

        self.image_list.append(self.scissor)
        self.image_list.append(self.face)
        self.image_list.append(self.compy)

        self.computer_list = arcade.SpriteList()

        self.computer_rock = arcade.Sprite("assets/srock.png", scale=0.7)
        self.computer_rock.center_x = 620
        self.computer_rock.center_y = 150

        self.computer_paper = arcade.Sprite("assets/spaper.png", scale=0.7)
        self.computer_paper.center_x = 620
        self.computer_paper.center_y = 154

        self.computer_scissor = arcade.Sprite("assets/scissors.png", scale=0.7)
        self.computer_scissor.center_x = 620
        self.computer_scissor.center_y = 154

        self.computer_list.append(self.computer_rock)
        self.computer_list.append(self.computer_paper)
        self.computer_list.append(self.computer_scissor)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.GRAY)
        self.rock_list.draw()
        self.paper_list.draw()
        self.scissor_list.draw()
        self.image_list.draw()
        self.computer_list.draw()
        arcade.draw_text(f"Roche, Papier, Ciseaux",
                         100,
                         self.window_height - 90,
                         arcade.color.DARK_RED,
                         50)
        if self.game_state == State.ROUND_ACTIVE:
            arcade.draw_text(f"Utiliser le clavier pour choisir et [Entrée] pour confirmer",
                             20,
                             self.window_height - 125,
                             arcade.color.LIGHT_BLUE,
                             25)
        elif self.game_state == State.NOT_STARTED:
            arcade.draw_text(f"Appuyer sur [Espace] pour commencer!",
                             135,
                             self.window_height - 125,
                             arcade.color.LIGHT_BLUE,
                             25)
        for x in range(0, 3):
            arcade.draw.draw_lrbt_rectangle_outline((self.box_x - 50) + 120 * x,
                                                    (self.box_x + 50) + 120 * x,
                                                    self.box_y - 50,
                                                    self.box_y + 50,
                                                    arcade.color.BRICK_RED,
                                                    3
                                                    )

        arcade.draw.draw_lrbt_rectangle_outline(570,
                                                670,
                                                self.box_y - 50,
                                                self.box_y + 50,
                                                arcade.color.BRICK_RED,
                                                3
                                                )

        arcade.draw.draw_lrbt_rectangle_outline(self.cursor_left - 120,
                                                self.cursor_right - 120,
                                                self.cursor_bottom,
                                                self.cursor_top,
                                                self.cursor_color,
                                                3
                                                )
        arcade.draw_text(f"Player point : {self.player_point}",
                         145,
                         75,
                         arcade.color.LIGHT_BLUE,
                         20
                         )
        arcade.draw_text(f"Bot point : {self.bot_point}",
                         555,
                         75,
                         arcade.color.LIGHT_BLUE,
                         20
                         )

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.game_state == State.ROUND_ACTIVE and button == arcade.MOUSE_BUTTON_LEFT:
            if self.cursor_position == 1:
                self.player_choice = AttackType.ROCK

            elif self.cursor_position == 2:
                self.player_choice = AttackType.PAPER

            elif self.cursor_position == 3:
                self.player_choice = AttackType.SCISSOR

            self.game_state = State.ROUND_DONE

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.game_state == State.ROUND_ACTIVE:
            if 50 <= x <= 150 and 100 <= y <= 200:
                self.cursor_position = 1
            elif 170 <= x <= 270 and 100 <= y <= 200:
                self.cursor_position = 2
            elif 290 <= x <= 390 and 100 <= y <= 200:
                self.cursor_position = 3

    def on_update(self, delta_time: float):
        self.cursor_left = (self.box_x - 50) + (120 * self.cursor_position)
        self.cursor_right = (self.box_x + 50) + (120 * self.cursor_position)

        print(f"{self.bot_choice}")
        if self.cursor_position == 1:
            self.rock.on_update(delta_time)
        elif self.cursor_position == 2:
            self.paper.on_update(delta_time)
        elif self.cursor_position == 3:
            self.scissor.on_update(delta_time)

        if self.game_state == State.ROUND_ACTIVE:
            self.cursor_color = arcade.color.WHITE
            if self.bot_choice is None:
                self.bot_choice = random.randint(1, 3)
                if self.bot_choice == 1:
                    self.bot_choice = AttackType.ROCK
                elif self.bot_choice == 2:
                    self.bot_choice = AttackType.PAPER
                elif self.bot_choice == 3:
                    self.bot_choice = AttackType.SCISSOR

        elif self.game_state == State.ROUND_DONE:
            if self.bot_choice == AttackType.ROCK:
                if self.player_choice == AttackType.ROCK:
                    self.round_state = f"tie"
                elif self.player_choice == AttackType.PAPER:
                    self.round_state = f"win"
                elif self.player_choice == AttackType.SCISSOR:
                    self.round_state = f"lose"

            elif self.bot_choice == AttackType.PAPER:
                if self.player_choice == AttackType.ROCK:
                    self.round_state = f"lose"
                elif self.player_choice == AttackType.PAPER:
                    self.round_state = f"tie"
                elif self.player_choice == AttackType.SCISSOR:
                    self.round_state = f"win"

            elif self.bot_choice == AttackType.SCISSOR:
                if self.player_choice == AttackType.ROCK:
                    self.round_state = f"win"
                elif self.player_choice == AttackType.PAPER:
                    self.round_state = f"lose"
                elif self.player_choice == AttackType.SCISSOR:
                    self.round_state = f"tie"

            if self.round_state == f"win":
                self.player_point += 1
            elif self.round_state == f"lose":
                self.bot_point += 1

            self.bot_choice = None
            self.game_state = State.NOT_STARTED

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

            if key == arcade.key.ENTER:
                if self.cursor_position == 1:
                    self.player_choice = AttackType.ROCK

                elif self.cursor_position == 2:
                    self.player_choice = AttackType.PAPER

                elif self.cursor_position == 3:
                    self.player_choice = AttackType.SCISSOR
                self.game_state = State.ROUND_DONE


def main():
    MyGame()
    arcade.run()


main()
