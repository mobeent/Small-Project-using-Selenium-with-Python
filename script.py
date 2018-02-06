from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.get("https://zambeel.lums.edu.pk")
# assert "Python" in driver.title
count = 0
elem = driver.find_element_by_name("userid")
elem.clear()
# enter your username below
elem.send_keys("")
elem = driver.find_element_by_name("pwd")
elem.clear()
# enter you password below
elem.send_keys("")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("fldra_CO_EMPLOYEE_SELF_SERVICE")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("fldra_HCCC_ENROLLMENT")
elem.send_keys(Keys.RETURN)
driver.get("https://zambeel.lums.edu.pk/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_CART_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=HCCC_ENROLLMENT&EOPP.SCLabel=Enrollment&EOPP.SCPTfname=HCCC_ENROLLMENT&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false")
driver.switch_to.frame(driver.find_element_by_name("TargetContent"));
while 1:
	elem = driver.find_element_by_id("DERIVED_REGFRM1_LINK_ADD_ENRL$82$")
	elem.send_keys(Keys.RETURN)
	elem = driver.find_element_by_name("DERIVED_REGFRM1_SSR_PB_SUBMIT")
	elem.send_keys(Keys.RETURN)
	elem = driver.find_element_by_name("DERIVED_REGFRM1_SSR_LINK_STARTOVER")
	elem.send_keys(Keys.RETURN)
	count = count + 1
	print 'Count is: ', count
# assert "No results found." not in driver.page_source
driver.close()
