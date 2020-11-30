## Product Variants (style,size,color)

* 1. Create Models (Color, Size, Variants)  - OK        

* 2. Add variant filed to Product variant (none,size,color,size-color) - OK

* 3. Install image thumbnails
        pip install django-admin-thumbnails  -  OK
        Define thumbnails variants images    - 

* set admin for new models (Color, Size, Variants) - OK

* 4. Set Variants inline for Product in admin - OK

* 5. Product Detail
        Change product detail function -> views
        Change product link depending on variant -> templates
        Add variants on product detail -> templates
        Apply Ajax function -> View
        Select Variant Size, Color -> templates

* 6. Shopcart
        Define variant relation in shopcart -> Model
        Add variant id to shopcart -> views
        Get Variant price in list -> templates

* 7. Order
        Define variant relation in order -> Model
        Add variant id to order table -> views

