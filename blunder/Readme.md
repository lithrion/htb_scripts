This the rate limit bypass script that I used from the Hack the Box machine Blunder.
The proof of concept script came from: 
[https://rastating.github.io/bludit-brute-force-mitigation-bypass/](https://rastating.github.io/bludit-brute-force-mitigation-bypass/)

which takes advantage of CVE-2019-17240.

I made a few minor alternations to load passwords from a wordlist and to generate random IPs (isntead of using the passwords as an IP).
