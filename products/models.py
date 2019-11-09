from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from users.models import Profile


class Gallery(models.Model):
    name = models.CharField("Gallery name", max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gallery,self).save( *args, **kwargs)


class Category(models.Model):
    name = models.CharField("Category Name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    name = models.CharField("Subcategory Name", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"



# Countries
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

processor_list = (
    ('AMD', 'AMD'),
    ('SA', 'AMD Dual Core'),
    ('USA', 'AMD Phenom Triple-Core'),
    ('IN', 'Intel'),
    ('INA', 'Intel Atom'),
    ('INC', 'Intel Celeron'),
    ('IC3', 'Intel Core i3'),
    ('IC5', 'Intel Core i5'),
    ('IC7', 'Intel Core i7'),
    ('IDC','Intel Dual Core'),
    ('IPD','Intel Pentium Dual Core'),
    ('MA','Marvell'),
    ('NV','NVIDIA'),
    ('QDC','Qualcomm Dual Core'),
    ('TI','Texas Instrument'),
    ('VIA','VIA'),
)

os_list = (
    ('AND','Android'),
    ('BB7','BlackBerry OS 7.0'),
    ('BB1','BlackBerry OS 7.1'),
    ('BO1','Blackberry OS 10'),
    ('FDO','Free DOS'),
    ('IOS','IOS'),
    ('LIN','Linux'),
    ('MOX','Mac OS X'),
    ('MOS','Mobile OS'),
    ('NOS','No OS'),
    ('NOK','Nokia OS'),
    ('OT','Other'),
    ('SBA','Samsung Bada'),
    ('SYM','Symbian'),
    ('WIN','Windows'),
    ('WI1','Windows 10'),
    ('WI7','Windows 7'),
    ('WI8','Windows 8'),
)

gender_list = (
    ('M', 'Male'),
    ('F', 'Female'),
)

sim_sizes = (
    ('re','Regular Sim'),
    ('na', 'Nano Sim'),
    ('mi', 'Micro Sim'),
)



class Product(models.Model):
    name = models.CharField("Product Name", max_length=200,null=False, blank = False)
    slug = models.SlugField(max_length=100, editable=False, null=False, blank=False)
    brand = models.CharField("Brand", max_length=100, null=False , blank=False)
    weight = models.DecimalField("Weight", max_digits=10 , decimal_places=2, null=False, blank=False)
    colour = models.CharField("colour", max_length=30, default="N/A")
    category = models.ForeignKey(Category , on_delete=models.CASCADE, null=False , blank=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=False , blank=False)
    keywords = models.CharField("Keywords", default="N/A", max_length=200)
    country = models.CharField(max_length=2, choices=country_list, help_text="Add alternative keywords to this product to help in search")
    size = models.CharField("Size", max_length=100,help_text="Size(Lxwxh)", default="N/A")
    youtube_id = models.CharField("Youtube Id",  max_length=50, default="N/A")
    #description
    description = models.CharField("description", max_length=500, default="N/A")
    higlights = models.CharField("Highlights", max_length=300, default="N/A")
    #meta
    sold_by = models.OneToOneField(Profile, on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now,editable=False)
    active = models.BooleanField(default=False)
	# Specifications - For Electronic Devices
    battery = models.CharField("Battery Capacity (mAH)", max_length=20, help_text="Battery Capacity(mAH)", default="N/A")
    hdd = models.CharField("HardDisk(GB)",max_length=100 ,help_text="Hard Disk",default="N/A")
    camera_resolution = models.CharField("Camera Resolution",help_text="Resolution in Megapixels", max_length=10 ,default="N/A")
    usb = models.CharField("Usb Type", max_length=20, help_text="Eg: Usb c, Usb 3.0", default="N/A")
    ports = models.CharField("Number of Ports", max_length=10,default="N/A")
    sim = models.CharField("Sim Size" , max_length=2, choices=sim_sizes, help_text="Sim Slot Size")
    ram = models.CharField("RAM", max_length=100,help_text="Random Access Memory",default="N/A")
    display_size = models.CharField("Display Size",max_length=100,help_text="Inches",default="N/A")
    mainMaterial = models.CharField("Main Material",max_length=30,blank=True,null=True,help_text="Product Material")
    network = models.CharField("Network Connectivity", max_length=50, help_text ="Supported Network" , default="N/A")
    processor = models.CharField("Processor Type", max_length=3, choices = processor_list, help_text="Processor Type", default="N/A")
    opticalzoom = models.CharField("Optical Zoom", max_length=20, help_text="Optical Zoom",default="N/A")
    screentechnology = models.CharField("Screen Technology", max_length=50, help_text="Screen Technology", default="N/A")
    internalmemory = models.CharField("Internal Memory",max_length=10,  help_text="Internal Memory" , default="N/A")
    megapixels = models.CharField("Megapixels", max_length=10, help_text="Megapixels", default="N/A")
    operatingsystem = models.CharField("Operating System",max_length=3, choices=os_list, help_text="Operating System", default="N/A")

	# Fashion
    collection = models.CharField("Collection Family", max_length=50, help_text="Name of collection", default="N/A")
    colorfamily = models.CharField("Color Family", max_length=50, help_text="Color Family of product", default="N/A")
    gender = models.CharField("Gender", max_length=1, choices=gender_list, help_text="Gender", default="N/A")
    sleeve = models.CharField("Sleeve Length", max_length=50, help_text="Sleeve Length", default="N/A")
    skirt = models.CharField("Skirt Type", max_length=50, help_text="Skirt Type", default="N/A")
    age_group = models.CharField("Age Group", max_length=50, help_text="Age Group", default="N/A")
    season = models.CharField("Skirt Type", max_length=50, help_text="Skirt Type", default="N/A")

	#Books & Gaming
    author = models.CharField("Author", max_length=100, help_text="Author's Name", default="N/A")
    isbn = models.CharField("ISBN", max_length=100, help_text="ISBN", default="N/A")
    pages = models.CharField("Pages", max_length=10, help_text="Number of Pages", default="N/A")
    language = models.CharField("Language", max_length=50 ,help_text="Language", default="N/A")
    pub_year = models.CharField("Publication Year", max_length=4, help_text="Publication Year", default="N/A")
    edition = models.CharField("Edition", max_length=20, help_text="Edition", default="N/A")

    #gallery
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="photo_image_filename")
    image_1 = models.ImageField(upload_to="photo_image_filename")
    image_2 = models.ImageField(upload_to="photo_image_filename")
    image_3 = models.ImageField(upload_to="photo_image_filename",null=True, blank="True")
    image_4 = models.ImageField(upload_to="photo_image_filename",null=True, blank="True")
    image_5 = models.ImageField(upload_to="photo_image_filename",null=True, blank="True")
    image_6 = models.ImageField(upload_to="photo_image_filename",null=True, blank="True")

    def __str__(self):
        return self.name

    def photo_image_filename(instance, filename):
        return f'{instance.gallery.slug}/{filename}'

    def get_absolute_url(self):
        return reverse ('products.views.index', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        """
        Auto populating the SlugField with the slug friendly version of the product name
        """
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	# Pricing
	variation = models.CharField("Variation", max_length=2,choices=country_list, help_text="Variation", blank=True,null=True)
	sku = models.CharField("Stock Keeping Unit", max_length=70, help_text="Stock Keeping Unit")
	identification = models.CharField("ISBN/UPC/EAN", max_length=100 , help_text="ISBN/EAN/UPC", blank=True,null=True)
	quantity = models.PositiveIntegerField("Quantity", help_text="Quantity In Stock", blank=True,null=True)
	price = models.DecimalField("Price", max_digits=10, decimal_places=2,help_text="Price")
	saleprice = models.DecimalField("Sale Price", max_digits=10, decimal_places=2,help_text="Sale Price" , blank=True,null=True)
	salestart = models.DateField("Sale Start", help_text="Sale Start Date", blank=True,null=True)
	salestop = models.DateField("Sale End" , help_text="Sale End Date", blank=True,null=True)

	def __str__(self):
		return f'{self.product} - {self.sku}'


rating_count = (
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
)

class Review(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField("Review Title", max_length=50, null=False, blank=False)
	content = models.CharField("Review Content", max_length=300, null=False, blank=False)
	rating = models.PositiveIntegerField(choices=rating_count)
	date_added = models.DateField(default=timezone.now,editable=False)

	def __str__(self):
		return f'{self.author.name} - {self.title}'