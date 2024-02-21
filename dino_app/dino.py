# Import average function from dino_helpers
from utilities.dino_helpers import read_csv, get_avg, get_same_names


def dino_puzzle_solver():
    # Read CSV
    length_dict, names = read_csv("dino_app/dinosaurs.csv")
    try:
        longest_species = max(length_dict, key=lambda x: get_avg(length_dict[x]))
    except Exception as e:
        print(f"Error: {e} calculating species with longest length")
        longest_species = "not available"
    try:
        same_letters = get_same_names(names)
    except Exception as e:
        print(f"Error {e} in calculating the list of lists.")
        same_letters = "not available"

    return longest_species, same_letters


if __name__ == "__main__":
    longest_species, same_letters = dino_puzzle_solver()
    print(f"Longest species is: {longest_species}")
    print(f"Dinosaur names with the same letters: {same_letters}")
