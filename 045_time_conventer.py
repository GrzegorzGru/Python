#There is an application, which counts time only in seconds.
#Try to write a program to convert this values to day and time in classic format.
#Result should be displayed as Day: D Time: HH:MM:SS.
#Program should convert any input into classic format.
#Include error handling for unexpected inputs.

while True:
    try:
        time = float(input('Input time [in seconds] '))
        days = int(time // 86400)
        time = time % 86400
        time_hours = time / 3600
        time_minutes = time_hours % 1 * 60
        time_seconds = round(time_minutes % 1 * 60, 0)

        if len(str(int(round(time_hours, 0)))) == 1:
            time_hours = '0' + str(int(time_hours))
        else:
            time_hours = str(int(time_hours))

        if len(str(int(round(time_minutes, 0)))) == 1:
            time_minutes = '0' + str(int(time_minutes))
        else:
            time_minutes = str(int(time_minutes))

        if len(str(int(round(time_seconds, 0)))) == 1:
            time_seconds = '0' + str(int(time_seconds))
        else:
            time_seconds = str(int(time_seconds))

        print(f'Day: {days} \nTime: {time_hours}:{time_minutes}:{time_seconds}')
        break
    except:
        print('This is not a number!')