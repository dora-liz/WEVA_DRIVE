# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountDetails(models.Model):
    acc_no = models.AutoField(primary_key=True)
    acc_name = models.CharField(max_length=50)
    card_no = models.IntegerField()
    balance = models.DecimalField(max_digits=18, decimal_places=2)
    user_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'account_details'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    fk_portfolio_id = models.IntegerField()
    image_name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gallery'


class Login(models.Model):
    user_name = models.CharField(db_column='User_name', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    user_type = models.CharField(db_column='User_type', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login'


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    packagename = models.CharField(db_column='PackageName', max_length=80)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=50)  # Field name made lowercase.
    rate = models.IntegerField(db_column='Rate')  # Field name made lowercase.
    actions = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'package'


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_desc = models.TextField()
    fk_prj_id = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'portfolio'


class Projects(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_title = models.CharField(max_length=50)
    fk_cat_id = models.IntegerField()
    fk_reg_id = models.IntegerField()
    image_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'projects'


class Sam(models.Model):
    reg_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=70)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=40)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_number', max_length=10)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    user_type = models.CharField(max_length=25)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sam'


class ServiceproviderPayment(models.Model):
    pid = models.AutoField(primary_key=True)
    se_email = models.CharField(max_length=50)
    fk_pack_id = models.IntegerField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'serviceprovider_payment'
