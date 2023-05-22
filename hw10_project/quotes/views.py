from bson.objectid import ObjectId

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from .utils import get_mongodb

from .forms import AuthorForm, QuoteForm, TagForm
from .models import Author, Quote, Tag

def main(request, page=1):
    #db = get_mongodb()
    #quotes = db.quote.find()
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})

@login_required
def add_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
    return render(request, "quotes/addauthor.html", context={"form": form})

@login_required
def add_tag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST, instance=Tag())
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
    return render(request, "quotes/addtag.html", context={"form": form})

@login_required
def add_quote(request):
    #tags = Tag.objects.all()
    #author= Author.objects.all()
    #form = QuoteForm()
    form = QuoteForm(request.POST)
    if request.method == "POST":
        #form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            #choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            #for tag in choice_tags.iterator():
                #new_quote.tags.add(tag)
            #choice_author= Author.objects.filter(name__in=request.POST.get('author'))
            #new_quote.author.add(choice_author)
            return redirect(to="quotes:root")
        else:
            return render(request, 'quotes/addquote.html', {"form": form})

            
    return render(request, "quotes/addquote.html", context={"form": form})


def details(request, auth_id):
    #db = get_mongodb()
    #auth_about = db.author.find_one({"_id": ObjectId(auth_id)})
    auth_about = Author.objects.get(pk=auth_id)
    return render(request, 'quotes/details.html', {"auth_about": auth_about})

def quotes_with_tag(request, tag_name):
    #db = get_mongodb()
    #auth_about = db.author.find_one({"_id": ObjectId(auth_id)})
    quotes = Quote.objects.all()
    quotes_with_tag = []
    for quote in quotes:
        print(quote.tags.iterator())
        for tag in quote.tags.iterator():
            if tag.name == tag_name:
                quotes_with_tag.append(quote)
    print(quotes_with_tag)
    return render(request, 'quotes/quotes_with_tag.html', {"quotes_with_tag": quotes_with_tag})

def popular_tags(request):
    #db = get_mongodb()
    #auth_about = db.author.find_one({"_id": ObjectId(auth_id)})
    quotes = Quote.objects.all()
    tags_dict = {}
    popular_tags = []
    for quote in quotes:
        for tag in quote.tags.iterator():
            if tag.name in tags_dict:
                tags_dict[tag.name] += 1
            else:
                tags_dict[tag.name] = 1

    number_using_tags = []

    for value in tags_dict.values():
        number_using_tags.append(value)
    
    num_us_popular_tags = sorted(number_using_tags, reverse=True)

    for key, value in tags_dict.items():
        if value in num_us_popular_tags[:9]:
            popular_tags.append(key)

    return render(request, 'quotes/popular_tags.html', {"popular_tags": popular_tags})

