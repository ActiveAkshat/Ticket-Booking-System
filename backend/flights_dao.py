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

def get_flights_date(date,source,destination, connection):
    cursor = connection.cursor()
    print (date)
    if date is None or date == "DD-MM-YYYY":
        print("11111")
        query = "Select * from bookingsystem.flights where source = %s and destination = %s;"
        # cursor.execute(query, (date,))
        cursor.execute(query, (source, destination))
    else:
        query = "Select * from bookingsystem.flights where date = %s and source = %s and destination = %s;"
        print("2222222")
        # cursor.execute(query, (date,))
        cursor.execute(query, (date, source, destination))
    # query = "SELECT * FROM bookingsystem.flights WHERE date = %s"
    # query = "Select * from bookingsystem.flights where date = %s and source = %s and destination = %s;"
    # # cursor.execute(query, (date,))
    # cursor.execute(query, (date,source,destination))
    response = []
    for (flight_id, flight_name, source, destination, departure_time, arrival_time, fare,date) in cursor:
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