from booking.Booking import *


with Booking() as bot:
    bot.land_first_page()
    bot.choose_currency(currency= "gbp")
    bot.search_place_to_go("Islamabad")
    bot.select_dates(chk_in_date = '2021-09-14', chk_out_date = '2021-09-29')
    bot.select_adults_children_rooms(adults = 3, childrens = 2, ages = [13,16], rooms = 4)
    bot.apply_filterations()
    bot.report_results()

