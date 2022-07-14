from product_brand.models import Brand


def create_brand_from_brandform(brand_from, commit=False):
    new_brand = Brand()

    new_brand.name = brand_from.cleaned_data.get('name')
    new_brand.initials = brand_from.cleaned_data.get('initials')

    if commit is True:
        new_brand.save()

    return new_brand


def create_brand_from_brandeditform(brand_from, pk, commit=False):
    new_brand = Brand.objects.filter(pk=pk).first()

    new_brand.name = brand_from.cleaned_data.get('name')
    new_brand.initials = brand_from.cleaned_data.get('initials')

    if commit is True:
        new_brand.save()

    return new_brand
