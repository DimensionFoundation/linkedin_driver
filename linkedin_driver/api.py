from metatype import Dict

from linkedin_driver import _login

from linkedin_driver.utils import (
    open_contact,
    scroll_to_bottom,
    open_interest,
    text_or_default_accomp,
    open_accomplishments,
    open_more,
    flatten_list,
    one_or_default,
    text_or_default,
    all_or_default,
    get_info,
    get_job_info,
    get_school_info,
    get_volunteer_info,
    get_skill_info,
    personal_info,
    experiences,
    skills,
    recommendations
)


class Contact(Dict):

    @classmethod
    def _get(cls, url):

        driver = _login()

        #     '3168095199@qq.com',
        #     'shelock007',
        #     proxies={
        #         "socksProxy": "127.0.0.1:1080"}
        # )

        record = {}

        # INTERESTS
        interests_data = open_interest(driver, url)
        record.update({'interests': interests_data})

        # CONTACT
        contact_data = open_contact(driver, url)
        record.update({'contact': contact_data})

        # <<SCROLL-DOWN>>
        scroll_to_bottom(driver, contact_url=url)

        # ACCOMPLISHMENTS
        accomplishments_data = open_accomplishments(driver)
        record.update({'accomplishments': accomplishments_data})

        # RECOMMENDATIONS
        recommendations_data = recommendations(driver)
        record.update({'recommendations':recommendations_data})

        # <<EXPAND-TABS>>
        open_more(driver)
        import bs4

        # PERSONAL-INFO
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        personal_info_data = personal_info(soup)
        record.update({'personal_info': personal_info_data})

        # EXPERIENCES
        experiences_data = experiences(soup)
        record.update({'experiences': experiences_data})

        # SKILLS
        skills_data = skills(soup)
        record.update({'skills': skills_data})

        # END
        driver.quit()

        return cls(record)


    @classmethod
    def _filter(cls):
        raise NotImplemented

    def send_message(self):
        raise NotImplemented


class Post(Dict):

    def _get(self):
        raise NotImplemented

    @classmethod
    def _filter(cls):
        raise NotImplemented

    def _update(self):
        raise NotImplemented

    def add_comment(self):
        raise NotImplemented


class Comment(Dict):

    def _get(self):
        raise NotImplemented

    def _filter(self):
        raise NotImplemented

    def _update(self):
        raise NotImplemented


class PostLike(dict):
    pass


class CommentLike(Dict):
    pass
