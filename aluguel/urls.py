"""vcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import index, lista_car, realizar_aluguel, detalhar_car, realizar_aluguel_car,cadastrar_cliente,cadastrar_car

urlpatterns = [
    path('', index, name='index'),
    path('car/', lista_car, name='listar_car'),
    path('car/<int:pk>', detalhar_car, name='detalhar_car'),
    path('car/aluguel/<int:car_pk>', realizar_aluguel_car, name='realizar_aluguel_car' ),
    path('car/add',cadastrar_car, name='cadastrar_carro'),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
    path('clientes/add',cadastrar_cliente, name='cadastrar_cliente')
    
]
