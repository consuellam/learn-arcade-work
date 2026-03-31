# 
import arcade
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = "LAB 2"

def main():
	""" Main function """
	# Create a window class. This is what actually shows up on screen
	arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
	arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
	# Start the arcade drawing
	arcade.start_render()
	# draw cloud
	arcade.draw_circle_filled(460,490, 25, (255, 255, 255))
	arcade.draw_circle_filled(500,460, 45, (255, 255, 255))
	arcade.draw_circle_filled(450,500, 45, (255, 255, 255))
	arcade.draw_circle_filled(500,500, 45, (255, 255, 255))
	# draw rainbow
	arcade.draw_arc_outline(300, 400, 200+ 50, 200 + 25, arcade.csscolor.RED, 0, 180, 25)
	arcade.draw_arc_outline(300, 400, 175+ 50, 175 + 25, arcade.csscolor.ORANGE, 0, 180, 25)
	arcade.draw_arc_outline(300, 400, 150+ 50, 150 + 25, arcade.csscolor.YELLOW, 0, 180, 25)
	arcade.draw_arc_outline(300, 400, 125+ 50, 125 + 25, arcade.csscolor.GREEN, 0, 180, 25)
	arcade.draw_arc_outline(300, 400, 100+ 50, 100 + 25, arcade.csscolor.BLUE, 0, 180, 25)
	arcade.draw_arc_outline(300, 400, 75+ 50, 75 + 25, arcade.csscolor.INDIGO, 0, 180, 25)
	arcade.draw_arc_outline(300, 400, 50+ 50, 50 + 25, arcade.csscolor.VIOLET, 0, 180, 25)
	# Draw the grass
	arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BITTER_LIME)

	# --- Finish drawing ---

	# Keep the window up until someone closes it.
	arcade.finish_render()
	arcade.run()

if __name__ == "__main__":
	main()