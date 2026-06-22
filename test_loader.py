from services.data_service import load_stories

stories = load_stories('data/Krishna_stories.json')

print(f'total stories: {len(stories)}')
print(stories[0]['title'])
