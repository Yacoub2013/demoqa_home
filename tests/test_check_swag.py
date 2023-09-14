from conftest import browser
from pages.swag_labs import SwagLab

def test_1(browser):
    sw_ag_labs = SwagLab(browser)
    sw_ag_labs.visit()
    assert sw_ag_labs.exist_icon()
def test_2(browser):
    sw_ag_labs = SwagLab(browser)
    sw_ag_labs.visit()
    assert sw_ag_labs.exist_user_name()

def test_3(browser):
    sw_ag_labs = SwagLab(browser)
    sw_ag_labs.visit()
    assert sw_ag_labs.exist_password()







