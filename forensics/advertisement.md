# Advertisement

**Challenge Category: Forensics** <br />
**Challenge Points: 500**

## Challenge Description

Hmm... I wonder where is the flag?

[(Download flag.wim)](../.files/forensics_advertisement.wim)

## Analysis

1. `.wim` extension is unique to only Windows.
2. The challenge title "Advertisement" hints that it could be an ADS (Alternate Data Streams) challenge, also unique to Windows and the NTFS file system.

## Solution 1 (Easiest)

If the flag is hidden in plain sight behind an alternate data stream, we can easily extract out all the strings using the `strings` command.

```sh
strings -a flag.wim
```

```
MSWIM
Hmm... I wonder where is the flag?NYP{streams_@re_aL7ern@t1ng}
I] 9`
o./G
```

And if we clean up a little bit

```sh
strings -a flag.wim | grep -o "NYP{.*}"
```

```
NYP{streams_@re_aL7ern@t1ng}
```

## Solution 2 (Easy)

We can use Powershell to show us all the streams located in the file.

```ps
> Get-Item .\forensics_advertisement.wim -Stream *
```

```
PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\taronaeo\Documents\GitHub\CTF-NYP-DEC-2023\.files\forensics_advertisement.wim::$DATA
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\taronaeo\Documents\GitHub\CTF-NYP-DEC-2023\.files
PSChildName   : forensics_advertisement.wim::$DATA
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\taronaeo\Documents\GitHub\CTF-NYP-DEC-2023\.files\forensics_advertisement.wim
Stream        : :$DATA
Length        : 1467

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\Users\taronaeo\Documents\GitHub\CTF-NYP-DEC-2023\.files\forensics_advertisement.wim:Zone.Identifier
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\Users\taronaeo\Documents\GitHub\CTF-NYP-DEC-2023\.files
PSChildName   : forensics_advertisement.wim:Zone.Identifier
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\Users\taronaeo\Documents\GitHub\CTF-NYP-DEC-2023\.files\forensics_advertisement.wim
Stream        : Zone.Identifier
Length        : 263
```

Notice that there is a `$DATA` stream? We can extract the contents by using:

```ps
> Get-Item .\forensics_advertisement.wim | Get-Content -Stream $DATA
```

```
MSWIMÐ
☺€EÓù™*ÒKkµ3Pœ‘Ç@☺☺☺–☻q☻–´☻☻♥´☻Hmm... I wonder where is the flag?NYP{streams_@re_aL7ern@t1ng}
hÿÿÿÿxI] 9`∟Ú☺€ÿÿÿÿ►Ç„N`∟Ú☺☻►flag.txt(œP☺§òwà C“Ÿ
x☺[XŽæýœ8òëmŸIÇN{•hýßñ‹mè↔§Èflag"Ð"☺☺œP☺§òwà C“Ÿ
x☺[XŽæýœ▼ò▼☺☺òëmŸIÇN{•hýßñ‹mè↔§È▲`☺☻◄☺`☺☺☺íÊÔÅÍ→o./GŠ↨Ž‡ï(↕ã^'ÿþ<WIM><TOTALBYTES>775</TOTALBYTES><IMAGE INDEX="1"><NAME>1</NAME><DIRCOUNT>0</DIRCOUNT><FILECOUNT>1</FILECOUNT><TOTALBYTES>34</TOTALBYTES><CREATIONTIME><HIGHPART>0x01DA1C60</HIGHPART><LOWPART>0x91C5289B</LOWPART></CREATIONTIME><LASTMODIFICATIONTIME><HIGHPART>0x01DA1C60</HIGHPART><LOWPART>0x91C5289B</LOWPART></LASTMODIFICATIONTIME></IMAGE></WIM>
```

We got the flag. Let's cleanup the output a little.

```ps
> Get-Item .\forensics_advertisement.wim | Get-Content -Stream $DATA | Select-String -Pattern "NYP{.*}" -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $_.Value }
```

```
NYP{streams_@re_aL7ern@t1ng}
```
