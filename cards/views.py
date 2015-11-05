from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework import viewsets
from cards.models import Poll, Card, Author, Source
from cards.serializers import CardSerializer, AuthorSerializer, SourceSerializer


def index(request):
	template_name = 'cards/index.html'
	context_object_name = 'card_list'

	latest_cards_list = Card.objects.all().order_by('-last_modified')[:12]
	sources_list = Source.objects.all() # TODO: Pagination
	authors_list = Author.objects.all() # TODO: Pagination
	context = {
		'latest_cards_list': latest_cards_list,
		'sources_list': sources_list,
		'authors_list': authors_list
	}
	return render(request, 'cards/index.html', context)

class CreateView(generic.ListView):
	template_name = 'cards/create.html'
	context_object_name = 'sources_list'

	def get_queryset(self):
		# TODO: Pagination
		return Source.objects.order_by('title')

""" Rest Stuff """
class CardViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows cards to be viewed or edited
	"""
	queryset = Card.objects.all()
	serializer_class = CardSerializer

class AuthorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows authors to be viewed or edited
	"""
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

class SourceViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows sources to be viewed or edited
	"""
	queryset = Source.objects.all()
	serializer_class = SourceSerializer

""" Methods """
def create(request):
	return HttpResponseRedirect(reverse('cards:index'))

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render(request, 'cards/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('cards:results', args=(p.id,)))