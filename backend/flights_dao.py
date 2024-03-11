from sql_connection import get_sql_connection

def get_all_flights(connection):

    cursor = connection.cursor()

    query = "SELECT * FROM bookingsystem.flights"

    cursor.execute(query)

    response = []
    for(flight_id, flight_name, source, destination, departure_time, arrival_time, fare, date) in cursor:
       response.append(
           {
               'flight_id': flight_id,
               'flight_name': flight_name,
               'source': source,
               'destination': destination,
               'departure_time': departure_time,
               'arrival_time': arrival_time,
               'fare': fare,
               'date': date

           }
       )

    return response

def get_flights_date(date, connection):
    cursor = connection.cursor()
    query = "SELECT * FROM bookingsystem.flights WHERE date = %s"

    cursor.execute(query, (date,))

    response = []
    for (flight_id, flight_name, source, destination, departure_time, arrival_time, fare) in cursor:
        response.append(
            {
                'flight_id': flight_id,
                'flight_name': flight_name,
                'source': source,
                'destination': destination,
                'departure_time': departure_time,
                'arrival_time': arrival_time,
                'fare': fare

            }
        )

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_flights(connection))