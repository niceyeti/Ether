This repo contains a simulation of secure file distribution using ethereum's blockchain.

This is a class demo/simulation, but the protocol works by having a number of hosts H1-Hk,
each of whom have some local executable, call it myExe. Some other node (could be a master,
or another peer) needs to send an updated version of this executable, which it does by signing
and sending to each node. The nodes verify the signature, stage the file for installation/commit,
and then submit their own signatures on some contract on an ethereum block. The ethereum block
contains all signatures for hosts H1-Hk, such that each host can autonomously decide whether
or not to install/commit the file update based on the number of valid signatures submitted to the
block, such that some consensus threshold can give the nodes a high degree of security/corruption-detecting
for the executable they received.

Something like this can go way beyond a software update scheme, extending to all sorts of file sharing scenarios
for which consensus, auditing, source verification, and the like might be useful.

Dependencies: I set my system up and basically froze any ethereum updates, but iirc you should only
need pyethereum, serpent (for python), and whatever its dependencies are. Follow the pyethereum site
install instructions; pip or sudo apt-get install python-ethereum.


To run the simulations:
	0) Set up the test environment:
			sh runSetup

	1) Run the "good" scenario (successful primary use-case of an update distribution):

			python runSimulation --good

		Here, some node sends out a verifiable update, all nodes verify and register it on the
		blockchain, reach consensus, and then install the new executable. The nodes run their executables before and
		after the exe install, so you should see Bender turn into a Penguin.

	2) Run the "evil" attack scenario:
			
			python runSimulation --evil

		Some node sends out verifiable updates, except that host 2 is sent a malicious copy. (Each "update" contains data
		and the PKCS1_v1_5 signature for that data; the assumption here is just that an attacker has kept this signature,
		but replaced the data segment of the update.) The nodes then verify the update they received, and submit their
		signatures to the blockchain, but host 2 catches the unverified signature. As a result, no consensus is reached,
		the hosts don't commit the new update, and so when they re-run their exe's they will all continue to run "Bender".


Output from --good and --evil simulations is in goodTestOutput.txt and evilTestOuput.txt.

These use-cases are not particularly well-defined, and yes, the security/attack has all sorts of holes. This is just
a demo, and maybe the ethereum/contract implementation help someone with starter code.





