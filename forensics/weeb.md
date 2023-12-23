# Weeb

**Challenge Category: Forensics** <br />
**Challenge Points: 500**

## Challenge Description

Got this from a weeb. There is probably data inside.

[(Download bruh_moment.png)](../.files/forensics_weeb.png)

## Solution

Running commands such as `file`, `binwalk`, `exiftool` will not reveal the flag as it is really an image file. However, this is a steganography challenge.

> Using tools such as `steghide` will not work on this file because it is a `png` file instead of `jpeg`.

```sh
$ zsteg bruh_moment.png
```

```
b1,rgb,lsb,xy       .. text: "NYP{domain_expansion}"
b2,r,msb,xy         .. text: ["U" repeated 153 times]
b2,g,msb,xy         .. text: "@UUUUUUUUUUUUUUUUUUU"
b2,b,msb,xy         .. text: ["U" repeated 8 times]
b2,rgb,msb,xy       .. text: "EQUUUUUUUUUEQ"
b2,bgr,msb,xy       .. text: "UUUUUUUUUUEQ"
b2,abgr,lsb,xy      .. file: OpenPGP Public Key
b2,abgr,msb,xy      .. text: "SCCCCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGCCCCCCCCCCSSSSSSSSSSSSSSSSSSWWWWWWWWWWWWWGGGGGGGCCGGGGGGGGGGGGGWGGGGGGGGGWWWWWWWWWWSSSWWWWWWWWWSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWWSSSSSSSSSSSSSSWWWWWWSSSSCCCCCCCCCCCCCCC"
b3,abgr,msb,xy      .. text: "vdGvdGveWveWveWveWveWveWveWveWveWveWveWveWveWveWveGvdGvdGvdGvdGvd"
b4,r,msb,xy         .. text: ["w" repeated 228 times]
b4,g,msb,xy         .. file: OpenPGP Public Key
b4,b,lsb,xy         .. text: ["\"" repeated 14 times]
b4,b,msb,xy         .. text: "@DDDDDDDDDDDDDD"
b4,rgb,msb,xy       .. text: "7pC7tC7tC7tC7tC7tC7tC7tC7tC7tC7tC7tC7tC7tC7tC7p"
b4,bgr,msb,xy       .. text: "s0Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs4Gs0"
b4,abgr,lsb,xy      .. file: MIDI audio System Exclusive (SysEx) message - GreyMatter, at 6 EOX, at 10 EOX
b4,abgr,msb,xy      .. text: "sOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOsOs"
```

Let's cleanup the output.

```sh
$ zsteg bruh_moment.png | grep -o "NYP{.*}"
```

```
NYP{domain_expansion}
```
