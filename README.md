# Ether
This repo contains a blockchain-based protocol for secure, P2P file distribution using Ethereum.
Peers maintain trust lists which allow them to receive, verify, and commit files (such as executables and updates)
only when a concensus of their peers verify and stage their updates as well. Once k peers have verified the
update, all peers can detect this condition and actually commit the file changes, such as by installing the software.

There ought to be a paper in this repo detailing the protocol.

The Ethereum toolchain and implementation is subject to a lot of rapid change, so anything in this repo is likely to be obsolete
within months, if not weeks.

All work in this repo is copyright Jesse Waite, 2016.
