"""
Program to clear groups by kicking out all members (except specified ones)
and clearing the purpose of the groups
"""
from pprint import PrettyPrinter
from slacker import Slacker
from private import SLACK_AUTH_TOKEN, members_to_keep
from slackFunctions import get_slack_groups, kick_members, rename_groups

__author__ = 'Lindsay Ward'
FILENAME = "data/slackGroups.txt"


def main():
    # pp = PrettyPrinter(indent=4)
    slack = Slacker(SLACK_AUTH_TOKEN)
    # TODO: might be more helpful if members_to_keep was specified as emails or Slack usernames instead of Slack IDs

    group_details = get_slack_groups(slack)
    # pp.pprint(group_details)

    # for testing a small number, not all in file:
    # groups_to_clear = ["cp1406-2017-team01", "cp1406-2017-team02"]
    # for group in groups_to_clear:
    groups_file = open(FILENAME, "r")
    for group in groups_file:
        group = group.strip()
        try:
            print("For {}: {}".format(group, group_details[group]))
            group_id, members = group_details[group]
            kick_members(slack, group_id, members, members_to_keep)
            print("Kicking from {}".format(group))
            # set "purpose" of group to blank
            slack.groups.set_purpose(group_id, "")
            # ARCHIVE GROUP!!
            slack.groups.archive(group_id)
        except:
            pass
    groups_file.close()


main()


def rename():
    slack = Slacker(SLACK_AUTH_TOKEN)
    rename_groups(slack, "cp3402-2017", "cp3402-2018")

# rename()
