from oscar.apps.catalogue.categories import create_from_breadcrumbs
from oscar.apps.catalogue.models import AttributeOptionGroup, AttributeOption, Option, ProductClass

def create_categories():
    categories = [
        'Headlights & Lighting > Turn Signals',
        'Headlights & Lighting > Fog Lights',
        'Headlights & Lighting > Headlights > Lights',

        'Interial Parts > Floor Mats',
        'Interial Parts > Gauges',
        'Interial Parts > Steering Wheels',
        'Interial Parts > Cargo Accessories',

        'Repair Manual',
        'Fuel System',
    ]

    for breadcrumbs in categories:
        create_from_breadcrumbs(breadcrumbs)

def create_product_attributes(name, options):
    ''' Create option group attributes and assign options to the option group
    '''
    option_group = AttributeOptionGroup.objects.create(name=name)
    bulk_list = [AttributeOption(group=option_group, option=option) for option in options]
    AttributeOption.objects.bulk_create(bulk_list)

#def create_product_attributes():
#    # create material attributes and assign options to material option group
#    material = AttributeOptionGroup.objects.create(name='material')
#    material_options = ['Steel', 'Aluminium', 'Thorium']
#    material_bulk_list = [AttributeOption(group=material, option=option) for option in material_options]
#    AttributeOption.objects.bulk_create(material_bulk_list)
#
#    colour = AttributeOptionGroup.objects.create(name='color')
#    colour_options = ['Red', 'Blue', 'Green', 'Black', 'White']
#    colour_bulk_list = [AttributeOption(group=colour, option=option) for option in colour_options]
#    AttributeOption.objects.bulk_create(colour_bulk_list)


#    # Assign options to material option group
#    AttributeOption.objects.bulk_create(colour_bulk_list)
#    AttributeOption.objects.create(
#        group=material,
#        option='Steel'
#    )

def create_product_class(option_name, pc_name, type, option_group, help_text, order, req_ship=True, track_stk=True):
    ''' Create
    '''
    co = Option.objects.create(name='size choices', type=Option.SELECT, option_group=att_opt_group, help_text='my size help text', order=3)
    pc = ProductClass.objects.create(name='Size', requires_shipping=req_ship, track_stock=track_stk)
    pc.options.add(co) # add the m2m relationship


def create_product(name, options, order, req_ship=True, track_stk=True):
    ''' Create option group attributes and assign options to the option group
    '''
    # Create Product Attributes
    option_group = AttributeOptionGroup.objects.create(name=name)
    bulk_list = [AttributeOption(group=option_group, option=option) for option in options]
    AttributeOption.objects.bulk_create(bulk_list)

    # Create Product Class
    co = Option.objects.create(name=f'{name} choices', type=Option.SELECT, option_group=option_group, help_text=f'my {name} help text', order=order)
    pc = ProductClass.objects.create(name=name, requires_shipping=req_ship, track_stock=track_stk)
    pc.options.add(co) # add the m2m relationship

def main():
#    create_categories()
#    create_product_attributes(name='material', options=['Steel', 'Aluminium', 'Thorium'])
#    create_product_attributes(name='colour', options=['Red', 'Blue', 'Green', 'Black', 'White'])
#    create_product_attributes(name='size', options=['S', 'M', 'L', 'XL', 'XXL'])
#    create_product_class(name='size c', options=['S', 'M', 'L', 'XL', 'XXL'])
#    create_product_class(option_name='size choices', pc_name='Size', type='Option.SELECT', option_group, help_text, order, req_ship=True, track_stk=True):

    create_product(name='material2', options=['Steel2', 'Aluminium2', 'Thorium2'], order=4)
    create_product(name='colour2', options=['Red2', 'Blue2', 'Green2', 'Black2', 'White2'], order=5)

if __name__ == "__main__":
        main()
