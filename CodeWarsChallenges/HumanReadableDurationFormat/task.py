def format_duration(seconds):
    data = {'year': 0, 'day': 0, 'hour': 0, 'minute': 0, 'second': 0}
    
    year = seconds//31536000
    data['year'] = year
    seconds -= year*31536000
    
    day = seconds//86400
    data['day'] = day
    seconds -= day*86400
    
    hour = seconds//3600
    data['hour'] = hour
    seconds -= hour*3600
    
    minute = seconds//60
    data['minute'] = minute
    seconds -= minute*60
    
    data['second'] = seconds
                
    r = []
    for x, y in zip(data, data.values()):
        if y != 0:
            if y > 1:
                r.append(f'{y} {x}s')
            else:
                r.append(f'{y} {x}')
    q = []
    
    if len(r)==0:
        return 'now'
    
    elif len(r)>1:
        for x in range(len(r)):
            if x+2 == len(r):
                q.append(r[x])
                q.append(' and ')
            else:
                q.append(r[x])
                q.append(', ')                
        return "".join(q[:-1])
    else:
        return "".join(r)

def test(fun, x):
    return fun == x

print(test(format_duration(1), "1 second"))
print(test(format_duration(62), "1 minute and 2 seconds"))
print(test(format_duration(120), "2 minutes"))
print(test(format_duration(3600), "1 hour"))
print(test(format_duration(3662), "1 hour, 1 minute and 2 seconds"))