s = input()

pos = 0
result = ''

while True:
  start = s.find('<', pos)
  if start == -1:
    break
  words = s[pos:start]
  if words:
    t = words.split()
    for i in range(len(t)):
      t[i] = t[i][::-1]
    result += ' '.join(t)
  end = s.find('>', pos + 1)
  result += s[start:end+1]
  pos = end + 1

t = s[pos:].split()
for i in range(len(t)):
  t[i] = t[i][::-1]
result += ' '.join(t)
print(result)