import numpy as np
import pandas as pd

PATH = "eg_poste_monitore_quartier_a.csv"
MAXLINES = 113

def calculConsoTotaleMois(file):
    i = 1
    date = file.loc[i, 'datedebut'][:7]
    dateCourante = date
    
    valpv = file.loc[i, 'valuepv']
    print(type(valpv))
    sumPv = pd.DataFrame([(None, None)], columns = ['Date', 'valuepv'])
    
    while i < MAXLINES:
        i += 1
        dateCourante = file.loc[i, 'datedebut'][:7]
        if date == dateCourante:
            valpv += file.loc[i, 'valuepv']
        else:
            print("else")
            sumPv = sumPv.append({'Date' : date, 'valuepv' : valpv }, ignore_index=True)
            date = dateCourante
            valpv = 0
    sumPv = sumPv.append({'Date' : date, 'valuepv' : valpv }, ignore_index=True)
    
    return sumPv.loc[1:]

if __name__ == '__main__':
	file = pd.read_csv(PATH, header=0, sep=';')
	

	# Calculs :
	dfProdMois = calculConsoTotaleMois(file)

    # Visualisation :
    ml.title("Production totale d'énergie mois par mois (paneaux photovoltaïque)")
    ml.plot(dfProdMois['Date'], 
        dfProdMois['valuepv'], 
        color = 'blue', 
        label = "Production par mois")



    #ml.plot(file['Date et Heure de la mesure'], file['Valeur'])
    #ml.plot(dfMoyJ['Date'], dfMoyJ['Valeur'], color = 'red', label = "Moyenne par jour")
    #
    #dfMoyJourDeSemaine.plot(kind='bar', title="Moyenne de la consommation d'énergie par jour de la semaine (toute période)")
    x = np.arange(len(SEMAINE))
    ml.bar(x-0.3, dfMoyJourDeSemaineTout.loc['Valeur'], width=0.3, label='Tout', color='#ff5000')
    ml.bar(x, dfMoyJourDeSemaineVac.loc['Valeur'], width=0.3, label='Vacances', color='#7eb54e')
    ml.bar(x+0.3, dfMoyJourDeSemaineSco.loc['Valeur'], width=0.3, label='Scolaire', color='#158bef')
    #ml.xlabel('Jour de la semaine')
    ml.ylabel('Production (en kW)')
    #ml.xticks(x, SEMAINE)
    ml.axis('auto')
    ml.legend()
    ml.show()

