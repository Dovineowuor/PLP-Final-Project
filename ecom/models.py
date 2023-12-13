from django.db import models
from django.contrib.auth.models import User
from django.db import migrations
from django.utils import timezone





class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(unique=True, default='')
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True) 

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

class Category(models.Model):
    CATEGORY = [
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Toddlers', 'Toddlers'),
    ('Unisex', 'Unisex'),
]

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=CATEGORY, default= 'Choose one below')

    def __str__(self):
        return self.name

class Brand(models.Model):
    BRAND = [
        ('Abercrombie & Fitch', 'Abercrombie & Fitch'),
        ('Adidas', 'Adidas'),
        ('Adore Me', 'Adore Me'),
        ('Aerie', 'Aerie'),
        ('Altra', 'Altra'),
        ('American Apparel', 'American Apparel'),
        ('American Eagle Outfitters', 'American Eagle Outfitters'),
        ('Ann Taylor', 'Ann Taylor'),
        ('Anna Sui', 'Anna Sui'),
        ('Anne Klein', 'Anne Klein'),
        ('Anthropologie', 'Anthropologie'),
        ('Arden B.', 'Arden B.'),
        ('Ariat', 'Ariat'),
        ('Armani', 'Armani'),
        ('Asics', 'Asics'),
        ('Athleta', 'Athleta'),
        ('Avenue', 'Avenue'),
        ('Away', 'Away'),
        ('Aéropostale', 'Aéropostale'),
        ('BCBG', 'BCBG'),
        ('Banana Republic', 'Banana Republic'),
        ('Bealls', 'Bealls'),
        ('Bebe', 'Bebe'),
        ('Birkenstock', 'Birkenstock'),
        ('Bombas', 'Bombas'),
        ('Boohoo', 'Boohoo'),
        ('Born Shoes', 'Born Shoes'),
        ('Borsalino', 'Borsalino'),
        ('Brooks Brothers', 'Brooks Brothers'),
        ('Brooks Sports', 'Brooks Sports'),
        ('Burberry', 'Burberry'),
        ('C by Champion', 'C by Champion'),
        ('Calvin Klein', 'Calvin Klein'),
        ('Cartier', 'Cartier'),
        ('Catherines Plus Sizes', 'Catherines Plus Sizes'),
        ('Cato', 'Cato'),
        ('Champion', 'Champion'),
        ('Chanel', 'Chanel'),
        ('Charlotte Russe', 'Charlotte Russe'),
        ('Chicos', 'Chicos'),
        ('Christopher & Banks', 'Christopher & Banks'),
        ('Churchs', 'Churchs'),
        ('CitiTrends', 'CitiTrends'),
        ('Claires Accessories', 'Claires Accessories'),
        ('Clarks', 'Clarks'),
        ('Coach', 'Coach'),
        ('Columbia', 'Columbia'),
        ('Converse', 'Converse'),
        ('Crocs', 'Crocs'),
        ('DKNY', 'DKNY'),
        ('Dior', 'Dior'),
        ('Dockers', 'Dockers'),
        ('Dolce & Gabbana', 'Dolce & Gabbana'),
        ('Dr. Scholls shoes', 'Dr. Scholls shoes'),
        ('DressBarn', 'DressBarn'),
        ('Duluth Trading Co.', 'Duluth Trading Co.'),
        ('Dune', 'Dune'),
        ('Eddie Bauer', 'Eddie Bauer'),
        ('Everlane', 'Everlane'),
        ('Express', 'Express'),
        ('Fabletics', 'Fabletics'),
        ('Forever', 'Forever'),
        ('Fossil', 'Fossil'),
        ('Fruit of the Loom', 'Fruit of the Loom'),
        ('G-star', 'G-star'),
        ('Gap', 'Gap'),
        ('GapBody', 'GapBody'),
        ('Gloria Vanderbilt', 'Gloria Vanderbilt'),
        ('Goodys', 'Goodys'),
        ('Gucci', 'Gucci'),
        ('H&M', 'H&M'),
        ('Hanes', 'Hanes'),
        ('Hollister', 'Hollister'),
        ('Honey', 'Honey'),
        ('Hot Topic', 'Hot Topic'),
        ('Hugo Boss', 'Hugo Boss'),
        ('Hush Puppies', 'Hush Puppies'),
        ('Ivanka Trump (Brand)', 'Ivanka Trump (Brand)'),
        ('J. Jill', 'J. Jill'),
        ('J.Crew', 'J.Crew'),
        ('Jimmy Choo', 'Jimmy Choo'),
        ('Jos. A. Bank', 'Jos. A. Bank'),
        ('Juicy Couture', 'Juicy Couture'),
        ('K & G Fashion Superstore', 'K & G Fashion Superstore'),
        ('K-Swiss', 'K-Swiss'),
        ('Kate Spade', 'Kate Spade'),
        ('Kenneth Cole', 'Kenneth Cole'),
        ('KidSuper', 'KidSuper'),
        ('L. L. Bean', 'L. L. Bean'),
        ('LOFT', 'LOFT'),
        ('Lands End', 'Lands End'),
        ('Lane Bryant', 'Lane Bryant'),
        ('Lee', 'Lee'),
        ('Levis', 'Levis'),
        ('LifeStride', 'LifeStride'),
        ('Liz Claiborne', 'Liz Claiborne'),
        ('London Fog', 'London Fog'),
        ('Louis Vuitton', 'Louis Vuitton'),
        ('Lucy', 'Lucy'),
        ('Lululemon', 'Lululemon'),
        ('MVMT', 'MVMT'),
        ('Madewell', 'Madewell'),
        ('Marc Jacobs', 'Marc Jacobs'),
        ('Marmot', 'Marmot'),
        ('Maurices', 'Maurices'),
        ('Mens Wearhouse', 'Mens Wearhouse'),
        ('Merrell', 'Merrell'),
        ('Michael Kors', 'Michael Kors'),
        ('Mudd', 'Mudd'),
        ('Naturalizer', 'Naturalizer'),
        ('Nautica', 'Nautica'),
        ('New Balance', 'New Balance'),
        ('New Era', 'New Era'),
        ('New York & Company', 'New York & Company'),
        ('Nike', 'Nike'),
        ('Nine West', 'Nine West'),
        ('Oakley', 'Oakley'),
        ('Obey', 'Obey'),
        ('Old Navy', 'Old Navy'),
        ('Omega', 'Omega'),
        ('Oscar de La Renta', 'Oscar de La Renta'),
        ('PUMA', 'PUMA'),
        ('Pacific Sunwear', 'Pacific Sunwear'),
        ('Patagonia', 'Patagonia'),
        ('Polo Ralph Lauren', 'Polo Ralph Lauren'),
        ('Prada', 'Prada'),
        ('QUIZ', 'QUIZ'),
        ('Quiksilver', 'Quiksilver'),
        ('Ralph Lauren', 'Ralph Lauren'),
        ('RayBan', 'RayBan'),
        ('Red Wing Shoes', 'Red Wing Shoes'),
        ('Reebok', 'Reebok'),
        ('Rockport', 'Rockport'),
        ('Rolex', 'Rolex'),
        ('Ryka', 'Ryka'),
        ('SOREL', 'SOREL'),
        ('Sam Edelman', 'Sam Edelman'),
        ('Samsonite', 'Samsonite'),
        ('Sean John', 'Sean John'),
        ('Seiko', 'Seiko'),
        ('Shape-ups', 'Shape-ups'),
        ('Skechers', 'Skechers'),
        ('Stitch Fix', 'Stitch Fix'),
        ('Stussy', 'Stussy'),
        ('Swarovski', 'Swarovski'),
        ('Swatch', 'Swatch'),
        ('TAG Heuer', 'TAG Heuer'),
        ('TUMI', 'TUMI'),
        ('Talbots', 'Talbots'),
        ('Ted Baker', 'Ted Baker'),
        ('Teva', 'Teva'),
        ('The Buckle', 'The Buckle'),
        ('The Limited', 'The Limited'),
        ('The North Face', 'The North Face'),
        ('Timberland', 'Timberland'),
        ('Tissot', 'Tissot'),
        ('Tommy Hilfiger', 'Tommy Hilfiger'),
        ('Tommy John', 'Tommy John'),
        ('Toms', 'Toms'),
        ('Torrid', 'Torrid'),
        ('True Religion', 'True Religion'),
        ('UGG', 'UGG'),
        ('UNIQLO', 'UNIQLO'),
        ('Under Armour', 'Under Armour'),
        ('Urban Outfitters', 'Urban Outfitters'),
        ('VS Pink', 'VS Pink'),
        ('Van Heusen', 'Van Heusen'),
        ('Vans', 'Vans'),
        ('Vera Wang', 'Vera Wang'),
        ('Versace', 'Versace'),
        ('Victorias Secret', 'Victorias Secret'),
        ('Victorinox Swiss Army', 'Victorinox Swiss Army'),
        ('Vince Camuto', 'Vince Camuto'),
        ('Vineyard Vines', 'Vineyard Vines'),
        ('Wet Seal', 'Wet Seal'),
        ('White House Black Market', 'White House Black Market'),
        ('Wilson Sporting Goods', 'Wilson Sporting Goods'),
        ('Wilsons Leather', 'Wilsons Leather'),
        ('Wolverine', 'Wolverine'),
        ('Wrangler', 'Wrangler'),
        ('Yves Saint Laurent', 'Yves Saint Laurent'),
        ('Zara', 'Zara'),
        ('rue', 'rue'),
    ]
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=32, choices=BRAND, default='Choose a brand Matching the product Below', null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    BRAND = (
        ('New', 'New'),
        ('Second Hand', 'Second Hand'),
        ('Shipped From Abroad', 'Shipped From Abroad'),
        ('Knighted', 'Knighted'),
        ('Locally Made', 'Locally Made')
    )
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=15)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=5000)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=BRAND, default='Choose One Below', null=True)

    def get_prep_value(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return 1  # Set a default value,

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-created_at',) 


class Orders(models.Model):
    PAYMENT_CHOICES = (
            ('Order Placed', 'Order Placed'),
            ('Order Confirmed', 'Order Confirmed'),
            ('Out for Delivery', 'Out for Delivery'),
            ('Delivered', 'Delivered'),
            )


    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=PAYMENT_CHOICES)
    payment_status = models.CharField(max_length=16, choices=PAYMENT_CHOICES, default='', null=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"

class OrderItem(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True, blank=True, verbose_name='Quantity')
    rate = models.FloatField(max_length=100)
    total = models.FloatField(max_length=100)
    status = models.IntegerField()

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# Email Subscription

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
