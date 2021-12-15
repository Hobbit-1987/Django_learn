from django.shortcuts import render

def posts_list(request):
    f = ['bonBon', 'cat', 'parrot', 'bird']
    return render(request, 'blog/index.html', context={'names': f})
