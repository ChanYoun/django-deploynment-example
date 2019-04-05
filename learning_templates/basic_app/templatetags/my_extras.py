from django import template

register = template.Library()  #to make this is filter

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut) #to use decoration
