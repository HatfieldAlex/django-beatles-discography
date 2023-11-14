from django.shortcuts import render


albums = {
    "1": {
        "name": "Please Please Me",
        "slug": "please-please-me",
        "release_year": "1963",
        "label": "Parlophone",
        "fun_fact": "The majority of this album was recorded in just one 10-hour session on February 11, 1963. This was quite unusual for an album at the time."
    },
    "2": {
        "name": "Help!",
        "slug": "help",
        "release_year": "1965",
        "label": "Parlophone",
        "fun_fact": "The track \"You\’ve Got to Hide Your Love Away\" signals the band's foray into folk rock, influenced by Bob Dylan."
    },
    "3": {
        "name": "Let It Be",
        "slug": "let-it-be",
        "release_year": "1970",
        "label": "Apple",
        "fun_fact": "Although recorded before \"Abbey Road,\" \"Let It Be\" was the last album released by The Beatles."
    }
}


# Create your views here.

def home(request):
    context = {'albums': albums}
    return render(request, 'beatles_site/index.html', context)

def album_detail(request, album_name_slug):
    for item in albums:
        album = albums[item]
        if album['slug'] == album_name_slug:
            return render(request, "beatles_site/album_detail.html", album)


def please_please_me(request):
    return render(request, 'beatles_site/albums/please_please_me.html')

def help(request):
    return render(request, 'beatles_site/albums/help.html')

def let_it_be(request):
    return render(request, 'beatles_site/albums/let_it_be.html')