import os
import sys
import time
import getopt
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getArguments(argv):
    arg_invisible = True
    arg_url = ""
    arg_xpath = ""
    arg_help = """{0}
    -i <True or False>
    -s <site>
    -x <xpath>""".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hs:i:x:", ["help", 
        "site=", "xpath="])
        if opts == []:
            print(arg_help)
            sys.exit(2)
        
    except getopt.GetoptError as err:
        print(err)
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)
            sys.exit(2)
        elif opt in ("-i", "--invisible"):
            arg_invisible = arg
        elif opt in ("-s", "--site"):
            arg_url = arg
        elif opt in ("-x", "--xpath"):
            arg_xpath = arg

    arguments = {
        'invisible': arg_invisible,
        'url': arg_url,
        'xpath': arg_xpath
    }
    
    return arguments



def Download(arguments):
    crdownload = False

    options = EdgeOptions()
    options.use_chromium = True

    if arguments['invisible'] == True:
        options.add_argument('--headless')
    options.add_argument('disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Edge(executable_path='C:\\config\\drivers\\browser\\msedgedriver.exe', options = options)

    try:
        params = {'behavior': 'allow', 'downloadPath': os.environ['userprofile'] + '\\Downloads'}
        driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

        driver.get(arguments['url'])
        if arguments['xpath'] != "":
            for xpath in arguments['xpath'].split(","):
                if xpath.startswith('remove_ads:'):
                    time.sleep(3)
                    driver.execute_script("""const elements = document.getElementsByTagName("iframe");while(elements.length > 0){elements[0].parentNode.removeChild(elements[0]);};const elements2 = document.getElementsByClassName("adsbygoogle");while(elements2.length > 0){elements2[0].parentNode.removeChild(elements2[0]);}""")
                    xpath = xpath[11:]
                            
                print(xpath)
                time.sleep(2)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

        while crdownload == False:
            if any(fname.endswith('.crdownload') for fname in os.listdir(os.environ['userprofile'] + '\\Downloads')):
                crdownload = True

        while crdownload == True:
            for fileName in os.listdir(os.environ['userprofile'] + '\\Downloads'):
                if fileName.startswith('NÃ£o'):
                    os.remove(os.environ['userprofile'] + '\\Downloads\\' + fileName)

            if not any(fname.endswith('.crdownload') for fname in os.listdir(os.environ['userprofile'] + '\\Downloads')):
                crdownload = False

    except Exception as e:
        print(e)
        driver.quit()
        sys.exit(2)
    
    driver.quit()
    sys.exit(2)

if __name__ == "__main__":
    Download(getArguments(sys.argv))

# python .\autopy-downloader.py -s "https://uvnc.com/downloads/ultravnc.html" -x "//tr[@class='cat-list-row0'][1]/td/a,//*[@id='sp-component']/div/div[2]/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/a,//*[@id='jd_agreeForm']/input[1],//*[@id='jd_license_submit']" -i "False"

# /html/body/div/div[1]/div[3]/div
