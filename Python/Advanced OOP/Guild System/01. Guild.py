from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if not player.guild == 'Unaffiliated':
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        if player_name not in [p.name for p in self.players]:
            return f'Player {player_name} is not in the guild.'
        player = [p for p in self.players if p.name == player_name][0]
        player.guild = 'Unaffiliated'
        self.players.remove(player)
        return f'Player {player_name} has been removed from the guild.'

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players:
            result += p.player_info()
        return result
