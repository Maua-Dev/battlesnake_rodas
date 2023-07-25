from src.app.entities.coordinates import Coordinates

class Test_Coordinates:
    def test_coordinates(self):
        x = 5.0
        y = 5.0

        coordinates = Coordinates(x,y)

        assert coordinates.x == 5.0
        assert coordinates.y == 5.0


    def test_coordinates_same_point(self):
        x = 5.0
        y = 5.0

        first_coordinates = Coordinates(x,y)
        second_coordinates = Coordinates(x,y)

        assert first_coordinates.x == second_coordinates.x
        assert first_coordinates.y == second_coordinates.y 

    def test_coordinates_different_points(self):
        x = 5.0
        y = 5.0

        first_coordinates = Coordinates(x,y)
        second_coordinates = Coordinates(1.0,1.0)

        assert first_coordinates.x != second_coordinates.x
        assert first_coordinates.y != second_coordinates.y

    def test_coordinate_distance(self):
        first = Coordinates(4.0,4.0)
        second = Coordinates(3.0,3.0)

        assert Coordinates.distance(first, second) == 1.4142135623730951

    def test_moviments(self):

        location = Coordinates(5.0, 5.0)

        assert location.moviment("up") == Coordinates(5.0, 6.0)
        assert location.moviment("down") == Coordinates(5.0, 4.0)
        assert location.moviment("left") == Coordinates(4.0, 5.0)
        assert location.moviment("right") == Coordinates(6.0, 5.0)
