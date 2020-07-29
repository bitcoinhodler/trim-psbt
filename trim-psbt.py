#!/usr/bin/env python3
import fileinput
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'f469-disco', 'libs', 'common'))
from bitcoin import psbt
# base64 encoding
from binascii import a2b_base64, b2a_base64


def strip(orig_psbt):
    """Given a base64 PSBT, strip it and return base64 PSBT."""
    # first convert it to binary
    raw = a2b_base64(orig_psbt)
    # then parse
    tx = psbt.PSBT.parse(raw)

    for inp in tx.inputs:
        if inp.witness_utxo and inp.non_witness_utxo:
            inp.non_witness_utxo = None
    rawout = tx.serialize()
    # convert to base64
    b64_psbt = b2a_base64(rawout)
    # somehow b2a ends with \n...
    if b64_psbt[-1:] == b"\n":
        b64_psbt = b64_psbt[:-1]
    # print
    new_psbt = b64_psbt.decode('utf-8')
    return new_psbt


def main():
    # Read base64 PSBT from stdin, or file specified on cmdline
    with fileinput.input() as fin:
        orig_psbt = next(fin)
    print(strip(orig_psbt))


if __name__ == '__main__':
    main()
