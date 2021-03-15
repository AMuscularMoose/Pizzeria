def main():
    def textfile():
        inputfile = open("text.txt", "r")
        file_contents = inputfile.read()
        # print(file_contents)

        file_contents = file_contents.lower()
        words = file_contents.split()
        words = [word.strip(",.-") for word in words]
        word_list = []

        for i in words:
            word_list.append(words.count(i))

        fileDict = dict(zip(words, word_list))
        print(fileDict)
        inputfile.close()

    def world_series():
        inputfile = open("WorldSeriesWinners.txt", "r")
        list_content = inputfile.readline()
        # print(list_content)
        BEG_YEAR = 1903

        team_list = {}
        while list_content:
            if BEG_YEAR in [1904, 1994]:
                BEG_YEAR += 1
            if list_content.strip() in team_list:
                team_list[list_content.strip()].append(BEG_YEAR)
            else:
                team_list[list_content.strip()] = [BEG_YEAR]

            BEG_YEAR += 1
            list_content = inputfile.readline()
        print(team_list)

        user_input = int(
            input("Enter a year between 1903 and 2008 to see the world series winner: ")
        )
        while user_input < 1903 and user_input > 2008:
            print("No data on that year")
            user_input = input("Enter another year")

        while user_input == 1904 or user_input == 1994:
            print("The World Series was not played in this year")
            user_input = input("Enter another year")

        inputfile.close()
        teams = team_list.keys()
        teams.sort()
        for team in teams:
            print()

    textfile()
    world_series()


main()