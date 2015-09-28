from notpasswords import *

# selenium is used automate web browser interaction, you'll need to install it
from selenium import webdriver


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

introductory_text = view_all_items_in_this_collection_text + bentley_historical_library_banner_text + h2_text + record_group_text + division_of_reference_and_access_services_text + abstract_text + history_or_biography_text

# copyright
copyright_text = open('copyright.txt', 'r').read()

# liscense
liscense_text = 'As the designated coordinator for this Deep Blue Collection, I am authorized by the Community members to serve as their representative in all dealings with the Repository. As the designee, I ensure that I have read the Deep Blue policies. Furthermore, I have conveyed to the community the terms and conditions outlined in those policies, including the language of the standard deposit license quoted below and that the community members have granted me the authority to deposit content on their behalf.'


# create deep blue collection
# setup web driver
driver = webdriver.Firefox()

# login
driver.get('https://weblogin.umich.edu/?factors=UMICH.EDU&cosign-deepblue.lib&http://deepblue.lib.umich.edu/webiso-login')
driver.find_element_by_id('login').send_keys(login_id)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('loginSubmit').click()

# go to archival collections
driver.get('http://deepblue.lib.umich.edu/handle/2027.42/65133')

# create collection
driver.find_element_by_link_text('Create Collection').click()

# name
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_name').send_keys(name_text)

# introductory text
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_introductory_text').send_keys(introductory_text)

# copyright
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_copyright_text').send_keys(copyright)

# license
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_license').send_keys(license)

# create
driver.find_element_by_id('aspect_administrative_collection_CreateCollectionForm_field_submit_save').click()

# assign roles

# go back and add handle

'''
known issues'''
# anything where there is raw input needs to be debugged
# more than one record group or manuscript collection
# copyright won't always be transferred
# web archives