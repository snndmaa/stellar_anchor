from pagacollect.paga_collect import Collect

principal = "public_key"
credentials = "private"
hash_key = "hash_key"

collect = Collect(principal, credentials, hash_key, False)

payment_request_payload = {
    "referenceNumber": "6020000011z",
    "amount": "100",
    "currency": "NGN",
    "payer": {
        "name": "John Doe",
        "phoneNumber": "07033333333",
        "bankId": "3E94C4BC-6F9A-442F-8F1A-8214478D5D86"
    },
    "payee": {
        "name": "Payee Tom",
        "accountNumber": "1188767464",
        "bankId": "40090E2F-7446-4217-9345-7BBAB7043C4C",
        "bankAccountNumber": "0000000000",
        "financialIdentificationNumber": "03595843212"
    },
    "expiryDateTimeUTC": "2021-05-27T00:00:00",
    "isSuppressMessages": "true",
    "payerCollectionFeeShare": "0.5",
    "recipientCollectionFeeShare": "0.5",
    "isAllowPartialPayments": "true",
    "callBackUrl": "http://localhost:9091/test-callback",
    "paymentMethods": ["BANK_TRANSFER", "FUNDING_USSD"]
}

response = collect.payment_request(payment_request_payload)

print(response)