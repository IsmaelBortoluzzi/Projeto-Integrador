from product_brand.models import Brand


def create_brand_from_brandform(brand_from, commit=False):
    new_brand = Brand()

    new_brand.name = brand_from.cleaned_data.get('name')
    new_brand.initials = brand_from.cleaned_data.get('initials')
    new_brand.supplier = brand_from.cleaned_data.get('supplier')

    if commit is True:
        new_brand.save()

    return new_brand
