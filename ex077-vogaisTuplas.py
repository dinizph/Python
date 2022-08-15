times = ('Palmeiras',	   'Corinthians',	 'Internacional',	   'Atletico-MG',	 'Fluminense',	  'Athletico-PR',	    'Sao Paulo',	   'Santos',	  'Flamengo',	    'Botafogo',	    'Bragantino',	  'Goias',	   'Cuiaba',	  'Coritiba',	    'America-MG',	  'Avai',	    'Ceara SC',	    'Atletico-GO',	 'Juventude',	   'Fortaleza',	)

for i in times:
    print(f'Na palavra {i.upper()} temos ', end=' ')
    for letter in i:
        if letter in 'aeiouAEIOU':
            print(letter.lower(), end=' ')
    print('\n')


