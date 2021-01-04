from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView

from fortyk_ffg_companion.black_crusade.models import Weapon


class BCIndexPage(LoginRequiredMixin, TemplateView):
    template_name = 'bc/index.html'


index_page = BCIndexPage.as_view()


class BCWeaponDetail(LoginRequiredMixin, DetailView):

    model = Weapon
    slug_field = "weapon"
    slug_url_kwarg = "weapon"


bc_weapon_detail = BCWeaponDetail.as_view()


class BCWeaponUpdate(LoginRequiredMixin, UpdateView):

    model = Weapon

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, "Weapon successfully updated"
        )
        return super().form_valid(form)


bc_weapon_update = BCWeaponUpdate.as_view()
