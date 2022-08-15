times = ('Palmeiras',	'Corinthians',	'Internacional',	'Atlético-MG',	'Fluminense',	'Athletico-PR',	'São Paulo',	'Santos',	'Flamengo',	'Botafogo',	'Bragantino',	'Goiás',	'Cuiabá',	'Coritiba',	'América-MG',	'Avai',	'Ceará SC',	'Atlético-GO',	'Juventude',	'Fortaleza',
)

print('='*50)
print('\nCinco primeiros colocados',times[0:5])
print('\nQuatro ultimos: ',times[-4:])
print('\nOdem alfabetica',sorted(times))
print('\nPosiçao do Avai',times.index('Avai')+1)
print('='*50)