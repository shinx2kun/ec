from django.contrib import admin


from backend.models import ParentCategory, ChildCategory, Product, ProductImage, ProductCompositionTable


@admin.register(ParentCategory)
class AdminParentCategory(admin.ModelAdmin):
    pass

@admin.register(ChildCategory)
class AdminChildCategory(admin.ModelAdmin):
    pass

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    pass

@admin.register(ProductCompositionTable)
class AdminProductCompositionTable(admin.ModelAdmin):
    pass

