import sys 
import re
from os import system

scriptnum = 0

def file_len(fname):
    with open(fname) as b:
        for i, l in enumerate(b):
            pass
    return i + 1

if sys.argv[1] > 0:
	scriptnum = sys.argv[1]
#o = open(newfile,"w")
#f = open(sys.argv[1],'r')

try:
   with open(str(scriptnum) + ".qst") as f: pass
except IOError as e:
   print 'Oh dear.'
 
f = open(str(scriptnum) + ".qst",'r')
FINAL = open(str(scriptnum) + ".lua",'a')
brackets = 0
in_event = False
lines_read = 0

SAY = False
AGGROSAY = False
SPAWN = False
SCRIPT = False
ITEM = False
TRIGGERALL = False
SIGNAL = False
COMBATEND = False
DEATH = False
HP = False
SLAY = False
SPELL = False
ATTACK = False
uses_buffID = False
uses_calc = False	
uses_hasitem = False
uses_script_status = False
uses_substring_1 = False
uses_substring_0 = False
uses_substring_2 = False
uses_substring_3 = False
uses_substring_4 = False
uses_substring_5 = False
uses_substring_6 = False
uses_substring_7 = False
uses_substring_8 = False
uses_substring_9 = False
uses_sex = False
uses_sex2 = False
uses_sex3 = False
uses_sex4 = False
uses_npc_count = False
uses_EVENT_HP = False
uses_EVENT_SCRIPT = False
uses_EVENT_TRIGGERALL = False
uses_EVENT_SAY = False
uses_EVENT_AGGROSAY = False
uses_primarytarget = False
uses_randtarget = False
uses_auxtarget = False
uses_highestdamage = False
uses_highestheals = False
uses_lowesttarget = False
uses_ramptarget = False
uses_meleetarget = False
uses_auxmeleetarget = False
uses_fartarget = False
uses_lostarget = False
uses_nolostarget = False
uses_getdmghate = False	
uses_hatesizetotal = False
uses_hatesizeclients = False
uses_npccorpse_count = False
uses_clientcount = False
	
g = open(str(scriptnum) + ".qst",'r')

for s in g:
	if "$buffID" in s:
		uses_buffID = True
	if "$hasitem" in s:
		uses_hasitem = True
	if "$script_status" in s:
		uses_script_status = True
	if "$substring(0)" in s or "setsubstring(0" in s:
		uses_substring_0 = True
	if "$substring(1)" in s or "setsubstring(1" in s:
		uses_substring_1 = True
	if "$substring(2)" in s or "setsubstring(2" in s:
		uses_substring_2 = True
	if "$substring(3)" in s or "setsubstring(3" in s:
		uses_substring_3 = True
	if "$substring(4)" in s or "setsubstring(4" in s:
		uses_substring_4 = True
	if "$substring(5)" in s or "setsubstring(5" in s:
		uses_substring_5 = True
	if "$substring(6)" in s or "setsubstring(6" in s:
		uses_substring_6 = True
	if "$substring(7)" in s or "setsubstring(7" in s:
		uses_substring_7 = True
	if "$substring(8)" in s or "setsubstring(8" in s:
		uses_substring_8 = True
	if "$substring(9)" in s or "setsubstring(9" in s:
		uses_substring_9 = True
	if "$sex " in s:
		uses_sex = True
	if "$sex2" in s:
		uses_sex2 = True
	if "$sex3" in s:
		uses_sex3 = True
	if "$sex4" in s:
		uses_sex4 = True
	if "$npc_count" in s:
		uses_npc_count = True
	if "EVENT_HP" in s:
		uses_EVENT_HP = True
	if "EVENT_SCRIPT" in s:
		uses_EVENT_SCRIPT = True
	if "EVENT_TRIGGERALL" in s:
		uses_EVENT_TRIGGERALL = True
	if "$primarytarget" in s:
		uses_primarytarget = True
	if "$randtarget" in s:
		uses_randtarget = True
	if "$auxtarget" in s:
		uses_auxtarget = True
	if "$highestdamage" in s:
		uses_highestdamage = True
	if "$highestheals" in s:
		uses_highestheals = True
	if "$lowesttarget" in s:
		uses_lowesttarget = True
	if "$ramptarget" in s:
		uses_ramptarget = True
	if "$meleetarget" in s:
		uses_meleetarget = True
	if "$auxmeleetarget" in s:
		uses_auxmeleetarget = True
	if "$fartarget" in s:
		uses_fartarget = True
	if "$lostarget" in s:
		uses_lostarget = True
	if "$nolostarget" in s:
		uses_nolostarget = True
	if "$getdmghate" in s:
		uses_getdmghate = True	
	if "$hatesizetotal" in s:
		uses_hatesizetotal = True
	if "$hatesizeclients" in s:
		uses_hatesizeclients = True
	if "$npccorpse_count" in s:
		uses_npccorpse_count = True
	if "$clientcount" in s:
		uses_clientcount = True


g.close()

for line in f:
	if not in_event and brackets < 1:
		if re.search(r'^EVENT',line):
			in_event = True
			name_start = re.search("_", line).start() + 1
			bracket_on_event_line = re.search("{",line)
			if bracket_on_event_line:
				brackets = 1
			else:
				brackets = 0
			name_end = re.search('[^a-zA-z]',line).start()
			if name_end:
				event_tag = line[name_start:name_end]
			else:
				event_tag = line[name_start:]
			#print event_tag
			if event_tag == "SAY":
				SAY = True
			if event_tag == "SCRIPT":
				SCRIPT = True
			if event_tag == "SPAWN":
				SPAWN = True
			if event_tag == "ITEM":
				ITEM = True
			if event_tag == "SIGNAL":
				SIGNAL = True
			if event_tag == "TRIGGERALL":
				TRIGGERALL = True
			if event_tag == "COMBATEND":
				COMBATEND = True
			if event_tag == "HP":
				HP = True
			if event_tag == "AGGROSAY":
				AGGROSAY = True
			if event_tag == "SLAY":
				SLAY = True
			if event_tag == "SPELL":
				SPELL = True
			if event_tag == "DEATH":
				DEATH = True
			if event_tag == "ATTACK":
				ATTACK = True
			lines_read = lines_read + 1
			newfile = str(scriptnum) + event_tag + ".tmp"
			N = open(newfile,"w")
			N.write("EVENT_" + event_tag + " {\n")
			if event_tag == "SPAWN" and uses_EVENT_HP:
				N.write("hptrigger(90);" + "\n")
				
	else:
		if brackets > 0 or lines_read < 3:
			if re.search('{',line):
				brackets = brackets + 1
			if re.search('}',line):
				brackets = brackets - 1
			lines_read = lines_read + 1
			if lines_read == 2 and not bracket_on_event_line:
				r = line.find('{')
				N.write(line[r+1:].lstrip())
			else:
				if line.lstrip()[:1] == "{":
					N.write("{" + "\n" + line.lstrip()[2:])
				else:
					N.write(line.lstrip())
		if brackets == 0 and lines_read >= 3:
			in_event = False
			lines_read = 0
			N.close()

try:
   with open(str(scriptnum) + 'SPAWN' + ".tmp") as SPAWN: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_SPAWN"
 
if SPAWN:
	system("handle_event.py " + scriptnum + " SPAWN")
	l = open(str(scriptnum) + 'SPAWN' + ".out",'r')
	for line in l:
		FINAL.write(line)
elif uses_EVENT_HP:
	FINAL.write("function EVENT_SPAWN(self)" + "\n")
	FINAL.write("\t" + "self:hptrigger(90)" + "\n")
	FINAL.write("end" + "\n" + "\n")
	
try:
   with open(str(scriptnum) + 'SCRIPT' + ".tmp") as SCRIPT: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_SCRIPT"
 
if SCRIPT:
	system("handle_event.py " + scriptnum + " SCRIPT")
	size = file_len(str(scriptnum) + 'SCRIPT' + ".out")
	l = open(str(scriptnum) + 'SCRIPT' + ".out",'r')
	if not uses_EVENT_TRIGGERALL:
		for line in l:
			FINAL.write(line)
	else:
		print "BOTH script AND trigger"
		lines_read = 0
		for line in l:
			if lines_read < size-2:
				FINAL.write(line)
			lines_read = lines_read + 1
		
try:
   with open(str(scriptnum) + 'TRIGGERALL' + ".tmp") as TRIGGERALL: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_TRIGGERALL"
 
if TRIGGERALL:
	system("handle_event.py " + scriptnum + " TRIGGERALL")
	size = file_len(str(scriptnum) + 'TRIGGERALL' + ".out")
	l = open(str(scriptnum) + 'TRIGGERALL' + ".out",'r')
	if not uses_EVENT_SCRIPT:
		for line in l:
			FINAL.write(line)
	else:
		print "BOTH script AND trigger"
		lines_read = 0
		for line in l:
			if lines_read > 0 and lines_read < size:
				FINAL.write(line)
			lines_read = lines_read + 1
		
try:
   with open(str(scriptnum) + 'SAY' + ".tmp") as SAY: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_SAY"
 
if SAY:
	system("handle_event.py " + scriptnum + " SAY")
	l = open(str(scriptnum) + 'SAY' + ".out",'r')
	if not uses_EVENT_AGGROSAY:
		for line in l:
			FINAL.write(line)
	else:
		print "BOTH say AND aggro"
		lines_read = 0
		for line in l:
			if lines_read > 0 and lines_read < size:
				FINAL.write(line)
			lines_read = lines_read + 1

try:
   with open(str(scriptnum) + 'AGGROSAY' + ".tmp") as AGGROSAY: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_AGGROSAY"
 
if AGGROSAY:
	system("handle_event.py " + scriptnum + " AGGROSAY")
	l = open(str(scriptnum) + 'AGGROSAY' + ".out",'r')
	if not uses_EVENT_SAY:
		for line in l:
			FINAL.write(line)
	else:
		print "BOTH say AND aggro"
		lines_read = 0
		for line in l:
			if lines_read > 0 and lines_read < size:
				FINAL.write(line)
			lines_read = lines_read + 1

try:
   with open(str(scriptnum) + 'ITEM' + ".tmp") as ITEM: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_ITEM"
 
if ITEM:
	system("handle_event.py " + scriptnum + " ITEM")
	l = open(str(scriptnum) + 'ITEM' + ".out",'r')
	for line in l:
		FINAL.write(line)
		
try:
   with open(str(scriptnum) + 'SIGNAL' + ".tmp") as SIGNAL: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_SIGNAL"
 
if SIGNAL:
	system("handle_event.py " + scriptnum + " SIGNAL")
	l = open(str(scriptnum) + 'SIGNAL' + ".out",'r')
	for line in l:
		FINAL.write(line)

try:
   with open(str(scriptnum) + 'COMBATEND' + ".tmp") as COMBATEND: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_COMBATEND"
 
if COMBATEND:
	system("handle_event.py " + scriptnum + " COMBATEND")
	l = open(str(scriptnum) + 'COMBATEND' + ".out",'r')
	for line in l:
		FINAL.write(line)

try:
   with open(str(scriptnum) + 'HP' + ".tmp") as HP: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_HP"
 
if HP:
	system("handle_event.py " + scriptnum + " HP")
	l = open(str(scriptnum) + 'HP' + ".out",'r')
	for line in l:
		FINAL.write(line)

try:
   with open(str(scriptnum) + 'DEATH' + ".tmp") as DEATH: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_DEATH"
 
if DEATH:
	system("handle_event.py " + scriptnum + " DEATH")
	l = open(str(scriptnum) + 'DEATH' + ".out",'r')
	for line in l:
		FINAL.write(line)

try:
   with open(str(scriptnum) + 'ATTACK' + ".tmp") as ATTACK: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_ATTACK"
 
if ATTACK:
	system("handle_event.py " + scriptnum + " ATTACK")
	l = open(str(scriptnum) + 'ATTACK' + ".out",'r')
	for line in l:
		FINAL.write(line)

try:
   with open(str(scriptnum) + 'SLAY' + ".tmp") as SLAY: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_SLAY"
 
if SLAY:
	system("handle_event.py " + scriptnum + " SLAY")
	l = open(str(scriptnum) + 'SLAY' + ".out",'r')
	for line in l:
		FINAL.write(line)

try:
   with open(str(scriptnum) + 'SPELL' + ".tmp") as SPELL: pass
except IOError as e:
   print str(scriptnum) + " has no EVENT_SPELL"
 
if SPELL:
	system("handle_event.py " + scriptnum + " SPELL")
	l = open(str(scriptnum) + 'SPELL' + ".out",'r')
	for line in l:
		FINAL.write(line)

if uses_buffID:
	FINAL.write("function HasBuff(mob,spell_id)" + "\n")
	FINAL.write("\t" + "bl = mob:GetBuffs(\"spellid\")" + "\n")
	FINAL.write("\t" + "for k,v in pairs(bl) do" + "\n")
	FINAL.write("\t" + "\t" + "if v = spell_id then" + "\n")
	FINAL.write("\t" + "\t" + "\t" + "return true" + "\n")
	FINAL.write("\t" + "\t" + "end" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("\t" + "return false" + "\n")
	FINAL.write("end" + "\n")

if uses_hasitem:
	FINAL.write("function HasItem(mob,item_id)" + "\n")
	FINAL.write("\t" + "inv = mob:GetInventory()" + "\n")
	FINAL.write("\t" + "for k,v in pairs(inv) do" + "\n")
	FINAL.write("\t" + "\t" + "if GetItemID(v) = item_id then" + "\n")
	FINAL.write("\t" + "\t" + "\t" + "return 1" + "\n")
	FINAL.write("\t" + "\t" + "end" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("\t" + "return 0" + "\n")
	FINAL.write("end" + "\n")

if uses_script_status:
	FINAL.write("script_status = 0" + "\n")

if uses_substring_0:
	FINAL.write("substring_0 = nil" + "\n")

if uses_substring_1:
	FINAL.write("substring_1 = nil" + "\n")

if uses_substring_2:
	FINAL.write("substring_2 = nil" + "\n")

if uses_substring_3:
	FINAL.write("substring_3 = nil" + "\n")

if uses_substring_4:
	FINAL.write("substring_4 = nil" + "\n")

if uses_substring_5:
	FINAL.write("substring_5 = nil" + "\n")

if uses_substring_6:
	FINAL.write("substring_6 = nil" + "\n")

if uses_substring_7:
	FINAL.write("substring_7 = nil" + "\n")

if uses_substring_8:
	FINAL.write("substring_8 = nil" + "\n")

if uses_substring_9:
	FINAL.write("substring_9 = nil" + "\n")

if uses_sex:
	FINAL.write("function sex(self)" + "\n")
	FINAL.write("\t" + "if self:GetGender() == 0 then return \"he\"" + "\n")
	FINAL.write("\t" + "elseif self:GetGender() == 1 then return \"she\"" + "\n")
	FINAL.write("\t" + "else return \"it\"" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("end" + "\n")

if uses_sex2:
	FINAL.write("function sex2(self)" + "\n")
	FINAL.write("\t" + "if self:GetGender() == 0 then return \"his\"" + "\n")
	FINAL.write("\t" + "elseif self:GetGender() == 1 then return \"her\"" + "\n")
	FINAL.write("\t" + "else return \"its\"" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("end" + "\n")

if uses_sex3:
	FINAL.write("function sex(self)" + "\n")
	FINAL.write("\t" + "if self:GetGender() == 0 then return \"him\"" + "\n")
	FINAL.write("\t" + "elseif self:GetGender() == 1 then return \"her\"" + "\n")
	FINAL.write("\t" + "else return \"it\"" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("end" + "\n")

if uses_sex4:
	FINAL.write("function sex(self)" + "\n")
	FINAL.write("\t" + "if self:GetGender() == 0 then return \"man\"" + "\n")
	FINAL.write("\t" + "elseif self:GetGender() == 1 then return \"woman\"" + "\n")
	FINAL.write("\t" + "else return \"thing\"" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("end" + "\n")

if uses_npc_count:
	FINAL.write("function NPCCount(npc_id)" + "\n")
	FINAL.write("\t" + "count = 0" + "\n")
	FINAL.write("\t" + "nl = GetNPCList()" + "\n")
	FINAL.write("\t" + "for k,v in pairs(nl) do" + "\n")
	FINAL.write("\t" + "\t" + "if GetNPCID(v) == npc_id then" + "\n")
	FINAL.write("\t" + "\t" + "\t" + "count = count + 1" + "\n")
	FINAL.write("\t" + "\t" + "end" + "\n")
	FINAL.write("\t" + "end" + "\n")
	FINAL.write("\t" + "return count" + "\n")
	FINAL.write("end" + "\n")

if uses_primarytarget:
	FINAL.write("function primarytarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("dl = GetHateList(self,\"hate\")" + "\n")
	FINAL.write("max_index = 1" + "\n")
	FINAL.write("max_hate = 0" + "\n")
	FINAL.write("for k,v in pairs(dl) do" + "\n")
	FINAL.write("if v > max_hate then" + "\n")
	FINAL.write("max_hate = v" + "\n")
	FINAL.write("max_index = k" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return hl[k]" + "\n")
	FINAL.write("end" + "\n")

if uses_randtarget:
	FINAL.write("function randtarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("return hl[math.random(#hl)]" + "\n")
	FINAL.write("end" + "\n")

if uses_auxtarget:
	FINAL.write("function auxtarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("if #hl == 1 then " + "\n")
	FINAL.write("return hl[1] " + "\n")
	FINAL.write("else" + "\n")
	FINAL.write("return_index = 0" + "\n")
	FINAL.write("dl = GetHateList(self,\"hate\")" + "\n")
	FINAL.write("max_index = 1" + "\n")
	FINAL.write("max_hate = 0" + "\n")
	FINAL.write("for k,v in pairs(dl) do" + "\n")
	FINAL.write("if v > max_hate then" + "\n")
	FINAL.write("max_hate = v" + "\n")
	FINAL.write("max_index = k" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("repeat" + "\n")
	FINAL.write("return_index = math.random(#hl)" + "\n")
	FINAL.write("until return_index ~= max_index" + "\n")
	FINAL.write("return hl[return_index]" + "\n")
	FINAL.write("end" + "\n")

if uses_highestdamage:
	FINAL.write("function highestdamage(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("dl = GetHateList(self,\"damage\")" + "\n")
	FINAL.write("max_index = 1" + "\n")
	FINAL.write("max_dmg = 0" + "\n")
	FINAL.write("for k,v in pairs(dl) do" + "\n")
	FINAL.write("if v > max_hdmg then" + "\n")
	FINAL.write("max_hdmg = v" + "\n")
	FINAL.write("max_index = k" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return hl[k]" + "\n")
	FINAL.write("end" + "\n")

if uses_highestheals:
	FINAL.write("function highestheals(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"healing\")" + "\n")
	FINAL.write("dl = GetHateList(self,\"damage\")" + "\n")
	FINAL.write("max_index = 1" + "\n")
	FINAL.write("max_dmg = 0" + "\n")
	FINAL.write("for k,v in pairs(dl) do" + "\n")
	FINAL.write("if v > max_hdmg then" + "\n")
	FINAL.write("max_hdmg = v" + "\n")
	FINAL.write("max_index = k" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return hl[k]" + "\n")
	FINAL.write("end" + "\n")

if uses_lowesttarget:
	FINAL.write("function lowesttarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("dl = GetHateList(self,\"hate\")" + "\n")
	FINAL.write("min_index = 1" + "\n")
	FINAL.write("min_hate = 2000000000" + "\n")
	FINAL.write("for k,v in pairs(dl) do" + "\n")
	FINAL.write("if v < min_hate then" + "\n")
	FINAL.write("min_hate = v" + "\n")
	FINAL.write("min_index = k" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return hl[k]" + "\n")
	FINAL.write("end" + "\n")

if uses_ramptarget:
	FINAL.write("function ramptarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if k > 1 then" + "\n")
	FINAL.write("if InCombatRange(self,v) then" + "\n")
	FINAL.write("return v" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return hl[1]" + "\n")
	FINAL.write("end" + "\n")

if uses_meleetarget:
	FINAL.write("function meleetarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("candidates = {}" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if InCombatRange(self,v) then" + "\n")
	FINAL.write("table.insert(candidates,v)" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("if #candidates < 1 then return hl[1] end" + "\n")
	FINAL.write("return candidates[math.random(#candidates)]" + "\n")
	FINAL.write("end" + "\n")

if uses_auxmeleetarget:
	FINAL.write("function auxmeleetarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("candidates = {}" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if k > 1 then" + "\n")
	FINAL.write("if InCombatRange(self,v) then" + "\n")
	FINAL.write("table.insert(candidates,v)" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("if #candidates < 1 then return hl[1] end" + "\n")
	FINAL.write("return candidates[math.random(#candidates)]" + "\n")
	FINAL.write("end" + "\n")

if uses_fartarget:
	FINAL.write("function fartarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("candidates = {}" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if not InCombatRange(self,v) then" + "\n")
	FINAL.write("table.insert(candidates,v)" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("if #candidates < 1 then return -2 end" + "\n")
	FINAL.write("return candidates[math.random(#candidates)]" + "\n")
	FINAL.write("end" + "\n")

if uses_lostarget:
	FINAL.write("function lostarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("candidates = {}" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if InLos(self,v) then" + "\n")
	FINAL.write("table.insert(candidates,v)" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("if #candidates < 1 then return hl[1] end" + "\n")
	FINAL.write("return candidates[math.random(#candidates)]" + "\n")
	FINAL.write("end" + "\n")

if uses_nolostarget:
	FINAL.write("function nolostarget(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("candidates = {}" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if not InLos(self,v) then" + "\n")
	FINAL.write("table.insert(candidates,v)" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("if #candidates < 1 then return hl[1] end" + "\n")
	FINAL.write("return candidates[math.random(#candidates)]" + "\n")
	FINAL.write("end" + "\n")

if uses_getdmghate:	
	FINAL.write("function getdmghate(self,other)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("dl = GetHateList(self,\"damage\")" + "\n")
	FINAL.write("return_index = 1" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if v == other then" + "\n")
	FINAL.write("return_index = k" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return dl[k]" + "\n")
	FINAL.write("end" + "\n")

if uses_hatesizetotal:
	FINAL.write("function hatesizetotal(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("return #hl" + "\n")
	FINAL.write("end" + "\n")

if uses_hatesizeclients:
	FINAL.write("function hatesizeclients(self)" + "\n")
	FINAL.write("hl = GetHateList(self,\"entity\")" + "\n")
	FINAL.write("clients = {}" + "\n")
	FINAL.write("for k,v in pairs(hl) do" + "\n")
	FINAL.write("if IsClient(v) then" + "\n")
	FINAL.write("table.insert(clients,v)" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return #clients" + "\n")
	FINAL.write("end" + "\n")

if uses_npccorpse_count:
	FINAL.write("function npccorpse_count(npcid)" + "\n")
	FINAL.write("cl = GetCorpseList()" + "\n")
	FINAL.write("total = 0" + "\n")
	FINAL.write("for k,v in pairs(nl) do" + "\n")
	FINAL.write("if GetNPCID(v) == npcid then" + "\n")
	FINAL.write("total = total + 1" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("end" + "\n")
	FINAL.write("return total" + "\n")
	FINAL.write("end" + "\n")

if uses_clientcount:
	FINAL.write("function clientcount()" + "\n")
	FINAL.write("return #GetClientList()" + "\n")
	FINAL.write("end" + "\n")

		
# for if:
# new_line = line[0:line.find('(')] + line[line.find('(')+ 1:line.find(')') + line[line.find(')') + 1:] + ' then'

	
	
	
	
	
	
	