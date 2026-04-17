"""
Module 5 OWASP Code Fixes
This will display the original codes with vulnerabilties and their fixed versions.
"""

# Original code for Broken Access Control
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())

# Fixed code for Broken Access Control
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    if user.id != current_user.id:
        return jsonify({'error': 'Unauthorized access'}), 403
    return jsonify(user.to_dict())

#-----------------------------------------#

# Original code for Cryptographic Failures
import hashlib
from urllib import request

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
# Fixed code for Cryptographic Failures
import bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

#-----------------------------------------#

# Original code for Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    user = db.users.find_one({"username": username})
    return jsonify(user)
# Fixed code for Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')

    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        return {"error": "User not found"}, 404

    return user.to_dict()

#-----------------------------------------#

# Original code for Insecure Design
@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return 'Password reset'
# Fixed code for Insecure Design
import bcrypt
@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email'] 
    new_password = request.form['new_password'] 
    user = User.query.filter_by(email=email).first()
    if not user: # Validate user existence before proceeding
        return 'User not found', 404
    hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()) # Hash the new password before storing it
    user.password = hashed_password # Store the hashed password instead of the plain text password
    db.session.commit()  
    return 'Password reset email sent'

#-----------------------------------------#

# Original code for Software and Data Integrity Failures
<script src="https://cdn.example.com/lib.js"></script>
# Fixed code for Software and Data Integrity Failures
<script src="https://cdn.example.com/lib.js" integrity="sha384-abc123" crossorigin="anonymous"></script>

#------------------------------------------#

# Original code for Server-Side Request Forgery (SSRF)
url = input("Enter URL: ")
response = requests.get(url)
print(response.text)
# Fixed code for Server-Side Request Forgery (SSRF)
import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = {"example.com", "api.example.com"} # Define a set of allowed domains to restrict outgoing requests

def is_allowed(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"): # Ensure only HTTP and HTTPS schemes are allowed
        return False

    return parsed.hostname in ALLOWED_DOMAINS 

url = input("Enter URL: ")

if not is_allowed(url): # Validate the URL against the allowed domains before making the request
    raise ValueError("Blocked unsafe URL")

response = requests.get(url, timeout=5)
print(response.text)

#------------------------------------------#

# Original code for Identification and Authentication Failures
if (inputPassword.equals(user.getPassword())) { 
    // Login success
}
# Fixed code for Identification and Authentication Failures
import bcrypt

def login(input_password, stored_password):
    if bcrypt.checkpw(input_password.encode(), stored_password.encode()):
        # Login success
        return True
    else:
        # Login failed
        return False
