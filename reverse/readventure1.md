# Re Adventure 1

**Challenge Category: Reverse** <br />
**Challenge Points: 500**

## Challenge Description

Deep within the game files, you found a piece of note README.TXT Could it be a clue to how to escape the game? You took a look at the note:
"Greetings, ye unfortunate who have found this note. You are such an unlucky fellow to also be trapped in this game. Now LISTEN UP!!! Don't worry, this game have an exit, but it is locked behind a very difficult RE challenge! But fret not, for I have prepared for you a training course, going through this course will help in preparing you to be more prepared for the final challenge to escape the game! Here's a chall file, the first challenge contains just the basics. Solve it, and move on to the next stage in this little adventure I have prepared for you!"

[(Download chall)](../.files/reverse_re_adventure_1)

## Solution

The challenge file exposes the flag prefix directly, and we can extract it easily using the `strings` tool.

```sh
$ strings chall | grep NYP
```

```
NYP{RE_4dven7uRE_7h3_b4siCs}
```
