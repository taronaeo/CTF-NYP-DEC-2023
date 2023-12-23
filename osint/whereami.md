# Where am I

**Challenge Category: OSINT** <br />
**Challenge Points: 500**

## Challenge Description

HELP ME PLEASE...I'm stuck-in-a-videogame :'(( I don't know how to get out! గితుబ్

## Solution

1. The challenge description included some funky looking characters that look like some sort of emoji `గితుబ్`.
2. Put those "emoji" into Google and it will return GitHub as the first result — this is the clue.
3. Use GitHub's search feature with the next clue `stuck-in-a-videogame` and it will return the repository https://github.com/ctfwhoami/stuck-in-a-videogame.
4. Clone the repository locally using `git clone https://github.com/ctfwhoami/stuck-in-a-videogame`.
5. Iterate through all commit code and get the flag.

```sh
git --no-pager log --patch | grep -o "NYP{.*}"
```

```
NYP{Y0u-f0unD-m3!}
NYP{Y0u-f0unD-m3!}
```
