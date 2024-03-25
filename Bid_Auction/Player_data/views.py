from django.shortcuts import render,HttpResponse,redirect
from Player_data.models import Player
# Create your views here.
def index(request):
    plyer= Player.objects.all()
    context={
        'player' : plyer
    }
    return render(request,'index.html',context)

def Add(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        Bat_style = request.POST.get('Bat_style')
        Bowl_style = request.POST.get('Bowl_style')
        image=request.POST.get('image')

        player = Player(
            name=name,
            role=role,
            Batting_style=Bat_style,
            Bowling_style=Bowl_style,
            image=image,
        )

        player.save()
        return redirect('home')

    return render(request,'index.html'),  


