class Workout:
    def __init__(self,
                 workout_id: int,
                 user: User,
                 exercise_type: str,
                 duration: float,
                 date: str):
        self.workout_id: int = workout_id
        self.user = user
        self.exercise_type: str = exercise_type
        self.duration: float = duration
        self.date: str = date

class Summary:
    def __init__(self,
                 user: User,
                 time_span: str,
                 total_workouts: int,
                 total_time_spent: float,
                 most_common_exercise: str):
        self.user = user
        self.time_span = time_span
        self.total_workouts = total_workouts
        self.total_time_spent = total_time_spent
        self.most_common_exercise = most_common_exercise

class User:
    def __init__(self, user_id: int, first_name: str, surname: str):
        self.user_id: int = user_id
        self.first_name: str = first_name
        self.surname: str = surname