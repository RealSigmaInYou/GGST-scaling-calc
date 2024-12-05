from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup
dynamic_url = "https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data"
def sigma(dynamic_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        
        driver.get(dynamic_url)
        page_source = driver.page_source
        suppe = BeautifulSoup(page_source, "html.parser")
        ryddig_html = suppe.prettify()
        
        regex = r"""<tr.*?>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(-?\d+)</td>\s*<td>(\+?\d+)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(\d+)%</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>"""
        matches = re.findall(regex, page_source)
        print(6)
        for match in matches:
            print("huh?")
            for watersigma in match:
                print("what")

                print(watersigma, "agagagagagagagagagagagagagagagagagagagagagag")
            suppe = BeautifulSoup(match, "html.parser")
            print(2)
            print(suppe.prettify())


        # new_page_source = page_source.split('<td class="details-control"></td>')
        
        # for bakaraka in new_page_source:
        #     splitchan = bakaraka.split("                          ")
        #     for w in splitchan:
        #         splitchan = w.split("</td>\t\t\t\t<td></td>\t\t\t\t<td")
        #         # regex = r"""<tr.*?>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(-?\d+)</td>\s*<td>(\+?\d+)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(\d+)%</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>"""
        #         for thigma in splitchan:
        #             water = thigma.split()
        #             # matches = re.findall(regex, thigma)
        #             for match in water:
        #                 print(match)
        #                 print("aikaaia")
        #                 if match == "":
        #                     print("watersigma")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

sigma(dynamic_url)


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import re
# dynamic_url = "https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data"
# def sigma(dynamic_url):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     driver = webdriver.Chrome(options=chrome_options)

#     try:
#         driver.get(dynamic_url)
#         page_source = driver.page_source
#         new_page_source = page_source.split('<td class="details-control"></td>')
        
#         for bakaraka in new_page_source:
#             splitchan = bakaraka.split("                          ")
#             regex = r"""<tr.*?>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>\s*<td>(-?\d+)</td>\s*<td>(\+?\d+)</td>\s*<td>(\d+)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(\d+)%</td>\s*<td>(\d+)</td>\s*<td>(\d+)</td>"""

#             for thigma in splitchan:
#                 matches = re.findall(regex, thigma)
#                 for match in matches:
#                     print(match)
#                     print("aikaaia")
#                     if match == "":
#                         print("watersigma")

#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         driver.quit()

# sigma(dynamic_url)

# import requests
# character = "Anji_Mito"
# dynamic_url = "https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data"

# def sigma(dynamic_url):
#     character_html = requests.get(dynamic_url, timeout=600)


#     print(character_html.text)

# sigma(dynamic_url)