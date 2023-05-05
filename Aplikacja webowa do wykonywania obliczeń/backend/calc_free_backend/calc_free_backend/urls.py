"""calc_free_backend URL Configuration

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
from calc_free_backend import views

urlpatterns = [
    path('', views.return_page),
    path('linear-equation/',views.solve_linear_equation),
    path('square-equation/', views.solve_square_equation),
    path('arithmetic-average/', views.arithmetic_average),
    path('weighted-average/', views.weighted_average),
    path('points-distance/', views.distance_between_points),
    path('bubble-sort/', views.bubble_sort),
    path('quick-sort/', views.quick_sort),
    path('triangle/', views.calculate_triangle_properties),
    path('<path:resource>', views.return_page2)
]
