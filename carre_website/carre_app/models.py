# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorie(models.Model):
    id_categorie = models.AutoField(db_column='id_Categorie', primary_key=True)  # Field name made lowercase.
    name_categorie = models.CharField(db_column='name_Categorie', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'

    def __str__(self):
        return self.name_categorie


class Collection(models.Model):
    id_collection = models.AutoField(db_column='id_Collection', primary_key=True)  # Field name made lowercase.
    name_collection = models.CharField(db_column='name_Collection', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collection'

    def __str__(self):
        return self.name_collection


class Comporter(models.Model):
    id_categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_Categorie')  # Field name made lowercase.
    id_collection = models.ForeignKey(Collection, models.DO_NOTHING, db_column='id_Collection', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comporter'
        unique_together = ('id_categorie', 'id_collection')

    def __str__(self):
        return str(self.id_categorie) + ' | ' + str(self.id_collection)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Product(models.Model):
    id_product = models.AutoField(db_column='id_Product', primary_key=True)  # Field name made lowercase.
    name_product = models.CharField(db_column='name_Product', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reference_product = models.CharField(db_column='reference_Product', max_length=50, blank=True, null=True)  # Field name made lowercase.
    couleur_product = models.CharField(db_column='couleur_Product', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dimensions_product = models.CharField(db_column='dimensions_Product', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url_product = models.CharField(db_column='url_Product', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_subcategorie = models.ForeignKey('Subcategorie', models.DO_NOTHING, db_column='id_SubCategorie', blank=True, null=True)  # Field name made lowercase.
    collection_id_collection = models.ForeignKey(Collection, models.DO_NOTHING, db_column='collection_id_collection', blank=True, null=True)
    type_id_type = models.ForeignKey('TypeProduct', models.DO_NOTHING, db_column='type_id_type', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self):
        return self.name_product


class Subcategorie(models.Model):
    id_subcategorie = models.AutoField(db_column='id_SubCategorie', primary_key=True)  # Field name made lowercase.
    name_subcategorie = models.CharField(db_column='name_SubCategorie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_Categorie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subcategorie'

    def __str__(self):
        return self.name_subcategorie


class TypeProduct(models.Model):
    id_type = models.AutoField(db_column='id_Type', primary_key=True)  # Field name made lowercase.
    name_type = models.CharField(db_column='name_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type_product'

    def __str__(self):
        return self.name_type
