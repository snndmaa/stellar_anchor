def info(request, asset, lang, exchange):
    print(request, asset)
    return {
    "fields": {
        "email_address" : {
            "description": "your email address for transaction status updates",
            "optional": True
        },
        "amount" : {
            "description": "amount in USD that you plan to deposit"
        },
        "type" : {
            "description": "type of deposit to make",
            "choices": ["SEPA", "SWIFT", "cash"]
        }
    },
    "types": {
        "bank_account": {
            "fields": {
                "dest": {"description": "your bank account number" },
                "dest_extra": { "description": "your routing number" },
                "bank_branch": { "description": "address of your bank branch" },
                "phone_number": { "description": "your phone number in case there's an issue" }
            }
        },
        "cash": {
            "fields": {
                "dest": {
                    "description": "your email address. Your cashout PIN will be sent here.",
                    "optional": True
                }
            }
        }
    }
    }