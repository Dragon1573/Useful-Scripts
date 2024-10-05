# encoding: UTF-8
from os.path import dirname, join

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://docs.qq.com/form/page/DRnRDTklESlN4WERw"  # 在线收集表的 URL 地址

if __name__ == "__main__":
    services = webdriver.EdgeService(
        # 需要下载 EdgeDriver x64 版本，在项目根目录解压到 edgedriver_win64 目录下
        join(dirname(__file__), "edgedriver_win64", "msedgedriver.exe")
    )
    with webdriver.Edge(service=services) as driver:
        # 访问表单 URL
        driver.get(URL)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "blankpage-button-pc"))
        ).click()
        WebDriverWait(driver, 15).until(
            # 使用 QQ 互联登录
            EC.presence_of_element_located((By.XPATH, "//span[@class='qq']"))
        ).click()

        # 提供1分钟手动登录时长
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='请输入']")
            )
        )

        # 操作链
        (
            ActionChains(driver)
            .move_to_element(element)
            .click()
            .send_keys("啊对对队", Keys.TAB)
            .send_keys("比利·海灵顿", Keys.TAB)
            .send_keys("1145141919810", Keys.TAB)
            .send_keys("田所浩二")
            .send_keys(Keys.TAB, Keys.ENTER)
            .perform()
        )
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dui-button-container' and text()='确认']")
            )
        ).click()

        # 检查是否提交成功
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@type='form-submit-result-success']")
            )
        )
