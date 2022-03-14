from scrumboard.models import List

def get_all_lists():
    return List.objects.all().order_by('id')

def get_lists():
    return List.manager.get_list_with_related()

def find_list_by_id(id):
    return List.manager.find_by_id_with_related(id)