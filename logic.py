print "no of constant : ? "

n=int(raw_input())


def make(n) :
	a=0
	d={}
	while a<n :
        	temp=(2**(n-a-1))*[True] + (2**(n-a-1))*[False]
        	while len(temp)!=2**n :
                	temp+=temp
		d[chr(a+112)]=temp
		a+=1	
	return d


d=make(n)

print ""

def printing_table(d,n,list_of_statement) :
	for i in range(n) :
		print chr(i+112) + "		",
	
	for i in list_of_statement :
		print i + "		",
	
	print ""
	for j in range(2**n) :
		for i in range(n) :
			print d[chr(i+112)][j],
			print "		",
		for i in list_of_statement :
			print d[i][j],
			print "		",		
		
		print ""


list_of_statement=[]
printing_table(d,n,list_of_statement)



print "how many compound statement ? "

no_of_statement=int(raw_input())


counter=1

while counter<=no_of_statement :
	statement=raw_input("enter the " + str(counter) +"th statement : ")
	list_of_statement.append(statement)
	counter+=1



print list_of_statement


def precedence(c) :
	if c=='<' :
		return 1
	if c=='-' :
		return 2
	if c=='|' :
		return 3
	if c=='&' :
		return 4
	if c=='~' :
		return 5
	else :
		return -1


def postfix(string) :
	output_string=""
	l=[]
	i=0
	while i < len(string) :
		if ord(string[i]) in range(97,123) :
			output_string+=string[i]
		elif string[i]=='(' :
			l.append(string[i])
		elif string[i]==')' :
			while l[len(l)-1]!='(' :
				temp=l.pop()
				output_string+=temp
				if temp=='-' :
					output_string+='>'
				if temp=='<' :
					output_string+='->'
			r=l.pop()
		else :
			
			while len(l)!=0 and precedence(string[i]) <= precedence(l[len(l)-1]) :
				
				output_string+=l.pop()
				if output_string[len(output_string)-1]=='-' :
					output_string+='>'
				if output_string[len(output_string)-1]=='<' :
					output_string+='->'
			l.append(string[i])
			if string[i]=='-' :
				i+=1
			if string[i]=='<' :
				i+=2
				temp_list=range(i+3,len(string))
				
		i+=1

	while len(l)!=0 :
		output_string+=l.pop()
		if output_string[len(output_string)-1]=='-' :
					output_string+='>'
		if output_string[len(output_string)-1]=='<' :
					output_string+='->'

	return output_string






def disjunctive(x,y,n) :
	ans=[]
	for i in range(2**n) :
		ans.append(x[i] or y[i])

	return ans

def conjuctive(x,y,n) :
	ans=[]
	for i in range(2**n) :
		ans.append(x[i] and y[i])
			
	return ans

def conditional(x,y,n) :
	ans=[]
	for i in range(2**n) :
		ans.append((not x[i]) or y[i])
	return ans

def biconditional(x,y,n) :
	ans=[]
	for i in range(2**n) :
		ans.append(((not x[i]) or y[i]) and ((not y[i]) or x[i]))
	return ans


def negation(x,n) :
	ans=[]
	for i in range(2**n) :
		ans.append((not x[i]))
	return ans




def evaluating_postfix(string,d,n) :
	l=[]
	i=0
	while i < len(string) :
		if ord(string[i]) in range(97,123) :
			l.append(d[string[i]])
		elif string[i]=='~' : 
			val=l.pop()
			l.append(negation(val,n))
		else :
			val1=l.pop()
			val2=l.pop()
			if string[i]=='-' :
				l.append(conditional(val2,val1,n))
				i+=1
			if string[i]=='<' :
				l.append(biconditional(val2,val1,n))
				i+=2
			if string[i]=='|' :
				l.append(disjunctive(val2,val1,n))
			if string[i]=='&' :
				l.append(conjuctive(val2,val1,n))
		i+=1
	return l[0]





def evaluating_expression(list_of_statement,d,n) :
	for i in list_of_statement :
		converted_postfix=postfix(i)
		print converted_postfix
		d[i]=evaluating_postfix(converted_postfix,d,n)
	


def checking_tautology(list_of_statement,d) :
	for i in list_of_statement :
		if not False in d[i] :
			print i + " is Tautaulogy"

def checking_contradiction(list_of_statement,d) :
	for i in list_of_statement :
		if not True in d[i] :
			print i + " is self-contradictory"

def checking_contingencies(list_of_statement,d) :
	for i in list_of_statement :
		if True in d[i] and False in d[i] :
			print i + " is contingencies"


def checking_equivalence(list_of_statement,d) :
	for i in range(len(list_of_statement)) :
		for j in range(i+1,len(list_of_statement)) :
			if d[list_of_statement[i]]==d[list_of_statement[j]] :
				print list_of_statement[i] + " and " + list_of_statement[j] + " are equivalent"


def checking_entailment(list_of_statement,d,n) :
	for i in range(len(list_of_statement)) :
		for j in range(i+1,len(list_of_statement)) :
			if not False in conditional(d[list_of_statement[i]],d[list_of_statement[j]],n) :
				print  list_of_statement[i] + " and " + list_of_statement[j] + " are entailment"
			if not False in conditional(d[list_of_statement[j]],d[list_of_statement[i]],n) :
				print  list_of_statement[j] + " and " + list_of_statement[i] + " are entailment"



def checking_consistent(list_of_statement,d,n) :
	i=0
	x=0
	while i < 2**n :
		p=1
		for j in list_of_statement :
			if d[j][i]==False :
				p=0
				break
		if p==1 :
			x=1
			break
		i+=1
	
	if x==1 :
		print "yes given statements are logically consistent"
	else  :
		print "given statements are logically not consistent"

def checking(list_of_statment,d,n) :
	checking_tautology(list_of_statement,d)
	checking_contradiction(list_of_statement,d)
	checking_contingencies(list_of_statement,d)
	checking_equivalence(list_of_statement,d)
	checking_consistent(list_of_statement,d,n)


evaluating_expression(list_of_statement,d,n)




printing_table(d,n,list_of_statement)


checking(list_of_statement,d,n)






