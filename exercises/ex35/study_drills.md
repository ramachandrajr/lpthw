# Exercise 35: Branches and Functions  

### Problem 1
I can't put a map here :p !

### Problem 2
The truth is I am bad at spellings, and also the only code error I found is the
one I'll mention in problem 5.

### Problem 4
Added more to game, checkout `game_extended.py`.

### Problem 5
In gold room with getting number is that it chekcs if 0 or 1 are in the input
and runs if so. Problem is, if number is 232 it won't work. I'll try to convert to
int  and then throw the message as an error incase that is not possible.

``` python
try:
    how_much = int(choice)
except ValueError:
    dead("Man, learn to type a number.")
```
