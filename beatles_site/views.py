from django.shortcuts import render
from .models import Album, Track
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'beatles_site/index.html', context)

def album_detail(request, album_name_slug):
    album = get_object_or_404(Album, slug=album_name_slug)
    return render(request, "beatles_site/album_detail.html", {'album': album})

def album_tracks(request, album_name_slug):
    album = get_object_or_404(Album, slug=album_name_slug)
    tracks = Track.objects.filter(album=album)
    return render(request, "beatles_site/tracks.html", {'tracks': tracks, "album": album})


# def album_detail(request, album_name_slug):
#     for item in albums:
#         album = albums[item]
#         if album['slug'] == album_name_slug:
#             return render(request, "beatles_site/album_detail.html", album)



# albums = {
#     "1": {
#         "name": "Please Please Me",
#         "slug": "please-please-me",
#         "release_year": "1963",
#         "label": "Parlophone",
#         "fun_fact": "The majority of this album was recorded in just one 10-hour session on February 11, 1963."
#     },
#     "2": {
#         "name": "With The Beatles",
#         "slug": "with-the-beatles",
#         "release_year": "1963",
#         "label": "Parlophone",
#         "fun_fact": "This was the last Beatles album to feature a cover version until 1970."
#     },
#     "3": {
#         "name": "A Hard Day's Night",
#         "slug": "a-hard-days-night",
#         "release_year": "1964",
#         "label": "Parlophone",
#         "fun_fact": "It was the soundtrack to their first film, which was very successful."
#     },
#     "4": {
#         "name": "Beatles for Sale",
#         "slug": "beatles-for-sale",
#         "release_year": "1964",
#         "label": "Parlophone",
#         "fun_fact": "The album marked a departure from the upbeat tone that had characterized the Beatles' previous work."
#     },
#     "5": {
#         "name": "Help!",
#         "slug": "help",
#         "release_year": "1965",
#         "label": "Parlophone",
#         "fun_fact": "The track \"You’ve Got to Hide Your Love Away\" indicates the influence of Bob Dylan."
#     },
#     "6": {
#         "name": "Rubber Soul",
#         "slug": "rubber-soul",
#         "release_year": "1965",
#         "label": "Parlophone",
#         "fun_fact": "This album is considered a significant point in the band's evolution from pop to rock."
#     },
#     "7": {
#         "name": "Revolver",
#         "slug": "revolver",
#         "release_year": "1966",
#         "label": "Parlophone",
#         "fun_fact": "The album featured a wide range of styles, which was then unprecedented."
#     },
#     "8": {
#         "name": "Sgt. Pepper's Lonely Hearts Club Band",
#         "slug": "sgt-peppers-lonely-hearts-club-band",
#         "release_year": "1967",
#         "label": "Parlophone",
#         "fun_fact": "It's the first rock LP to include complete lyrics printed on the album cover."
#     },
#     "9": {
#         "name": "Magical Mystery Tour",
#         "slug": "magical-mystery-tour",
#         "release_year": "1967",
#         "label": "Parlophone",
#         "fun_fact": "Originally released as a double EP in the UK, it was expanded to a full album in the US."
#     },
#     "10": {
#         "name": "The Beatles (White Album)",
#         "slug": "the-beatles",
#         "release_year": "1968",
#         "label": "Apple",
#         "fun_fact": "This was The Beatles' only double album and is often considered one of their best."
#     },
#     "11": {
#         "name": "Yellow Submarine",
#         "slug": "yellow-submarine",
#         "release_year": "1969",
#         "label": "Apple",
#         "fun_fact": "The album served as a soundtrack for the animated film of the same name."
#     },
#     "12": {
#         "name": "Abbey Road",
#         "slug": "abbey-road",
#         "release_year": "1969",
#         "label": "Apple",
#         "fun_fact": "The cover photo has become one of the most famous and imitated images in the history of recorded music."
#     },
#     "13": {
#         "name": "Let It Be",
#         "slug": "let-it-be",
#         "release_year": "1970",
#         "label": "Apple",
#         "fun_fact": "Although recorded before \"Abbey Road,\" it was the last album released by The Beatles."
#     }
# }
