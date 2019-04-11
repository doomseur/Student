#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii				

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")
################################# code given #######################################

ciphertext =474862643754336865489984490773307542016161159436213530034995807183836312346778617047666360854948178434525541089212091928949344492697684657497682106740050084305554758259427768463395264318566101255923490595579348647860471822284428834756812967844672795316325109976652375135659724572710513755433401072885408968307124213606768098411795080747616961236626790699862671834311406129266854138764009952421206625693567227556664511584573464971029270576495696636132292906861410359486612705079004947333371264698887189359265840678094723729950785568382017843975809503403984016678927664449791524785943376314787680072596720311587221852

from Crypto.PublicKey import RSA
# privKeyStr= 'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCgf4dwtr3uMrmiJwhBygCsMH7NvyZt394/+K+QFSgvkerAzRMz7GAXRiFjgdHxK93ZxHQpPWdYLt36eAlhWJJd5Eq8896pMdJuxaRUv9tPevkgEmE7bF6y8yyZs//1sSEuM6N6w7f0/2g1WsSdslIykZ5w3manD8ybiZ+20geJEW1Vnzp/QBwc0WijQBVrarugcA1Vnn5hdcY/yBzFTsWioHBaEoN1innr3kwcaNjMskXvshkO7+s+UTDvE8Qm3BE+IaqtKKQRwAipPv874BhTzRk5/RjgeXBTO/0SbAcBg+bQ6z0oIkZspDRIiW7NLL2nfpF20JhhC9e+DIjh67ghAgMBAAECggEAMd2trR16AWoNNw49iINEljszCqXbQMQPf3y6v19zbuQ9Nc4Bq15DtLd7ZDlPi0j/0ssw9Cc51rIpEcr9zxr/zuBBQFfc1GDAat5JYnOBpj4k7QwI3beb7KmVL+Q3IJT6JCqzHk909k/shrc+42gmFcQcoCDZcAp+ncyyrNCwuqsLgI+XUzyYTgEYnkThR0AkkMp7WPzaoG/ii3g+a3c9UAwfNou1kZhezwJtIWn50dY8mX60nx5wdGpiZ997EiyxabLYIXT/hf/RtzlAVd9VxcO/QEvFWfIdfGjZcjt07QjHWnllaQgl8Pc0uNjKDU2AZMTqOxnd2/zhzIbfsbRSyQKBgQDMrnnvMTp/v7AlgLzxM1yLAQT5++CJgxVqdHwcmazAewxe08vzEZSRFYEXzI+te1vTk10gfNg0Oe+936UDsfCXQDuS7D+1b7Q40nm2J1tG4b0ngObNAvS6esD6VqVNsLn4PHSde750v5sqGN8BLWIteBXCwWrLVCSGdO5ENWGYQwKBgQDIvSI6WMKBQAUKt7pw1XHKhdUvaz2FdesLnX+GHvBjDfZ+q4dcZkzBPfII/UI1gPYceBnA2hGvfPCWw0Us6TFVjUv7Yud2IE6MyiLBKHANjZoaQYkWT25waf1dEMEtba8Y9VzAR+qiNqn4jxjArTL39GcvhCM6/FLj1l+q1JHpywKBgQCkkJOQ8O+rzp79SCihdT4utL8fjpfVeAM7+DPhet0eVNB5XahY4gWlMLj+PYY3YTtPPOhfOoFKXFqZOrsd4W8i7I35buE6K3mnRfJ9td75en3uyQDITFwfopqNrCRz9mdPYqwQAnH6xCMpEZ4bADYzgJ1eXMxUdm53fIQlaxXwqQKBgAdplH37EROcvZLrveK0vwLvdjPODfODqy4+nprhQZcmyNdclh7/WA46r1lNoMhA/tWGSc0pQEXuoyOuCjviUIQMN6YMvOdLwhrIzAe96oVVmT8m9Fzyie10vHpXSArZZgHR7Z7cCPn8csJO5mcW/i7Rw42pn3NqJdVr8RRpzQmJAoGBAMXa7nizeu0gg34LXhNPPrSxQxM/ryjO+hyaF9Q8ne7K3jvTryuk56Fhe97mKhzW28QMpfqb5wuk6MNR0we1tyQ678jC7Oabn5tnr2w0CAu+BG0Zu+TcT0+gtvk3+44LIxa0nmPaikn/2bKQGo+jItZkFoC2IXQltAyObcB8o7DR'



from Crypto.PublicKey import RSA


f = open('rsa4_mykey3','r')
privKeyObj =  RSA.importKey(f) # generate the RSA key object
f.close()




rsa_key_var_n = privKeyObj.n
rsa_key_var_e = privKeyObj.e
rsa_key_var_d = privKeyObj.d
rsa_key_var_p = (privKeyObj.p)
rsa_key_var_q = (privKeyObj.q)
rsa_key_var_u = (privKeyObj.u)

## ----- decrypt ciphertext then convert number back to a string
decrypted = pow(ciphertext, rsa_key_var_d, rsa_key_var_n)   ## decrypt
plaintext = int2string(decrypted)
print (plaintext)

