import pytest

from homework.demoqa_tests.model.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()

def test_submit_form():
    registration_page.open()
    registration_page.set_name("Michael")
    registration_page.set_last_name("Rodionov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Michael Rodionov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )

def test_submit_form2():
    registration_page.open()
    registration_page.set_name("Valentin")
    registration_page.set_last_name("Rodionov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Valentin Rodionov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )

def test_submit_form3():
    registration_page.open()
    registration_page.set_name("Liam")
    registration_page.set_last_name("Redin")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Liam Redin',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )

def test_submit_form4():
    registration_page.open()
    registration_page.set_name("Zahar")
    registration_page.set_last_name("Mironov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Zahar Mironov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )

def test_submit_form_failed():
    registration_page.open()
    registration_page.set_name("Ivan")
    registration_page.set_last_name("Mironov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Zahar Mironov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )

def test_submit_form_failed2():
    registration_page.open()
    registration_page.set_name("Maria")
    registration_page.set_last_name("Mironov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Ivan Mironov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )

@pytest.mark.skip
def test_submit_form_failed2():
    registration_page.open()
    registration_page.set_name("Maria")
    registration_page.set_last_name("Mironov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Ivan Mironov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )