# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Attachment(models.Model):
    type = models.TextField()
    id = models.TextField(primary_key=True)
    filename = models.TextField()
    size = models.IntegerField()
    time = models.IntegerField()
    description = models.TextField()
    author = models.TextField()
    ipnr = models.TextField()
    class Meta:
        db_table = u'attachment'

class AuthCookie(models.Model):
    cookie = models.TextField(primary_key=True)
    name = models.TextField()
    ipnr = models.TextField()
    time = models.IntegerField()
    class Meta:
        db_table = u'auth_cookie'

class Component(models.Model):
    name = models.TextField(primary_key=True)
    owner = models.TextField()
    description = models.TextField()
    class Meta:
        db_table = u'component'

class Enum(models.Model):
    type = models.TextField(primary_key=True)
    name = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'enum'

class Milestone(models.Model):
    name = models.TextField(primary_key=True)
    due = models.IntegerField()
    completed = models.IntegerField()
    description = models.TextField()
    class Meta:
        db_table = u'milestone'

class NodeChange(models.Model):
    rev = models.TextField()
    path = models.TextField()
    node_type = models.TextField()
    change_type = models.TextField()
    base_path = models.TextField()
    base_rev = models.TextField()
    class Meta:
        db_table = u'node_change'

class Permission(models.Model):
    username = models.TextField()
    action = models.TextField()
    class Meta:
        db_table = u'permission'

class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.TextField()
    title = models.TextField()
    query = models.TextField()
    description = models.TextField()
    class Meta:
        db_table = u'report'

class Revision(models.Model):
    rev = models.TextField(primary_key=True)
    time = models.IntegerField()
    author = models.TextField()
    message = models.TextField()
    class Meta:
        db_table = u'revision'

class Session(models.Model):
    sid = models.TextField(primary_key=True)
    authenticated = models.IntegerField()
    last_visit = models.IntegerField()
    class Meta:
        db_table = u'session'

class SessionAttribute(models.Model):
    sid = models.TextField(primary_key=True)
    authenticated = models.IntegerField()
    name = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'session_attribute'

class SpamfilterBayes(models.Model):
    word = models.TextField(primary_key=True)
    nspam = models.IntegerField()
    nham = models.IntegerField()
    class Meta:
        db_table = u'spamfilter_bayes'

class SpamfilterLog(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.IntegerField()
    path = models.TextField()
    author = models.TextField()
    authenticated = models.IntegerField()
    ipnr = models.TextField()
    headers = models.TextField()
    content = models.TextField()
    rejected = models.IntegerField()
    karma = models.IntegerField()
    reasons = models.TextField()
    class Meta:
        db_table = u'spamfilter_log'

class System(models.Model):
    name = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'system'

class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.TextField()
    time = models.IntegerField()
    changetime = models.IntegerField()
    component = models.TextField()
    severity = models.TextField()
    priority = models.TextField()
    owner = models.TextField()
    reporter = models.TextField()
    cc = models.TextField()
    version = models.TextField()
    milestone = models.TextField()
    status = models.TextField()
    resolution = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    class Meta:
        db_table = u'ticket'

class TicketChange(models.Model):
    ticket = models.IntegerField()
    time = models.IntegerField()
    author = models.TextField()
    field = models.TextField()
    oldvalue = models.TextField()
    newvalue = models.TextField()
    class Meta:
        db_table = u'ticket_change'

class TicketCustom(models.Model):
    ticket = models.IntegerField()
    name = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'ticket_custom'

class Version(models.Model):
    name = models.TextField(primary_key=True)
    time = models.IntegerField()
    description = models.TextField()
    class Meta:
        db_table = u'version'

class Wiki(models.Model):
    name = models.TextField()
    version = models.IntegerField()
    time = models.IntegerField()
    author = models.TextField()
    ipnr = models.TextField()
    text = models.TextField()
    comment = models.TextField()
    readonly = models.IntegerField()
    class Meta:
        db_table = u'wiki'

