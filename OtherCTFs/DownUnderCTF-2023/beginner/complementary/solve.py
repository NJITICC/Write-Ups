from sympy import divisors


# Function to reverse the flag using a known starting substring
def reverse_flag_starting_with(n, starting_str):
    # Convert the starting string to its integer representation
    start_int = int.from_bytes(starting_str.encode("ascii"), byteorder="big")

    # Get all divisors of n
    all_divisors = divisors(n)

    # Filter out divisors that could be too small to be a factor derived from the flag
    # This is based on the length of the known starting string
    min_possible_value = start_int
    possible_divisors = [d for d in all_divisors if d >= min_possible_value]

    # Check each possible divisor
    for d in possible_divisors:
        try:
            # Convert the divisor to its byte representation
            d_bytes = d.to_bytes((d.bit_length() + 7) // 8, byteorder="big")

            # Decode to ASCII
            d_ascii = d_bytes.decode("ascii")

            # Check if it starts with the known starting string
            if d_ascii.startswith(starting_str):
                # Find the other factor
                other_factor = n // d

                # Convert the other factor to its byte and ASCII representation
                other_factor_bytes = other_factor.to_bytes(
                    (other_factor.bit_length() + 7) // 8, byteorder="big"
                )
                other_factor_ascii = other_factor_bytes.decode("ascii")

                # Combine to get the original flag
                return d_ascii + other_factor_ascii
        except UnicodeDecodeError:
            continue

    return "Failed to find a matching factor."


# Known starting string of the flag
known_starting_str = "DUCTF{"
n_given = 6954494065942554678316751997792528753841173212407363342283423753536991947310058248515278
# Try to reverse the flag using the known starting string
reversed_flag = reverse_flag_starting_with(n_given, known_starting_str)
print(reversed_flag)
