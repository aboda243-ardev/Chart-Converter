import json
import math
import os
import re



dir = "json files"
dirs = os.walk(dir)
outdir = "export"
if not os.path.exists(dir):
    os.mkdir(dir)
if not os.path.exists(outdir):
    os.mkdir(outdir)
# def split_funcs(file,func):
#     IF = False
#     IIF = False
#     word = ""
#     rec = False
#     for l in file7
flip = True
keys = 4
map_to = 0 # leave 0 if no map
allowed_strings = [[1,2],[2,3]] #set to 0 for nothing, set to 1 for everything

def sort_values(array,i):
    ar = array
    ea = []
    fin = False
    # ea.append(ar[0])
    for t in ar:
        fin = False
        for j in ea:
            if t[i] < j[i] :
                ea.insert(ea.index(j),t)
                fin = True
                break
        if fin == False:
            ea.insert(len(ea)+1, t)

    return ea



for files in dirs:
    for file in files[2]:
        print("file name : " + file)
        if file.endswith(".json"):
            with open(f"{dir}/{file}") as jsonf:
                JF = json.load(jsonf)
                song = JF['song']
                bpm = song["bpm"]
                songN = song["song"]
                songS = song["speed"]
                print("song name : " + str(songN))
                print("speed : " + str(songS))
                print("bpm : " + str(bpm))
                notes = song['notes']
                # songNotes = []
                # for i in range(len(notes)):
                #     for n in notes[i]['sectionNotes']:
                #         songNotes.append(n)
                #
                # songNotes = sort_values(songNotes,0)
                # print(songNotes)
                chart = []
                start = 0
                for i in range(len(notes)):
                    songNotes = notes[i]['sectionNotes']
                    songNotes = sort_values(songNotes, 0)
                    start = int(start + (((60 / bpm) * 4) * 1000) * (i > 0))
                    try:
                        if notes[i]["changeBPM"] == True:
                            bpm = notes[i]["bpm"]
                    except:
                        pass

                    cam = notes[i]['mustHitSection'] * 1
                    chart.append(str("#" + str(cam) + "-" + str(round(start))))
                    try :

                        for n in songNotes:


                            if flip == True :
                                if map_to == 0 :
                                    if math.fmod(n[1],keys*2) < keys :
                                         ty = n[1] + (keys * cam)
                                    else:
                                         ty = n[1] - (keys * cam)
                                else:
                                    if math.fmod(n[1],keys*2) < keys :
                                         ty = math.fmod(n[1],map_to) + (map_to * cam)
                                    else:
                                         ty = math.fmod(n[1]-keys, map_to) + map_to
                            else :
                                if map_to == 0 :
                                    ty = n[1]
                                else :
                                    if math.fmod(n[1],keys*2) < keys:
                                        ty = math.fmod(n[1],map_to)
                                    else:
                                        ty = math.fmod(n[1]-keys, map_to) + map_to

                            try:
                                if re.search('[a-zA-Z]', str(n[2])) == None:
                                    if not isinstance(allowed_strings, int):
                                        for v in allowed_strings :

                                            if n[3] == v[0]:
                                                ty += (keys*2) * (v[1] - 1)
                                                break


                            except: pass
                            char = str("?" + str(round(n[0])) + "_" + str(ty) + "_" + str(round(n[2])))
                            try :
                                if n[3] == "Spinel" or n[3] ==  "GF Sing" or n[3] == "GF Glitch":
                                    char = char + ":1"
                                elif n[3] == "BO":
                                    char = char + ":2"
                            except : pass
                            if re.search('[a-zA-Z]', str(n[2])) == None:

                                if isinstance(allowed_strings,int) :
                                    if allowed_strings == 0:
                                        if re.search('[a-zA-Z]', str(n[3])) == None:
                                            chart.append(char)

                                    else :
                                        chart.append(char)

                                else:
                                    chart.append(char)




                    except: pass
                out = ""
                for l in chart:
                    out = out + str(l) + "\n"
            letter = len(file) - len(".json")
            name = file[0:letter] + ".txt"
            fi = open(f"{outdir}/{name}","w+")
            fi.write(out)
            fi.close



