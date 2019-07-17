from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Utilies
from datetime import datetime
from posts.models import User


posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
users = [
    {
        'email': 'alejandro@kleverness.com',
        'first_name': 'Alejandro',
        'last_name': 'Bec',
        'password': '123456789',
        'is_admin': True
    },
    {
        'email': 'oscar@kleverness.com',
        'first_name': 'Oscar',
        'last_name': 'Valois',
        'password': '123456789',
        'is_admin': False
    },
    {
        'email': 'hector@kleverness.com',
        'first_name': 'Hector',
        'last_name': 'Mur',
        'password': '123456789',
        'is_admin': False
    }
]


def list_posts(request):
    """List existing posts."""
    for user in users:
        objt  = User(**user)
        objt.save()
        print(objt.email)
    return render(request, 'feed.html', {'posts': posts})
