from django.db import models

# Create your models here.


class Competition(models.Model):
	"""docstring for championat"""

	days = (
			('PR', '1er'),
			('SD', '2sd'),
			('TR', '3eme'),
			('QT', '4eme'),
		 )

	competition_name = models.CharField(max_length = 20)
	date = models.DateField('date')
	journee_encr = models.CharField(max_length = 2, choices = days)
	# nbr_equipes = models.IntegerField(default=0)
	# jr_joue =  models.IntegerField(default=0)


	def __str__(self):
		return self.competition_name + "-" + str(self.date)




class Stade(models.Model):
	nom_stade = models.CharField(max_length = 20)
	nombre_palce = models.IntegerField(default = 0)

	def __str__(self):
		return self.nom_stade

class Club(models.Model):


	SHIRT_SIZES = (
					('F', 'France'),
					('A', 'Allemagne'),
					('AG', 'Angleterre'),
					('E', 'Espagne'),
				  )
	"""docstring for club"""
	# championat = models.ForeignKey(Championat, on_delete=models.CASCADE)
	club_name = models.CharField(max_length = 30)
	abreviation_name = models.CharField(max_length = 6)
	pays_origine = models.CharField(max_length = 2, choices = SHIRT_SIZES)
	stade =  models.ForeignKey(Stade, on_delete=models.CASCADE)
	


	def __str__(self):
		return self.club_name


class Groupe(models.Model):
	"""docstring for Groupe"""
	nom_groupe = models.CharField(max_length = 1)
	equipe = models.ManyToManyField(Club, through='Classement')

	def __str__(self):
		return self.nom_groupe

class Classement(models.Model):
	"""docstring for classement"""
	# competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	# club = models.ForeignKey(Club, on_delete=models.CASCADE)
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	nbr_point = models.IntegerField(default=0)
	match_joue = models.IntegerField(default=0)
	# groupe =  models.CharField(max_length = 1, null = True)
	db = models.IntegerField(default=0)	
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)


class Match(models.Model):

	STATE = (
					('EN', 'EN ATTENDE'),
					('EC', 'EN_COUR'),
					('FT', 'FULL_TIME'),
					('RPT', 'REPORTER'),
				  )

	days = (
					('PR', '1er'),
					('SD', '2sd'),
					('TR', '3eme'),
					('QT', '4eme'),
				  )
	equipe_int = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='equipe_int')
	equipe_ext = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='equipe_ext')
	score_int = models.IntegerField(default = 0)
	score_ext = models.IntegerField(default = 0)
	date_match = models.DateField()
	stade =  models.ForeignKey(Stade, on_delete=models.CASCADE)
	competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
	journee = models.CharField(max_length = 2, choices = days)
	statu = models.CharField(max_length = 2, choices = STATE, default = 'EN ATTENDE')
	

	def __str__(self):
		return str(self.equipe_int) + " Vs "+ str(self.equipe_ext)



		

	
		