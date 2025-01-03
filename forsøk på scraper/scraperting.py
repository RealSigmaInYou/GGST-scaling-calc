from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup
import time

dynamic_url = "https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data"
def sigma(dynamic_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    

    try:
        driver.get(dynamic_url)
        check_thing = WebDriverWait(driver, 30).until(
            EC.title_contains("Anji Mito Frame Data")
        )
        print(check_thing)
        if check_thing == True:
            print("klarte")
            page_source = driver.page_source
            suppe = BeautifulSoup(page_source, "html.parser")
            ryddig_html = suppe.prettify()
            new_page_source = ryddig_html.split('<td class="details-control"></td>')
            with open("forsøk på scraper\html_output.txt", "w", encoding="utf-8") as html_dump_area: 
                html_dump_area.write(ryddig_html)
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

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

sigma(dynamic_url)
