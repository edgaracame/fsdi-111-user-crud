from app.database import get_db_vehicle


def output_formatter(results):
    out = []
    for result in results:
        vehicle = {
            "id": result[0],
            "brand": result[1],
            "model": result[2],
            "color": result[3],
            "year": result[4],
            "userid": result[5],
            "active": result[6]
        }
        out.append(vehicle)
    return out


def scan():
    cursor = get_db_vehicle().execute(
        "SELECT * FROM vehicle WHERE active = 1", ()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db_vehicle().execute(
        "SELECT * FROM vehicle WHERE id = ? AND active = 1",
        (pk,)
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict.get("brand"),
        vehicle_dict.get("model"),
        vehicle_dict.get("color"),
        vehicle_dict.get("year"),
        vehicle_dict.get("userid")
    )
    statement = """
        INSERT INTO vehicle (
            brand,
            model,
            color,
            year,
            userid
        ) VALUES (?, ?, ?, ?, ?)
    """
    cursor = get_db_vehicle()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("brand"),
        vehicle_data.get("model"),
        vehicle_data.get("color"),
        vehicle_data.get("year"),
        vehicle_data.get("userid"),
        pk
    )
    statement = """
        UPDATE vehicle SET
        brand = ?,
        model = ?,
        color = ?,
        year = ?,
        userid = ?
        WHERE id = ?
    """
    cursor = get_db_vehicle()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def deactivate(pk):
    cursor = get_db_vehicle()
    cursor.execute("UPDATE vehicle SET active = 0 WHERE id = ?", (pk,))
    cursor.commit()
    cursor.close()
