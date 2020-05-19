"""mysiteRestelli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

#spiegazione 
# 1
#il metodo path() con argomento: route, route è una stringa che contiene un pattern URL. Django inizia dal primo modello in entrata urlpatternse si sposta in fondo all'elenco, confrontando l'URL richiesto con ogni modello fino a quando non trova quello corrispondente.
#il metodo path() con argomento: view, quando Django trova un modello corrispondente, chiama la funz con un HttpRequestoggetto come argomento primario e tutti i valori presi dalla rotta come argomenti di parole chiave.
#il metodo path() con argomento: kwargs, gli argomenti delle parole chiave possono essere passati in un dizionario alla vista di destinazione.
#il metodo path() con argomento: name, tramite un'assegnazione di un nome al URL consente di far riferimento in modo inequivocabile da qualsiasi altra parte di Django.

# 2
#con makemigrations, si dice a django che si ha apportato in alcune modifiche ai modelli e che le modifiche vengano salvate.
#sqlmigrate accetta i nomi di migrazione e restituisce il loro sql.

# 3
#il probelma di questo approccio è che diventa difficile cambiare gli url sui progetti con molti template.
#Lo scopo dei namespace è quello di evitare confusione ed equivoci nel caso siano necessarie molte entità con nomi simili, fornendo il modo di raggruppare i nomi per categorie.

# 4
#request.POST è un  un oggetto simile a un dizionario che consente di accedere ai dati inviati in base al nome della chiave.
#la funzione reverse() evita di dover codificare un URL nella funzione di visualizzazione.