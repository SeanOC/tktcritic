class TracRouter(object):
    '''
    A router to direct all queries related to trac data to the trac database.
    '''
    
    def db_for_read(self, model, **hints):
        return self._simple_select_database(model)
            
    def db_for_write(self, model, **hints):
        return self._simple_select_database(model)
    
    def allow_relaton(self, obj1, obj2, **hints):
        allow_relation = None
        obj1_app = obj1._meta.app_label
        obj2_app = obj1._meta.app_label
        
        if obj1_app == 'trac' and obj2_app != 'trac':
            allow_relation = False
        elif obj1_app != 'trac' and obj2_app == 'trac':
            allow_relation = False
        elif obj1_app == 'trac' and obj2_app == 'trac':
            allow_relation = True
            
        return allow_relation
    
    def allow_syncdb(self, db, model):
        allow_syncdb = None
        
        if db == 'trac' or model._meta.app_label == 'trac':
            allow_syncdb = False
            
        return allow_syncdb
    
    def _simple_select_database(self, model):
        database = None
        
        if model._meta.app_label == 'trac':
            database = 'trac'

        return database