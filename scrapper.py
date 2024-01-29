from bs4 import BeautifulSoup
import requests
import csv
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

url = "https://www.pccomponentes.com/portatiles?page="


def buscar_cpu(laptop_data):
    cpu = []
    laptop_data.reverse()
    for el in laptop_data:
        cpu.append(el)
        if el == 'intel' or el == 'amd' or 'm' in el:
            return ' '.join(cpu[::-1])

def buscar_gpu(laptop_data):
    gpu = []
    for el in laptop_data:
        
        if 'rtx' in el or 'radeon' in el  or 'gpu' in el:
            return el
    
    return 'integrated graphics'

def bucar_opsys(laptop_data,marca):
    if marca == 'Apple':
        return 'MacOs'
    
    if 'windows' in laptop_data[-1]: 
        return 'Windows'
    
    return 'No Os/ Linux'

def guarda_datos_html(i=0):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        
        time.sleep(5)
        driver.get(url+str(i))
        
        accept_cookies = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'cookiesAcceptAll'))
        )
        
        accept_cookies.click()
        
        html = driver.page_source
        
        with open(f'html\\laptops_{i}.html','w',encoding="utf-8") as document:
            document.write(html)
            
        driver.close()
    except:
        print(f'Error en página: {i}')

def get_datos_html(i=1):
    try:
        with open(f'laptop_data_actual.csv','+a') as ldata:
            
            field = ['Company','Inches','Cpu','Ram','Gpu','OpSys','SSD','Price']
            writer = csv.DictWriter(ldata, fieldnames=field)
                
            
            with open(f'html\\laptops_{i}.html','r',encoding="utf-8") as document:
                html = BeautifulSoup(document.read(), 'html.parser')
                products = html.find_all('a')
                
                for element in products:
                    pc = element.get('data-product-name')
                    if pc:
                        pc = pc.lower()
                        marca = element.get('data-product-brand')
                        price = element.get('data-product-price')
                        pc_data = pc.split('/')
                        cpu = pc_data[0].split(' ')
                        
                        cpu = buscar_cpu(cpu)
                        gpu = buscar_gpu(pc_data)
                        inches = '.'.join([s for s in re.findall(r'\b\d+\b', pc_data[-1])])
                        OpSys = bucar_opsys(pc_data,marca)
                        # print(['Company','Inches','Cpu','Ram','Gpu','OpSys','SSD','Price'])
                        # print([marca,inches,cpu,pc_data[1],gpu,OpSys,pc_data[2],price])
                            
                        row = {
                            'Company':marca,
                            'Inches':inches,
                            'Cpu':cpu,
                            'Ram':pc_data[1],
                            'Gpu':gpu,
                            'OpSys':OpSys,
                            'SSD':pc_data[2],
                            'Price':price
                        }
                            
                        writer.writerow(row)
    except:
        print(f'Error en página: {i}')
    
                    
                    
            
def main():
    for i in range(21,58):
        guarda_datos_html(i)
        time.sleep(30)
        get_datos_html(i)
    
    print('Done!!')
main()