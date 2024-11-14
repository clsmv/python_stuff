def convert_time(time):
    splitted_time = time.split()
    hour, minutes = splitted_time[0].split(':')[0], splitted_time[0].split(':')[1]
    if len(splitted_time) > 1:
        meridien = splitted_time[1]
        if hour == '12':
            if meridien == "pm": return "12:00"
            else: return "0:00"
        else:
            if meridien == "pm":
                return str(int(hour)+12) + ':' + minutes
            return hour + ':' + minutes
    else:
        if hour == '0': hour = '12'
        elif hour == '12': hour = '24'
        if int(hour) > 12:
            return str(int(hour)-12) + ':' + minutes + ' pm'
        else: 
            return hour + ':' + minutes + ' am'

def main():
    print(convert_time("5:22 pm"))
main()