import grequests
import time
import datetime
from datetime import date
start_time=int(time.time())
print("CURRENT TIME OF SCRIPT STARTING -"+str(start_time))
end_time=int(time.time())
end_time=end_time+5
print("END TIME OF SCRIPT FINISHING -"+str(end_time))
#print(time.localtime(time.time()))
print("CURRENT DATE & TIME - "+time.asctime(time.localtime(time.time())))
j=0
urls= ['https://b2b.raptorsupplies.com/pd/ame/58034','https://b2b.raptorsupplies.com/pd/ame/15200','https://b2b.raptorsupplies.com/pd/ame/51008','https://b2b.raptorsupplies.com/pd/ame/51017','https://b2b.raptorsupplies.com/pd/ame/51450','https://b2b.raptorsupplies.com/pd/ame/65-1h','https://b2b.raptorsupplies.com/pd/ame/71500','https://b2b.raptorsupplies.com/pd/ame/79400','https://b2b.raptorsupplies.com/pd/ame/11244','https://b2b.raptorsupplies.com/pd/allpax/ax1318']
#arr=[urls,urls1,urls2,urls3,urls4]
arr=[urls]
while True:
    s1=(arr[0])
    rs=(grequests.head(u) for u in s1)
    s=grequests.map(rs)
    j+=1
    print("WHILE LOOP RUN NO OF TIMES - "+str(j))
    print("CURRENT DATE & TIME WHILE LOOP - "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(0.9)
    loop_end_time=int(time.time())
    if(end_time==loop_end_time):
        break