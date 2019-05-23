name='susmitha'
replacementstr='a'
i=len(name)
name2=name.replace(replacementstr,'')
j=len(name2)
if(replacementstr in name):
  count=i-j
else:
  count=0
msg='The alphabet {} occured {} time(s) in the string {}'.format(replacementstr,str(count),name)
print(msg)

