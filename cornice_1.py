from cornice import Service
from collections import defaultdict


user_info = Service(name='users', path='/{username}/info')

_USERS = defaultdict(dict)



@user_info.get()

def get_info(request):

    """Returns the public information about a **user**.

    If the user does not exists, returns an empty dataset.

    """

    username = request.matchdict['username']

    return _USERS[username]



@user_info.post()

def set_info(request):

    """Set the public information for a **user**.

    You have to be that user, and *authenticated*.

    Returns *True* or *False*.

    """

    username = request.matchdict["username"]

    _USERS[username] = request.json_body

    return {'success': True}