from django.shortcuts import render
from MiApp.models import Familia

def mostrar_familia (request):

  familiar1 = Familia (nombre= 'Monica', apellido='Haili', edad='60', nacimiento='1962-03-26', parentesco='Madre')
  familiar2 = Familia (nombre= 'Nestor', apellido='Aguirre',edad='62', nacimiento='1960-03-23', parentesco='Padre')
  familiar3 = Familia (nombre= 'Mailen', apellido='Haili', edad='25', nacimiento='1997-10-18', parentesco='Hermana')
  familiar4 = Familia (nombre= 'Agustin', apellido='Haili', edad='25', nacimiento='1997-10-18', parentesco='Hermano')

  return render(request, 'MiApp/index.html', {'objetos':[familiar1, familiar2, familiar3, familiar4]})