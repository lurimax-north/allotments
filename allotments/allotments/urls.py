from django.urls import path

from allotments.views import CommentCreateView, HomeView, MessageCreateView, MessageListView, PlotsView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path("plots", PlotsView.as_view(), name='plots'),
    path("news", HomeView.as_view(), name='news'),
]