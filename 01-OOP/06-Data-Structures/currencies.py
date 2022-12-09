# pylint: disable=missing-docstring
# pylint: disable=fixme
# pylint: disable=unused-argument

RATES = { 
         "USDEUR": 0.95,
         "GBPEUR": 1.17,
         "CHFEUR": 1.02
        } # TODO: add some currency rates

# `amount` is a `tuple` like (100, EUR). `currency` is a `string`
def convert(amount, currency):
    #pass # TODO 
    if  'USD' == amount[1]:
        return round(amount[0] * RATES["USDEUR"])
    elif amount[1] == "GBP":
        return round(amount[0] * RATES["GBPEUR"])
    elif amount[1] == "CHF":
        return round(amount[0] * RATES["USDEUR"])
    else:
        return  None