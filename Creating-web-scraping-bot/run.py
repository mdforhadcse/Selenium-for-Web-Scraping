from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='AED')
        bot.search_place_to_visit(place_to_visit='New York')  # input("Where you want to go?")
        bot.select_dates(check_in_date='2022-02-01', check_out_date='2022-02-11')
        bot.select_adults(5)
        bot.click_search()
        bot.apply_filtration()
        # bot.refresh()
        bot.report_results()


except Exception as e:
    if 'in PATH' in str(e):
        print('There is a problem running this program from command line interface')
    else:
        raise
