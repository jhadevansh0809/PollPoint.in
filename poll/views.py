from django.shortcuts import render,redirect
from .models import Poll
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView


class PollListView(ListView):
    model=Poll
    template_name='poll/home.html'
    ordering=["-id"]


class PollCreateView(CreateView):
    model=Poll
    fields=['question','option_1','option_2','option_3']
    template_name='poll/create.html'

def Vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    print(poll)
    if request.method == 'POST':
        selected_option = request.POST['op']
        if selected_option == 'option1':
            poll.option_1_count += 1
        elif selected_option == 'option2':
            poll.option_2_count += 1
        elif selected_option == 'option3':
            poll.option_3_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('home')

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

class PollResultDetailView(DetailView):
    model=Poll
    template_name='poll/result.html'