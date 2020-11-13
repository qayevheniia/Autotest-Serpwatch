import datetime
import email
import imaplib
import re
import time
from email import policy
from email.parser import BytesParser


class MailService:
    def __init__(
        self,
        user: str,
        password: str,
        time_wait: int = 20,
        time_sleep: int = 3,
        send_time: datetime = None,
        mailbox: str = "inbox",
        imap: str = "imap.gmail.com",
        pattern: str = "serpwatch.io/email/verify/",
        from_email: str = "notifications@serp-watch.com",
    ):
        self.mail = None
        self.imap = imap
        self.mailbox = mailbox
        self.pattern = pattern
        self.max_time_wait = time_wait
        self.time_sleep = time_sleep
        self.send_time = send_time
        self.from_email = from_email

        self.user = user
        self.password = password

        self.verify_url = ""

        self.link_regex = (
            r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]"
            r"{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+"
            r"(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        )

        if not self.mail:
            self._login()

    def _login(self):
        """
            Identify client using user and password.
​
            :return: None
        """

        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
        self.mail.login(self.user, self.password)

    def _select_mailbox(self, mailbox: str):
        """
            Select a mailbox.
​
            :param str mailbox: mailbox name.
            :return: None
        """

        self.mail.select(mailbox)

    def _find_link_by_pattern(self, body: list, pattern: str):
        """
            Find link by pattern.
​
            :param list body: mailbox name.
            :param str pattern: pattern.
            :return: None
        """

        for line in body:
            find_urls = re.findall(self.link_regex, line)
            if find_urls:
                urls = [x[0] for x in find_urls]
                for url in urls:
                    if url.find(pattern) != -1:
                        return url

    def _mail_ids(self):
        """
            Get all mail ids.
​
            :return: None
        """

        self._select_mailbox(mailbox=self.mailbox)
        _, mail_data = self.mail.search(None, "ALL")
        ids_list = mail_data[0].split()
        first_email_id = int(ids_list[0])
        latest_email_id = int(ids_list[-1])
        return range(latest_email_id, first_email_id, -1)

    def _find_verify_url(self, send_time: datetime = None):
        """
            find verify url.
​
            :return: None
        """

        for _id in self._mail_ids():
            _, data = self.mail.fetch(str(_id), "(RFC822)")
            try:
                msg = email.message_from_string(data[0][1])
            except TypeError:
                msg = email.message_from_bytes(data[0][1])

            if msg["from"].find(self.from_email) != -1:
                is_check = True
                date_tuple = email.utils.parsedate_tz(msg["date"])
                msg_date = datetime.datetime.fromtimestamp(
                    email.utils.mktime_tz(date_tuple)
                )

                print("_find_verify_url")
                print(msg_date)

                if send_time:
                    is_check = False
                    if send_time <= msg_date:
                        is_check = True
                if is_check:
                    body_msg = BytesParser(policy=policy.default).parsebytes(data[0][1])
                    body = body_msg.get_body(preferencelist=("plain", "html"))
                    verify_url = self._find_link_by_pattern(
                        body=body.get_content().splitlines(), pattern=self.pattern
                    )
                    if verify_url:
                        return verify_url

    def find_registration_verify_url(self):
        """
            find registration confirmation url.
​
            :return: None
        """

        time_wait = 0
        print("find_registration_verify_url")
        print(self.send_time)
        while time_wait < self.max_time_wait:
            time.sleep(self.time_sleep)
            self.verify_url = self._find_verify_url(send_time=self.send_time)
            if self.verify_url:
                break
            else:
                time_wait += self.time_sleep


