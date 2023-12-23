# Shucks

**Challenge Category: Forensics** <br />
**Challenge Points: 500**

## Challenge Description

Find the fragments of a long-lost flag scattered across the network.

[(Download Shucks.pcapng)](../.files/forensics_shucks.pcapng)

## Solution

1. We can use `tcpdump` to quickly filter through all packets to find a match closest to our flag.

```sh
tcpdump -qns 0 -A -r Shucks.pcapng | grep NYP
```

```html
reading from file Shucks.pcapng, link-type EN10MB (Ethernet), snapshot length
262144
<title>NYP InfoSec CTF</title>
username=NYP%7Bpack&password=e7_dE7ec7ive%7D
<title>NYP InfoSec CTF</title>
```

2. The flag is split between the `username` and `password` form data. We can remove the `username=` and `&password=`

```sh
$ tcpdump -qns 0 -A -r forensics_shucks.pcapng | grep NYP | sed 's/username=//; s/&password=//' | grep -o "^NYP.*$"
```

```
NYP%7Bpacke7_dE7ec7ive%7D
```

3. URL decode the flag

```sh
$ tcpdump -qns 0 -A -r forensics_shucks.pcapng | grep NYP | sed 's/username=//; s/&password=//' | grep -o "^NYP.*$" | php -r 'echo urldecode(fgets(STDIN));'
```

```
NYP{packe7_dE7ec7ive}
```
