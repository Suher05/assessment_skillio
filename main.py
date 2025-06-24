from show_flights import insert_flight, show_flights



if __name__ == "__main__":
    insert_flight('FR555', '2025-07-05 08:30:00', '2025-07-05 10:45:00', 'ARN', 'CPH', 'Ryanair')
    insert_flight('SK777', '2025-07-06 09:15:00', '2025-07-06 11:00:00', 'GOT', 'LHR', 'SAS')
    insert_flight('DY999', '2025-07-07 13:00:00', '2025-07-07 15:40:00', 'OSL', 'FRA', 'Norwegian')

    show_flights()
