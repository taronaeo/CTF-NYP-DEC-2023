# One too many

**Challenge Category: Forensics** <br />
**Challenge Points: 500**

## Challenge Description

Someone decoded all our text files and now we cant find our super duper important flag

[(Download challenge.zip)](../.files/forensics_one_too_many.zip)

## Solution

The flag is hidden in 1 out of the 1,000 files with Base64 encoding on all the files.

```sh
#!/bin/bash

for file in *; do
  decoded_content=$(base64 -d "$file")
  if grep -q "NYP" <<< "$decoded_content"; then
    echo "Found $file: $decoded_content"
    break
  fi
done
```

```
...
base64: invalid input
base64: invalid input
...
Found flag5934.txt: NYP{th3_0n3_oF_m4ny} cry
```
