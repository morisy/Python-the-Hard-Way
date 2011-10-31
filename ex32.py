the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change =[1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice that we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

elements = []
# we can also build lists. Start with an empty one.
for i in range(0,6):
    print "Adding %d to the list." % i
# append is a function that lists understand.
    elements.append(i)

# now we can print them out, too
for i in elements:
    print "Element was: %d" % i
# Just adding an extra comment to test using Git pull. - MM