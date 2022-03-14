from scrumboard.models import Card
import accounts.services.account_service

def get_all_cards():
    return Card.objects.all()

def get_cards_list():
    ## example of a call to a service outside the current app
    print(accounts.services.account_service.get_users())
    return Card.manager.get_list_with_related()
    
def find_card_by_id(id):
    return Card.manager.find_by_id_with_related(id)

def create_card(validated_data):
    card = Card(**validated_data)
    card.save()
    return card