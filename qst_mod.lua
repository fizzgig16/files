
function HasBuff(mob,spell_id)
	bl = mob:GetBuffs("spellid")
	for k,v in pairs(bl) do
		if v = spell_id then
			return true
		end
	end
	return false
end


function HasItem(mob,item_id)
	inv = mob:GetInventory()
	for k,v in pairs(inv) do
		if GetItemID(v) = item_id then
			return 1
		end
	end
	return 0
end


script_status = 0


substring_0 = nil


substring_1 = nil


substring_2 = nil


substring_3 = nil


substring_4 = nil


substring_5 = nil


substring_6 = nil


substring_7 = nil


substring_8 = nil


substring_9 = nil


function sex(self)
	if self:GetGender() == 0 then return "he"
	elseif self:GetGender() == 1 then return "she"
	else return "it"
end
end


function sex2(self)
	if self:GetGender() == 0 then return "his"
	elseif self:GetGender() == 1 then return "her"
	else return "its"
end
end


function sex(self)
	if self:GetGender() == 0 then return "him"
	elseif self:GetGender() == 1 then return "her"
	else return "it"
end
end


function sex(self)
	if self:GetGender() == 0 then return "man"
	elseif self:GetGender() == 1 then return "woman"
	else return "thing"
end
end


function NPCCount(npc_id)
	count = 0
	nl = GetNPCList()
	for k,v in pairs(nl) do
		if GetNPCID(v) == npc_id then
			count = count + 1
		end
	end
	return count
end


function primarytarget(self)
	hl = GetHateList(self,"entity")
	dl = GetHateList(self,"hate")
	max_index = 1
	max_hate = 0
	for k,v in pairs(dl) do
		if v > max_hate then
			max_hate = v
			max_index = k
		end
	end
	return hl[k]
end


function randtarget(self)
	hl = GetHateList(self,"entity")
	return hl[math.random(#hl)]
end


function auxtarget(self)
	hl = GetHateList(self,"entity")
	if #hl == 1 then 
		return hl[1] 
		else
		return_index = 0
		dl = GetHateList(self,"hate")
		max_index = 1
		max_hate = 0
		for k,v in pairs(dl) do
			if v > max_hate then
				max_hate = v
				max_index = k
			end
		end
	end
	repeat
	return_index = math.random(#hl)
	until return_index ~= max_index
	return hl[return_index]
end


function highestdamage(self)
	hl = GetHateList(self,"entity")
	dl = GetHateList(self,"damage")
	max_index = 1
	max_dmg = 0
	for k,v in pairs(dl) do
		if v > max_hdmg then
			max_hdmg = v
			max_index = k
		end
	end
	return hl[k]
end


function highestheals(self)
	hl = GetHateList(self,"healing")
	dl = GetHateList(self,"damage")
	max_index = 1
	max_dmg = 0
	for k,v in pairs(dl) do
		if v > max_hdmg then
			max_hdmg = v
			max_index = k
		end
	end
	return hl[k]
end


function lowesttarget(self)
	hl = GetHateList(self,"entity")
	dl = GetHateList(self,"hate")
	min_index = 1
	min_hate = 2000000000
	for k,v in pairs(dl) do
		if v < min_hate then
			min_hate = v
			min_index = k
		end
	end
	return hl[k]
end


function ramptarget(self)
	hl = GetHateList(self,"entity")
	for k,v in pairs(hl) do
		if k > 1 then
			if InCombatRange(self,v) then
				return v
			end
		end
	end
	return hl[1]
end


function meleetarget(self)
	hl = GetHateList(self,"entity")
	candidates = {}
	for k,v in pairs(hl) do
		if InCombatRange(self,v) then
			table.insert(candidates,v)
		end
	end
	if #candidates < 1 then return hl[1] end
	return candidates[math.random(#candidates)]
end


function auxmeleetarget(self)
	hl = GetHateList(self,"entity")
	candidates = {}
	for k,v in pairs(hl) do
		if k > 1 then
			if InCombatRange(self,v) then
				table.insert(candidates,v)
			end
		end
	end
	if #candidates < 1 then return hl[1] end
	return candidates[math.random(#candidates)]
end


function fartarget(self)
	hl = GetHateList(self,"entity")
	candidates = {}
	for k,v in pairs(hl) do
		if not InCombatRange(self,v) then
			table.insert(candidates,v)
		end
	end
	if #candidates < 1 then return -2 end
	return candidates[math.random(#candidates)]
end


function lostarget(self)
	hl = GetHateList(self,"entity")
	candidates = {}
	for k,v in pairs(hl) do
		if InLos(self,v) then
			table.insert(candidates,v)
		end
	end
	if #candidates < 1 then return hl[1] end
	return candidates[math.random(#candidates)]
end


function nolostarget(self)
	hl = GetHateList(self,"entity")
	candidates = {}
	for k,v in pairs(hl) do
		if not InLos(self,v) then
			table.insert(candidates,v)
		end
	end
	if #candidates < 1 then return hl[1] end
	return candidates[math.random(#candidates)]
end


function getdmghate(self,other)
	hl = GetHateList(self,"entity")
	dl = GetHateList(self,"damage")
	return_index = 1
	for k,v in pairs(hl) do
		if v == other then
			return_index = k
		end
	end
	return dl[k]
end


function hatesizetotal(self)
	hl = GetHateList(self,"entity")
	return #hl
end


function hatesizeclients(self)
	hl = GetHateList(self,"entity")
	clients = {}
	for k,v in pairs(hl) do
		if IsClient(v) then
			table.insert(clients,v)
		end
	end
	return #clients
end


function npccorpse_count(npcid)
	cl = GetCorpseList()
	total = 0
	for k,v in pairs(nl) do
		if GetNPCID(v) == npcid then
			total = total + 1
		end
	end
	return total
end


function clientcount()
	return #GetClientList()
end

