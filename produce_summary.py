def produce(delivery_log, day):

    print "Day %s" % day
    the_file = open(delivery_log)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    the_file.close()

produce("um-deliveries-20140519.txt",1)
produce("um-deliveries-20140520.txt",2)
produce("um-deliveries-20140521.txt",3)
#     print "Day 2"
#     the_file = open("um-deliveries-20140520.txt")
#     for line in the_file:
#         line = line.rstrip()
#         words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()


# print "Day 3"
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()
