import operator

from bowling_engine import analyzing_result


def file_handler(read_file, write_file):
    with open(file=read_file, mode='r', encoding='UTF-8') as read_file:
        with open(file=write_file, mode='a', encoding='utf8') as write_file:
            res = {}
            for line in read_file:
                if '###' in line:
                    number_symbol, tour, tour_id = line.split(' ')
                    write_file.write(f'\n{number_symbol} {tour} {tour_id}')
                    continue
                elif 'winner' in line:
                    winner, _is, dots = line[:-1].split(' ')
                    try:
                        _max = max(res.items(), key=operator.itemgetter(1))[0]
                        write_file.write(f'{winner} {_is} {_max} !!! \n')
                    except Exception:
                        write_file.write(f'В этом туре нет победителей... + \n')
                    res = {}
                    continue
                if not line.strip():
                    pass
                else:
                    player_name = line[:-1].split()
                    try:
                        count_res = analyzing_result(result=player_name[1])
                        write_file.write(f'{player_name[0]:<8} {player_name[1]:<20} --> {count_res} \n')
                        res.update({player_name[0]: count_res})
                    except Exception as exc:
                        write_file.write(f'{player_name[0]:<8} Дисквалифицирован! {exc} \n')
