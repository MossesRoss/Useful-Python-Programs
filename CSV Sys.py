import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

class Voter:
    def __init__(self, name, voter_id):
        self.name = name
        self.voter_id = voter_id
        self.voted = False

class VotingSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.voters = {}

    def register_voter(self, name, voter_id):
        if voter_id not in self.voters:
            self.voters[voter_id] = Voter(name, voter_id)
            print(f"Voter {name} registered successfully.")
        else:
            print("Voter already registered.")

    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            voter = self.voters[voter_id]
            if not voter.voted:
                block_data = {"voter_id": voter_id, "candidate": candidate}
                new_block = Block(len(self.blockchain.chain), datetime.datetime.now(), block_data, self.blockchain.get_latest_block().hash)
                self.blockchain.add_block(new_block)
                voter.voted = True
                print(f"Vote from {voter.name} recorded successfully.")
            else:
                print("Voter has already cast their vote.")
        else:
            print("Voter not found.")

    def display_results(self):
        print("\nVoting Results:")
        candidate_votes = {}
        for block in self.blockchain.chain[1:]:
            candidate = block.data["candidate"]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

        for candidate, votes in candidate_votes.items():
            print(f"{candidate}: {votes} votes")

voting_system = VotingSystem()

voting_system.register_voter("Alice", "123")
voting_system.register_voter("Bob", "456")

# Vote
voting_system.vote("123", "Candidate A")
voting_system.vote("456", "Candidate B")
voting_system.vote("123", "Candidate B")  # Attempt to vote again (should fail)

# Display Results
voting_system.display_results()
