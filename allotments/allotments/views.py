from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from allotments.forms import CommentForm, MessageForm
from allotments.models import Comment, Message, Plot
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'


class MessageCreateView(CreateView):
    model = Message
    fields = ['message']
    success_url = reverse_lazy("messages")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CommentCreateView(CreateView):
    model = Comment
    success_url = reverse_lazy("messages")
    fields = ["comment", "message"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class MessageListView(ListView):
    model = Message
    template_name = 'messages.html' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_form'] = MessageForm()
        context["comment_form"] = CommentForm()
        return context



class PlotsView(TemplateView):
    template_name = "plots.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["plots"] = Plot.objects.prefetch_related("users").all().order_by("plot_number")
        return context
