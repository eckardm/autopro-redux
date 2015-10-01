'''
first, import what we need'''

from notpasswords import *

# selenium is used automate web browser interaction, you'll need to install it
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
gather some information about the collection'''

# name
name_text = raw_input('Name: ')

# introductory text
# view all items in this collection
view_all_items_in_this_collection_text = open('view-all-items-in-this-collection.txt', 'r').read()

# bentley historical library banner
bentley_historical_library_banner_text = open('bentley-historical-library-banner.txt', 'r').read()

# h2 section
h2_text = '<h2>' + name_text + '</h2>'

# record group or manuscript collection
record_group_or_manuscript_collection_input = raw_input('Is it part of a larger record group or manuscript collection? ')
if record_group_or_manuscript_collection_input == 'yes':
    record_group_input = raw_input('Which one? ')
    if record_group_input == 'record group':
        eadid_text = raw_input('EAD ID: ')
        record_group_text = open('record-group.txt', 'r').read().replace('XXXXX', eadid_text).replace('XXXX', name_text).replace(' / manuscript collection', '')
    elif record_group_input == 'manuscript collection':
        eadid_text = raw_input('EAD ID: ')
        record_group_text = open('record-group.txt', 'r').read().replace('XXXXX', eadid_text).replace('XXXX', name_text).repalce('record groupt / ', '')

        # division of reference and access services
division_of_reference_and_access_services_text = open('division-of-reference-and-access-services.txt', 'r').read()

# abstract
abstract = raw_input('Abstract (HTML): ')
abstract_text = '<p><b>Abstract:</b><br />' + abstract + '</p>'

# history or biography
history_or_biography_input = raw_input('Does this collection have a history or biography? ')
history_or_biography_text_input = raw_input('What is it (HTML)? ')
if history_or_biography_input == 'history':
    history_or_biography_text = '<p><b>History:</b><br />' + history_or_biography_text_input + '</p>'
elif history_or_biography_input == 'biography':
    history_or_biography_text = '<p><b>Biography:</b><br />' + history_or_biography_text_input + '</p>'

# final[ish] product
introductory_text = view_all_items_in_this_collection_text + bentley_historical_library_banner_text + h2_text + record_group_text + division_of_reference_and_access_services_text + abstract_text + history_or_biography_text

# copyright
copyright_text = open('copyright.txt', 'r').read()

# license
license_text = 'As the designated coordinator for this Deep Blue Collection, I am authorized by the Community members to serve as their representative in all dealings with the Repository. As the designee, I ensure that I have read the Deep Blue policies. Furthermore, I have conveyed to the community the terms and conditions outlined in those policies, including the language of the standard deposit license quoted below and that the community members have granted me the authority to deposit content on their behalf.'

# depositor uniqname
uniqname = raw_input('Depositor: ')


'''
create deep blue collection'''

# setup web driver
driver = webdriver.Firefox()

# login
driver.get('http://' + dev_login_id + ':' + dev_password + '@' + 'dev.deepblue.lib.umich.edu:8080/')
driver.get('https://weblogin-test.itcs.umich.edu/?factors=UMICH.EDU&cosign-dev.deepblue.lib&http://dev.deepblue.lib.umich.edu:8080/webiso-login')
driver.find_element_by_id('login').send_keys(login_id)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('loginSubmit').click()

# go to bogus collection
driver.get('http://dev.deepblue.lib.umich.edu:8080/handle/TEMP-BOGUS/235581')

# create collection
driver.find_element_by_link_text('Create Collection').click()

# fill out form
# name
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_name').send_keys(name_text)

# copyright
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_copyright_text').send_keys(copyright_text)

# license
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_license').send_keys(license_text)

# create
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_submit_save').click()

# roles
# administrators
driver.find_element_by_id('aspect_administrative_collection_AssignCollectionRoles_field_submit_create_admin').click()
# mike
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_query').send_keys('shallcro')
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_search_epeople').click()
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_add_eperson_366').click()
# max
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_query').clear()
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_query').send_keys('eckardm')
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_search_epeople').click()
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_add_eperson_4864').click()
# save
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_save').click()

# depositor
driver.find_element_by_id('aspect_administrative_collection_AssignCollectionRoles_field_submit_create_submit').click()
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_query').send_keys(uniqname)
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_search_epeople').click()
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_add_eperson_' + driver.find_element_by_css_selector('td.ds-table-cell.odd').text).click()
# save
driver.find_element_by_id('aspect_administrative_group_EditGroupForm_field_submit_save').click()

# put handle in introductory text
# get handle
driver.find_element_by_id('aspect_administrative_collection_AssignCollectionRoles_field_submit_return').click()
handle = driver.find_element(By.XPATH, '//span[text()="' + name_text + '"]/parent::a').get_attribute('href').split('/')[5]

# add it to introductory text
driver.find_element_by_link_text(name_text).click()
driver.find_element_by_link_text('Edit Collection').click()
driver.find_element_by_id('aspect_administrative_collection_EditCollectionMetadataForm_field_introductory_text').send_keys(introductory_text.replace('XXXXXX', handle))
driver.find_element_by_id('aspect_administrative_collection_EditCollectionMetadataForm_field_submit_save').click()

# that's it, we're done!
driver.close()


'''
known issues'''

# anything where there is raw input needs to be debugged
# more than one record group or manuscript collection
# more than one paragraph
# copyright won't always be transferred
# web archives
# more than one depositor