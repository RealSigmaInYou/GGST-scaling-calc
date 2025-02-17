move_info_list = ['', '632146H', 'Issei Ougi: Sai', '13×6,67', 'All', '11+6', '3(6)3(6)3(6)3(6)3(6)3', 'Total 122', '-30', 'HKD +55', 'i', 'Very Small', '', '100%', '350', '1000']
move_info_list_2 =['', '632146S Attack Near', 'Kachoufuugetsu Kai', '53,13×4,49', 'All', '2+1', '', '', '', 'HKD +36', '', '', '', '100%', '', '1000']

hits = []
if "," in move_info_list[3]:
    remove_noise = move_info_list[3].split(",")

for damage in remove_noise:
    if "×" in damage:
        check_for_x = damage.split("×")
        print(check_for_x)
        number_of_hits = int(check_for_x[1])
        print(number_of_hits)
        i = 0
        while i != number_of_hits:
            hits.append(int(check_for_x[0]))
            i +=1
    else:
        hits.append(int(damage))
            
    print(hits)
    
    hits = []



# if "×" in remove_noise:
#     check_for_x = remove_noise.split("×")
#     print(check_for_x)
#     for i in check_for_x:
#         hits.append(int(check_for_x[0]))
# else:
#     print("watersigma")
# print(remove_noise)

# print(hits)