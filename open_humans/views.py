from account.views import (SignupView as AccountSignupView,
                           SettingsView as AccountSettingsView)

from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from activities.twenty_three_and_me.models import ActivityDataFile as \
    ActivityDataFile23andme

from .forms import (MyMemberChangeEmailForm,
                    MyMemberContactSettingsEditForm,
                    MyMemberProfileEditForm,
                    SignupForm)
from .models import Member
from .serializers import MemberSerializer
from .viewsets import SimpleCurrentUserViewset


class MemberDetailView(DetailView):
    """
    Creates a view of a member's public profile.
    """
    model = Member
    template_name = 'member/member-detail.html'
    slug_field = 'user__username'

    def get_context_data(self, **kwargs):
        """Add context so login and signup return to this page."""
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        context.update({
            'redirect_field_name': 'next',
            'redirect_field_value': reverse_lazy(
                'member-detail',
                kwargs={'slug': self.object.user.username}),
        })
        return context


class MemberListView(ListView):
    """
    Creates a view listing members.
    """
    model = Member
    template_name = 'member/member-list.html'


class MyMemberDashboardView(DetailView):
    """
    Creates a dashboard for the current user/member.

    The dashboard also displays their public member profile.
    """
    context_object_name = 'member'
    model = Member
    template_name = 'member/my-member-dashboard.html'

    def get_object(self, queryset=None):
        return self.request.user.member


class MyMemberProfileEditView(UpdateView):
    """
    Creates an edit view of the current user's public member profile.
    """
    form_class = MyMemberProfileEditForm
    model = Member
    template_name = 'member/my-member-profile-edit.html'
    success_url = reverse_lazy('my-member-dashboard')

    def get_object(self, queryset=None):
        return self.request.user.member


class MyMemberSettingsEditView(UpdateView):
    """
    Creates an edit view of the current user's member account settings.
    """
    form_class = MyMemberContactSettingsEditForm
    model = Member
    template_name = 'member/my-member-settings.html'
    success_url = reverse_lazy('my-member-settings')

    def get_object(self, queryset=None):
        return self.request.user.member


class MyMemberChangeEmailView(AccountSettingsView):
    """
    Creates a view for the current user to change their email.

    This is an email-only subclass of account's SettingsView.
    """
    form_class = MyMemberChangeEmailForm
    template_name = 'member/my-member-change-email.html'
    success_url = reverse_lazy('my-member-settings')
    messages = {
        "settings_updated":
        {"level": messages.SUCCESS,
         "text": "Email address updated and confirmation email sent."
         },
        }

    def get_success_url(self, *args, **kwargs):
        kwargs.update(
            {'fallback_url': reverse_lazy('my-member-settings')})
        return super(MyMemberChangeEmailView, self).get_success_url(
            *args, **kwargs)


# TODO: Make more generic.
class MyMemberDatasetsView(ListView):
    """
    Creates a view for displaying and importing research/activity datasets.
    """
    model = ActivityDataFile23andme
    template_name = "member/my-member-research-data.html"
    context_object_name = 'data_sets'

    def get_queryset(self):
        return ActivityDataFile23andme.objects.filter(
            study_user__user=self.request.user)


class ExceptionView(View):
    """
    Raises an exception for testing purposes.
    """
    def get(self, request):
        raise Exception('A test exception.')


class SignupView(AccountSignupView):
    """
    Creates a view for signing up for an account.

    This is a subclass of accounts' SignupView using our form customizations,
    including addition of a TOU confirmation checkbox.
    """
    form_class = SignupForm

    def generate_username(self, form):
        """Override as StandardError instead of NotImplementedError."""
        raise StandardError(
            "Username must be supplied by form data."
        )


class MemberViewSet(SimpleCurrentUserViewset):
    queryset = User.objects.all()
    serializer_class = MemberSerializer
