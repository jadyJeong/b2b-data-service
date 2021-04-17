from django.db import models


class User(models.Model):
    email            = models.EmailField(max_length=255, unique=True)
    password         = models.CharField(max_length=200)
    corporation_name = models.CharField(max_length=200)
    is_verified      = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'


class Corporation(models.Model):
    cocode     = models.CharField(max_length=8)
    coname     = models.CharField(max_length=200)
    coname_eng = models.CharField(max_length=200, null=True)
    stock_name = models.CharField(max_length=200, null=True)
    ticker     = models.CharField(max_length=20, unique=True, null=True)
    jurir_no   = models.CharField(max_length=50, unique=True, null=True)
    bizr_no    = models.CharField(max_length=50, unique=True, null=True)
    adres      = models.CharField(max_length=200, null=True)
    hm_url     = models.CharField(max_length=500, null=True)
    ir_url     = models.CharField(max_length=500, null=True)
    phn_no     = models.CharField(max_length=50, null=True)
    fax_no     = models.CharField(max_length=50, null=True)
    est_dt     = models.DateField(null=True)

    class Meta:
        db_table = 'corporations'


class CeoName(models.Model):
    name        = models.CharField(max_length=100)
    corporation = models.ForeignKey('Corporation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ceo_names'


class CorporationClassification(models.Model):
    symbol      = models.CharField(max_length=1)
    corporation = models.OneToOneField('Corporation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'corporation_classifications'


class AccountingMonth(models.Model):
    month       = models.IntegerField()
    corporation = models.OneToOneField('Corporation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounting_months'


class IndustryCode(models.Model):
    code        = models.CharField(max_length=50)
    corporation = models.OneToOneField('Corporation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'industry_codes'


class MainShareholder(models.Model):
    rcept_no                  = models.CharField(max_length=20)
    nm                        = models.CharField(max_length=50)
    bsis_posesn_stock_co      = models.DecimalField(max_digits=20, decimal_places=2)
    bsis_posesn_stock_qota_rt = models.DecimalField(max_digits=20, decimal_places=2)
    corporation               = models.ForeignKey('Corporation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_shareholders'


class StockType(models.Model):
    name             = models.CharField(max_length=50, unique=True)
    main_shareholder = models.OneToOneField('MainShareholder', on_delete=models.CASCADE)

    class Meta:
        db_table = 'stock_types'


class IncomeStatement(models.Model):
    year_month     = models.DateField(null=True)
    sales_ind      = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    ebit_ind       = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    ni_ind         = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    sales_con      = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    ebit_con       = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    ni_con         = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    ni_control_con = models.DecimalField(max_digits=20,decimal_places=2, null=True)
    corporation    = models.ForeignKey('Corporation', on_delete=models.CASCADE)

    class Meta:
        db_table = 'income_statements'


class CurrencyUnit(models.Model):
    name             = models.CharField(max_length=20, unique=True)
    income_statement = models.OneToOneField('IncomeStatement', on_delete=models.CASCADE)

    class Meta:
        db_table = 'currency_units'
