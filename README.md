# SMTP Client (Computer Networks Lab)

A Python script that sends an email by speaking the SMTP protocol directly over a TCP socket, without an email library.

## How it works

It connects to smtp.gmail.com on port 587 and sends EHLO, then upgrades the connection to TLS with STARTTLS. It authenticates with AUTH LOGIN using base64-encoded credentials, then sends MAIL FROM, RCPT TO, DATA and QUIT, checking each reply code from the server along the way.

## Run

Add your own email address and an app password where the code has placeholders, then run `python Lab_3.py`. Credentials are redacted in this repo.
