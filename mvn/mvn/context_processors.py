from quotes.models import Quote
import random

def random_quote(request):
    total = Quote.objects.count()
    if total == 0:
        quote = Quote(quote="These are not the quotes you're looking for", name="The system administrator") 
        return {'quote': quote}
    else:
        id = random.randint(1, total)
        return {'quote': Quote.objects.get(pk=id)}
