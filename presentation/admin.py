from django.contrib import admin

from .models import Competition, Club, Classement, Match, Groupe, Stade


class ClassementInline(admin.TabularInline):
    model = Classement
    extra = 3

class MatchInline(admin.TabularInline):
	"""docstring for MatchInline"""
	model = Match
	extra = 0


class CompetitionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('NOM : ',               {'fields': ['competition_name']}),
        ('Date', {'fields': ['date']}),
        ('Journee en Cour',    {'fields': ['journee_encr']}),
    ]
    
    inlines = [ClassementInline, MatchInline ]

		
		

# Register your models here.

# admin.site.register(Classement)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Club)
admin.site.register(Groupe)
admin.site.register(Match)
admin.site.register(Stade)

