import pandas as pd

storie = pd.read_csv('Storie.csv')
post = pd.read_csv('Post.csv')

storie["Orario di pubblicazione"] = pd.to_datetime(storie["Orario di pubblicazione"])
post["Orario di pubblicazione"] = pd.to_datetime(post["Orario di pubblicazione"])

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


