#!/usr/bin/env python3
import fileinput
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'f469-disco', 'libs', 'common'))
from bitcoin import psbt
# base64 encoding
from binascii import a2b_base64, b2a_base64


def main():
    # Read base64 PSBT from stdin, or file specified on cmdline
    with fileinput.input() as fin:
        orig_psbt = next(fin)

    # first convert it to binary
    raw = a2b_base64(orig_psbt)
    # then parse
    tx = psbt.PSBT.parse(raw)

    for inp in tx.inputs:
        if inp.witness_utxo and inp.non_witness_utxo:
            inp.non_witness_utxo = None

    print_psbt(tx)


def print_psbt(psbt):
    """Given a PSBT object, write it in base64 to stdout."""
    raw = psbt.serialize()
    # convert to base64
    b64_psbt = b2a_base64(raw)
    # somehow b2a ends with \n...
    if b64_psbt[-1:] == b"\n":
        b64_psbt = b64_psbt[:-1]
    # print
    new_psbt = b64_psbt.decode('utf-8')
    print(new_psbt)


if __name__ == '__main__':
    main()
