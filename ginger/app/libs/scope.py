class AdminScope:
    allow_api = ['super_get_user']

class UserScope:
    allow_api = []

def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False