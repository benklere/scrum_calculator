class SprintPredictor:

    @staticmethod
    def calculate_average_velocity(story_points, number_of_sprints):
        if story_points <= 0.0 or number_of_sprints <= 0.0:
            return 0.0
        average_velocity = story_points / number_of_sprints
        return average_velocity

    @staticmethod
    def calculate_remaining_sprints(remaining_product_backlog_points, average_velocity):
        if remaining_product_backlog_points <= 0.0 or average_velocity <= 0.0:
            return 0.0
        remaining_sprints = remaining_product_backlog_points / average_velocity
        return remaining_sprints

    @staticmethod
    def calculate_remaining_weeks(remaining_sprints, weeks_per_sprint):
        if remaining_sprints <= 0.0 or weeks_per_sprint <= 0.0:
            return 0.0
        remaining_weeks = remaining_sprints * weeks_per_sprint
        return remaining_weeks


