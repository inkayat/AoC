def solve(time, ids):
    optimum =  min(ids, key= lambda x: x-(time%x))
    return (optimum-(time%optimum))*optimum


if __name__ == "__main__":
    with open('input.txt') as fp:
        lines = fp.readlines()
        time_stamp = int(lines[0])
        bus_ids = list()
        for line in lines[1:]:
            for bus_id in line[:-1].split(','):
                if bus_id != 'x':
                    bus_ids.append(int(bus_id))
    result = solve(time_stamp, bus_ids)
    print(result)
