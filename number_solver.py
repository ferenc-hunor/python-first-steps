minimum = 0
maximum = 100
tipp = 50
vege = False

while not vege:
    valasz = input('%d\n' % tipp)
    if valasz == 'nagyobb':
        minimum = tipp
    elif valasz == 'kisebb':
        maximum = tipp
    elif valasz == 'igen':
        print('Ezaaaaaaaaaaaz!!!')
        vege = True
    tipp = (maximum - minimum) / 2 + minimum
