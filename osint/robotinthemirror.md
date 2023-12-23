# Boss Encounter - The Robot In The Mirror

**Challenge Category: OSINT** <br />
**Challenge Points: 500**

> As of writing, the video is no longer available. You may not be able to reproduce the steps.

## Challenge Description

You enter a dungeon room. Inside was a completely normal bed room, with a giant broze mirror in the middle. You look through the mirror, u see the background of the room you are in. However, instead of you in the mirrror, a pure white robot is instead in your place. He does not make a sound or attempt to talk, just following you actions as if you are looking into a real mirror. The only detail on him is a wierd code indnted on his forehead that reads "MVZz4iWRK2f="

## Solution

1. Google "The Robot In The Mirror" and there will be countless videos on YouTube showcasing a robot looking at itself through the mirror — this is the clue.
2. The challenge description also included a clue that looks like a typical YouTube video identifier `MVZz4iWRK2f=`.
3. Take any YouTube video URL and replace the address to `/watch?v=MVZz4iWRK2f=`.
4. An unlisted YouTube video will be found, with clues of Base64 everywhere.
5. The actual flag can be found in the video transcription `TllQe0wxa0Umc1ViNWNyMUJlfQo=`.
6. Base64 decode and you will get the flag.

```sh
$ echo "TllQe0wxa0Umc1ViNWNyMUJlfQo=" | base64 -d
```

```
NYP{L1kE&sUb5cr1Be}
```
