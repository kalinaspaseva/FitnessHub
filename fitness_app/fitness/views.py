from django.shortcuts import render, get_object_or_404, redirect
from .models import Trainer, Client, TrainingSession
from .forms import TrainerForm, TrainingSessionForm, ClientForm


def index(request):
    trainers = Trainer.objects.all()
    clients = Client.objects.all()
    sessions = TrainingSession.objects.all()

    context = {
        'trainers': trainers,
        'clients': clients,
        'sessions': sessions,
    }
    return render(request, 'fitness/index.html', context)


def edit_trainer(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)

    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'fitness/edit_trainer.html', {'form': form, 'trainer': trainer})


def add_session(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TrainingSessionForm()

    return render(request, 'fitness/add_session.html', {'form': form})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()
    return render(request, 'fitness/add_client.html', {'form': form})

def trainer_detail(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    sessions = TrainingSession.objects.filter(trainer=trainer)
    return render(request, 'fitness/trainer_detail.html', {'trainer': trainer, 'sessions': sessions})

def cancel_session(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk)
    if request.method == 'POST':
        session.delete()
        return redirect('index')
    return render(request, 'fitness/cancel_session.html', {'session': session})