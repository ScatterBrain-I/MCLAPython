import NEMO

adj1 = NEMO.userString("Enter an adjective:")
adj2 = NEMO.userString("Enter an adjective:")
pln1 = NEMO.userString("Enter a plural noun:")
pln2 = NEMO.userString("Enter a plural noun:")
cel1 = NEMO.userString("Enter a celebrity:")
n1 = NEMO.userString("Enter a noun:")

print
print "In the shadowy world of spies, a/an %s organization like the US \
Governement uses spies to infiltrate %s groups for the purpose of obtaining top \
secret %s. A teacher, %s, or even the little old %s with a cane and fifteen \
pet %s could be a spy." % (adj1, adj2, pln1, cel1, n1, pln2)


# Professor Cohen used placeholders in sentence and used replace command to change them. His idea is better than my solution.