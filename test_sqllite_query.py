import sqlite3
#import icecream as ic

#con = sqlite3.connect("mdsbalance.db")

 
def getRunSensorCount(cursor,balance_session_id):
    try:
      cursor.execute("""
                   SELECT count(*) as count from  RunSensors c
                    JOIN  Runs r on r.RunId = c.RunId
                    JOIN BalanceSessions b on b.BalanceSessionId = r.BalanceSessionId
                    WHERE b.BalanceSessionId = ?
                   """,balance_session_id)
      data = cursor.fetchone()
      print("data")
      print(data['count'])
      if not data:
        raise ValueError(f"getRunSensorQuery returned 0 rows found with BalanceSession ID {balance_session_id}")

    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Error querying run sensor data: {str(e)}")

    
    return data
  
def getRunSensorData(cursor,balance_session_id):
  try:
    cursor.execute("""
                  SELECT Amp,Phase,Weigting from  RunSensors c
                  JOIN  Runs r on r.RunId = c.RunId
                  JOIN BalanceSessions b on b.BalanceSessionId = r.BalanceSessionId
                  WHERE b.BalanceSessionId = ?
                  """,balance_session_id)
    data = cursor.fetchall()
    if not data:
        raise ValueError(f"getRunSensorQuery returned 0 rows found with BalanceSession ID {balance_session_id}")

  except sqlite3.Error as e:
      raise RuntimeError(f"Database error: {str(e)}")
  except Exception as e:
      raise RuntimeError(f"Error querying run sensor data: {str(e)}")

  
  return data


def getRunSpeedConditions(cursor, balance_session_id):
  try:
    cursor.execute("""
     SELECT count(UnitConditionId) 
      FROM  UnitConditions uc
      JOIN BalanceSessions b on b.UnitId = u.UnitId
       WHERE uc.Enabled = true
        AND b.BalanceSessionId = ?;
    """,balance_session_id)
    data = cursor.fetchall()
    if not data:
        raise ValueError(f"getRunSensorQuery returned 0 rows found with BalanceSession ID {balance_session_id}")

  except sqlite3.Error as e:
      raise RuntimeError(f"Database error: {str(e)}")
  except Exception as e:
      raise RuntimeError(f"Error querying run sensor data: {str(e)}")

  
  return data


def getUnitConditionWeighting(cursor, balance_session_id):
  try:
    cursor.execute("""
     SELECT name,weighting 
      FROM  UnitConditions uc
      JOIN BalanceSessions b on b.UnitId = u.UnitId
       WHERE uc.Enabled = true
        AND b.BalanceSessionId = ?;
    """,balance_session_id)
    data = cursor.fetchall()
    if not data:
        raise ValueError(f"getRunSensorQuery returned 0 rows found with BalanceSession ID {balance_session_id}")

  except sqlite3.Error as e:
      raise RuntimeError(f"Database error: {str(e)}")
  except Exception as e:
      raise RuntimeError(f"Error querying run sensor data: {str(e)}")

  
  return data


def getDirectionOfRotation(cursor,balance_session_id):
  try:
    cursor.execute("""
     SELECT rotation 
      FROM  Units u
      JOIN BalanceSessions b on b.UnitId = u.UnitId
       WHERE b.BalanceSessionId = ?;
    """,balance_session_id)
    data = cursor.fetchall()
    if not data:
        raise ValueError(f"getRunSensorQuery returned 0 rows found with BalanceSession ID {balance_session_id}")

  except sqlite3.Error as e:
      raise RuntimeError(f"Database error: {str(e)}")
  except Exception as e:
      raise RuntimeError(f"Error querying run sensor data: {str(e)}")

  
  return data
  
def getUnitPlainData(cursor, balance_session_id):
  try:
    cursor.execute("""
       select up.* from UnitPlanes up
        join UnitComponents uc on uc.UnitComponentId = up.UnitComponentId
        join BalanceSessions b on b.UnitId = uc.UnitId
        where b.BalanceSessionId = ?
          """,balance_session_id)
    data = cursor.fetchall()
    if not data:
        raise ValueError(f"getUnitPlane query returned 0 rows found with BalanceSession ID {balance_session_id}")

  except sqlite3.Error as e:
      raise RuntimeError(f"Database error: {str(e)}")
  except Exception as e:
      raise RuntimeError(f"Error querying run sensor data: {str(e)}")

  
  return data

print("start")   
with sqlite3.connect("mdsbalance.db") as con:
  con.row_factory = sqlite3.Row  # Enable column access by name
  cursor = con.cursor()

  getRunSensorCount(cursor,"1")
print("end")
