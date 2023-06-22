from django.shortcuts import render
from .models import Item, Restaurants

def search_items(request):
    query = request.GET.get('query', '')  # Get the search query from the request

    # Search for items matching the query
    items = Item.objects.filter(name__icontains=query)

    # Sort the items based on the aggregate rating of their restaurants in descending order
    items = items.order_by('-restaurant__aggregate_rating')

    context = {
        'query': query,
        'items': items,
    }

    return render(request, 'search.html', context)
