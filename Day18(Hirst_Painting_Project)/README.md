# 🎨 Hirst Painting Dot Grid

A Python turtle graphics project inspired by the dot paintings of artist Damien Hirst. This program draws a colorful 10x10 grid of dots using randomly selected RGB colors.

## ▶️ Features

- Uses `turtle` graphics to draw 100 evenly spaced dots
- Colors extracted from an image using the `colorgram` module (optional)
- Generates randomized color pattern from a preset palette
- Runs fast and ends with click-to-close interaction

## 🧠 Concepts Practiced

- Working with the turtle graphics module
- Custom RGB color support using `turtle.colormode(255)`
- Loops and grid drawing logic
- Using `random.choice()` to select colors
- Pen control and heading manipulation with `setheading()`

## 🖼️ Optional Color Extraction

You can use the `colorgram` module to extract colors from an image:

```python
import colorgram
colors = colorgram.extract('image.jpg', 30)