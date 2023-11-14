"""pratice for exam 2."""

def favorite_colors(colors: dict[str, str]) -> str:
    color_count = {}
    max_count = 0
    favorite_color = ""
    
    for name, color in colors.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
        if color_count[color] > max_count:
            max_count = color_count[color]
            favorite_color = color
        elif color_count[color] == max_count and favorite_color != color:
            # If there is a tie for most popular color, return both colors
            favorite_color += ", " + color
    
    return favorite_color


print(favorite_colors({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Jordan": "yellow"}))