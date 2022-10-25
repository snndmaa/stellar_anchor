import os
from pymono import Mono

print(dir(Mono))
#App Secret Key
os.environ['MONO-SEC-KEY'] = "test_sk_7U2TH2kPxGwwrmpB6Hik"

#Code gotten from Mono Connect Vanilla JS app
mono = Mono('code_iBNdxM9EJmmEyEgTiCgD')

#Authenticate user and save user object and http status code
(data, status) = mono.Auth()
print(data)

#Get user Id from user object saved above
mono.SetUserId(data.get("id"))

#Get this particular users account object
print(mono.getAccount())

#Get account statement from the last 12 months and a pdf file that can be downloaded from browser
print(f'------------------------\
    \n \
    {mono.getStatement("last12month", "pdf")}')