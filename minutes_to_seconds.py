def minutes_to_seconds(time):
    minutes, seconds = int(time.split(":")[0]), int(time.split(":")[1])
    if seconds >= 60: return -1
    return minutes*60+seconds

def main():
    print(minutes_to_seconds("121:49"))

if __name__ == '__main__':
    main()