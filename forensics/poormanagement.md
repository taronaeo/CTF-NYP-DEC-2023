# Poor Management

**Challenge Category: Forensics** <br />
**Challenge Points: 500**

## Challenge Description

We got an image of one of the servers used by the game devs of the game we've been trying to get out of. Could you find anything of use? Open it in VMWare. DO NOT DOWNLOAD THIS WITH DATA. DOWNLOAD ONLY WITH WIFI

[(Download kalictf.ova)](https://drive.google.com/drive/folders/1_bnw2rvirwJL8SjRvY-7VRsriIYFXPQ-)

## Analysis

Running the challenge virtual machine in VMWare Workstation, you will realise that it is an image of the original snapshot of the Kali Linux distribution. However, there are some hidden quirks.

### Login Details

Since we know that the challenge virtual machine is based on the original snapshot of the Kali Linux distribution, we know that the default login `username` and `password` is `kali`.

```
Username: kali
Password: kali
```

The `root` account is available to be logged in as well using the `username` and `password` as `root` and `kali`. This login credential will come in later.

```
Username: root
Password: kali
```

### Clues on the Desktop

Logging in with the default `username` and `password`, you will realise that the desktop has 2 text files. `to_do_list.txt` and `note_to_employees.txt`.

```sh
$ cat to_do_list.txt
```

```txt
hmm since i am the boss of this hacking group, i should make a to do list to keep up to date with everything

1. Clean up the "just dump everything here" directory. its in such a messy state, it even has really important files inside that im supposed to be protecting

2. Should probably change my password. I shouldnt use the kali account with its default password. But I mean, it is no longer part of the sudoers group so. good enough right?

3. Find the flag.txt file, i seem to have lost it, but its really important

4. Learn how to actually hack
```

```sh
$ cat note_to_employees.txt
```

```txt
hey guys, i know the system is a mess. if you wanna put anything in the server, just leave it somewhere in the /just_dump_everything_here directory.
i'll sort it out later i guess

~ boss
```

From the clues placed on the desktop, we get hints of the following:

1. There is a `just_dump_everything_here` directory located in the root of the filesystem.
2. The accounts `root` and `kali` have their passwords left as defaults from the base Kali image.
3. The account `kali` has been removed from the sudoers group, which means we can't execute administrative commands.
4. The flag is contained in a file called `flag.txt`.

## Solution

1. Switch to `root` using default password `kali`.

```sh
$ su
```

```
Password: <OUTPUT HIDDEN BY DEFAULT>
```

2. Use the `locate` command to find where the `flag.txt` file is located.

```sh
$ locate flag.txt
```

```
/just_dump_all_stuff_here/important/Bolognese Sauce/spaghetti/bolognese/flag.txt
```

3. Print out the file details

```sh
$ cat "/just_dump_all_stuff_here/important/Bolognese Sauce/spaghetti/bolognese/flag.txt"
```

```
NYP{u5e_str0nk_p@5sw0rDs}
```
