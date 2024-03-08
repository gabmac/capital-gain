#!/bin/bash

# Directory to search in, "." means current directory.
# Replace "." with "/path/to/your/directory" to search in a specific directory.
DIRECTORY="cases"

# File pattern to match
PATTERN="*_input.txt"

# Flag to indicate if any test has failed
failed=0

# Find files that match the pattern
find "$DIRECTORY" -type f -name "$PATTERN" | while read -r file; do
  # Extract the base name of the file without the directory path
  base_name=$(basename "$file" "_input.txt")

  # Define the expected output file path by replacing "input" with "output"
  expected_output_file="${file%_input.txt}_output.txt"

  # Execute the Python command with the current file as input
  # and store the output in a temporary file
  temp_output=$(mktemp)
  python -m system < "$file" > "$temp_output"

  # Remove any space characters from the temporary file
  tr -d ' ' < "$temp_output" > "${temp_output}_nospace"
  mv "${temp_output}_nospace" "$temp_output"

  # Ensure there's no newline at the end of the temporary file
  # Using Perl as a more compatible alternative to sed across different systems
  perl -pi -e 'chomp if eof' "$temp_output"

  # Compare the temporary output file with the expected output file
  if diff -Z "$temp_output" "$expected_output_file" > /dev/null; then
    echo "Success: Output matches for $file"
  else
    echo "Failure: Output does not match for $file. Differences shown below:"
    # Show the differences, ignoring trailing whitespace
    diff -Z "$temp_output" "$expected_output_file"
    failed=1
    break # Exit the loop on the first failure
  fi
  # Clean up the temporary file
  rm "$temp_output"
done

# Exit with a failure status if any test failed
if [ "$failed" -eq 1 ]; then
  exit 1
fi
