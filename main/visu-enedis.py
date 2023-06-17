import pandas as pd
import numpy as np
import matplotlib.pyplot as ml
PATH = "Enedis_M021_CDC_E427P41Q_16111287961486.csv"
MAX_DATE = 4464
MAX_DATE_VAC = 3024
D_H_DEPART_SEM = 1681 	# Commence le 6/12/21 (début de semaine à minuit)
#D_H_DEPART_J = 1505 	# Commence dès la première mesure connue
D_H_DEPART_SCO = 3025
D_H_DEPART_VAC = 2353
SEMAINES_VACANCES_SCO = [	"20/12/21", "27/12/21", "14/02/22", "21/02/22", 
							"18/04/22", "25/04/22"]
SEMAINE = ['Lu', 'Ma', 'Me', 'Je', 'Ve', 'Sa', 'Di']

def color(date):
	l = []

	for d in date:
		if d in SEMAINES_VACANCES_SCO:
			l.append('#7eb54e')
		else:
			l.append('#158bef')
	return l

# Calcul de la moyenne de la consommation par semaine
def calculMoyenne(date_depart, date_arrivee, echelle_temps):
	i = date_depart

	moy = file.loc[i:i+echelle_temps, ['Valeur']].mean()
	date = file.loc[i, ['Date et Heure de la mesure']]
	date = date['Date et Heure de la mesure']
	moy = [(date[:8], moy['Valeur'])]
	dfMoy = pd.DataFrame(moy, columns = ['Date', 'Valeur'])

	i+=echelle_temps

	while i < date_arrivee:
		moy = file.loc[i:i+echelle_temps, ['Valeur']].mean()
		date = file.loc[i, ['Date et Heure de la mesure']]
		date = date['Date et Heure de la mesure']
		dfMoy = dfMoy.append({'Date' : date[:8], 'Valeur' : moy['Valeur']}, ignore_index=True)
		i += echelle_temps
	print(dfMoy)
	return dfMoy

def calculMoyJourDeLaSemaine(df, date_depart, arrivee):
	j = 0
	moy = 0
	div = 0
	dfJ = pd.DataFrame([[0,0,0,0,0,0,0]], columns=SEMAINE, index=['Valeur'])
	#print(df.loc[0, ['Valeur']]['Valeur'])
	#print(dfJ)
	for i in range(7):
		while j+i < arrivee:
			moy += df.loc[j+i, ['Valeur']]['Valeur']
			j+=7
			div+=1
		dfJ.iloc[0, i] = moy/div
		j=0
		moy=0
		div=0
	return dfJ

#Ouverture du fichier
file = pd.read_csv(PATH, header=0)
#loc pour ligne / at pour colonne / i pour l'index de <loc/at>

#dfMoySem = calculMoyenne(D_H_DEPART_SEM, MAX_DATE, 48*7)
dfMoyJ = calculMoyenne(D_H_DEPART_SEM, MAX_DATE, 48)
dfMoyJVac = calculMoyenne(D_H_DEPART_VAC, MAX_DATE_VAC, 48)
dfMoyJSco = calculMoyenne(D_H_DEPART_SCO, MAX_DATE, 48)
dfMoyJourDeSemaineTout = calculMoyJourDeLaSemaine(dfMoyJ, D_H_DEPART_SEM, 57)
dfMoyJourDeSemaineVac = calculMoyJourDeLaSemaine(dfMoyJVac, D_H_DEPART_SEM, 14)
dfMoyJourDeSemaineSco = calculMoyJourDeLaSemaine(dfMoyJSco, D_H_DEPART_SCO, 30)

#Visualisation
ml.title("Moyenne de la consommation d'énergie par jour de la semaine")
#ml.plot(file['Date et Heure de la mesure'], file['Valeur'])
#ml.plot(dfMoyJ['Date'], dfMoyJ['Valeur'], color = 'red', label = "Moyenne par jour")
#ml.plot(dfMoySem['Date'], dfMoySem['Valeur'], color = 'blue', label = "Moyenne par semaine")
#dfMoyJourDeSemaine.plot(kind='bar', title="Moyenne de la consommation d'énergie par jour de la semaine (toute période)")
x = np.arange(len(SEMAINE))
ml.bar(x-0.3, dfMoyJourDeSemaineTout.loc['Valeur'], width=0.3, label='Tout', color='#ff5000')
ml.bar(x, dfMoyJourDeSemaineVac.loc['Valeur'], width=0.3, label='Vacances', color='#7eb54e')
ml.bar(x+0.3, dfMoyJourDeSemaineSco.loc['Valeur'], width=0.3, label='Scolaire', color='#158bef')
#ml.xlabel('Jour de la semaine')
ml.ylabel('Consommation moyenne (en W)')
ml.xticks(x, SEMAINE)
ml.axis('auto')
ml.legend()
ml.show()