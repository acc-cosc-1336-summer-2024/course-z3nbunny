#
import decisions

options = float( input ("Please enter options: ") )

total = float( input ("Please enter total: ") )

ratio = decisions.get_options_ratio(options, total)

rating = decisions.get_faculty_rating(ratio)

print(rating)
