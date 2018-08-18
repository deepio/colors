# Style
This is the logging format and colors I use when using logging modules for local dev. It is possible to edit the colors yourself by following the information bellow. Here is how the ANSI escape codes work for fonts and colors.

<img src="./Screen Shot.png">

#### Escape codes
All escape codes in this project (there are others you can use) start with the escape key `\033` + `[`.

#### Font face
You can add styles with the following codes.
```
0     Reset all colors and styles
1     Bold text
3     Italic text
4     Underline
9     Strikethrough
22    Remove Bold
23    Remove Italic
24    Remove Underline
29    Remove Strikethrough
```

#### Font colors
Each character is in a box, these codes are for the text only.
```
30    black
31    red
32    green
33    yellow
34    blue
35    magenta
36    cyan
37    white
```
This is for the background of each character box.
```
40    black
41    red
42    green
43    yellow
44    blue
45    magenta
46    cyan
47    white
```
For more advanced colors, you can use `38;5;` and an additional color number from 0-255. For example, `38;5;245` is gray, `38;5;255` is white.

### Finished codes
Once you have decided on your style, finish the code with `m`. An example of a finished `ANSI` code is this `\033[40m` or this `\033[38;5;245m`.

As you can see, the different numbers are seperated with a `;` semi-colon. This is how you can add a `font face` with a color `\033[38;5;255;1m` at the same time. You can also compound codes `\033[91;1m\033[40m` if you want to make it more readable. Remember to add a reset code at the end of your string to remove all your styles at the end of the string.
