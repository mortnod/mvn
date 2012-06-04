from quotes.models import Quote
import random

def random_quote(request):
	total = Quote.objects.count()
	id = random.randint(1, total)
	return {'quote': Quote.objects.get(pk=id)}