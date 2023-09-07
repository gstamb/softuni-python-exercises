from django.shortcuts import redirect, render
from music_app.albums.forms import AlbumDeleteForm, AlbumForm
from music_app.albums.models import Album
from django.contrib.auth.decorators import login_required

@login_required
def add_album(request):
    form = AlbumForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            album = form.save()
            album.users.add(request.user)
            album.save()
            return redirect('user home')
        else:
            album_name = form.cleaned_data['album_name']
            artist = form.cleaned_data['artist']
            if album_name and artist:
                existing_album = Album.objects.filter(
                    album_name=album_name, artist=artist).first()
                if existing_album:
                    existing_album.users.add(request.user)
                    return redirect('user home')
    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    owned_by_user = album.users.filter(pk=request.user.pk).exists()
    context = {
        'album': album,
        'has_permission' : owned_by_user
    }
    return render(request, 'album-details.html', context)


@login_required
def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.users.remove(request.user)
        return redirect('user home')

    form = AlbumDeleteForm(instance=album)
    context = {
        'album': album,
        'form': form
    }
    return render(request, 'delete-album.html', context)

@login_required
def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('user home')

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'edit-album.html', context)


def show_albums(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'browse-albums.html', context)
