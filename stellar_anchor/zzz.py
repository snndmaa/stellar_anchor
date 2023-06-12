from stellar_sdk import Account, Asset, Keypair, Network, TransactionBuilder, Operation, ChangeTrust, TransactionEnvelope, Server
from django.http import JsonResponse

def zzz(request):
    server_url = "https://horizon-testnet.stellar.org"  # Replace with the desired Horizon server URL

    # # Asset details
    asset_code = "RUPEE"  # Replace with the asset code
    asset_issuer = "GCUNL4X72TO6D62UB6ABMJBFNWIJFTAJM6N3IGUNW6AFITTYQ4JWKPX6"  # Replace with the asset issuer's account ID

    # # Client details
    # client_secret_key = "SCVL5E5HIJWKXDKJ4NRJ3RQUU7SGWJ7UV3PHYHEKV6CJG3EWOLPUPRZS"  # Replace with the client's secret key

    # # Load the client's keypair
    # client_keypair = Keypair.from_secret(client_secret_key)

    # # Create the server object
    server = Server(server_url)

    # # Retrieve the client's account details from the server
    # client_account = server.load_account(client_keypair.public_key)
    # print(client_account)
    # # Build the transaction
    # transaction = (
    #     TransactionBuilder(client_account, network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE)
    #     .append_operation(
    #         ChangeTrust(
    #             asset=Asset(asset_code, asset_issuer),
    #             source=client_keypair.public_key
    #         )
    #     )
    #     .build()
    # )

    # # Sign the transaction with the client's keypair
    # transaction.sign(client_keypair)

    # # Submit the transaction to the Stellar network
    # response = server.submit_transaction(transaction)

    # # print(type(response))
    # return JsonResponse(response)



    # Server details
    server_secret_key = "SBT4LQXX3JGH4IE3753SW7O6VNLYGQC7MSPHRB3MN4VVUSGZXUKOL3IL"  # Replace with the server's secret key
    server_keypair = Keypair.from_secret(server_secret_key)
    server_account_id = server_keypair.public_key
    print(server_account_id)
    # Load the server's account details from the server
    server_account = server.load_account(server_account_id)

    # Build the transaction
    transaction = (
        TransactionBuilder(server_account, network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE)
        .append_change_trust_op(Asset(asset_code, asset_issuer))
        .build()
    )

    transaction.sequence = 0
    # Sign the transaction with the server's keypair
    transaction.sign(server_keypair)

    # Get the signed transaction in XDR format
    signed_transaction_xdr = transaction.to_xdr()

    # Return the signed transaction as a JSON response
    return JsonResponse({"signed_transaction": signed_transaction_xdr})