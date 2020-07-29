# trim-psbt

This is a tool to trim Bitcoin PSBTs (Partially Signed Bitcoin
Transactions) down to a smaller size by removing unnecessary info.

# Who is this for?

Only me. Unless you can audit the code (including the changes I made
in the submodule), you should not use this. It could maliciously alter
the PSBT (to send your coins to me, for example).

# How do I use it?

With your base64-encoded PSBT in a file, run:

  $ ./trim_psbt.py < my-psbt.txt > trimmed-psbt.txt

# What does it remove?

For each input that has both `non_witness_utxo` and `witness_utxo`
input data, it will remove the `non_witness_utxo`.

# Why?

My PSBT use case is offline signing via printed QR codes. The
`non_witness_utxo` can be huge, and is only there to work around a
minor security issue.

# Security issue? What?

See [Trezor's
blog](https://blog.trezor.io/latest-firmware-updates-correct-possible-segwit-transaction-vulnerability-266df0d2860)
and the [Bitcoin Core
response](https://github.com/bitcoin/bitcoin/pull/19215).

As long as you don't sign the same UTXOs multiple times, you are not
vulnerable.
