#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" STEP FIVE """

import logging
import re


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)


def parse_to_meaning_ful_text(in_dict):
    """ convert the dictionary returned in STEP FOUR
    into Telegram HTML text """
    me_t = ""
    me_t += "<i>App Configuration</i>"
    me_t += "\n"
    me_t += "<b>APP ID</b>: "
    me_t += "<code>{}</code>".format(in_dict["App Configuration"]["app_id"])
    me_t += "\n"
    me_t += "<b>API HASH</b>: "
    me_t += "<code>{}</code>".format(in_dict["App Configuration"]["api_hash"])
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>Available MTProto Servers</i>"
    me_t += "\n"
    me_t += "<b>Production Configuration</b>: "
    me_t += "<code>{}</code>".format(
        in_dict["Available MTProto Servers"]["production_configuration"]
    )
    me_t += "\n"
    me_t += "<b>Test Configuration</b>: "
    me_t += "<code>{}</code>".format(
        in_dict["Available MTProto Servers"]["test_configuration"]
    )
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>Disclaimer</i>: "
    me_t += "<u>{}</u>".format(
        in_dict["Disclaimer"]
    )
    return me_t


def extract_code_imn_ges(ptb_message):
    """ extracts the input message, and returns the
    Telegram Web login code"""
    # initialize a variable that can be used
    # to store the web login code after a
    # sequence of conditionals
    telegram__web_login_code = None
    # the original message text sent by the user
    incoming_message_text = ptb_message.text
    # lower case can be used as a helper in the
    # comparison logic
    # N.B.: the PASSWORD is case sensitive,
    # so, "telegram__web_login_code" should have the original text,
    # without conversion
    incoming_message_text_in_lower_case = incoming_message_text.lower()
    if "web login code" in incoming_message_text_in_lower_case:
        parted_message_pts = incoming_message_text.split("\n")
        # this logic is deduced by Trial and Error
        if len(parted_message_pts) >= 2:
            telegram__web_login_code = parted_message_pts[1]
            # there might be a better way, but 😐😪😪
    elif "\n" in incoming_message_text_in_lower_case:
        # this condition ideally, should not occur,
        LOGGER.info("did it come inside this 'elif' ?")
    else:
        telegram__web_login_code = incoming_message_text
    return telegram__web_login_code