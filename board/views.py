# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import NewTopicForm
from .models import Board, Topic, Post

# Create your views here.

def home(request):
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards' : boards})


def topic(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board':board}) 

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = User
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=User
            )
            return redirect('new_topic', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
        
    return render(request, 'new_topic.html', {'board':board, 'form': form})

    