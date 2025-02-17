from bs4 import BeautifulSoup

# with open("forsøk på scraper\html_output.txt", "r") as html_dump_area:
#     html_dump_area_plzman = html_dump_area.read()

filopen = open("forsøk på scraper\html_output.txt", encoding="utf-8")  


def sigma(dynamic_url):

    page_source = dynamic_url
    suppe = BeautifulSoup(page_source, "html.parser")
    ryddig_html = suppe.prettify()
    tables = []

    table_id = 0
    table_rows = []
    all_tables = suppe.find_all('table')

    for table in all_tables:
        rows = table.find_all('tr')
        for row in (rowa for rowa in rows if len(rowa) >= 14):
            cells = row.find_all('td')
            cells = [element.text.strip() for element in cells]
            table_rows.append(cells)
        table_id+=1
    
    for rowthing in table_rows:
        charged_ver_row = rowthing
        semicharged_ver_row = rowthing
        if rowthing != []:    
            if rowthing[0] == "":
                print(rowthing)
                hits = []
                try:
                    remove_noise = rowthing[2].split(",")
                    for number_but_str in remove_noise:
                        if "[" in number_but_str:
                            charged_number = number_but_str.split("[")
                            for x in charged_number:
                                if "]" in x:
                                    x.removesuffix("]")
                                    charged_ver_row[2] = x
                                else: 
                                    rowthing[2] = rowthing[2]+ x


                        if "{" in number_but_str:
                            semi_charged_number = number_but_str.split("{")
                            for x in semi_charged_number:
                                if "}" in x:
                                    x.removesuffix("}")
                                    semicharged_ver_row[2] = x
                                else: 
                                    rowthing[2] = rowthing[2] + x
                                

                        if "×" in number_but_str:
                            check_for_x = number_but_str_2.split("×")
                            for i in len(int(check_for_x[1])):
                                hits.append(int(check_for_x[0]))
                        else:
                            number_but_int = int(number_but_str)
                            hits.append(number_but_int)

                except:
                    try:
                        remove_commas = rowthing[3].split(",")
                        for number_but_str_2 in remove_commas:
                            if "[" in number_but_str_2:
                                charged_number = number_but_str.split("[")
                                for x in charged_number:
                                    if "]" in x:
                                        x.removesuffix("]")
                                        charged_ver_row[3] = x
                                    else: 
                                        rowthing[3] = rowthing[3] + x
                                number_but_str_2[3] = number_but_str_2[3]
                                        

                            if "{" in number_but_str_2:
                                semi_charged_number = number_but_str.split("{")
                                for x in semi_charged_number:
                                    if "}" in x:
                                        x.removesuffix("}")
                                        semicharged_ver_row[3] = x
                                    else: 
                                        rowthing[3] = rowthing[3] + x

                            print(number_but_str_2)
                            if "×" in number_but_str_2:
                                print("bakaraka")
                                check_for_x = number_but_str_2.split("×")
                                for i in len(int(check_for_x[1])):
                                    hits.append(int(check_for_x[0]))
                            else:
                                number_but_int = int(number_but_str_2)
                                hits.append(number_but_int)
                    except Exception as a:
                        print("neither the 2nd index nor the third index are attacks. this is so not sigma", a)
                finally:
                    print(hits)


    print("finished")
    
    # for bakaraka in ryddig_html:
    #     html_dump_area.write(bakaraka + "\n")
    
    # regex = r"""<tr.*?>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(-?\d+)</td>\s*<td>(\+?\d+)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(\d+)%</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>"""
    # matches = re.findall(regex, page_source)
    # print(ryddig_html)
    # for match in matches:
    #     suppe = BeautifulSoup(match, "html.parser")
    #     print(suppe.prettify())


    # new_page_source = page_source.split('<td class="details-control"></td>')
    
    # for bakaraka in new_page_source:
    #     splitchan = bakaraka.split("                          ")
    #     for w in splitchan:
    #         splitchan = w.split("</td>\t\t\t\t<td></td>\t\t\t\t<td")
    #         for thigma in splitchan:
    #             water = thigma.split()
    #             matches = re.findall(regex, thigma)
    #             for match in water:
    #                 print(match)
    #                 if match == "":
    #                     print("watersigma")

sigma(filopen)
