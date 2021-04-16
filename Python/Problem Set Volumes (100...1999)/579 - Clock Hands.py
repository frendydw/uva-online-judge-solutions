while True:
    clock = input()

    if clock == '0:00':
        break

    hour, minute = clock.split(':')

    hour_angle = 0.5 * (int(hour) * 60 + int(minute))
    minute_angle = 6 * int(minute)

    angle = abs(hour_angle-minute_angle)

    print('{:.3f}'.format(min(360 - angle, angle)))