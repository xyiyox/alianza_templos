from django.test import TestCase
from django.urls import reverse
from usuarios.models import Usuario

# Create your tests here.
class SimpleTest(TestCase):
	
	def setUp(self):
		self.usuario = Usuario.objects.create_user(email='prueba', nombre='Prueba', 
			apellidos='Prueba', password='prueba')

	def test_views(self):

		# Prueba para la vista del home en caso de estar logueado
		self.client.login(email='prueba', password='prueba')
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code, 200)
		# Prueba para la vista del home en caso de no estar logueado
		self.client.logout()
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code, 302)
		