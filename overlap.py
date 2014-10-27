import ipaddr

n1 = ipaddr.IPNetwork('10.39.88.0/21')
n3 = ipaddr.IPNetwork('10.57.0.0/16')
n4 = ipaddr.IPNetwork('10.160.0.0/11')

subnets = ['10.0.0.0/8', '192.168.192.0/21']

for subnet in subnets:
        #print subnet
        n2 = ipaddr.IPNetwork(subnet)
        #print n2
        result1 = n1.overlaps(n2)
        result2 = n3.overlaps(n2)
        result3 = n4.overlaps(n2)
        print subnet
        print result1
        print result2
        print result3
        if result1 == True:
                print "Zurich subnet overlaps with %s" % subnet
        else:
                print "%s is False" % subnet
        if result2 == True:
                print "Bangalore subnet overlaps with %s" % subnet
        else:
                print "%s is False" % subnet
        if result3 == True:
                print "Cloud subnet overlaps with %s" % subnet
        else:
                print "%s is False" % subnet
                
print subnets