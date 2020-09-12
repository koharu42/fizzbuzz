f = open('input.txt')
lines = f.read().splitlines()
target_num = int(lines[-1])
rules_dict = {int(i.split(':')[0]): i.split(':')[1] for i in lines[:-1]}
num_keys = sorted(list(rules_dict.keys()))
output_str = ""
for num in num_keys:
    if target_num%num == 0:
        output_str += rules_dict[num]
if output_str:
    print(output_str)
else:
    print(target_num)
