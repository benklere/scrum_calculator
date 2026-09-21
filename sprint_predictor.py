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

    def test_calculate_average_velocity():
        result = SprintPredictor.calculate_average_velocity(100, 4)
        assert result == 25.0


    def test_calculate_average_velocity_with_zero_story_points():
        result = SprintPredictor.calculate_average_velocity(0.0, 4)
        assert result == 0.0


    def test_calculate_average_velocity_with_zero_sprints():
        result = SprintPredictor.calculate_average_velocity(100, 0.0)
        assert result == 0.0


    def test_calculate_remaining_sprints():
        result = SprintPredictor.calculate_remaining_sprints(100, 25)
        assert result == 4.0


    def test_calculate_remaining_sprints_with_zero_backlog():
        result = SprintPredictor.calculate_remaining_sprints(0.0, 25)
        assert result == 0.0


    def test_calculate_remaining_sprints_with_zero_velocity():
        result = SprintPredictor.calculate_remaining_sprints(100, 0.0)
        assert result == 0.0


    def test_calculate_remaining_weeks():
        result = SprintPredictor.calculate_remaining_weeks(4, 2)
        assert result == 8.0


    def test_calculate_remaining_weeks_with_zero_sprints():
        result = SprintPredictor.calculate_remaining_weeks(0.0, 2)
        assert result == 0.0


    def test_calculate_remaining_weeks_with_zero_weeks_per_sprint():
        result = SprintPredictor.calculate_remaining_weeks(4, 0.0)
        assert result == 0.0


