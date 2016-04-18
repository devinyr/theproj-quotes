from django.contrib.auth import login, authenticate, forms, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from apps.accounts.models import User
from apps.quotes.models import Quote, Favorite
from apps.quotes.forms import QuoteForm


class Dashboard(View):
    def get(self, request):    
        f = Favorite.objects.filter(usr_id=request.user)
        o = Quote.objects.exclude(favorite__usr_id=request.user)    
    	q = Quote.objects.all()
        dictionary = {
            "fav" : f,
            "otherlist" : o,
        }
        return render(request, "quotes/quotes.html", dictionary)

class QuoteView(View):
    form_class = QuoteForm
    initial = {'key': 'value'}
    template_name = 'quotes/quote_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=True)
            print "Quote"
            print data
            print request.user
            return redirect ('/quotes/')
        return render(request, self.template_name, {'form': form})

class UserPosts(View):
    def get(self,request,id):
        pst = Quote.objects.filter(posted_id=id)
        context = {
            "count" : pst.count(),
            "posts" : pst,
        }
        return render(request, "quotes/posts.html", context)

def add(request, id):
        print id
        new_q = Quote.objects.get(id=id)
        new_f = Favorite.objects.create(usr_id=request.user,quote_id=new_q)
        new_f.save()

        f = Favorite.objects.filter(usr_id=request.user)
        o = Quote.objects.exclude(favorite__usr_id=request.user)    
        q = Quote.objects.all()
        dictionary = {
            "fav" : f,
            "otherlist" : o,
        }
        return render(request, "quotes/quotes.html", dictionary)

def remove(request, id):
        print id
        rm_f = Favorite.objects.get(id=id)
        rm_f.delete()
        f = Favorite.objects.filter(usr_id=request.user)
        o = Quote.objects.exclude(favorite__usr_id=request.user)    
        q = Quote.objects.all()
        dictionary = {
            "fav" : f,
            "otherlist" : o,
        }
        return render(request, "quotes/quotes.html", dictionary)

