from __future__ import print_function
import update
import signature
import host
#import paramiko
import simulator as sim
import sys
import serpent
from ethereum import tester, utils, abi



"""
This simulator just instantiates a bunch of hosts. The hosts are just run serially,
for simplicity, although this simulation is intended to demonstrate host processes
running completely independently/asynchronously.


"""

#init the blockchain, with the consensus contract
print("building tester and contract...")
s = tester.state()
c = s.abi_contract("consensusContract.se")

simulator = sim.Simulator("newExe.exe","oldExe.exe","evilExe.exe",["./h1","./h2","./h3","./h4","./h5"],c)

if simulator.Init():
	if "--good" in sys.argv:
		"""
		Success example: have master send the update, hosts register, and commit the changes

			0) Have hosts run their current exe's in turn
			1) Master sends update to all hosts
			2) Each host receives, and then registers the change (this is done serially in simulation, for simplicity)
			3) Each host re-polls the contract, committing if and only if all registrations are correct
			4) Each host runs their exe to verify the new file has been "installed"
		"""
		simulator.RunHostExes()
		simulator.GoodUpdateAllHosts()
		simulator.RegisterAll()
		simulator.RepollAll()
		simulator.RunHostExes()

	elif "--evil" in sys.argv:
		"""
		Malicious example:

			0) Have hosts all run their current exe's, to show current context
			1) Master sends update to all hosts, but have host-j receive a malicious copy
			2) Each host receives, and then registers the change, but host-j's registration should fail
			3) Each host re-polls, but they all see that host-j received a bad copy
			4) Each host discards the update they received, if an insufficient number of registrations are correct
			5) Each host re-runs their exe to show which version they have installed
		"""
		simulator.RunHostExes()
		simulator.EvilUpdateAllHosts(2)
		simulator.RegisterAll()
		simulator.RepollAll()
		simulator.RunHostExes()

	else:
		print("ERROR no option [--good,--evil] found for testing")


