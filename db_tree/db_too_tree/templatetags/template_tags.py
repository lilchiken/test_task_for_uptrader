from django import template
from django.shortcuts import get_object_or_404

from db_too_tree.models import Dir

register = template.Library()

@register.inclusion_tag('main_menu.html', name='draw_menu')
def draw_menu(str):
    context = dict()
    obj = Dir.objects.select_related('parent')
    current_dir = get_object_or_404(obj, title=str)
    context['current_dir'] = current_dir
    sm_list = []
    if not current_dir.parent:
        return context
    f_parent = get_object_or_404(obj, id=current_dir.parent.id)
    sm_list.append(f_parent)
    while True:
        parent = sm_list[-1]
        parent = parent.parent
        if not parent:
            break
        const = get_object_or_404(obj, id=parent.id)
        sm_list.append(const)
    sm_list.reverse()
    context['new'] = sm_list
    return context