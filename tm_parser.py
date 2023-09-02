import sys
import tyrone_mings

input_file = sys.argv[1]  # 'argentina.txt'
country = input_file.split('.')[0]

# read file with clubs links
with open(input_file, 'r') as input_file_source:
    clubs = input_file_source.readlines()

# data storage
final_data = {}

# process link by link
for club in clubs:
    # split str on CLUB and URL
    club_data = club.split('__')
    club_name = club_data[0]
    club_url = club_data[1]

    print(f'Processing {club_name}...')

    player_urls = tyrone_mings.get_player_urls_from_club_page(club_url)
    player_urls = [
        player_url for player_url in player_urls if
        'marktwertverlauf' not in player_url
    ]

    print(f'Fetched {len(player_urls)} players.')
    final_data[club_name] = player_urls

print('\nSaving players data...\n')

with open(f'FIFA_{country}_2023.txt', 'w+') as output_file:
    for club, players in final_data.items():
        output_file.write(club + '\n\n')
        for player in players:
            output_file.write(player + '\n')
        output_file.write('\n\n')

print('Players data saved.\n')
