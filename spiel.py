"""
Example of Pymunk Physics Engine Platformer
"""
import arcade

SCREEN_TITLE = "Future Wires"

# Size of screen to show, in pixels
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """
        Kaefer = 0
        Dead_poeple_all = 0
        Dead_poeple_experts = 0
        Dead_poeple_army = 0
        
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        

        # Init the parent class
        super().__init__(width, height, title)

    def setup(self):
        """ Set up everything with the game """
        pass

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        
        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()