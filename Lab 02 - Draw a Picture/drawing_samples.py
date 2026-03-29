""" This is a sample program to show how to draw using the Python Arcade library"""

import arcade

# opens a window with size(width,height) and title
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
# start drawing
arcade.start_render()

# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rect_filled(arcade.XYWH(100, 320, 20, 60), arcade.csscolor.SIENNA)
# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_lrbt_rectangle_filled(0,599,0,300, arcade.csscolor.GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_rect_filled(arcade.XYWH(200, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 arcade.color.BLACK, 24)
# stop drawing
arcade.finish_render()
# keeps the window open till someone close it
arcade.run()