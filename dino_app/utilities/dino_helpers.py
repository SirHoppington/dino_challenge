import csv

# Function to read results from CSV
def read_csv(filepath):
    try:
        # Open the CSV file for reading
        with open(filepath, mode="r") as file:
            reader = csv.DictReader(file)

            # Store data from CSV in a dictionary
            lengths = {}
            names = []
            for row in reader:
                # Convert the length to a float by splitting based on m string, if empty set to 1
                length = (
                    float(row["length"].split("m")[0]) if row["length"] != "" else 1.0
                )
                # Check if species already exists in dictionary
                if row["species"] in lengths:
                    lengths[row["species"]].append(length)
                elif row["species"] != "":
                    lengths[row["species"]] = [length]
                names.append(row["name"])
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except PermissionError:
        print(f"Permission denied: {filepath}")

    return lengths, names

# Get average of the list of booleans
def get_avg(lengths):
    try:
        return sum(lengths) / len(lengths)
    except ZeroDivisionError:
        print("The list of lengths is empty.")
        return lengths
    except TypeError:
        print("The list of lengths contain invalid types.")
        return []
    except Exception as e:
        raise e


# Function to get list of lists where each sublist contains strings with the same letters
def get_same_names(names):
    # Create empty dictionary
    dict_of_letters = {}
    # Loop through names
    for name in names:
        try:
            # Sort letters and make unique using set and convert back to string
            unique_letters = "".join(sorted(set(name)))
            # Assign as key for dictionary and add name to the associated key
            if unique_letters in dict_of_letters:
                dict_of_letters[unique_letters].add(name)
            else:
                dict_of_letters[unique_letters] = {name}
        except TypeError as e:
            print(f"Error occurred when processing the name '{name}': {e}")
            continue
    try:
        # List comprehension to create list of lists from the values of the dict where there is more than 1 name
        list_of_lists = [
            sorted(dinosaurs)
            for dinosaurs in dict_of_letters.values()
            if len(dinosaurs) > 1
        ]
    except TypeError as e:
        print(f"Error occurred when processing the dictionary values: {e}")
        return []

    return list_of_lists
