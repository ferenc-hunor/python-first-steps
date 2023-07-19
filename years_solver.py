import datetime

x = input('Hany eves vagy?')
print('Tehát a te születesi évéd %d' % (datetime.date.today().year-int(x)))
