from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from products.models import  Product

from .managers import VelocityUserManager


#Recommended by documentation for future User model customizations
class VelocityUser(AbstractUser):

    gender_list = (
        ('M', 'Male'),
        ('F','Female'),
    )

    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10,blank=True)
    fullname = models.CharField(max_length=50,blank=True)
    gender = models.CharField("Gender", choices= gender_list, max_length=1, null=False, blank=False)
    is_influencer = models.BooleanField(_('influencer'), default=False)
    is_seller = models.BooleanField(_('seller'),default=False)

    USERNAME_FIELD = 'email'

    objects = VelocityUserManager()#custom user Manager to Replace username identifier with email

    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # def __str__(self):
    #     # split_fullname = self.fullname.split(" ")
    #     # firstname = split_fullname[0]
    #     # lastname = split_fullname[-1]
    #     # new_fullname = f'{firstname} {lastname}'
    #     # return new_fullname
    #     return self.fullname

country_list = (
	('AF' , 'AFGHANISTAN'),
	('AL' , 'ALBANIA'),
	('DZ' , 'ALGERIA'),
	('AS' , 'AMERICAN SAMOA'),
	('AD' , 'ANDORRA'),
	('AO' , 'ANGOLA'),
	('AI' , 'ANGUILLA'),
	('AQ' , 'ANTARCTICA'),
	('AG' , 'ANTIGUA AND BARBUDA'),
	('AR' , 'ARGENTINA'),
	('AM' , 'ARMENIA'),
	('AW' , 'ARUBA'),
	('AU' , 'AUSTRALIA'),
	('AT' , 'AUSTRIA'),
	('AZ' , 'AZERBAIJAN'),
	('BS' , 'BAHAMAS'),
	('BH' , 'BAHRAIN'),
	('BD' , 'BANGLADESH'),
	('BB' , 'BARBADOS'),
	('BY' , 'BELARUS'),
	('BE' , 'BELGIUM'),
	('BZ' , 'BELIZE'),
	('BJ' , 'BENIN'),
	('BM' , 'BERMUDA'),
	('BT' , 'BHUTAN'),
	('BO' ,'BOLIVIA'),
	('BA' , 'BOSNIA AND HERZEGOVINA'),
	('BW' , 'BOTSWANA'),
	('BV' , 'BOUVET ISLAND'),
	('BR' , 'BRAZIL'),
	('IO' , 'BRITISH INDIAN OCEAN TERRITORY'),
	('BN' , 'BRUNEI DARUSSALAM'),
	('BG' , 'BULGARIA'),
	('BF' , 'BURKINA FASO'),
	('BI' , 'BURUNDI'),
	('KH' , 'CAMBODIA'),
	('CM' , 'CAMEROON'),
	('CA' , 'CANADA'),
	('CV' , 'CAPE VERDE'),
	('KY' , 'CAYMAN ISLANDS'),
	('CF' ,' CENTRAL AFRICAN REPUBLIC'),
	('TD' , 'CHAD'),
	('CL' , 'CHILE'),
	('CN' , 'CHINA'),
	('CO' , 'COLOMBIA'),
	('KM' , 'COMOROS'),
	('CG' , 'CONGO'),
	('CD' ,  'DR CONGO'),
	('CK' , 'COOK ISLANDS'),
	('CR' , 'COSTA RICA'),
	('CI' , 'CÔTE D\'IVOIRE'),
	('HR' , 'CROATIA'),
	('CU' , 'CUBA'),
	('CY' , 'CYPRUS'),
	('CZ' , 'CZECH REPUBLIC'),
	('DK' , 'DENMARK'),
	('DJ' , 'DJIBOUTI'),
	('DM' , 'DOMINICA'),
	('DO' , 'DOMINICAN REPUBLIC'),
	('EC' , 'ECUADOR'),
	('EG' , 'EGYPT'),
	('EH' , 'WESTERN SAHARA'),
	('SV' , 'EL SALVADOR'),
	('GQ' , 'EQUATORIAL GUINEA'),
	('ER' , 'ERITREA'),
	('EE' , 'ESTONIA'),
	('ET' , 'ETHIOPIA'),
	('FK' , 'FALKLAND ISLANDS'),
	('FO' ,'FAROE ISLANDS'),
	('FJ' , 'FIJI'),
	('FI' , 'FINLAND'),
	('FR' , 'FRANCE'),
	('GA' , 'GABON'),
	('GM' , 'GAMBIA'),
	('GE' , 'GEORGIA'),
	('DE' , 'GERMANY'),
	('GH' , 'GHANA'),
	('GI' , 'GIBRALTAR'),
	('GR' , 'GREECE'),
	('GL' , 'GREENLAND'),
	('GD' , 'GRENADA'),
	('GP' , 'GUADELOUPE'),
	('GU' , 'GUAM'),
	('GT' , 'GUATEMALA'),
	('GN' , 'GUINEA'),
	('GW' , 'GUINEA-BISSAU'),
	('GY' , 'GUYANA'),
	('HT' , 'HAITI'),
	('HN' , 'HONDURAS'),
	('HK' , 'HONG KONG'),
	('HU' , 'HUNGARY'),
	('IS' , 'ICELAND'),
	('IN' , 'INDIA'),
	('ID' , 'INDONESIA'),
	('IR' , 'IRAN'),
	('IQ' , 'IRAQ'),
	('IE' , 'IRELAND'),
	('IL' , 'ISRAEL'),
	('IT' , 'ITALY'),
	('JM' , 'JAMAICA'),
	('JP' , 'JAPAN'),
	('JO' , 'JORDAN'),
	('KZ' , 'KAZAKHSTAN'),
	('KE' , 'KENYA'),
	('KI' , 'KIRIBATI'),
	('KP' , 'KOREA'),
	('KW' , 'KUWAIT'),
	('KG' , 'KYRGYZSTAN'),
	('LA' , 'LAO' ),
	('LV' , 'LATVIA'),
	('LB' , 'LEBANON'),
	('LS' , 'LESOTHO'),
	('LR' , 'LIBERIA'),
	('LY' , 'LIBYA'),
	('LI' , 'LIECHTENSTEIN'),
	('LT' , 'LITHUANIA'),
	('LU' , 'LUXEMBOURG'),
	('MO' , 'MACAO'),
	('MK' , 'MACEDONIA'),
	('MG' , 'MADAGASCAR'),
	('MW' , 'MALAWI'),
	('MY' , 'MALAYSIA'),
	('MV' , 'MALDIVES'),
	('ML' , 'MALI'),
	('MT' , 'MALTA'),
	('MH' , 'MARSHALL ISLANDS'),
	('MQ' , 'MARTINIQUE'),
	('MR' , 'MAURITANIA'),
	('MU' , 'MAURITIUS'),
	('YT' , 'MAYOTTE'),
	('MX' , 'MEXICO'),
	('FM' , 'MICRONESIA'),
	('MD' , 'MOLDOVA'),
	('MC' , 'MONACO'),
	('MN' , 'MONGOLIA'),
	('MS' , 'MONTSERRAT'),
	('MA' , 'MOROCCO'),
	('MZ' , 'MOZAMBIQUE'),
	('MM' , 'MYANMAR'),
	('NA' , 'NAMIBIA'),
	('NR' , 'NAURU'),
	('NP' , 'NEPAL'),
	('NL' , 'NETHERLANDS'),
	('AN' , 'NETHERLANDS ANTILLES'),
	('NC' , 'NEW CALEDONIA'),
	('NZ' , 'NEW ZEALAND'),
	('NI' , 'NICARAGUA'),
	('NE' , 'NIGER'),
	('NG' , 'NIGERIA'),
	('NU' , 'NIUE'),
	('NF' , 'NORFOLK ISLAND'),
	('MP' , 'NORTHERN MARIANA ISLANDS'),
	('NO' , 'NORWAY'),
	('OM' , 'OMAN'),
	('PK' , 'PAKISTAN'),
	('PW' , 'PALAU'),
	('PA' , 'PANAMA'),
	('PG' , 'PAPUA NEW GUINEA'),
	('PY' , 'PARAGUAY'),
	('PE' , 'PERU'),
	('PH' , 'PHILIPPINES'),
	('PN' , 'PITCAIRN'),
	('PL' , 'POLAND'),
	('PT' , 'PORTUGAL'),
	('PR' , 'PUERTO RICO'),
	('QA' , 'QATAR'),
	('RO' , 'ROMANIA'),
	('RU' , 'RUSSIAN FEDERATION'),
	('RW' , 'RWANDA'),
	('SH' , 'SAINT HELENA'),
	('KN' , 'SAINT KITTS AND NEVIS'),
	('LC' , 'SAINT LUCIA'),
	('WS' , 'SAMOA'),
	('SM' , 'SAN MARINO'),
	('ST' , 'SAO TOME AND PRINCIPE'),
	('SA' , 'SAUDI ARABIA'),
	('SN' , 'SENEGAL'),
	('CS' , 'SERBIA AND MONTENEGRO'),
	('SC' , 'SEYCHELLES'),
	('SL' , 'SIERRA LEONE'),
	('SG' , 'SINGAPORE'),
	('SK' , 'SLOVAKIA'),
	('SI' , 'SLOVENIA'),
	('SB' , 'SOLOMON ISLANDS'),
	('SO' , 'SOMALIA'),
	('ZA' , 'SOUTH AFRICA'),
	('GS' , 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'),
	('ES' , 'SPAIN'),
	('LK' , 'SRI LANKA'),
	('SD' , 'SUDAN'),
	('SR' , 'SURINAME'),
	('SJ' , 'SVALBARD AND JAN MAYEN'),
	('SZ' , 'SWAZILAND'),
	('SE' , 'SWEDEN'),
	('CH' , 'SWITZERLAND'),
	('TW' , 'TAIWAN'),
	('TJ' , 'TAJIKISTAN'),
	('TZ' , 'TANZANIA'),
	('TH' , 'THAILAND'),
	('TG' , 'TOGO'),
	('TK' , 'TOKELAU'),
	('TO' , 'TONGA'),
	('TT' , 'TRINIDAD AND TOBAGO'),
	('TN' , 'TUNISIA'),
	('TR' , 'TURKEY'),
	('TM' , 'TURKMENISTAN'),
	('TV' , 'TUVALU'),
	('UG' , 'UGANDA'),
	('UA' , 'UKRAINE'),
	('AE' , 'UNITED ARAB EMIRATES'),
	('GB' , 'UNITED KINGDOM'),
	('US' , 'UNITED STATES'),
	('UY' , 'URUGUAY'),
	('UZ' , 'UZBEKISTAN'),
	('VE' , 'VENEZUELA'),
	('VU' , 'VANUATU'),
	('VN' , 'VIETNAM'),
	('YE' , 'YEMEN'),
	('ZW' , 'ZIMBABWE'),
)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/")
    business_name = models.CharField("Business Name", max_length=100 ,default="")
    business_email = models.EmailField("Business Email", blank=True,default="")
    business_registration_number = models.CharField("Regsitration Number", max_length=50, default="")
    shop_name = models.CharField("Shop Name", max_length=50, default="")
    tax_id = models.CharField("Tax Identification Number", max_length=100, default="")
    country = models.CharField("Country", max_length=2, choices=country_list)
    region = models.CharField("State/Region/Province", max_length=100)
    city = models.CharField("City", max_length=100)
    bank_name = models.CharField("Bank", max_length=100)
    account_number = models.CharField("Account Number", max_length=30,blank=True)
    account_holder = models.CharField("Account Holder's Name", max_length=100,blank=True)
    momo_number = models.CharField("Mobile Money Number", max_length=10, null=True, blank=True)


    def __str__(self):
        return f'{self.user}\'s Profile'

class Relationship(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target = models.ForeignKey(Profile, on_delete=models.CASCADE) #Profile to be followed

    def __str__(self):
        return f'{self.creator} followed {self.target}'

    # def save(self, *args, **kwargs):
    #     sup



class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField("Contact Name", max_length=100, null=False, blank=False)
    country  = models.CharField("Country", choices=country_list, max_length=2)
    region = models.CharField("State/Province/Country", max_length=100, null=False, blank=False)
    city = models.CharField("City", max_length=100, null=False, blank=False)
    apartment_number = models.CharField("Apt,Suite, Unit.. etc", max_length=100, null=False, blank=False)
    box_number = models.CharField("P.O. Box, Street Address..etc", max_length=100, null=False, blank=False)
    zip_code = models.CharField("Zip/Postal Code", max_length=100, null=False, blank=False)
    default = models.BooleanField("Default Shipping Address? ", default=False)

    def __str__(self):
        return self.id


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.ForeignKey)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)