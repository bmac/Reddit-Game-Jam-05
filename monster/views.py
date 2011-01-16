import random
random.seed()

from django.shortcuts import render_to_response
from django.template import RequestContext
from monster.models import Monster, DamageReport

def show_fight(request):
    u = request.user
    profile = u.get_profile() 
    if profile.dr is None:
        m = Monster.objects.all()[0]
        profile.dr = DamageReport(monster=m, damage=0)
        profile.save()
    
    if request.method == 'POST':
        print 'in post'
        fight_results = _process_fight(request)

    user_health = profile.health
    user_mana = profile.mana
    user_xp = profile.xp

    mon = profile.dr.monster
    mon_name = mon.name
    mon_health = mon.health
    mon_description = mon.description
    mon_pic = mon.pic

    return render_to_response('monster/show_fight.html', locals(), context_instance=RequestContext(request))
    

def _process_fight(request):
    u = request.user
    profile = u.get_profile()
    mon = profile.dr.monster
    dr = profile.dr

    damage = profile.attack + random.randint(0, 6)

    dr.damage += damage
    if dr.damage <= mon.health:
        kill = True
    else:
        kill = False
    return locals()
    
