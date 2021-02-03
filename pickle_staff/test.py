instructor = {}

jacore_leader = {}
andrew_leader = {}
aris_leader = {}
richard_leader = {}
gaberiel_leader = {}

jacore_member = {}
aris_member = {}
gaberiel_member = {}
andrew_member = {}
richard_member = {}

jacore_member['Jacore Baptiste'] = '(845) 200-6250'
jacore_member['Moussa Ndiaye'] = '(123) 456-7890'
jacore_member['Morris Jones'] = '(925) 286-5922'
jacore_member['Prince Fields'] = '(510) 472-0804'
jacore_member['Akari Johnson'] = '(510) 500-2206'

andrew_member['Andrew Lubega'] = '(925) 727-4611'
andrew_member['Mallick Abdullah'] = '(510) 409-8755' 
andrew_member['Ronin Youngjones'] = '(415) 910-3415'
andrew_member['Glenn Ivory'] = '(510) 328-8290'

richard_member['Richard Kamu'] = '000-000-0000'
richard_member['Matthew Dudley'] = '000-000-0000'
richard_member['Kymari Rhodes'] = '000-000-0000'
richard_member['Josiah Johnson'] = '000-000-0000'

gaberiel_member['Gaberiel Reader'] = '000-000-0000'
gaberiel_member['Emmanuel Tobor'] = '000-000-0000'
gaberiel_member['David Brickly'] = '000-000-0000'
gaberiel_member['Myles Wilkerson'] = '000-000-0000'

aris_member['Aris Carter'] = '000-000-0000'
aris_member['Maurice Richardson'] = '000-000-0000'
aris_member['Zyion Williams'] = '000-000-0000'
aris_member['Hyab Isayas'] = '000-000-0000'
aris_member['Milan Kral'] = '000-000-0000'

jacore_leader['Jacore'] = jacore_member
andrew_leader['Andrew'] = andrew_member
aris_leader['Aris'] = aris_member
richard_leader['Richard'] = richard_member
gaberiel_leader['Gaberiel'] = gaberiel_member

instructor['Baba'] = jacore_leader
instructor["Hodari"] = andrew_leader
instructor["David"] = aris_leader
instructor["Paris"] = gaberiel_leader
instructor["Akeem"] = richard_leader
#print(instructor)

for instructor, pod_leader in instructor.items():
    print("instructor:", instructor)
    
    for pod_leader, pod_member in pod_leader.items():
        print("pod_leader:", pod_leader)
        for pod_member, phone_number in pod_member.items():
            
            print(pod_member, phone_number);
    print("\n")




