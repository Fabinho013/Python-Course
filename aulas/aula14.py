a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
formato = string.format(
  nome1=a, nome2=b, nome3=c)

print(formato)
# .
