import urllib

from allauth.account.models import EmailAddress
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm
from braces.views import LoginRequiredMixin, UserPassesTestMixin


class IndexView(ListView):
    print('호롤롤로')
    model = Review
    template_name = 'coplate/index.html'

    context_object_name = 'reviews'

    paginate_by = 4
    ordering = ['-dt_created']
    print("테스트용으로 김은수 유저가 추가한 아무쓸모없는 코드한줄")
    print("테스트용으로 김은수 유저가 추가한 아무쓸모없는 코드한줄222")

    print('hi~^D^')
    print("hihihihihihihihisoeun")
    ordering = ['dt_created']




class ReviewDetailView(DetailView):
    model = Review
    template_name = 'coplate/review_detail.html'
    pk_url_kwarg = 'review_id'


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("review-detail", kwargs={'review_id': self.object.id})

    def test_func(self, user):
        if EmailAddress.objects.filter(user=user, verified=True).exists():
            pass


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = "review_id"

    def get_success_url(self):
        return reverse("review-detail", kwargs={'review_id': self.object.id})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'coplate/review_confirm_delete.html'
    pk_url_kwarg = 'review_id'

    def get_success_url(self):
        return reverse("index")


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")


"excuse me"
