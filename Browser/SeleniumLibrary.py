from robotlibcore import keyword
from Browser import Browser
from .assertion_engine import AssertionOperator
from .keywords.waiter import ElementState
from .keywords.input import SelectAttribute, MouseButton, KeyboardModifier
from .keywords.playwright_state import SupportedBrowsers

br = Browser()


@keyword(tags=['NotImplemented'])
def add_cookie(name, value, path="None", domain="None", secure="None", expiry="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def add_location_strategy(strategy_name, strategy_keyword, persist="False"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def alert_should_be_present(text="", action="ACCEPT", timeout="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def alert_should_not_be_present(action="ACCEPT", timeout="0"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def assign_id_to_element(locator, id):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def capture_element_screenshot(locator, filename="selenium-element-screenshot-{index}.png"):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def capture_page_screenshot(filename="selenium-screenshot-{index}.png"):
    br.take_page_screenshot(filename)  # ToDo: filename could habe {index} in it.
    raise NotImplementedError


@keyword(tags=['Implemented'])
def checkbox_should_be_selected(locator):
    br.get_checkbox_state(locator, AssertionOperator['=='], True)


@keyword(tags=['Implemented'])
def checkbox_should_not_be_selected(locator):
    br.get_checkbox_state(locator, AssertionOperator['=='], False)


@keyword(tags=['NotImplemented'])
def choose_file(locator, file_path):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def clear_element_text(locator):
    br.clear_text(locator)


@keyword(tags=['PartImplemented'])
def click_button(locator, modifier="False"):
    br.click(locator)


@keyword(tags=['PartImplemented'])
def click_element(locator, modifier="False", action_chain="False"):
    br.click(locator)


@keyword(tags=['Implemented'])
def click_element_at_coordinates(locator, xoffset, yoffset):
    br.click_with_options(locator, position_x=xoffset, position_y=yoffset)


@keyword(tags=['PartImplemented'])
def click_image(locator, modifier="False"):
    br.click(locator)


@keyword(tags=['PartImplemented'])
def click_link(locator, modifier="False"):
    br.click(locator)


@keyword(tags=['PartImplemented'])
def close_all_browsers():
    br.close_browser()


@keyword(tags=['Implemented'])
def close_browser():
    br.close_browser()


@keyword(tags=['Implemented'])
def close_window():
    br.close_page()


@keyword(tags=['NotImplemented'])
def cover_element(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def create_webdriver(driver_name, alias="None", kwargs="{}", **init_kwargs):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def current_frame_should_contain(text, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def current_frame_should_not_contain(text, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def delete_all_cookies():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def delete_cookie(name):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def double_click_element(locator):
    br.click_with_options(locator, click_count=2, delay='100ms')


@keyword(tags=['NotImplemented'])
def drag_and_drop(locator, target):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def drag_and_drop_by_offset(locator, xoffset, yoffset):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def element_attribute_value_should_be(locator, attribute, expected, message="None"):
    br.get_attribute(locator, attribute, AssertionOperator['=='], expected)


@keyword(tags=['NotImplemented'])
def element_should_be_disabled(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def element_should_be_enabled(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def element_should_be_focused(locator):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def element_should_be_visible(locator, message="None"):
    br.wait_for_elements_state(locator, ElementState.visible, timeout='0 ms')


@keyword(tags=['NotImplemented'])
def element_should_contain(locator, expected, message="None", ignore_case="False"):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def element_should_not_be_visible(locator, message="None"):
    br.wait_for_elements_state(locator, ElementState.hidden, timeout='0 ms')


@keyword(tags=['NotImplemented'])
def element_should_not_contain(locator, expected, message="None", ignore_case="False"):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def element_text_should_be(locator, expected, message="None", ignore_case="False"):
    br.get_text(locator, AssertionOperator['=='], expected)


@keyword(tags=['PartImplemented'])
def element_text_should_not_be(locator, not_expected, message="None", ignore_case="False"):
    br.get_text(locator, AssertionOperator['!='], not_expected)


@keyword(tags=['NotImplemented'])
def execute_async_javascript(*code):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def execute_javascript(*code):
    return br.execute_javascript_on_page(code)


@keyword(tags=['NotImplemented'])
def frame_should_contain(locator, text, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_all_links():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_browser_aliases():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_browser_ids():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_cookie(name):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_cookies(as_dict="False"):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def get_element_attribute(locator, attribute):
    return br.get_attribute(locator, attribute)


@keyword(tags=['Implemented'])
def get_element_count(locator):
    return br.get_element_count(locator)


@keyword(tags=['NotImplemented'])
def get_element_size(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_horizontal_position(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_list_items(locator, values="False"):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def get_location():
    return br.get_url()


@keyword(tags=['NotImplemented'])
def get_locations(browser="CURRENT"):
    raise NotImplementedError
    # locations = []
    # catalog = br.get_browser_catalog()
    # for browser in catalog:
    #     for context in browser['contexts']:
    #         for page in context['pages']:
    #             if browser[]


@keyword(tags=['Implemented'])
def get_selected_list_label(locator):
    labels = br.get_selected_options(locator, SelectAttribute.label)
    if len(labels) > 0:
        return labels[0]


@keyword(tags=['Implemented'])
def get_selected_list_labels(locator):
    return br.get_selected_options(locator, SelectAttribute.label)


@keyword(tags=['Implemented'])
def get_selected_list_value(locator):
    values = br.get_selected_options(locator, SelectAttribute.value)
    if len(values) > 0:
        return values[0]


@keyword(tags=['Implemented'])
def get_selected_list_values(locator):
    return br.get_selected_options(locator, SelectAttribute.value)


@keyword(tags=['NotImplemented'])
def get_selenium_implicit_wait():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_selenium_speed():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_selenium_timeout():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_session_id():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_source():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_table_cell(locator, row, column, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def get_text(locator):
    br.get_text(locator)


@keyword(tags=['Implemented'])
def get_title():
    br.get_title()


@keyword(tags=['Implemented'])
def get_value(locator):
    br.get_textfield_value(locator)


@keyword(tags=['NotImplemented'])
def get_vertical_position(locator):
    raise NotImplementedError


@keyword(name="Get WebElement", tags=['NotImplemented'])
def get_webelement(locator):
    raise NotImplementedError


@keyword(name="Get WebElements", tags=['NotImplemented'])
def get_webelements(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_window_handles(browser="CURRENT"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_window_identifiers(browser="CURRENT"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_window_names(browser="CURRENT"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def get_window_position():
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def get_window_size(inner="False"):
    return br.get_viewport_size()


@keyword(tags=['NotImplemented'])
def get_window_titles(browser="CURRENT"):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def go_back():
    br.go_back()


@keyword(tags=['Implemented'])
def go_to(url):
    br.go_to(url)


@keyword(tags=['NotImplemented'])
def handle_alert(action="ACCEPT", timeout="None"):
    raise NotImplementedError


@keyword(tags=['Implemented'])
def input_password(locator, password, clear="True"):
    br.type_secret(locator, password, clear=clear)


@keyword(tags=['Implemented'])
def input_text(locator, text, clear="True"):
    br.type_text(locator, text, clear=clear)


@keyword(tags=['NotImplemented'])
def input_text_into_alert(text, action="ACCEPT", timeout="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def list_selection_should_be(locator, *expected):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def list_should_have_no_selections(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def location_should_be(url, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def location_should_contain(expected, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def locator_should_match_x_times(locator, x, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def log_location():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def log_source(loglevel="INFO"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def log_title():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def maximize_browser_window():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def mouse_down(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def mouse_down_on_image(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def mouse_down_on_link(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def mouse_out(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def mouse_over(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def mouse_up(locator):
    raise NotImplementedError


@keyword(tags=['PartImplemented'])
def open_browser(url="None",
                 browser="firefox",
                 alias="None",
                 remote_url="False",
                 desired_capabilities="None",
                 ff_profile_dir="None",
                 options="None",
                 service_log_path="None",
                 executable_path="None",
                 ):
    if browser.lower() in ['firefox', 'ff']:
        browser = SupportedBrowsers.firefox
        headless = False
    elif browser.lower() in ['googlechrome', 'chrome', 'gc']:
        browser = SupportedBrowsers.chromium
        headless = False
    elif browser.lower() == 'headlesschrome':
        browser = SupportedBrowsers.chromium
        headless = True
    elif browser.lower() == 'headlessfirefox':
        browser = SupportedBrowsers.firefox
        headless = True
    elif browser.lower() == 'safari':
        browser = SupportedBrowsers.webkit
        headless = False
    else:
        raise ValueError(f'{browser} is not a supported Browser.')
    Browser().open_browser(url, browser, headless)


@keyword(tags=['NotImplemented'])
def open_context_menu(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain(text, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_button(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_checkbox(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_element(locator, message="None", loglevel="TRACE", limit="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_image(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_link(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_list(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_radio_button(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_contain_textfield(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain(text, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_button(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_checkbox(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_element(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_image(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_link(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_list(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_radio_button(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def page_should_not_contain_textfield(locator, message="None", loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def press_key(locator, key):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def press_keys(locator="None", *keys):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def radio_button_should_be_set_to(group_name, value):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def radio_button_should_not_be_selected(group_name):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def register_keyword_to_run_on_failure(keyword):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def reload_page():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def remove_location_strategy(strategy_name):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def scroll_element_into_view(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_all_from_list(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_checkbox(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_frame(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_from_list_by_index(locator, *indexes):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_from_list_by_label(locator, *labels):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_from_list_by_value(locator, *values):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_radio_button(group_name, value):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def select_window(locator="MAIN", timeout="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_browser_implicit_wait(value):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_focus_to_element(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_screenshot_directory(path):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_selenium_implicit_wait(value):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_selenium_speed(value):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_selenium_timeout(value):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_window_position(x, y):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def set_window_size(width, height, inner="False"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def simulate_event(locator, event):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def submit_form(locator="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def switch_browser(index_or_alias):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def switch_window(locator="MAIN", timeout="None", browser="CURRENT"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def table_cell_should_contain(locator, row, column, expected, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def table_column_should_contain(locator, column, expected, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def table_footer_should_contain(locator, expected, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def table_header_should_contain(locator, expected, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def table_row_should_contain(locator, row, expected, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def table_should_contain(locator, expected, loglevel="TRACE"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def textarea_should_contain(locator, expected, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def textarea_value_should_be(locator, expected, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def textfield_should_contain(locator, expected, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def textfield_value_should_be(locator, expected, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def title_should_be(title, message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def unselect_all_from_list(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def unselect_checkbox(locator):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def unselect_frame():
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def unselect_from_list_by_index(locator, *indexes):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def unselect_from_list_by_label(locator, *labels):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def unselect_from_list_by_value(locator, *values):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_for_condition(condition, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_element_contains(locator, text, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_element_does_not_contain(locator, text, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_element_is_enabled(locator, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_element_is_not_visible(locator, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_element_is_visible(locator, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_location_contains(expected, timeout="None", message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_location_does_not_contain(location, timeout="None", message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_location_is(expected, timeout="None", message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_location_is_not(location, timeout="None", message="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_page_contains(text, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_page_contains_element(locator, timeout="None", error="None", limit="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_page_does_not_contain(text, timeout="None", error="None"):
    raise NotImplementedError


@keyword(tags=['NotImplemented'])
def wait_until_page_does_not_contain_element(locator, timeout="None", error="None", limit="None"):
    raise NotImplementedError
