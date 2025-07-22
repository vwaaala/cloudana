# governance_service.py
# TODO: Proposal creation, vote recording, finalization

# TODO: create_proposal(creator_pubkey, title, desc_uri, options)
# - Validate stake > minimum threshold
# - Create proposal in DB
# - Set status = active

# TODO: vote(voter_pubkey, proposal_id, option)
# - Confirm user hasn't voted
# - Use staked CLD as weight
# - Append to vote tally

# TODO: finalize(proposal_id)
# - Tally votes
# - Update proposal status to passed/rejected
# - Store outcome in DB
