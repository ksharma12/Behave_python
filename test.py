# from selenium import webdriver
#
# driver = webdriver.Chrome()
# asdf = driver.find_elements()
# asdf[1].find_element()
# print("asdf_asdf".replace("_", " "))
import inspect
import oR


def get_variable_name(var):
    for name, value in inspect.getmembers(object_repository):
        if value is var:
            return name
    return None

turbulacne = 'asdasfafdjvdbjvdsjvsd'
# print(get_variable_name(object_repository.))
# print(get_variable_name(x))  # Output: x
# print(get_variable_name(y))  # Output: y
# print(get_variable_name(10))  # Output: None
# print(object_repository.z)  # Output: 20
# print(get_variable_name(object_repository.z))  # Output: z
