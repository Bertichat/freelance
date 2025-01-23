from django.shortcuts import render
from django.views.generic import TemplateView
from freelance.settings import BASE_DIR


class MainPageView(TemplateView):
    template_name = "main_page.html"

main_page = MainPageView.as_view()
