implementing a simplified version of consensus algorithms, 2PC and Raft. Through this assignment, you will understand how 2PC achieves distributed commit and Raft achieves fault-tolerant consensus, handle leader election, maintain log consistency, and manage distributed state transitions.

Distributed Banking System (2PC Voting Phase)
Description:
Simulate a distributed banking system where different bank branches must agree on processing a transaction.
Each branch (participant) votes to either commit or abort the transaction based on local account balances and constraints.
Components:
Coordinator (Transaction Manager)
Sends a VoteRequest to all bank branches.
Collects VoteCommit or VoteAbort responses.
Participants (Bank Branches)
Receive a VoteRequest from the coordinator.
Decide to vote commit or abort based on business rules (e.g., account balance, fraud detection).
Failure Handling
Simulate a scenario where some branches may fail (network failure, system crash) and handle responses.

To-Do Implementation steps:

1. Define gRPC Proto File
   Create RPC methods for VoteRequest, VoteCommit, VoteAbort.

2. Implement Coordinator & Participants
   Coordinator sends requests, waits for responses.
   Participants decide commit/abort.

3. Simulate Failures
   Drop some vote responses.
   Introduce artificial delays.

4. Containerize with Docker
   Run at least 5 nodes in separate containers.
   Use Docker Compose for multi-container deployment.
