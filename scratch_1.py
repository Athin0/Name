
from colorthief import ColorThief
from PIL import Image



color_thief = ColorThief('1567288354942.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=2)
print (palette)
