from espn_api.football import League

import weekly_review
import html_generator
from weekly_review import WeeklyReview
from arg_parser import get_args

# get args
# TODO: set arguments to ints and strings so i don't need to cast each time
args = get_args()

# connect to league
league = League(int(args.leagueid), int(args.year), args.espn_s2, args.swid)

start_week = 0
end_week = 0

if args.range:
    start_week = int(args.range[0])
    end_week = int(args.range[1])
else:
    start_week = int(args.week)
    end_week = start_week

# TODO see if there is a better way to do inclusive
for i in range(start_week, end_week+1):
    weeklyReview = WeeklyReview(league, i)
    html = html_generator.gen_weekly_review_html(weeklyReview)
    html_generator.write_weekly_review_html(html)