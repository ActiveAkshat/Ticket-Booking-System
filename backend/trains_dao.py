from sql_connection import get_sql_connection

def get_all_trains(connection):

    cursor = connection.cursor()

    query = "SELECT * FROM bookingsystem.trains"

    cursor.execute(query)

    response = []
    for(train_id, train_name, source, destination, departure_time, arrival_time, fare) in cursor:
       response.append(
           {
               'train_id': train_id,
               'train_name': train_name,
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
    print(get_all_trains(connection))