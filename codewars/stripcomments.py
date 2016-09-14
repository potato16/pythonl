def solution(strng,markers):
 l= strng.split('\n')
 ln=[]
 for i in l:
  for m in markers:
   if m in i:
    i=i[:i.index(m)].rstrip()
  ln.append(i)
 return '\n'.join(ln)
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
