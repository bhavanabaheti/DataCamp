# Writing a generator to load data in chunks (3)
# Great! You've just created a generator function that you can use to help you process large files.

# Now let's use your generator function to process the World Bank dataset like you did previously. You will process the file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire dataset!

# The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and ready for your use. Go for it!

# Instructions
# 100 XP
# Instructions
# 100 XP
# Bind the file 'world_dev_ind.csv' to file in the context manager with open().
# Complete the for loop so that it iterates over the generator from the call to read_large_file() to process all the rows of the file.

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)

#<script.py> output:
#    {'Europe & Central Asia (developing only)': 89, 'Lower middle income': 126, 'European Union': 116, 'Low & middle income': 138, 'High income: nonOECD': 68, 'Latin America & Caribbean (developing only)': 133, 'Caribbean small states': 77, 'East Asia & Pacific (all income levels)': 122, 'Low income': 80, 'North America': 123, 'Heavily indebted poor countries (HIPC)': 99, 'Latin America & Caribbean (all income levels)': 130, 'Fragile and conflict affected situations': 76, 'Small states': 69, 'Middle income': 138, 'East Asia & Pacific (developing only)': 123, 'High income': 131, 'Middle East & North Africa (developing only)': 94, 'Central Europe and the Baltics': 71, 'Pacific island small states': 66, 'High income: OECD': 127, 'Arab World': 80, 'OECD members': 130, 'Europe & Central Asia (all income levels)': 109, 'South Asia': 36, 'CountryName': 1, 'Middle East & North Africa (all income levels)': 89, 'Euro area': 119, 'Other small states': 63, 'Least developed countries: UN classification': 78}