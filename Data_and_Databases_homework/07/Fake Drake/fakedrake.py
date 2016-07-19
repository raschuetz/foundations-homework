import pandas as pd
import random
import twython
from config import *

# POS
pos = {}
pos_keys = [ 'NN', 'NN', 'NN',
        'VB', 'VB',
        'VBN', 'VBN',
        'JJS', 'JJS',
        'NNS', 'NNS',
        'JJ', 'JJ',
        'NNP_thing', 'NNP_thing',
        'IVB', 'RB', 'IN_NN', 'RB_IN', 'VB_place', 'pos_JJ',
        'JJ_to', 'VB_to', 'VB_me', 'JJR', 'NNP', 'NNP_place',
        'VBN_to', 'VBG', 'VBG_IN', 'neg_NNS']
for x in pos_keys:
    filename = x + '.csv'
    df = pd.read_csv(filename)
    if not x in pos.keys():
        pos[x] = random.choice(df[x].tolist())
    else:
        if not x + '2' in pos.keys():
            pos[x + '2'] = random.choice(df[x].tolist())
        else:
            pos[x + '3'] = random.choice(df[x].tolist())
# Other variables
think_vb = random.choice(['think', 'know', 'believe', 'feel like'])
# Mini-functions
def t1_you_dont_know_generator():
    t1_IN_NN = random.choice([w for w in pd.read_csv('IN_NN.csv')['IN_NN'].tolist() if
        w[:2] != 'of'
        and w[:2] != 'as'
        and w != 'at sit'
        and w[:4] != 'like'
        and w[:2] != 'by'
        and w[:5] != 'on da'
        and w[:4] != 'than'])
    return """You don't know what's {}
    But you know what you're {}""".format(
        t1_IN_NN,
        pos['RB_IN'])
def t2_girl_put_generator():
    t2_NN = random.choice(['hustle', 'experience', 'overtime', 'intention', 'bliss', 'honey',
        'reputation', 'taste', 'indifference', 'skin', 'sweat', 'discretion',
        'surgery', 'booze', 'action', 'risk'])
    return """Girl put in {}
    {} it through the {}""".format(
        t2_NN,
        pos['VB'], pos['NN'])
def t3_I_live_for_generator():
    return """I live for the {} I can't {}
    with the people that I won't {}""".format(
        pos['NN'], pos['VB'],
        pos['VB2'])
def t4_at_the_same_time_generator():
    return """{} is just {} and {} at the same time""".format(
        pos['NN'][0].upper() + pos['NN'][1:], pos['NN2'], pos['NN3'])
def t5_when_all_is_generator():
    return """When all is {} and {}
    more is always {} than {}""".format(
        pos['VBN'], pos['VBN2'],
        pos['VBN2'], pos['VBN'])
def t6_i_know_they_say_generator():
    return """I know they say the first {} is the {},
    but that first {} is the {}""".format(
        pos['NN'], pos['JJS'],
        pos['NN2'], pos['JJS2'])
def t7_sometimes_generator():
    return """'Cause your {} don't {} what it {} sometimes""".format(
        pos['NN'], pos['VB'], pos['VB2'])
def t8_one_place_generator():
    return """{} in one place, {} in another""".format(
        pos['NN'][0].upper() + pos['NN'][1:], pos['NN2'])
def t9_im_more_generator():
    return """I'm more than just a {}; I doubt you'll find another.""".format(pos['NN'])
def t10_just_as_i_generator():
    return """Just as I predicted, here we {} again.
    They always say the {} {} has the {} {}""".format(
        pos['IVB'],
        pos['JJS'], pos['NN'], pos['JJS2'], pos['NN2'])
def t11_metaphor_generator():
    return """The {} I want to {}
    is like a {} to my {}""".format(
        pos['NN'], pos['IVB'],
        pos['NN2'], pos['NN3'])
def t12_you_aint_the_only_generator():
    return """You ain't the only {}
    that's tryna be the only {}""".format(pos['NN'], pos['NN'])
def t13_wish_you_would_learn_generator():
    return """Wish you would learn to love {} and use {},
    and not the other way around""".format(
        pos['NNS'], pos['NNS2'])
def t14_looking_back_generator():
    return """Looking back on the {}, at least my {} is intact.
    'Cause we said no {} attached, and I still got tied up in that""".format(
        pos['NN'], pos['NN2'],
        pos['NNS'], pos['VBN'])
def t15_so_you_should_generator():
    t15_verbs = random.choice(['fly', 'go', 'roam', 'stop', 'walk', 'turn', 'escape'])
    t15_adverbs = random.choice(['long', 'much', 'endlessly', 'often', 'many times'])
    return """The {} ones {}, if you wait too {}.
    So you should {}, before you stay too {}""".format(
        pos['pos_JJ'], t15_verbs, t15_adverbs,
        t15_verbs, t15_adverbs)
def t16_you_know_its_real_generator():
    return """You know it's real when you {}
    who you think you {}""".format(pos['VB'], pos['VB'])
def t17_you_know_its_generator():
    return """You know it's {} when you {}
    who you think you {}""".format(
        pos['JJ'], pos['VB'],
        pos['VB'])
def t18_dont_really_give_a_generator():
    t18_nouns = random.choice(['damn', 'darn', 'drat', 'sweat', 'fu**', 'shit'])
    return """I don't really give a {}
    and my excuse is that I'm {}""".format(
        t18_nouns,
        pos['JJ'])
def t19_lookin_for_generator():
    return """Lookin' for the {} way
    to do the {} things""".format(
        pos['JJ'],
        pos['JJ2'])
def t20_nobody_understood_generator():
    return """Nobody understood what it was like to be {} and {}""".format(
        pos['JJ'],
        pos['JJ2'])
def t21_we_just_got_generator():
    return """You got {}
    we just got {}""".format(
        pos['NNS'],
        pos['NNS2'])
def t22_i_warned_them_generator():
    t22_IN_NN = random.choice([w for w in pd.read_csv('IN_NN.csv')['IN_NN'].tolist() if
        w[:4] != 'like'
        and w[:2] != 'in'
        and w[:4] != 'than'
        and w[-3:] != 'cup'
        and w[-4:] != 'than'
        and w[-4:] != 'fuck'
        and w[-3:] != 'dog'
        and w[:3] != 'up'
        and w[:6] != 'though'])
    return """I warned them {}""".format(t22_IN_NN)
def t23_i_never_generator():
    return """But I never {}
    Even when I'm {}""".format(
        pos['VB_place'],
        pos['VB_place'].split()[1])
def t24_way_too_generator():
    return """No, I'm too {} you
    I'm way too {} you""".format(pos['JJ_to'], pos['JJ_to'])
def t25_look_generator():
    return """Look... I don't know how to {} you
    I don't know how to ask you if you're {}""".format(pos['VB_to'], pos['JJ']) #, pos['VB'], pos['JJR'])
def t26_friends_always():
    return """My friends always feel the need to {} things
    Seems like they're just {} than us these days""".format(pos['VB_me'], pos['JJR'])
def t27_for_you():
    t27_rhyme = random.choice([
        ['riiiide', 'decide', 'slide', 'ride'],
        ['twist', 'resist', 'exist'],
        ['sleep', 'creep'],
        ['overlook', 'look', 'cook'],
        ['fly', 'die', 'lie', 'cry'],
        ['kiss', 'diss'],
        ['skate', 'concentrate', 'hesitate', 'appreciate', 'relate', 'wait'],
        ['appear', 'disappear'],
        ['spit', 'forfeit', 'vomit'],
        ['sneak', 'speak'],
        ['return', 'burn', 'turn'],
        ['stop', 'pop', 'hop'],
        ['flow', 'grow']
        ])
    a = t27_rhyme.pop(random.randrange(len(t27_rhyme)))
    b = random.choice(t27_rhyme)
    return """I {} I'd {} for you
    I {} I'd {} for you""".format(
        think_vb, a,
        think_vb, b)
def t28_old_new():
    return """My old {} is my new {} now""".format(pos['NN'], pos['NN'])
def t29_workin():
    return """My old {} is my new {} now, and we're workin' on it""".format(pos['NN'], pos['NN'])
def t30_woo():
    return """I just found my {} like I'm {}, woo""".format(pos['NN'], pos['NNP'])
def t31_i_miss():
    return """{} and {} for all my {} that I miss""".format(pos['NNP_thing'], pos['NNP_thing2'], pos['NNS'])
def t32_uh():
    return """Uh, uh, uh, I {} I need some {}""".format(think_vb, pos['NNP_thing'])
def t33_hundred():
    return """Hundred {} out in {}, they so {}, wow""".format(pos['NNS'], pos['NNP_place'], pos['JJ'])
def t34_yeah():
    return """You {}, you {}
    yeah""".format(pos['VBN_to'], pos['VBN_to'])
def t35_ever_since():
    return """Cause ever since I left the city, you
    Started {} less and {} more""".format(pos['VBG'], pos['VBG_IN'])
def t36_got_a_lotta():
    return """I got {},
    got a lotta {}""".format(pos['NNS'], pos['NNS'])
def t37_pictures():
    return """They show me pictures of they {},
    Just to tell me they ain't really {}""".format(pos['NNS'], pos['NNS'])
def t38_written_on_me():
    return """I'm {} {}, got it written on me""".format(pos['JJ'], pos['NN'])
def t39_friends():
    return """My {} want to be friends with my other {}
    I don't let it get to me""".format(pos['neg_NNS'], pos['neg_NNS'])
def t40_wish():
    return """My only wish is that I die {}""".format(pos['pos_JJ'])
def t41_we_both():
    return """I've had mine, you've had yours, we both {}""".format(pos['IVB'])
def t42_drinking():
    return """Drinking every night because we drink to my {}""".format(pos['NNS'])
def t43_accomplishments():
    t43_pair = random.choice([['sipping', 'sip'],
        ['smoking', 'smoke'],
        ['grinding', 'grind'],
        ['plotting', 'plot'],
        ['cooking', 'cook'],
        ['puffing', 'puff'],
        ['skating', 'skate'],
        ['stunting', 'stunt'],
        ['dancing', 'dance'],
        ['rolling', 'roll'],
        ['swerving', 'swerve'],
        ['tripping', 'trip'],
        ['praying', 'pray'],
        ['flying', 'fly'],
        ['popping', 'pop'],
        ['PMSing', 'PMS'],
        ['scheming', 'scheme'],
        ['spending', 'spend'],
        ['swagging', 'swag'],
        ['crying', 'cry'],
        ['riding', 'ride'],
        ['splurging', 'splurge'],
        ['eating', 'eat'],
        ['undressing', 'undress'],
        ['tweaking', 'tweak'],
        ['balling', 'ball'],
        ['chilling', 'chill'],
        ['bouncing', 'bounce'],
        ['twerking', 'twerk'],
        ['romancing', 'romance']])
    return """{} every night because we {} to my accomplishments""".format(t43_pair[0][0].upper() + t43_pair[0][1:], t43_pair[1])
def t44_drizzy_got():
    return """Drizzy got the {}, so Drizzy gonna {} it""".format(pos['NN'], pos['VB'])
def t45_yelling_out():
    return """I be yelling out {} over everything, {} on my mind""".format(pos['NN'], pos['NN'])
def t46_i_heard():
    return """I heard once that they would rather hear about {} than {}""".format(pos['NNS'], pos['NNS2'])
def t47_last_name():
    return """Last name ever
    First name {}""".format(pos['JJS'])
def t48_do_it_real():
    t48_pair = random.choice([['light', 'lighter'],
        ['low', 'lower'],
        ['soon', 'sooner'],
        ['bright', 'brighter'],
        ['cold', 'colder'],
        ['stinky', 'stinkier'],
        ['legit', 'more legit'],
        ['soft', 'softer'],
        ['deep', 'deeper'],
        ['cheap', 'cheaper'],
        ['close', 'closer'],
        ['big', 'bigger'],
        ['small', 'smaller'],
        ['easy', 'easier'],
        ['fine', 'finer'],
        ['happy', 'happier'],
        ['rad', 'radder'],
        ['rich', 'richer'],
        ['sick', 'sicker'],
        ['high', 'higher'],
        ['hard', 'harder'],
        ['tough', 'tougher'],
        ['slick', 'slicker'],
        ['good', 'better'],
        ['green', 'greener'],
        ['bad', 'badder'],
        ['bad', 'worse'],
        ['little', 'less'],
        ['hot', 'hotter'],
        ['loud', 'louder']])
    return """We could do it real {}, {} than you ever done it""".format(t48_pair[0], t48_pair[1])
def t49_listen():
    return """Goddamn,
    Should I listen to {} or myself?""".format(pos['NNP'])
def t0_she_asked():
    return """She asked
    What have I learned since getting {}""".format(pos['JJR'])

# Using each template equally
keeping_track_df = pd.read_csv('keeping_track.csv')
if not False in [x for x in keeping_track_df['used']]:
    keeping_track_df['used'] = False
unused = [keeping_track_df['t'][x] for x in range(50) if keeping_track_df['used'][x] == False]
tnum = random.choice(unused)
keeping_track_df = keeping_track_df.set_value(tnum, 'used', True)
keeping_track_df.to_csv('keeping_track.csv', index = False)

# Picking out the lyrics
template_options = [t0_she_asked(),
        t1_you_dont_know_generator(),
        t2_girl_put_generator(),
        t3_I_live_for_generator(),
        t4_at_the_same_time_generator(),
        t5_when_all_is_generator(),
        t6_i_know_they_say_generator(),
        t7_sometimes_generator(),
        t8_one_place_generator(),
        t9_im_more_generator(),
        t10_just_as_i_generator(),
        t11_metaphor_generator(),
        t12_you_aint_the_only_generator(),
        t13_wish_you_would_learn_generator(),
        t14_looking_back_generator(),
        t15_so_you_should_generator(),
        t16_you_know_its_real_generator(),
        t17_you_know_its_generator(),
        t18_dont_really_give_a_generator(),
        t19_lookin_for_generator(),
        t20_nobody_understood_generator(),
        t21_we_just_got_generator(),
        t22_i_warned_them_generator(),
        t23_i_never_generator(),
        t24_way_too_generator(),
        t25_look_generator(),
        t26_friends_always(),
        t27_for_you(),
        t28_old_new(),
        t29_workin(),
        t30_woo(),
        t31_i_miss(),
        t32_uh(),
        t33_hundred(),
        t34_yeah(),
        t35_ever_since(),
        t36_got_a_lotta(),
        t37_pictures(),
        t38_written_on_me(),
        t39_friends(),
        t40_wish(),
        t41_we_both(),
        t42_drinking(),
        t43_accomplishments(),
        t44_drizzy_got(),
        t45_yelling_out(),
        t46_i_heard(),
        t47_last_name(),
        t48_do_it_real(),
        t49_listen()]
new_lyric = template_options[tnum]

# Twitter stuff
twitter = twython.Twython(api_key, api_secret, access_token, token_secret)
twitter.update_status(status=new_lyric)
