# Flag Guesser

**Challenge Category: Reverse** <br />
**Challenge Points: 500**

## Challenge Description

No luck? Try this challenge for some easy points! All you need is to guess... or brute force?

[(Download flag_guesser)](../.files/reverse_flag_guesser)

## Analysis

```sh
$ file flag_guesser
```

```
flag_guesser: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=565025f93bc78caf780efe5134a7de8ecf211fdb, for GNU/Linux 3.2.0, not stripped
```

Hints:

- `ELF 64-bit LSB pie executable` - looks like we're working with an Executable and Linkable Format file
- `not stripped` - debugging information and other redundant data are not stripped from the executable, making debugging easier.

## Solution

1. Run `gdb` to analyse the ELF executable.

```sh
gdb flag_guesser
```

```sh
GNU gdb (Debian 13.2-1) 13.2
...[truncated]...

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from flag_guesser...
(No debugging symbols found in flag_guesser)
(gdb)
```

2. Find out the functions used in the executable.

```sh
(gdb) info functions
```

```diff
  All defined functions:

  Non-debugging symbols:
  0x0000000000001000  _init
  0x0000000000001030  puts@plt
  0x0000000000001040  strlen@plt
  0x0000000000001050  printf@plt
+ 0x0000000000001060  strcmp@plt
  0x0000000000001070  __isoc99_scanf@plt
  0x0000000000001080  strcat@plt
  0x0000000000001090  __cxa_finalize@plt
  0x00000000000010a0  _start
  0x00000000000010d0  deregister_tm_clones
  0x0000000000001100  register_tm_clones
  0x0000000000001140  __do_global_dtors_aux
  0x0000000000001180  frame_dummy
  0x0000000000001189  main
  0x000000000000132c  _fini
```

`strcmp@plt` is interesting because it is most likely the function responsible for comparing our input against theirs. We'll set a breakpoint at it's function address `0x0000000000001060`.

3. Set breakpoint at function-of-interest.

```sh
(gdb) b *0x0000000000001060
```

```
Breakpoint 1 at 0x1060
```

4. Run the executable.

```sh
(gdb) run
```

```sh
Starting program: flag_guesser
Warning:
Cannot insert breakpoint 1.
Cannot access memory at address 0x1060
```

If you get the error above, proceed with the following commands. Otherwise, continue to Step 5.

```sh
(gdb) delete
```

```sh
Delete all breakpoints? (y or n) y
```

Re-attempt steps 2 to 4, and you should get a successful run.

5. Enter random input to hit breakpoint.

```sh
(gdb) run
```

```diff
  The program being debugged has been started already.
  Start it from the beginning? (y or n) y
  Starting program: flag_guesser
  [Thread debugging using libthread_db enabled]
  Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
+ Guess the flag: geagega

+ Breakpoint 2, 0x0000555555555060 in strcmp@plt ()
```

6. Check registers.

```sh
(gdb) info registers
```

```diff
+ rax            0x7fffffffdd30      140737488346416
  rbx            0x37                55
  rcx            0x594e007d          1498284157
  rdx            0x7fffffffdd70      140737488346480
  rsi            0x7fffffffdd70      140737488346480
  rdi            0x7fffffffdd30      140737488346416
  rbp            0x7fffffffde00      0x7fffffffde00
  rsp            0x7fffffffdd18      0x7fffffffdd18
  r8             0x7fffffffdd20      140737488346400
  r9             0x7ffff7f9eaa0      140737353738912
  r10            0x7ffff7ddd0a0      140737351897248
  r11            0x7ffff7f1f270      140737353216624
  r12            0x0                 0
  r13            0x7fffffffdf28      140737488346920
  r14            0x555555557dd8      93824992247256
  r15            0x7ffff7ffd000      140737354125312
  rip            0x555555555060      0x555555555060 <strcmp@plt>
  eflags         0x246               [ PF ZF IF ]
  cs             0x33                51
  ss             0x2b                43
  ds             0x0                 0
  es             0x0                 0
  fs             0x0                 0
  gs             0x0                 0
```

`rax` is interesting here because by convention, `rax` is used to store a function's return value.

7. Convert `rax` memory address to string.

```sh
(gdb) x/s 0x7fffffffdd30
```

```sh
0x7fffffffdd30: "NYP{b1n4ry_C_FL4g_GU35S1ng}"
```
