class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.ties = 0

    def record_win(self):
        self.wins += 1

    def record_tie(self):
        self.ties += 1

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def play_match(self):
        # simulate the match and determine the scores
        self.score1 = float(input("Enter the score of player 1: "))
        self.score2 = float(input("Enter the score of player 2: "))

        if self.score1 > self.score2:
            self.player1.record_win()
        elif self.score2 > self.score1:
            self.player2.record_win()
        else:
            self.player1.record_tie()
            self.player2.record_tie()

class Tournament:
    def __init__(self, players):
        self.players = players
        self.matches = []

    def create_matches(self):
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                match = Match(self.players[i], self.players[j])
                self.matches.append(match)

    def play_tournament(self):
        self.create_matches()
        for match in self.matches:
            match.play_match()

    def view_standings(self):
        players = sorted(self.players, key=lambda x: (x.wins, x.ties), reverse=True)
        for player in players:
            print('{}: {} wins, {} ties'.format(player.name, player.wins, player.ties))

players = [Player('player1'), Player('player2'), Player('player3')]
numOfPlayers = int(input("Enter the number of players: "))
for i in range(numOfPlayers):
    if numOfPlayers > 3:
        players.append(Player("player"+str(numOfPlayers)))

tournament = Tournament(players)
tournament.play_tournament()
tournament.view_standings()
