from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(10)

def robot ():

    browser.get("https://www.instagram.com/accounts/login")
    login_credentials = browser.find_elements_by_css_selector("._2hvTZ.pexuQ.zyHYP")
    login_credentials[0].send_keys("your account")
    login_credentials[1].send_keys("password")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    explore = browser.find_element_by_xpath("//a[@href='/explore/']")
    explore.click()

    sleep(5)
    search_sharp = browser.find_element_by_xpath("//input[@class='XTCLo x3qfX ']")
    search_sharp.send_keys("#python")

    sleep(1)
    search_sharp = browser.find_element_by_xpath("//a[@class='-qQT3']")
    search_sharp.click()

    sleep(1)
    page_like = browser.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
    page_like.click()


    number_like = 0
    number_comment = 0
    while True:
        if number_like < 70:
            # like 70 on day
            sleep(2)
            like = browser.find_element_by_xpath("//span[@class='fr66n']")
            like.click()
            print('like ' , number_like)
            number_like += 1

        elif number_like == 70:
            print('like exited 70 .')
            break


        if number_comment < 70:
            # comment 10 on day
            sleep(2)
            comment = browser.find_element_by_xpath("//span[@class='_15y0l']")
            if comment:
                comment.click()
                comment1 = browser.find_element_by_tag_name("textarea")
                comment1.send_keys(" @pyshoja "
                                   " #pyshoja ")
                                   # " https://github.com/pyshoja "
                                   # " https://gitlab.com/pyshoja "

                sleep(2)
                comment_sent = browser.find_element_by_xpath("//button[@type='submit']")
                comment_sent.click()
                print('comment ' , number_comment)
                number_comment += 1

            else:
                print('dont have a comment input . ')

        elif number_comment == 70 :
            print('comment exited 10 .')
            break

        sleep(5)
        page_next = browser.find_element_by_xpath("//a[@class=' _65Bje  coreSpriteRightPaginationArrow']")
        page_next.click()

        # print('liked')


robot()