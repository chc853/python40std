from currency_converter import CurrencyConverter
cc = CurrencyConverter()
print(cc.currencies)

cc1 = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc1.convert(1,'USD','KRW'))