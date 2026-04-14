from dtos import *
import sqlite3

class DAL:
    def __init__(self, connection_string: str):
        self.db = sqlite3.connect(connection_string)
        self.connection_string = connection_string
    
    def log_workout(self, workout: Workout) -> bool:
        cursor = self.db.cursor()
        query = """
        INSERT INTO workouts (user_id, exercise_type, duration, date)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        
        try:
            cursor.execute(query, (workout.user.user_id, workout.exercise_type, workout.duration, workout.date))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error logging workout: {e}")
            self.db.rollback()
            return False
    
    def get_workout(self, workout_id: int) -> Workout | None:
        cursor = self.db.cursor()
        query = """
        SELECT *
        FROM Workouts
        WHERE workout_id = ?
        """
        try:
            cursor.execute(query, (workout_id,))
        except Exception as e:
            print(f"Error logging workout: {e}")
            return None
        
        results = cursor.fetchall()
        
        user = self.get_user(results[1])
        if user is None:
            return None
        
        if len(results) == 1:
            row = results[0]
            return Workout(workout_id=row[0], user=user, exercise_type=row[2], duration=row[3], date=row[4])
        elif len(results) == 0:
            print(f"Error fetching workout with id {workout_id}: Workout not found")
            return None

    def get_workout_history(self, user_id: int) -> list[Workout]:
        cursor = self.db.cursor()
        query = """
        SELECT *
        FROM Workouts
        WHERE user_id = ?
        """
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        workouts = []
        for row in results:
            user = self.get_user(row[1])
            if user is not None:
                workouts.append(Workout(workout_id=row[0], user=user, exercise_type=row[2], duration=row[3], date=row[4]))
            else:
                print(f"Error fetching workout with id {row[0]}: User with id {row[1]} not found")
        return workouts

    def edit_workout(self, workout_id: int, update_json: dict)-> bool:
        cursor = self.db.cursor()
        query = """
        UPDATE Workouts
        SET ? = ?
        WHERE workout_id = ?
        """
        
        for key, value in update_json.items():
            try:
                cursor.execute(query, (key, value, workout_id))
            except Exception as e:
                print(f"Error updating workout for key {key}: {e}")
                print("Database returned to original state. No updates have been made.")
                self.db.rollback()
                return False
        return True
    
    def delete_workout(self, workout_id: int) -> bool:
        cursor = self.db.cursor()
        query = """
        DELETE FROM Workouts
        WHERE workout_id = ?
        """
        try:
            cursor.execute(query, (workout_id,))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error deleting workout: {e}")
            self.db.rollback()
            return False

    def get_user(self, user_id: int) -> User | None:
        cursor = self.db.cursor()
        query = """
        SELECT *
        FROM Users
        WHERE user_id = ?
        """
        
        try:
            cursor.execute(query, (user_id,))
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
        results = cursor.fetchall()
        if len(results) == 1:
            row = results[0]
            return User(user_id=row[0], first_name=row[1], surname=row[2])
        elif len(results) == 0:
            print(f"Error fetching user with id {user_id}: User not found")
            return None
        