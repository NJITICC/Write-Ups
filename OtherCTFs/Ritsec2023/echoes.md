# Echoes

Description: Do you hear that?

What do they give:

Echoes gives you a website that has one form. This form was XSS vulnerable, but that wasn't the *intended* solution.
The form simply echoes whatever text you enter.

Now, I believe they wanted a user to figure out that if you type the following:
```
; ls
```
That it would list the contents of the directory.

From there, a user could enter the following:
```
; cat flag.txt
```

However, that wasn't actually necessary.

I went out on a hunch and simply added /flag.txt to the url.

That wasn't secured, and out came the flag. 