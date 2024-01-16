from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

INFO = {
    "type": "service_account",
    "project_id": "shining-granite-409215",
    "private_key_id": "727f90d49b59fe597001a8ae799a05a9356577ae",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8AyvPwh0dO44I\ndVQiQOIWwbajnBfQNOw6MYkdtaVhLG896eut8WstX0A7wg1pHpEoOBNS+TTVVxD3\nbUcF2+uOyyjWBGTUXD/ApqgZWiGPrvdKrAjvRBWLPSHRqw3z/1zAu3RGwDvJ1BdB\nMccReP6IYxv64NzTPwiOMAlpijEAMBLTscZquiWa1tF41tyjXo3NVDo+04bIxzI5\nEbrXnN2b0rFaNjIAxQE7taV72V0UGsHTZg9nQh0whL2hvjQVMTnmQu8SDTz2LwVF\n03q+K1S3ty6zme5kLm/YdsTw3Q1kEoc6IwNr42ZdtcnCQUbIx6DfaIhfIlHG9LJl\nLXSy5Ge5AgMBAAECggEAAShV1zgfPMRWmge65mEW40P7D2PRI7eHss4GRZgONhxz\nbOKpUE9ZtRROjW+i7IBDLYe22r5tDFk2YgeatdcGSsFGdZbeVg5hWBrOkyViaoON\nwzhu76YwKcTNFgDjG5r5Y7hjvWHGnHYBVKXtT1a63nUZwYAr6+MJ9vIlxLAUoCco\n6O7Rc7tiARed0T/RnxZSrsuMyq8uwmKzCY/aBYmmKVe12Pff6QkKJFteShW1rxeZ\nmYsERGw4JQTXRf/jopvNGm3CeAEmW8mf84Q66xV0dKBwYyBl0HxhjmqOtYnSVafr\nH266enPRO9SkLUavpl8H8ii8+M9Wc8N4O8kwBDgRFwKBgQDssj5rJS8lJgOy/gl3\nf4e8UWuh49SkkWKOE7to75Nv+uTLwvKQLRe51SThkNXBlYW1VVgriUhboAdVHn8a\ntRWUFTSzR7Z4Glz4TNVvelevhsmYUIgIxwQ1tWSqHyel1iSGMjhs9V0HVgIi/fvu\nz5YmVlmDTLYM3nmbf7xFdzX6NwKBgQDLWIDAwGncTv+WecOkpPwUV+ogS8j9xYkr\nwIfBAU507hiZ+moX5DRNz49nUXplX/LTTSC6CCzJWAh79u4fFjwv+wQlu/0U1sFn\nSric/SqKLN78fdprjnLYPkei2Pw542tysRdfd+xmO30Vh8SY989BUHnXXHT8MxP+\nTs+Gh3H1jwKBgB0mSmeZmbfCebwmavYLf6TihhXW4A4wVWnX5kGjF4434MtzQ7ob\nw4tAQ51/38NKbcAKNaSO8JlQGPcTnWWlnXWyMt5NW5xo6sAtfi+PapMUT2lxqX8j\nO1J991q4IYLb332jW62XfhB0OCklDEy5xe0Mv1NbNCRblbBfx8jqSHx7AoGALpjn\nWEQ/ffa0Zx0cEhykj1zeD+yN8GlV16rU8QuFmRH+nTpfGX535eTMbdaj/5sPIBCq\nkTbSXIlJ2G5rfsAvpqcU+jir9ByKUUs0JvV0zBkgOCf253LLKnaLH+wtUG6m7q9a\nNcxbZcn4DfkAujT/T25LnWhYfnqN+FbDA4cCPE0CgYEA6lwz5ZeI6o07bLIHj1/g\nOO+kqp97NTN0jVdN5sqyRSl1mcrjbcLtjZ4Judi1WxlgD07gk0MurSweOf2g95M4\nkkWGn+yVewa2hMG43W6zMFM3ICyO2m31R+psFo6G4KKIHNMuHxN/N5XDDrpgxCit\ndWZWSyvvclF/oCvbL4iom3I=\n-----END PRIVATE KEY-----\n",
    "client_email": "petro2561@shining-granite-409215.iam.gserviceaccount.com",
    "client_id": "108389855424774100620",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/petro2561%40shining-granite-409215.iam.gserviceaccount.com",
}


credentials = ServiceAccountCreds(scopes=SCOPES, **INFO)


async def get_service():
    async with Aiogoogle(service_account_creds=credentials) as aiogoogle:
        yield aiogoogle
