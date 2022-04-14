temperature_range_arr = input('최소 온도와 최대 온도를 입력 : ').split()
machine_temperature_arr = input('기계 온도를 입력 : ').split()

for machine_temperature in machine_temperature_arr:
    machine_temperature = int(machine_temperature)

    if (machine_temperature == -999): break

    if(machine_temperature < int(temperature_range_arr[0]) or machine_temperature > int(temperature_range_arr[1])):
        print('Alert!')
        break
    
    else:
        print('Nothing to report')
        
