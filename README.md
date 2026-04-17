# OWASP-Top-Ten-Code-Fix

## Broken Access Control
The problem with the original code is that it allowed anyone to change the user_id to access other accounts and their data. I fixed this by adding a login check to verify that the user id matched the current user and if it didn't it would kick it out. 

## Cryptographic Failures
The problem with the original code is that it was using sha1 a very outdated and inefficient hashing algorithm. And a common cryptographic failure for password storage is a fast hashing method because it allows attackers to use rainbow tables or brute force attacks. So to protect from this I implemented the bcrypt library and used it to salt and hash the password, then added a verify password method since it was missing from the original code. 

## Injection
The problem with the original code is that it would allow attackers to inject malicious code into the database. I protected it from that by making it treat the input as a literal value instead of SQL code

## Insecure Design
The issue with the original code is that it had no user authentication or hashing for the password, and allowed anyone to change the password. This was resolved by adding a user validation check, hashing the new password, and sending the password reset to the email associated with the user. 

## Software and Data Integrity Failures
The issue with the original code was that there was no integrity check, this was resolved by adding an integrity check that would verify that the data or file hasn't been tampered with. 

## Server-Side Request Forgery
The issue with the original code is that it allowed the user to input any URL, which would allow them to access things they shouldn't be able to. This was resolved by implementing set allowed domains and verifying that the input URLs matched the allowed URLs before making the request. 

## Identification and Authentication Failures
The issue with the original code is that it was only checking for simple password checks and wasn't hashing the password in any way. I fixed this by adding a hash to the password and verifying that it matched before allowing a successful login.
