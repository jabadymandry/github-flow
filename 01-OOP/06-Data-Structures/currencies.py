# pylint: disable=missing-docstring
# pylint: disable=fixme
# pylint: disable=unused-argument

RATES = { 
         "USDEUR": 0.85,
         "GBPEUR": 1.13,
         "CHFEUR": 0.86
        } # TODO: add some currency rates

# `amount` is a `tuple` like (100, EUR). `currency` is a `string`
def convert(amount, currency):
    #pass # TODO 
    if  'USD' == amount[1]:
        return round(amount[0] * RATES["USDEUR"])
    elif amount[1] == "GBP":
        return round(amount[0] * RATES["GBPEUR"])
    elif amount[1] == "CHF":
        return round(amount[0] * RATES["CHFEUR"])
    else:
        return  None