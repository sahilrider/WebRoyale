from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404

from .models import Typ,Crd,Arena,Rarity
'''from .forms import CommentForm'''
def index(request):
	cards=Crd.objects.all()
	return render(request,'card/index.html',{'cards':cards})

def arena_index(request):
	arenas=Arena.objects.all()
	return render(request,'card/arenas.html',{'arenas':arenas})

def view_arena(request,arena_number):
	arena=get_object_or_404(Arena, pk=arena_number)
	card=Crd.objects.filter(arena=arena.number)
	return render(request,'card/view_arena.html',{'arena':arena,'cards':card})

def view_rarity(request,rarity_id):
	rarity=get_object_or_404(Rarity, pk=rarity_id)
	card=Crd.objects.filter(rarity=rarity_id)
	return render(request,'card/view_rarity.html',{'rarity':rarity,'cards':card})

def view_type(request,type_id):
	typ=get_object_or_404(Typ, pk=type_id)
	card=Crd.objects.filter(typ=type_id)
	return render(request,'card/view_type.html',{'type':typ,'cards':card})

def view_card(request,card_id):
	card=get_object_or_404(Crd,pk=card_id)
	return render(request,'card/view_card.html',{'card':card})