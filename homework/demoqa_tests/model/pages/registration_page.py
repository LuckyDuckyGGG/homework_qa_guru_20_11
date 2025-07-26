import allure
from selene import browser, have

from homework.demoqa_tests import resource


class RegistrationPage:

    def __init__(self, setup_browser):
        self.browser = setup_browser
        self.registration_user_data = self.browser.element('.table-responsive').all('td').even
        self.state = self.browser.element('#state')
        self.city = self.browser.element('#city')
        self.dropdown = self.browser.all('[id^=react-select][id*=option]')

    @allure.step("Открываем форму регистрации")
    def open(self):
        self.browser.config.window_width = 1920
        self.browser.config.window_height = 1080
        self.browser.open('https://demoqa.com/automation-practice-form')

    @allure.step("Заполняем имя")
    def set_name(self, value):
        self.browser.element('#firstName').type(value)

    @allure.step("Заполняем фамилию")
    def set_last_name(self, value):
        self.browser.element('#lastName').type(value)

    @allure.step("Заполняем email")
    def set_email(self, value):
        self.browser.element('#userEmail').type(value)

    @allure.step("Выбираем пол")
    def set_gender(self, gender):
        if gender == "Male":
            self.browser.element(f'[for="gender-radio-1"]').click()
        elif gender == "Female":
            self.browser.element(f'[for="gender-radio-2"]').click()
        elif gender == "Other":
            self.browser.element(f'[for="gender-radio-3"]').click()

    @allure.step("Заполняем номер телефона")
    def set_phone_number(self, value):
        self.browser.element('#userNumber').type(value)

    @allure.step("Указываем дату рождения")
    def set_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--otside-month)').click()

    @allure.step("Выбираем занятия")
    def set_subject(self, value):
        self.browser.element('#subjectsInput').type(value).press_enter()

    @allure.step("Выбираем хобби")
    def set_hobbies(self, *hobbies) -> None:
        hobbies_mapping = {
            "Sports": '1',
            "Reading": '2',
            "Music": '3'
        }

        for hobby in hobbies:
            if hobby in hobbies_mapping:
                self.browser.element(f'[for="hobbies-checkbox-{hobbies_mapping[hobby]}"]').click()

    @allure.step("Добавляем фото")
    def upload_picture(self):
        self.browser.element('#uploadPicture').set_value(resource.path('photo.jpg'))

    @allure.step("Указываем адрес")
    def set_address(self, value):
        self.browser.element('#currentAddress').type(value)

    @allure.step("Указываем штат")
    def set_state(self, value):
        self.state.click()
        self.dropdown.element_by(
            have.exact_text(value)
        ).click()

    @allure.step("Указываем город")
    def set_city(self, value):
        self.city.click()
        self.dropdown.element_by(
            have.exact_text(value)
        ).click()

    @allure.step("Отправляем форму")
    def submit_form(self):
        self.browser.element('#submit').click()

    @allure.step("Проверяем данные после отправки форму")
    def should_registration_user_data(self, full_name, email, gender, phone_number, date_of_birth, subject, hobbies, picture, address, state_and_city):
        self.browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobbies,
                picture,
                address,
                state_and_city
            )
        )