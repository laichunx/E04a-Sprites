#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)

        self.chars_list = arcade.SpriteList()
        

    def setup(self):
        x_pos = 0
        y_pos = 0
        chars = ['adventurer_cheer1', 'adventurer_stand','female_cheer1','female_stand','player_cheer1','player_stand','soldier_cheer1','soldier_stand','zombie_cheer1','zombie_stand']

        for i in range(500):
            if(x_pos >= 800):
                y_pos += 40
                x_pos = 0
            if(y_pos >= 600):
                break
            char = random.choice(chars)
            self.chars_sprite = arcade.Sprite("assets/{char}.png".format(char=char), 0.5)
            self.chars_sprite.center_x = x_pos
            self.chars_sprite.center_y = y_pos
            self.chars_list.append(self.chars_sprite)
            x_pos+=25
            
    def move(self):
        self.chars_list[random.randint(0,len(self.chars_list))].center_x += 5

    def on_draw(self):
        arcade.start_render()
        self.chars_sprite.center_x = self.x
        self.chars_sprite.center_y = self.y
        self.chars_list.draw()


    def update(self, delta_time):
        self.chars_list.update()


    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.move()

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()