import os
import pandas as pd
import json
from django.conf import settings
from .models import Restaurants, Item


def load_data():
    csv_file = os.path.join(settings.MEDIA_ROOT, 'restaurants_small.csv')
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        items = {}
        for item_key, item_value in json.loads(row['items']).items():
            item_name = item_key.strip()
            item_price = item_value.strip()
            items[item_name] = item_price
        
        full_details = row['full_details']
        if isinstance(full_details, float):
            full_details = str(full_details)  # Convert float to string representation

        try:
            full_details_data = json.loads(full_details)
            name = full_details_data.get("name", "").strip()
            aggregate_rating = full_details_data.get("user_rating", {}).get("aggregate_rating", "").strip()

            restaurant = Restaurants.objects.create(
                name=name,
                aggregate_rating=aggregate_rating,
            )
            print(f"Created restaurant: {restaurant.name}")
            
            for item_name, item_price in items.items():
                item = Item.objects.create(
                    name=item_name,
                    prize=str(item_price),  # Convert prize to string
                    restaurant=restaurant,
                )
                print(f"Created item: {item.name} (Price: {item.prize})")
            
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON data for restaurant: {row['name']}")
