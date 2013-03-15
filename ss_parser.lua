function substring_test(substring,op,val)
	if type(substring) == "userdata" then
		if type(val) == "userdata" then
			if op == "==" then
				return substring == val
			if op == "!=" then
				return substring ~= val
			else
				return false
		else
			return false
		end
	end
	if type(substring) == "number" then
		if type(val) == "number" then
			if op == "==" then
				return substring == val
			if op == "!=" then
				return substring ~= val
			if op == ">=" then
				return substring >= val
			if op == "<=" then
				return substring <= val
			if op == ">" then
				return substring > val
			if op == "<" then
				return substring < val
		else
			return false
		end
	end
	if type(substring) == "string" then
		if type(val) == "string" then
			if op == "==" then
				return substring == val
			if op == "!=" then
				return substring ~= val
			else
				return false
		else
			return false
		end
	end
end