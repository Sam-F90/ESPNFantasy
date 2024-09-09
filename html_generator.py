from bs4 import BeautifulSoup
from yattag import Doc
from weekly_review import WeeklyReview


def gen_weekly_review_html(weeklyReview):
    doc, tag, text = Doc().tagtext()

    # Creating the first section with Manager Awards
    with tag('section', klass='section', id=f"{weeklyReview.year}-{weeklyReview.week}"):
        with tag('h2', style="text-align: center;"):
            text(f"Week {weeklyReview.week}, Year {weeklyReview.year}")

        with tag('section', klass='section', id=f"{weeklyReview.year}-{weeklyReview.week}"):
            with tag('h4'):
                text('Manager Awards')

            # Creating the first table
            with tag('table'):
                with tag('thead'):
                    with tag('tr'):
                        with tag('th'):
                            text('Manager Awards')
                        with tag('th'):
                            text('Team')

                with tag('tbody'):
                    # First row
                    with tag('tr'):
                        with tag('td'):
                            text('Highest Scorer')
                        with tag('td'):
                            text(f"{weeklyReview.highest_score}")

                    # Second row
                    with tag('tr'):
                        with tag('td'):
                            text('Lowest Scorer')
                        with tag('td'):
                            text(f"{weeklyReview.lowest_score}")

                    # Third row
                    with tag('tr'):
                        with tag('td'):
                            text('Largest Difference')
                        with tag('td'):
                            text(f"{weeklyReview.largest_difference}")

                    # Fourth row
                    with tag('tr'):
                        with tag('td'):
                            text('Best Matchup Luck')
                        with tag('td'):
                            text(
                                f"{weeklyReview.best_luck.team_name} would have lost to {weeklyReview.best_luck.points} other team(s) this week")

                    # Fifth row
                    with tag('tr'):
                        with tag('td'):
                            text('Worst Matchup Luck')
                        with tag('td'):
                            text(
                                f"{weeklyReview.worst_luck.team_name} would have beat {weeklyReview.worst_luck.points} other team(s) this week")

                    # Sixth row
                    with tag('tr'):
                        with tag('td'):
                            text('Highest Bench Player')
                        with tag('td'):
                            text(f"{weeklyReview.highest_bench}")

        # Creating the second section with Player Awards
        with tag('section', klass='section'):
            with tag('h4'):
                text('Player Awards')

            # Creating the second table
            with tag('table'):
                with tag('thead'):
                    with tag('tr'):
                        with tag('th'):
                            text('Position')
                        with tag('th'):
                            text('Best Player')
                        with tag('th'):
                            text('Worst Player')

                with tag('tbody'):
                    # QB row
                    with tag('tr'):
                        with tag('td'):
                            text('QB')
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.bestQB).getvalue())
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.worstQB).getvalue())

                    # WR row
                    with tag('tr'):
                        with tag('td'):
                            text('WR')
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.bestWR).getvalue())
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.worstWR).getvalue())

                    # RB row
                    with tag('tr'):
                        with tag('td'):
                            text('RB')
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.bestRB).getvalue())
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.worstRB).getvalue())

                    # TE row
                    with tag('tr'):
                        with tag('td'):
                            text('TE')
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.bestTE).getvalue())
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.worstTE).getvalue())

                    # K row
                    with tag('tr'):
                        with tag('td'):
                            text('K')
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.bestKI).getvalue())
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.worstKI).getvalue())

                    # DE row
                    with tag('tr'):
                        with tag('td'):
                            text('DE')
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.bestDE).getvalue())
                        with tag('td'):
                            doc.asis(_gen_player_awards(weeklyReview.worstDE).getvalue())

    return doc


def write_weekly_review_html(doc):
    with open('index.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    week_id = soup.find_all(attrs={"id": True})

    new_content = BeautifulSoup(doc.getvalue(), 'html.parser')

    if week_id and new_content.find(id=week_id[0]['id']):
        return

    soup.body.append("\n")
    soup.body.append(new_content)
    soup.body.append("\n")

    # Step 4: Write the updated HTML back to index.html
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))


def _gen_player_awards(player_award):
    doc, tag, text = Doc().tagtext()
    with tag('span'):
        with tag('span', klass="team-name"):
            text(f"{player_award.team_name} | ")
        with tag('span', klass="player-name"):
            text(f"{player_award.player.name} ")
        with tag('span', klass="points"):
            text(f"{player_award.points}")

    return doc
