import pandas as pd

storie = pd.read_csv('Storie.csv')
post = pd.read_csv('Post.csv')

# Ci serviranno i seguenti campi per il dataset dei post:
# Descrizione 
# Durata (s)
# Orario di pubblicazione, da splittare in data e ora
# Permalink
# Tipo di post (da richiamare in Formato)
# Visualizzazioni
# Mi piace
# Condivisioni
# Commenti
# Salvataggi
# Copertura
# Follower

# per il dataset delle storie:
# Descrizione 
# Durata (s)
# Orario di pubblicazione, da splittare in data e ora
# Permalink
# Tipo di post 
# Visualizzazioni
# Copertura
# Mi piace
# Condivisioni
# Visite al profilo
# Risposte
# Clic su link
# Tocchi sugli adesivi
# Esiste un campo Follower
# Navigazione



split = post['Orario di pubblicazione'].str.split(' ', expand=True)
post['Data'] = split[0]
post['Ora'] = split[1]

post = post.rename(columns={'Tipo di post': 'Formato'})

cols = [
    'Descrizione', 'Durata (s)', 'Data', 'Ora', 'Permalink',
    'Formato', 'Visualizzazioni', 'Mi piace', 'Condivisioni',
    'Commenti', 'Salvataggi', 'Copertura', 'Follower'
]
df_post = post[cols]

split = storie['Orario di pubblicazione'].str.split(' ', expand=True)
storie['Data'] = split[0]
storie['Ora'] = split[1]


cols = [
    'Descrizione', 'Durata (s)', 'Data', 'Ora', 'Permalink',
    'Tipo di post', 'Visualizzazioni', 'Copertura', 'Mi piace', 'Condivisioni',
    'Visite al profilo', 'Risposte', 'Clic sul link', 'Tocchi sugli adesivi',
    'Follower', 'Navigazione'
]
df_storie = storie[cols]

