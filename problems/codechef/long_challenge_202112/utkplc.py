def compute_company(preferences, offers):
    for preference in preferences:
        if preference in offers:
            return preference
    return


for _ in range(int(input())):
    preferences = input().strip().split(' ')
    offers = input().strip().split(' ')

    print(compute_company(preferences, offers))
