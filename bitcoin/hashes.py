import hashlib


def double_sha256(msg: bytes) -> bytes:
    """sha256(sha256(msg)) -> bytes"""
    return hashlib.sha256(hashlib.sha256(msg).digest()).digest()


def hash160(msg: bytes) -> bytes:
    """ripemd160(sha256(msg)) -> bytes"""
    return hashlib.ripemd160(hashlib.sha256(msg).digest()).digest()


def sha256(msg: bytes) -> bytes:
    """one-line sha256(msg) -> bytes"""
    return hashlib.sha256(msg).digest()


def ripemd160(msg: bytes) -> bytes:
    """one-line rmd160(msg) -> bytes"""
    return hashlib.ripemd160(msg).digest()
