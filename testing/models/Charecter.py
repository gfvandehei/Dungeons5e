from Dungeons5e.Model.Pydantic.Charecter import BaseCharecterStats

def test_creation():
    b = BaseCharecterStats
    b.charisma = 1
    b.wisdom = 1

    print(b)


if __name__ == "__main__":
    test_creation()