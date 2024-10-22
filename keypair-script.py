from stellar_sdk import Keypair
 
issuer = Keypair.random()
distributor = Keypair.random()
 
with open("secretKeys.txt", "w") as f:
    f.write(f"Issuer Pubkey: {issuer.public_key} - Issuer Secret: {issuer.secret}\nDistributor Pubkey: {distributor.public_key} - Distributor Secret: {distributor.secret}")