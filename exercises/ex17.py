from sys import argv
from os.path import exists

script, from_file, to_file = argv
#
# print "Copying file from %s to %s" % (from_file, to_file)
#
# # we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
#
# print "The input file is %d bytes long" % len(indata)
#
# print "Does the output file exist? %r" % exists(to_file)
# # print "Ready, hit the RETURN to continur, CTRL-C to abort."
# # raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print "Alright, all done."
#
# out_file.close()
# in_file.close()

# 2
# ====
# one liner
# from sys import argv;from os.path import exists;script, from_file, to_file = argv;open(to_file, 'w').write(open(from_file).read());
