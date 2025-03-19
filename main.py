import os
import hashlib
import random


def generate_keys():
    """Generate public and private keys using a simulated PQC-safe method."""
    secret_key = os.urandom(32)  # Private key
    public_key = hashlib.sha3_256(
        secret_key
    ).digest()  # Public key derived from secret key
    return public_key, secret_key


# Simulated challenge-response signing function
def sign(secret_key, challenge):
    """Simulate signing a challenge using the private key."""
    signature = hashlib.sha3_512(
        secret_key + challenge
    ).digest()  # Use secret_key in signing
    return signature


# Fixed simulated verification function
def verify(secret_key, challenge, signature):
    """Verify the signature using the private key."""
    expected_signature = hashlib.sha3_512(
        secret_key + challenge
    ).digest()  # Fix applied
    return signature[:32] == expected_signature[:32]  # Compare only a portion


# Simulated OTP Generation
def generate_otp():
    """Generate a random 6-digit OTP for MFA."""
    return random.randint(100000, 999999)


# Simulated MFA check (OTP verification)
def verify_otp(user_otp, generated_otp):
    """Check if the OTP entered matches the generated OTP."""
    return user_otp == generated_otp


# Example usage
public_key, secret_key = generate_keys()
challenge = os.urandom(32)  # Generate a random challenge
signature = sign(secret_key, challenge)  # Sign using private key

is_valid_signature = verify(secret_key, challenge, signature)  # Fix: Use secret_key

# MFA step (OTP)
generated_otp = generate_otp()
print(f"Generated OTP: {generated_otp}")  # Simulating sending this to the user
user_otp = int(input("Enter OTP: "))  # Simulating user input

is_valid_otp = verify_otp(user_otp, generated_otp)

# Final MFA result
if is_valid_signature and is_valid_otp:
    print("✅ MFA authentication successful!")
else:
    print("❌ MFA authentication failed!")
