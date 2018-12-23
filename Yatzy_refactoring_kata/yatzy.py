class Yatzy:

    @staticmethod
    def chance(*args):
        total = 0
        for number in args:
            total += number
        return total

    @staticmethod
    def yatzy(dice):
       return 50 if dice.count(dice[0]) == 5 else 0
            
    @staticmethod
    def ones(*args):
        sum = 0
        for number in args:
            if number == 1:
                sum += 1

        return sum
    

    @staticmethod
    def twos(*args):
        sum = 0
        for number in args:
            if number == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes(*args):
        sum = 0
        for number in args:
            if number == 3:
                sum += 3
        return sum
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    @staticmethod
    def fours(*args):
        sum = 0
        for number in args:
            if number == 4:
                sum += 4
        return sum
    

    def fives(*args):
        sum = 0
        for number in args:
            if number == 5:
                sum += 5
        return sum
    

    def sixes(*args):
        sum = 0
        for number in args:
            if number == 6:
                sum += 6
        return sum
    
    @staticmethod
    def pair(*args):
        score = 0
        for number in range(6, 0, -1):
            if args.count(number) >= 2:
                score += (number) * 2
                return score
        return 0 
    
    @staticmethod
    def two_pair(*args):
        score = 0
        pair = 0
        for number in range(6, 0, -1):
            if args.count(number) >= 2:
                score += (number) * 2
                pair += 1
                if pair == 2:
                    return score
                continue
        return 0 
            
        
    
    @staticmethod
    def four_of_a_kind(*args):
        score = 0
        for number in range(6, 0, -1):
            if args.count(number) >= 4:
                score += (number) * 4
                return score
        return 0 
    

    @staticmethod
    def three_of_a_kind(*args):
        score = 0
        for number in range(6, 0, -1):
            if args.count(number) >= 3:
                score += (number) * 3
                return score
        return 0 
    

    @staticmethod
    def smallStraight(*args):
        score = 0
        count = 0
        for number in range(1, 6):
            if args.count(number) == 1:
                score += number
                count += 1
                if count == 5:
                    return score
                continue
        return 0
    

    @staticmethod
    def largeStraight(*args):
        score = 0
        count = 0
        for number in range(2, 7):
            if args.count(number) == 1:
                score += number
                count += 1
                if count == 5:
                    return score
                continue
        return 0
    

    @staticmethod
    def fullHouse(*args):
        score_same_three = 0
        score_pair = 0
        for number in args:
            if args.count(number) == 3:
                if score_same_three:
                    continue
                score_same_three += number * 3
            if args.count(number) == 2:
                if score_pair:
                    continue
                score_pair += number * 2
            if score_pair and score_same_three:
                return score_pair + score_same_three
        else:
            return 0

if __name__ == "__main__":
    
    # TEST CASES #

    ''' TEST CASES FOR CHANCE ''' 
        
    assert Yatzy.chance(2,3,4,5,1) == 15
    assert Yatzy.chance(3,3,4,5,1) == 16

    ''' TEST CASES FOR ONES '''

    assert Yatzy.ones(1,2,3,4,5) == 1
    assert Yatzy.ones(1,2,1,4,5) == 2
    assert Yatzy.ones(6,2,2,4,5) == 0
    assert Yatzy.ones(1,2,1,1,1) == 4

    ''' TEST CASES FOR TWOS '''
    assert Yatzy.twos(1,2,3,2,6) == 4
    assert Yatzy.twos(2,2,2,2,2) == 10

    ''' TEST CASES FOR THREES '''
    assert Yatzy.threes(1,2,3,2,3) == 6
    assert Yatzy.threes(2,3,3,3,3) == 12

    ''' TEST CASES FOR FOURS '''

    assert Yatzy.fours(4,4,4,5,5) == 12
    assert Yatzy.fours(4,4,5,5,5) == 8
    assert Yatzy.fours(4,5,5,5,5) == 4

    ''' TEST CASES FOR YATZY '''
    assert Yatzy.yatzy([6,6,6,6,6]) == 50
    assert Yatzy.yatzy([6,6,6,6,3]) == 0

    ''' TEST CASES FOR FIVES '''
    assert Yatzy.fives(4,4,4,5,5) == 10
    assert Yatzy.fives(4,4,5,5,5) == 15
    assert Yatzy.fives(4,5,5,5,5) == 20

    ''' TEST CASES FOR SIXES '''
    assert Yatzy.sixes(4,4,4,5,5) == 0
    assert Yatzy.sixes(4,4,6,5,5) == 6
    assert Yatzy.sixes(6,5,6,6,5) == 18

    ''' TEST CASES FOR PAIR '''
    assert 4 == Yatzy.pair(1, 1, 2, 2, 2)
    assert Yatzy.pair(3,4,3,5,6) == 6
    assert Yatzy.pair(5,3,3,3,5) == 10
    assert Yatzy.pair(5,3,6,6,5) == 12
    assert Yatzy.pair(3, 3, 3, 4, 4) == 8
    assert Yatzy.pair(1, 2, 3, 4, 5) == 0

    ''' TEST CASES FOR TWO PAIR'''
    assert Yatzy.two_pair(3,3,5,4,5) == 16
    assert Yatzy.two_pair(3,3,6,6,6) == 18
    assert Yatzy.two_pair(3,3,6,5,4) == 0

    ''' TEST CASES FOR THREE OF A KIND '''
    assert 6 == Yatzy.three_of_a_kind(1, 1, 2, 2, 2)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5,3,5,4,5)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,5)

    ''' TEST CASES FOR FOUR OF A KIND '''
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,5)
    assert 20 == Yatzy.four_of_a_kind(5,5,5,4,5)
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
    assert 0  == Yatzy.four_of_a_kind(3,3,3,2,1)

    ''' TEST CASES FOR SMALL STRAIGHT '''
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.smallStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.smallStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.smallStraight(1, 2, 3, 4, 6)
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 15 == Yatzy.smallStraight(2,3,4,5,1)
    assert 0 == Yatzy.smallStraight(1,2,2,4,5)
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)

    ''' TEST CASES FOR LARGE STRAIGHT '''
    assert 20 == Yatzy.largeStraight(6,2,3,4,5)
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,2,2,4,5)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.largeStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.largeStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 6)

    ''' TEST CASES FOR FULL HOUSE '''
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)
    assert 18 == Yatzy.fullHouse(6,2,2,2,6)
    assert 0 == Yatzy.fullHouse(2,3,4,5,6)