try:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
    from cryptography.hazmat.primitives import serialization
except ImportError:
    Ed25519PrivateKey = Ed25519PublicKey = None

def sign_digest(private_key, digest):
    if Ed25519PrivateKey is None: raise RuntimeError("cryptography is required for Ed25519 signing")
    if isinstance(private_key, str): private_key = bytes.fromhex(private_key)
    key = Ed25519PrivateKey.from_private_bytes(private_key)
    return key.sign(digest.encode()).hex()

def verify_signature(public_key, digest, signature):
    if Ed25519PublicKey is None: raise RuntimeError("cryptography is required for Ed25519 verification")
    if isinstance(public_key, str): public_key = bytes.fromhex(public_key)
    try:
        Ed25519PublicKey.from_public_bytes(public_key).verify(bytes.fromhex(signature), digest.encode())
        return True
    except Exception:
        return False
