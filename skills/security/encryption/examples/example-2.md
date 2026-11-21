# Example 2 — Key held by the key store, not the code

Note: demonstrates SE-147 — key material lives in the KMS/platform key store and is referenced by ID, never committed beside the data (BAN-SE-075, DET-CODE-018).

## Before

```python
# config.py — committed to the repo, next to the encrypted columns it
# unlocks. Anyone with read access to either one has both.
FIELD_KEY = "9f2c41aa07d3e58b1c6f04d92a77be10"  # AES key for users.tax_id

def encrypt_tax_id(value: str) -> bytes:
    return aes_gcm_encrypt(bytes.fromhex(FIELD_KEY), value.encode())
```

## After

```python
# The repo holds only a key ID. The key itself is generated and kept by
# the key store; every use is access-logged there (SE-149).
FIELD_KEY_ID = "projects/app-prod/keys/field-encryption"  # not key material

def encrypt_tax_id(value: str) -> bytes:
    key = key_store.get_key(FIELD_KEY_ID)  # KMS / platform key store client
    return aes_gcm_encrypt(key, value.encode())
```
