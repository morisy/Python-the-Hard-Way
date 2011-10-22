from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script" % (user_name, script)

print "I'd like to ask a few questions."
print "Do you like me, %s" % (user_name)
likes = raw_input(prompt)


print "Where do you live, %s?" % (user_name)
lives = raw_input(prompt)

print "Hey %s, what kind of computer do you have?" % (user_name)
computer = raw_input(prompt)

print """
So you said %r about liking me,
you live in %r (never heard of it),
and you have a %r computer. Cool.
"""% (likes, lives, computer) 
