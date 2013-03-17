import sys 
import re
from itertools import tee, izip
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)
scriptnum = sys.argv[1]
EVENT = sys.argv[2]
#o = open(newfile,"w")
#f = open(sys.argv[1],'r')
qst_funcs = ['if','elseif','msg','dialog','gobind','break','summonitem','setflag','journal','lawpoints','chaospoints','removeitem','cleardebt','emote','msgnote','newbindpoint','}']
qst_vars = ['1-','flag','race','class','uclass','urace','deity']
target_loc = {'adjusthate':0,'aggro':0,'aggrotarget':0,'castspell':1,'casttime':2,'customhit':7,'customhitother':9,'customnuke':8,'customspell':10,'customtextother':0,'doattack':0,'doattackround':0,'drainhp':1,'drainmana':1,'loadpet':2,'losecontrol':3,'mobidcast':1,'purgetargetbufftype':1,'sethate':0,'stun':1,'summontarget':0,'swaphate':0,'unresistablestun':1,'killpc':0,'playercast':1}
var_tars = {'auxmeleetarget(self)','auxtarget(self)','fartarget(self)','getowner','highestdamage(self)','lostarget(self)','lowesttarget(self)','meleetarget(self)','nolostarget(self)','petid','primarytarget(self)','ramptarget(self)','randtarget(self)','selfid','userid','substring_0','substring_1','substring_2','substring_3','substring_4','substring_5','substring_6','substring_7','substring_8','substring_9'}
flag_funcs = ['flagmove','flaglastnpc','walktoflag','runtoflag','followflag','assault','assaultnorandom']
f = open(str(scriptnum) + EVENT + ".tmp",'r')
g = open(str(scriptnum) + EVENT + ".tmp",'r')
temp_report = open("FUNCTIONS.TXT",'a')
outfile = open(str(scriptnum) + EVENT + ".out",'a')
brackets = 0
in_event = False
lines_read = 0
tabs = 0
uses_chance = False
uses_bchance = False
uses_cchance = False
uses_dchance = False
updates_script = False
updates_s0 = False
updates_s1 = False
updates_s2 = False
updates_s3 = False
updates_s4 = False
updates_s5 = False
updates_s6 = False
updates_s7 = False
updates_s8 = False
updates_s9 = False
up_script = False
up_s0 = False
up_s1 = False
up_s2 = False
up_s3 = False
up_s4 = False
up_s5 = False
up_s6 = False
up_s7 = False
up_s8 = False
up_s9 = False
for line in g:
	if "$chance" in line:
		uses_chance = True
	if "$bchance" in line:
		uses_bchance = True
	if "$cchance" in line:
		uses_cchance = True
	if "$dchance" in line:
		uses_dchance = True
	if "scriptstatus(" in line:
		up_script = True
	if "setsubstring(0" in line:
		up_s0 = True
	if "setsubstring(1" in line:
		up_s1 = True
	if "setsubstring(2" in line:
		up_s2 = True
	if "setsubstring(3" in line:
		up_s3 = True
	if "setsubstring(4" in line:
		up_s4 = True
	if "setsubstring(5" in line:
		up_s5 = True
	if "setsubstring(6" in line:
		up_s6 = True
	if "setsubstring(7" in line:
		up_s7 = True
	if "setsubstring(8" in line:
		up_s8 = True
	if "setsubstring(9" in line:
		up_s9 = True
g.close()
g = open(str(scriptnum) + EVENT + ".tmp",'r')
for line in g:
	if up_script and "$script_status" in line:
		updates_script = True
	if up_s0 and "$substring(0" in line:
		updates_s0 = True
	if up_s0 and "$substring(1" in line:
		updates_s1 = True
	if up_s0 and "$substring(2" in line:
		updates_s2 = True
	if up_s0 and "$substring(3" in line:
		updates_s3 = True
	if up_s0 and "$substring(4" in line:
		updates_s4 = True
	if up_s0 and "$substring(5" in line:
		updates_s5 = True
	if up_s0 and "$substring(6" in line:
		updates_s6 = True
	if up_s0 and "$substring(7" in line:
		updates_s7 = True
	if up_s0 and "$substring(8" in line:
		updates_s8 = True
	if up_s0 and "$substring(9" in line:
		updates_s9 = True
g.close()
def do_vars(s):
	s = s.replace("&&","and")
	s = re.sub(r'\$1\- =~[^"]*(".*")', r'string.find(words,string.lower(\1))', s)
	s = s.replace("$flag","other:GetFlag")
	s = re.sub(r'\$random\((\d+)\)', r'math.random(\1) - 1', s)
	if updates_s0:
		s = s.replace("$substring(0)","check_substring_0")
	if updates_s1:
		s = s.replace("$substring(1)","check_substring_1")
	if updates_s2:
		s = s.replace("$substring(2)","check_substring_2")
	if updates_s3:
		s = s.replace("$substring(3)","check_substring_3")
	if updates_s4:
		s = s.replace("$substring(4)","check_substring_4")
	if updates_s5:
		s = s.replace("$substring(5)","check_substring_5")
	if updates_s6:
		s = s.replace("$substring(6)","check_substring_6")
	if updates_s7:
		s = s.replace("$substring(7)","check_substring_7")
	if updates_s8:
		s = s.replace("$substring(8)","check_substring_8")
	if updates_s9:
		s = s.replace("$substring(9)","check_substring_9")
	s = s.replace("$substring(0)","substring_0")
	s = s.replace("$substring(1)","substring_1")
	s = s.replace("$substring(2)","substring_2")
	s = s.replace("$substring(3)","substring_3")
	s = s.replace("$substring(4)","substring_4")
	s = s.replace("$substring(5)","substring_5")
	s = s.replace("$substring(6)","substring_6")
	s = s.replace("$substring(7)","substring_7")
	s = s.replace("$substring(8)","substring_8")
	s = s.replace("$substring(9)","substring_9")
	s = s.replace("NULL","nil")
	s = s.replace("$ustat(MR)","other:GetStat(\"mr\")")
	s = s.replace("$ustat(FR)","other:GetStat(\"fr\")")
	s = s.replace("$ustat(CR)","other:GetStat(\"cr\")")
	s = s.replace("$ustat(PR)","other:GetStat(\"pr\")")
	s = s.replace("$ustat(DR)","other:GetStat(\"dr\")")
	s = s.replace("$urace","other:GetRace()")
	s = s.replace("$uclass","other:GetClass()")
	s = s.replace("$userid","GetID(other)")
	s = s.replace("$deity","other:GetStat(\"deity\")")
	s = s.replace("$spellid","spellid")
	s = s.replace("$race","other:GetRaceName()")
	s = s.replace("$faction","other:GetCon(self)")
	s = s.replace("$name","other:GetName()")
	s = s.replace("$mname","self:GetName()")
	s = s.replace("$ulevel","other:GetLevel()")
	s = s.replace("$zoneid","GetZoneID()")
	s = s.replace("$ssex","other:GetGender()")
	s = s.replace("$udist","self:GetDist(other)")
	s = s.replace("$npc_count","NPCCount")
	s = s.replace("$locx","other:GetX()")
	s = s.replace("$locy","other:GetY()")
	s = s.replace("$locz","other:GetZ()")
	s = s.replace("$npc_locx","self:GetX()")
	s = s.replace("$npc_locy","self:GetY()")
	s = s.replace("$npc_locz","self:GetZ()")
	s = s.replace("$global(","GetGlobal(")
	s = s.replace("$signal","tonumber(signal)")
	s = s.replace("$eventratio","self:GetHPTrigger()")
	s = s.replace("$hpratio","self:GetStat(\"hpratio\")")
	if updates_script:
		s = s.replace("$script_status","check_script_status")
	s = s.replace("$script_status","script_status")
	s = s.replace("$primarytarget","primarytarget(self)")
	s = s.replace("$randtarget","randtarget(self)")
	s = s.replace("$auxtarget","auxtarget(self)")
	s = s.replace("$highestdamage","highestdamage(self)")
	s = s.replace("$lowesttarget","lowesttarget(self)")
	s = s.replace("$ramptarget","ramptarget(self)")
	s = s.replace("$meleetarget","meleetarget(self)")
	s = s.replace("$auxmeleetarget","auxmeleetarget(self)")
	s = s.replace("$fartarget","fartarget(self)")
	s = s.replace("$lostarget","lostarget(self)")
	s = s.replace("$nolostarget","nolostarget(self)")
	s = s.replace("$getdmghate","getdmghate(self)")
	s = s.replace("$hatesizetotal","hatesizetotal(self)")
	s = s.replace("$hatesizeclients","hatesizeclients(self)")
	s = s.replace("$npccorpse_count(","npccorpse_count(")
	s = s.replace("$clientcount","clientcount(self)")
	s = s.replace("$itemcount","items_table")
	s = s.replace("$hasitem(","HasItem(other,")
	s = s.replace("$casting == 0","not self:IsCasting()")
	s = s.replace("$battle == 0","not self:InCombat()")
	s = s.replace("$casting == 1","self:IsCasting()")
	s = s.replace("$battle == 1","self:InCombat()")
	s = s.replace("$combatrange == 1","self:InCombatRange(other)")
	s = s.replace("$combatrange == 0","not self:InCombatRange(other)")
	s = s.replace("$fighting == 0","not self:InCombat()")
	s = s.replace("$fighting == 1","self:InCombat()")
	s = re.sub(r'\$buffID\((\d+)\) == 1', r'HasBuff(other,\1)', s)
	s = re.sub(r'\$buffID\((\d+)\) == 0', r'not HasBuff(other,\1)', s)
	return s
def do_msg_vars(s):
	s = s.replace("$ustat(MR)","other:GetStat(\"mr\")")
	s = s.replace("$ustat(FR)","other:GetStat(\"fr\")")
	s = s.replace("$ustat(CR)","other:GetStat(\"cr\")")
	s = s.replace("$ustat(PR)","other:GetStat(\"pr\")")
	s = s.replace("$ustat(DR)","other:GetStat(\"dr\")")
	s = s.replace("$substring(0)","substring_0")
	s = s.replace("$substring(1)","substring_1")
	s = s.replace("$substring(2)","substring_2")
	s = s.replace("$substring(3)","substring_3")
	s = s.replace("$substring(4)","substring_4")
	s = s.replace("$substring(5)","substring_5")
	s = s.replace("$substring(6)","substring_6")
	s = s.replace("$substring(7)","substring_7")
	s = s.replace("$substring(8)","substring_8")
	s = s.replace("$substring(9)","substring_9")
	s = re.sub(r'\$calc\((.+)\)', r'" .. \1 .. "', s)
	s = re.sub(r'\$flag\((\d+)\)', r'" .. other:GetFlag(\1) .. "', s)
	s = s.replace("$sex ","\" .. sex() .. \"")
	s = s.replace("$sex2","\" .. sex2() .. \"")
	s = s.replace("$sex3","\" .. sex3() .. \"")
	s = s.replace("$sex4","\" .. sex4() .. \"")
	s = s.replace("$race","\" .. other:GetRaceName() .. \"")
	s = s.replace("$name","\" .. other:GetName() .. \"")
	s = s.replace("$ulevel","\" .. other:GetLevel() .. \"")
	s = s.replace("$mname","\" .. self:GetName() .. \"")
	s = s.replace("$class","\" .. other:GetClassName() .. \"")
	return s
def do_msg_calcs(s):
	calcs_done = False
	changes = 0
	while not calcs_done:
		if "$calc" not in s:
			calcs_done = True
		else:
			calc_extract_start = s.find("$calc")
			parens = 0
			started = False
			offset = 0
			for x in s[calc_extract_start:]:
				offset = offset + 1
				if x == "(" and not started:
					parens = parens + 1
					started = True
				elif x == "(":
					parens = parens + 1
				elif x == ")" and parens > 1:
					parens = parens - 1
				elif x == ")":
					break
			calc_string = s[calc_extract_start:calc_extract_start + offset]
			if changes == 0:
				s = s.replace(calc_string, "\" .. (" + calc_string[6:offset-1] + ") .. \"")
			else:
				s = s.replace(calc_string, calc_string[6:offset-1])
			changes = changes + 1
			s = s.replace("$flag","other:GetFlag")
			s = re.sub(r'\$ustat\((\w+)\) == 1', r'other:GetStat(\1)', s)
			s = s.replace("$npc_count","NPCCount")
	return s
def do_calcs(s):
	calcs_done = False
	changes = 0
	while not calcs_done:
		if "$calc" not in s:
			calcs_done = True
		else:
			calc_extract_start = s.find("$calc")
			parens = 0
			started = False
			offset = 0
			for x in s[calc_extract_start:]:
				offset = offset + 1
				if x == "(" and not started:
					parens = parens + 1
					started = True
				elif x == "(":
					parens = parens + 1
				elif x == ")" and parens > 1:
					parens = parens - 1
				elif x == ")":
					break
			calc_string = s[calc_extract_start:calc_extract_start + offset]
			s = s.replace(calc_string, "(" + calc_string[6:offset-1] + ")")
			changes = changes + 1
			s = re.sub(r'\$random\((\d+)\)', r'math.random(\1) - 1', s)
			s = s.replace("$flag","other:GetFlag")
			s = s.replace("$ustat(MR)","other:GetStat(\"mr\")")
			s = s.replace("$ustat(FR)","other:GetStat(\"fr\")")
			s = s.replace("$ustat(CR)","other:GetStat(\"cr\")")
			s = s.replace("$ustat(PR)","other:GetStat(\"pr\")")
			s = s.replace("$ustat(DR)","other:GetStat(\"dr\")")
			s = s.replace("$hpratio","self:GetStat(\"hpratio\")")
			s = s.replace("$npc_count","NPCCount")
	return s
for line, next_line in pairwise(f):
	if not in_event and brackets < 1:
		if re.search(r'^EVENT_SPAWN',line):
			in_event = True
			outfile.write("function EVENT_SPAWN(self)" + "\n")
		elif re.search(r'^EVENT_SAY',line):
			in_event = True
			outfile.write("function EVENT_SAY(self, other, words)" + "\n")
			outfile.write("words = string.lower(words)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
			outfile.write("if not self:InCombat() then" + "\n")
		elif re.search(r'^EVENT_AGGROSAY',line):
			in_event = True
			outfile.write("function EVENT_AGGROSAY(self, other)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
			outfile.write("if self:InCombat() then" + "\n")
		elif re.search(r'^EVENT_ITEM',line):
			in_event = True
			outfile.write("function EVENT_ITEM(self, other, items_table)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_SCRIPT',line):
			in_event = True
			outfile.write("function EVENT_TIMER(self, timer_id)" + "\n")
			outfile.write("if timer_id == \"script\" then" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_TRIGGERALL',line):
			in_event = True
			outfile.write("function EVENT_TIMER(self, timer_id)" + "\n")
			outfile.write("if timer_id == \"triggerall\" then" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
			outfile.write("op_success = 0" + "\n")
			outfile.write("iter = 0" + "\n")
			outfile.write("hate = self:GetHateList(\"entity\")" + "\n")
			outfile.write("for k,other in pairs(hate) do" + "\n")
			outfile.write("iter = iter + 1" + "\n")
			outfile.write("if iter == #hate then op_success = 1" + "\n")
		elif re.search(r'^EVENT_SIGNAL',line):
			in_event = True
			outfile.write("function EVENT_SIGNAL(self, other, signal)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_COMBATEND',line):
			in_event = True
			outfile.write("function EVENT_COMBATEND(self)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_HP',line):
			in_event = True
			outfile.write("function EVENT_HP(self, other, damage)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_ATTACK',line):
			in_event = True
			outfile.write("function EVENT_ATTACK(self, other)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_DEATH',line):
			in_event = True
			outfile.write("function EVENT_DEATH(self, other, damage, killed_by_DoT)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_SLAY',line):
			in_event = True
			outfile.write("function EVENT_SLAY(self, other)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		elif re.search(r'^EVENT_SPELL',line):
			in_event = True
			outfile.write("function EVENT_SPELL(self, other, spellname, spellid, element, mana_used)" + "\n")
			if updates_script:
				outfile.write("check_script_status = script_status" + "\n")
			if updates_s0:
				outfile.write("check_substring_0 = substring_0" + "\n")
			if updates_s1:
				outfile.write("check_substring_1 = substring_1" + "\n")
			if updates_s2:
				outfile.write("check_substring_2 = substring_2" + "\n")
			if updates_s3:
				outfile.write("check_substring_3 = substring_3" + "\n")
			if updates_s4:
				outfile.write("check_substring_4 = substring_4" + "\n")
			if updates_s5:
				outfile.write("check_substring_5 = substring_5" + "\n")
			if updates_s6:
				outfile.write("check_substring_6 = substring_6" + "\n")
			if updates_s7:
				outfile.write("check_substring_7 = substring_7" + "\n")
			if updates_s8:
				outfile.write("check_substring_8 = substring_8" + "\n")
			if updates_s9:
				outfile.write("check_substring_9 = substring_9" + "\n")
		if uses_chance:
			outfile.write("chance = math.random(100) - 1" + "\n")
		if uses_bchance:
			outfile.write("bchance = math.random(100) - 1" + "\n")
		if uses_cchance:
			outfile.write("cchance = math.random(100) - 1" + "\n")
		if uses_dchance:
			outfile.write("dchance = math.random(100) - 1" + "\n")
	else:
		f_line = line[:int(line.find("("))]
		if "if" not in f_line and "}" not in f_line:
			filler = line[int(line.find("(")) + 1:int(line.find(");"))]
			if f_line == "msgtext":
				filler = do_msg_vars(filler)
				outfile.write("self:text(\"" + filler + "\",other)" + "\n")
			if f_line == "msg":
				filler = do_msg_vars(filler)
				outfile.write("self:text(self:GetName() .. \" tells you, '" + filler + "'\",other)" + "\n")
			elif f_line == "emote":
				filler = do_msg_vars(filler)
				outfile.write("self:text(self:GetName() .. \" " + filler + "\",other)" + "\n")
			elif f_line == "text":
				filler = do_msg_vars(filler)
				outfile.write("self:text(\"" + filler + "\")" + "\n")
			elif f_line == "say":
				filler = do_msg_vars(filler)
				outfile.write("self:text(self:GetName() .. \" says, '" + filler + "'\")" + "\n")
			elif f_line == "shout":
				filler = do_msg_vars(filler)
				outfile.write("zonetext(self:GetName() .. \" shouts, '" + filler + "'\")" + "\n")
			elif f_line == "zonetext":
				filler = do_msg_vars(filler)
				outfile.write("zonetext(\"" + filler + "\")" + "\n")
			elif f_line == "msgnote":
				filler = do_msg_vars(filler)
				outfile.write("self:text(\"NOTE: " + filler + "\",other,15)" + "\n")
			elif f_line == "dialog":
				filler = do_msg_vars(filler)
				outfile.write("other:dialog(self,\"" + filler + "\")" + "\n")
			elif f_line == "break":
				outfile.write("return" + "\n")
			elif f_line == "summonitem":
				item_id = filler[:int(filler.find(","))]
				amt = int(filler[int(filler.find(","))+1:])
				if amt > 0:
					outfile.write("other:giveitem(" + filler + ")" + "\n")
				else:
					outfile.write("other:giveitem(" + item_id + ")" + "\n")
			elif f_line == "exp":
				outfile.write("other:exp(" + filler + ")" + "\n")
			elif f_line == "signal":
				npc_id = filler[:int(filler.find(","))]
				val = filler[int(filler.find(","))+1:]
				outfile.write("signal(" + npc_id + "," + val + ",self)" + "\n")
			elif f_line == "setglobal":
				filler = do_vars(filler)
				filler = do_calcs(filler)
				outfile.write("setglobal(" + filler + ")" + "\n")
			elif f_line == "repopspawn":
				outfile.write("respawn(" + filler + ")" + "\n")
			elif f_line == "scriptstatus":
				if filler == "-1":
					outfile.write("script_status = script_status + 1" + "\n")
				else:
					filler = do_calcs(filler)
					filler = do_vars(filler)
					outfile.write("script_status = " + filler + "\n")
			elif f_line == "startscript":
				outfile.write("self:timer(\"script\"," + filler + ")" + "\n")
			elif f_line == "pulltrigger":
				outfile.write("self:timer(\"triggerall\"," + filler + ")" + "\n")
			elif f_line == "doanim":
				outfile.write("self:doanim(" + filler + ")" + "\n")
			elif f_line == "setanim":
				outfile.write("self:setanim(" + filler + ")" + "\n")
			elif f_line == "setrace":
				outfile.write("self:setappearance(" + filler + ")" + "\n")
			elif f_line == "setsize":
				outfile.write("self:setsize(" + filler + ")" + "\n")
			elif f_line == "wipehate":
				outfile.write("self:wipehate()" + "\n")
			elif f_line == "fade":
				setting = str(filler == "1").lower()
				outfile.write("self:fade(" + setting + ")" + "\n")
			elif f_line == "depop":
				if int(filler) == 0:
					outfile.write("self:depop()" + "\n")
				else:
					outfile.write("depop(" + filler + ")" + "\n")
			elif f_line == "takecash":
				outfile.write("other:takecash(" + filler + ")" + "\n")
			elif f_line == "adjusthate":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				value = vars[1]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:addhate(self:GetTarget()," + value + ")" + "\n")
				else:
					outfile.write("self:addhate(" + target + "," + value + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "aggro":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:addhate(self:GetTarget(),1)" + "\n")
				else:
					outfile.write("self:addhate(" + target + ",1)" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "aggrotarget":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:addhate(self:GetTarget(),1)" + "\n")
				else:
					outfile.write("self:addhate(" + target + ",1)" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "casttime":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_id = vars[0]
				time = vars[1]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("if other ~= nil then" + "\n")
					outfile.write("self:castspell(" + spell_id + "," + time + "," + ",other)" + "\n")
					outfile.write("elseif self:GetTarget() then" + "\n")
					outfile.write("self:castspell(" + spell_id + "," + time + "," + ",self:GetTarget())" + "\n")
					outfile.write("else self:castspell(" + spell_id + "," + time + "," + ",self) end" + "\n")
				else:
					outfile.write("self:castspell(" + spell_id + "," + time + "," + target + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "customhit":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				damage = vars[0]
				skill = vars[1]
				check_AC = str(vars[2] == "1").lower()
				check_aux = str(vars[3] == "1").lower()
				check_hit = str(vars[4] == "1").lower()
				check_avoid = str(vars[5] == "1").lower()
				check_mods = str(vars[6] == "1").lower()
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:customhit(" + "self:GetTarget()" + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
				else:
					outfile.write("self:customhit(" + target + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "customhitother":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				actor = vars[0]
				damage = vars[1]
				skill = vars[2]
				check_AC = str(vars[3] == "1").lower()
				check_aux = str(vars[4] == "1").lower()
				check_hit = str(vars[5] == "1").lower()
				check_avoid = str(vars[6] == "1").lower()
				check_mods = str(vars[7] == "1").lower()
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				outfile.write("if GetByID(" + actor + ") then" + "\n")
				if target == "0":
					outfile.write("self:customhit(" + "self:GetTarget()" + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
				else:
					outfile.write("self:customhit(" + target + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
					outfile.write("end" + "\n")
				outfile.write("end" + "\n")
			elif f_line == "customnuke":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				name = vars[0]
				element = vars[1]
				resist_adjust = vars[2]
				range = vars[3]
				secondary = vars[4]
				tertiary = vars[5]
				message = vars[6]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:customnuke(" + "self:GetTarget()" + ",\"\"" + name + "\"\"," + damage + "," + element + "," + resist_adjust + ",\"" + message + "\"," + secondary + "," + tertiary + ")" + "\n")
				else:
					outfile.write("self:customnuke(" + target + ",\"" + name + "\"," + damage + "," + element + "," + resist_adjust + ",\"" + message + "\"," + secondary + "," + tertiary + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "customspell":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_id = vars[0]
				name = vars[0]
				damage = vars[1]
				element = vars[2]
				resist_adjust = vars[3]
				range = vars[4]
				secondary_spell = vars[5]
				tertiary_spell = vars[6]
				message = vars[7]
				coneVal = vars[8]
				losVal = vars[9]
				if target == "0":
					target = "self"
				if int(coneVal) == 1:
					s_cone = ""
				elif int(coneVal) == 2:
					s_cone = "and not self:IsBehind(v) "
				elif int(coneVal) == 0:
					s_cone = "and self:IsBehind(v) "
				if int(losVal) == 1:
					s_los = ""
				elif int(coneVal) == 2:
					s_los = "and self:InLos(v) "
				elif int(coneVal) == 0:
					s_los = "and not self:InLos(v) "
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					target = "self"
				outfile.write("local hl = self:GetHateList(\"entity\")" + "\n")
				outfile.write("for k,v in pairs(hl) do" + "\n")
				outfile.write("if " + target + ":GetDist(v) <= " + range + s_cone + s_los + " then" + "\n")
				outfile.write("self:customnuke(v,\"" + name + "\"," + damage + "," + element + "," + resist_adjust + ",\"" + message + "\"," + secondary_spell + "," + tertiary_spell + ")" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
			elif f_line == "doattack":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				damage = "self:GetStat(\"maxdmg\")"
				skill = "0"
				check_AC = "true"
				check_aux = "true"
				check_hit = "true"
				check_avoid = "true"
				check_mods = "true"
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:customhit(" + "self:GetTarget()" + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
				else:
					outfile.write("self:customhit(" + target + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "doattackround":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				damage = "self:GetStat(\"maxdmg\")"
				skill = "0"
				check_AC = "true"
				check_aux = "true"
				check_hit = "true"
				check_avoid = "true"
				check_mods = "true"
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				outfile.write("for i=1,self:GetStat(\"attacks\") do")
				if target == "0":
					outfile.write("self:customhit(" + "self:GetTarget()" + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
				else:
					outfile.write("self:customhit(" + target + "," + skill + "," + check_AC + "," + check_aux + "," + check_hit + "," + check_avoid + "," + check_mods + ")" + "\n")
					outfile.write("end" + "\n")
				outfile.write("end" + "\n")
			elif f_line == "drainhp":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				damage = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:customnuke(self:GetTarget(),\"Drain\"," + damage + ",0,0,\"You feel your life force drain away.\",0,0)" + "\n")
				else:
					outfile.write("self:customnuke(" + target + ",\"Drain\"," + damage + ",0,0,\"You feel your life force drain away.\",0,0)" + "\n")
					outfile.write("end" + "\n")
				outfile.write("self:set(\"hp\",self:GetStat(\"hp\") + " + damage + ")" + "\n")
			elif f_line == "drainmana":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				damage = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:GetTarget():alter(\"mana\",self:GetTarget():GetStat(\"mana\") - " + damage + ")" + "\n")
				else:
					outfile.write(target + ":alter(\"mana\",self:GetTarget():GetStat(\"mana\") - " + damage + ")" + "\n")
					outfile.write("end" + "\n")
				outfile.write("self:set(\"mana\",self:GetStat(\"mana\") + " + damage + ")" + "\n")
			elif f_line == "loadpet":
				outfile.write("-- BAD COMMAND: LOADPET" + "\n")
			elif f_line == "losecontrol":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				setting = str(vars[0] == "1").lower()
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("--LOSE CONTROL ON SELF? NO." + "\n")
				else:
					outfile.write(target + ":freeze(" + setting + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "mobidcast":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_id = vars[0]
				caster = int(vars[2])
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				outfile.write("nl = GetNPCList()" + "\n")
				outfile.write("mob = self" + "\n")
				outfile.write("for k,v in pairs(nl) do" + "\n")
				outfile.write("if GetNPCID(v) == " + caster + " then" + "\n")
				outfile.write("mob = caster" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
				if target == "0":
					outfile.write("mob:castspell(" + spell_id + ",self:GetTarget())" + "\n")
				else:
					outfile.write("mob:castspell(" + spell_id + "," + target + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "purgetargetbufftype":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_effect = vars[0]
				if spell_effect == "22":
					type = "charm"
				elif spell_effect == "35":
					type = "disease"
				elif spell_effect == "36":
					type = "poison"
				elif spell_effect == "40":
					type = "divineaura"
				elif spell_effect == "57":
					type = "levitate"
				elif spell_effect == "58":
					type = "illusion"
				elif spell_effect == "59":
					type = "damageshield"
				else:
					type = "UNKNOWN EFFECT"
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("--ridiculous assertion: PTBT on self" + "\n")
				else:
					outfile.write("bl = " + target + ":GetBuffs(\"spellid\")" + "\n")
					outfile.write("for k,v in bl do" + "\n")
					outfile.write("if IsSpellType(v,\"" + type + "\") then" + "\n")
					outfile.write(target + ":removebuff(" + v + ")" + "\n")
					outfile.write("end" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "sethate":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				amount = vars[1]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:sethate(self:GetTarget()" + "," + amount + ")" + "\n")
				else:
					outfile.write("self:sethate(" + target + "," + amount + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "stun":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				duration = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:stun(self:GetTarget()," + duration + ")" + "\n")
				else:
					outfile.write("self:stun(" + target + "," + duration + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "summontarget":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:summon(self:GetTarget())" + "\n")
				else:
					outfile.write("self:summon(" + target + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "swaphate(userid)":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_id = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				outfile.write("hl = GetHateList(self,\"entity\"" + "\n" + ")" + "\n")
				outfile.write("dl = GetHateList(self,\"hate\"" + "\n" + ")" + "\n")
				outfile.write("max_index = 1" + "\n")
				outfile.write("max_hate = 0" + "\n")
				outfile.write("for k,v in pairs(dl) do" + "\n")
				outfile.write("if v > max_hate then" + "\n")
				outfile.write("max_hate = v" + "\n")
				outfile.write("max_index = k" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
				outfile.write("for k,v in pairs(hl) do" + "\n")
				outfile.write("if v == GetByID(" + target + " then" + "\n")
				outfile.write("other_guy_index = k" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
				outfile.write("if hl[other_guy_index] ~= nil and hl[max_index] ~= nil then" + "\n")
				outfile.write("self:sethate(hl[other_guy_index],dl[max_index])" + "\n")
				outfile.write("self:sethate(hl[max_index],dl[other_guy_index])" + "\n")
				outfile.write("end" + "\n")
			elif f_line == "unresistablestun":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				duration = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:stun(self:GetTarget()," + duration + ",true)" + "\n")
				else:
					outfile.write("self:stun(" + target + "," + duration + ",true)" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "killpc":
				outfile.write("-- BAD COMMAND: KILLPC" + "\n")
			elif f_line == "telerandom":
				outfile.write("repeat" + "\n")
				outfile.write("x = self:GetX() + (filler / 2) + math.random(filler / 2)" + "\n")
				outfile.write("y = self:GetX() + (filler / 2) + math.random(filler / 2)" + "\n")
				outfile.write("z = self:GetZ()" + "\n")
				outfile.write("until self:InCoordLos(x,y,z)" + "\n")
				outfile.write("self:teleto(x,y,z)" + "\n")
			elif f_line == "playercast":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_id = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("self:GetTarget():castspell(" + spell_id + ",self:GetTarget():GetTarget())" + "\n")
				else:
					outfile.write("self:GetTarget():castspell(" + spell_id + "," + target + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "castspell":
				filler = do_vars(filler)
				q = target_loc[f_line]
				vars = filler.split(",")
				target = vars[q]
				spell_id = vars[0]
				if target in var_tars:
					target = "GetByID(" + target + ")"
					outfile.write("if " + target + " then" + "\n")
				if target == "0":
					outfile.write("if other ~= nil then" + "\n")
					outfile.write("self:castspell(" + spell_id + ",other)" + "\n")
					outfile.write("elseif self:GetTarget() then" + "\n")
					outfile.write("self:castspell(" + spell_id + ",self:GetTarget())" + "\n")
					outfile.write("else self:castspell(" + spell_id + ",self) end" + "\n")
				else:
					outfile.write("self:castspell(" + spell_id + "," + target + ")" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "movegrp":
				vars = filler.split(",")
				zone = "\"" + vars[0] + "\", "
				x = vars[1] + ", "
				y = vars[2] + ", "
				z = vars[3]
				filler = zone + x + y + z
				outfile.write("if not other:InGroup() then" + "\n")
				outfile.write("other:zone(" + filler + ")" + "\n")
				outfile.write("else" + "\n")
				outfile.write("gl = other:GetGroup(\"entity\")" + "\n")
				outfile.write("for k,v in pairs(gl) do" + "\n")
				outfile.write("other:zone(" + filler + ")" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
			elif f_line == "movepc":
				vars = filler.split(",")
				zone = "\"" + vars[0] + "\", "
				x = vars[1] + ", "
				y = vars[2] + ", "
				z = vars[3]
				filler = zone + x + y + z
				outfile.write("other:zone(" + filler + ")" + "\n")
			elif f_line == "runto":
				outfile.write("self:runto(" + filler + ")" + "\n")
			elif f_line == "walkto":
				outfile.write("self:walkto(" + filler + ")" + "\n")
			elif f_line == "runtoheading":
				outfile.write("self:runto(" + filler + ")" + "\n")
			elif f_line == "walktoheading":
				outfile.write("self:walkto(" + filler + ")" + "\n")
			elif f_line == "setdmg":
				outfile.write("self:set(\"damage\"," + filler + ")" + "\n")
			elif f_line == "faction":
				outfile.write("other:faction(" + filler + ")" + "\n")
			elif f_line == "setflag":
				outfile.write("other:setflag(" + filler + ")" + "\n")
			elif f_line == "journal":
				outfile.write("other:journal(" + filler + ")" + "\n")
			elif f_line == "lawpoints":
				outfile.write("other:setflag(4998, other:GetFlag(4998) + " + filler + ")" + "\n")
			elif f_line == "hptrigger":
				outfile.write("self:hptrigger(" + filler + ")" + "\n")
			elif f_line == "flagreplace":
				outfile.write("flagmobs = {}" + "\n")
			elif f_line == "unattackable":
				npc_id = filler
				if filler == "0":
					outfile.write("self:set(\"cares\",false)" + "\n")
					outfile.write("self:invul(true)" + "\n")
				else:
					outfile.write("nl = GetNPCList()" + "\n")
					outfile.write("for k,mob in pairs(nl) do" + "\n")
					outfile.write("if GetNPCID(mob) == " + npc_id + " then" + "\n")
					outfile.write("mob:set(\"cares\",false)" + "\n")
					outfile.write("mob:invul(true)" + "\n")
					outfile.write("end" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "attackable":
				npc_id = filler
				if filler == "0":
					outfile.write("self:set(\"cares\",true)" + "\n")
					outfile.write("self:invul(false)" + "\n")
				else:
					outfile.write("nl = GetNPCList()" + "\n")
					outfile.write("for k,mob in pairs(nl) do" + "\n")
					outfile.write("if GetNPCID(mob) == " + npc_id + " then" + "\n")
					outfile.write("mob:set(\"cares\",true)" + "\n")
					outfile.write("mob:invul(false)" + "\n")
					outfile.write("end" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "heal":
				npc_id = filler
				if filler == "0":
					outfile.write("self:set(\"hp\",self:GetStat(\"maxhp\"))" + "\n")
				else:
					outfile.write("nl = GetNPCList()" + "\n")
					outfile.write("for k,mob in pairs(nl) do" + "\n")
					outfile.write("if GetNPCID(mob) == " + npc_id + " then" + "\n")
					outfile.write("mob:set(\"hp\",mob:GetStat(\"maxhp\"))" + "\n")
					outfile.write("end" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "sethpratio":
				filler = do_calcs(filler)
				vars = filler.split(",")
				npc_id = vars[0]
				amt = vars[1]
				if filler == "0":
					outfile.write("self:set(\"hp\",self:GetStat(\"maxhp\") * (" + amt + "/100))" + "\n")
				else:
					outfile.write("nl = GetNPCList()" + "\n")
					outfile.write("for k,mob in pairs(nl) do" + "\n")
					outfile.write("if GetNPCID(mob) == " + npc_id + " then" + "\n")
					outfile.write("mob:set(\"hp\",mob:GetStat(\"maxhp\") * (" + amt + "/100))" + "\n")
					outfile.write("end" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "flaglastnpc":
				flag_id = filler
				outfile.write("a.flag = " + flag_id + "\n")
			elif f_line == "flagmove":
				vars = filler.split(",")
				flag_id = vars[0]
				x = vars[1]
				y = vars[2]
				z = vars[3]
				heading = vars[4]
				outfile.write("nl = GetNPCList()" + "\n")
				outfile.write("for k,mob in pairs(nl) do" + "\n")
				outfile.write("if mob.flag ~= nil and mob.flag == flag_id then" + "\n")
				outfile.write("mob:walkto(" + x + "," + y + "," + z + "," + heading + ")" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
			elif f_line == "invul":
				if filler == "0":
					outfile.write("self:invul(false)" + "\n")
				else:
					outfile.write("self:invul(true)" + "\n")
			elif f_line == "uninvul":
				if filler == "0":
					outfile.write("self:invul(false)" + "\n")
				else:
					check_id = filler
					outfile.write("nl = GetNPCList()" + "\n")
					outfile.write("for k,v in pairs(nl) do" + "\n")
					outfile.write("if v:GetNPCID() == " + filler + " then" + "\n")
					outfile.write("v:invul(false)" + "\n")
					outfile.write("end" + "\n")
					outfile.write("end" + "\n")
			elif f_line == "increaseflag":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				flag_id = filler[:int(filler.find(","))]
				amt = int(filler[int(filler.find(","))+1:])
				outfile.write("other:setflag(" + str(flag_id) + ", other:GetFlag(" + str(flag_id) +") + (" + str(amt) + "))" + "\n")
			elif f_line == "setsubstring":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				substring_id = filler[:int(filler.find(","))]
				val = filler[int(filler.find(","))+1:]
				outfile.write("substring_" + substring_id + " = " + val + "\n")
			elif f_line == "clearsubstring":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				outfile.write("substring_" + filler + " = 0" + "\n")
			elif f_line == "set":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				attribute = vars[0]
				val1 = vars[1]
				val2 = vars[2]
				outfile.write("self:set(\"" + attribute + "\", " + val1 + ", " + val2 + ")" + "\n")
			elif f_line == "chaospoints":
				outfile.write("other:setflag(4999, other:GetFlag(4999) + " + filler + ")" + "\n")
			elif f_line == "keepitem":
				outfile.write("items_table(" + filler + ")" + "\n")
			elif f_line == "destroycorpse":
				outfile.write("self:destroycorpse()" + "\n")
			elif f_line == "spawnnear":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				npc_id = filler[:int(filler.find(","))]
				time = filler[int(filler.find(","))+1:]
				outfile.write("a = ")
				outfile.write("spawn(" + npc_id + ", self:GetX() + 3 + math.random(5),self:GetY() + 3 + math.random(5),self:GetZ(),self:GetHeading()," + time + ")" + "\n")
			elif f_line == "spawnat":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				npc_id = vars[0]
				depop_id = int(vars[1])
				x = vars[2]
				y = vars[3]
				z = vars[4]
				heading = vars[5]
				time = vars[6]
				outfile.write("a = ")
				outfile.write("spawn(" + npc_id + "," + x + "," + y + "," + z + "," + heading + "," + time + ")" + "\n")
				if depop_id > 0:
					outfile.write("depop(" + str(depop_id) + ")" + "\n")
			elif f_line == "spawn":
				filler = do_calcs(filler)
				filler = do_vars(filler)
				vars = filler.split(",")
				npc_id = vars[0]
				time = vars[1]
				outfile.write("if other ~= nil then" + "\n")
				outfile.write("x = other:GetX()" + "\n")
				outfile.write("y = other:GetY()" + "\n")
				outfile.write("z = other:GetZ()" + "\n")
				outfile.write("else" + "\n")
				outfile.write("x = self:GetX()" + "\n")
				outfile.write("y = self:GetY()" + "\n")
				outfile.write("z = self:GetZ()" + "\n")
				outfile.write("end" + "\n")
				outfile.write("a = ")
				outfile.write("spawn(" + npc_id + ",x,y,z,0," + time + ")" + "\n")
			elif f_line == "cleardebt":
				outfile.write("other:setexpdebt(0,true)" + "\n")
			elif f_line == "removeitem":
				item_id = filler[:int(filler.find(","))]
				amt = int(filler[int(filler.find(","))+1:])
				outfile.write("inv = other.GetInventory()" + "\n")
				outfile.write("for i in pairs(inv) do" + "\n")
				outfile.write("if GetItemID(inv[i]) == " + item_id + " then" + "\n")
				if amt == 0:
					outfile.write("other:takeitem(inv[i])" + "\n")
				else:
					outfile.write("inv[i]:reduceitemcharges(" + str(amt) + ")" + "\n")
				outfile.write("end" + "\n")
				outfile.write("end" + "\n")
		elif "}" in f_line:
			if next_line and not next_line.startswith("else"):
				outfile.write(("end" + "\n") * line.count("}"))
		elif "if" in f_line:
			if line[2] == " ":
				filler = line[:line.find('(')] + line[line.find('(')+1:line.rfind(')')]
			else:
				filler = line[:line.find('(')] + " " + line[line.find('(')+1:line.rfind(')')]
			filler = do_calcs(filler)
			filler = do_vars(filler)
			outfile.write("\t")
			outfile.write(filler + " then" + "\n")
			bracket = brackets + 1
		else:
			outfile.write("FUNCTION NOT FOUND" + "\n")
		temp_report.write(f_line + "\n")
temp_report.close()
#if updates_script:
	#outfile.write("script_status = check_script_status" + "\n")
if updates_s0:
	outfile.write("substring_0 = check_substring_0" + "\n")
if updates_s1:
	outfile.write("substring_1 = check_substring_1" + "\n")
if updates_s2:
	outfile.write("substring_2 = check_substring_2" + "\n")
if updates_s3:
	outfile.write("substring_3 = check_substring_3" + "\n")
if updates_s4:
	outfile.write("substring_4 = check_substring_4" + "\n")
if updates_s5:
	outfile.write("substring_5 = check_substring_5" + "\n")
if updates_s6:
	outfile.write("substring_6 = check_substring_6" + "\n")
if updates_s7:
	outfile.write("substring_7 = check_substring_7" + "\n")
if updates_s8:
	outfile.write("substring_8 = check_substring_8" + "\n")
if updates_s9:
	outfile.write("substring_9 = check_substring_9" + "\n")
if EVENT == "SCRIPT" or EVENT == "TRIGGERALL":
	outfile.write("end" + "\n" + "\n")
if EVENT == "SAY" or EVENT == "AGGROSAY":
	outfile.write("end" + "\n" + "\n")
if EVENT == "HP":
	outfile.write("self:hptrigger(self:GetHPTrigger() - 10)" + "\n" + "\n")
#outfile.write("end" + "\n" + "\n")
outfile.close()