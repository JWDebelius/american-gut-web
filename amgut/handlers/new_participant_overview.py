from tornado.web import authenticated

from amgut.handlers.base_handlers import BaseHandler


class NewParticipantOverviewHandler(BaseHandler):
    """"""
    @authenticated
    def get(self):
        self.render("new_participant_overview.html", skid=self.current_user)
