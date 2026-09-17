#!/bin/bash

set -e # This exits on any command failure so bash doesn't keep running if a command fails
set -u # This throws an error for undefined variables, which bash usually doesn't do on its own
set -o pipefail # This makes pipelines fail if any command fails. This means bash will exit if any command
# in the pipeline fails, which bash usually doesn't do (It usually just looks at the last command for failure)

set -euo pipefail # This does all three at once

# Prompt for number of runs
echo "Number of runs?"
read runNum
echo "Simulation will run" $runNum "times"


# Uncomment this section to request a specific parameter to change when running the script
# Prompt for Parameter
# echo "Parameter to increment?"
# read param
# echo "$param selected"

# Prompt for increment
echo "Increment amount?"
read increment
echo "Parameter will increment by $increment"

sif_file="iteration-case.sif"
db_file="results.db"
iterations=$runNum
variable_name="Relative Permittivity"
# Uncomment this line to request a specific parameter to change when running the script
# variable_name = $param
initial_value=1
# increment=10

# Create the SQLite database and table if it doesn't exist
# sqlite3 "$db_file" "CREATE TABLE IF NOT EXISTS simulation_results (
#     iteration INTEGER,
#     parameter REAL,
#     result_value REAL,
#     col1 TEXT,
#     col2 TEXT,
#     col3 TEXT
# );"

# Overwrite old data files and old output log
echo > ./results/iteration-results/results.dat
echo > ./results/iteration-results/results.csv
echo > ./results/iteration-results/results.dat.names
echo > output.log

for i in $(seq 1 $iterations); do

    # Print the start of the next run to output.log
    echo >> output.log
    echo >> output.log
    echo "<><><><><><><><><><><><><><><><><><><><><><><>" >> output.log
    echo "BEGINNING OF RUN $i" >> output.log
    echo "<><><><><><><><><><><><><><><><><><><><><><><>" >> output.log
    echo >> output.log
    echo >> output.log

    echo "Running iteration $i..."
    
    # Run ElmerSolver and print the output to the output.log
    ElmerSolver ./sif/$sif_file >> output.log
    
    # Extract your result
    # Example: let's say you have a 'Temperature' file output (replace with your actual file/output)
    # Here, we just grab the max temperature as an example

    # THIS IS WHAT NEEDS TO BE FIGURED OUT. I NEED TO WRITE DATA FROM THE .DAT to this result variable
    # result=$(grep "Temperature" case.result | awk '{print $2}')  # adjust to your actual output format

    # Calculate new parameter
    new_value=$(( initial_value + (i-1)*increment ))
    # echo $new_value

    # Insert into database
    # sqlite3 "$db_file" "INSERT INTO simulation_results (iteration, parameter, result_value) VALUES ($i, $new_value, $result);"
    
    # Update the .sif file
    # sed -i "s/^\($variable_name *= *\).*/\1$new_value/" "./sif/$sif_file"
    sed -i "s/^\([[:space:]]*$variable_name[[:space:]]*=[[:space:]]*\)[^!]*\(.*\)/\1$new_value\2/" "./sif/$sif_file"


    # Print the end of the output.log file
    echo >> output.log
    echo >> output.log
    echo "<><><><><><><><><><><><><><><><><><><><><><><>" >> output.log
    echo END OF RUN $i >> output.log
    echo "<><><><><><><><><><><><><><><><><><><><><><><>" >> output.log
    echo >> output.log
    echo >> output.log
done

# Turn white space delimited file into a csv file
awk 'BEGIN { OFS="," } { $1=$1; print }' ./results/iteration-results/results.dat > ./results/iteration-results/results.csv
echo "Creating csv from .dat"

# Create table
# Heredoc: bash reads everything to be outputted into the results.db file up until it reads the SQL part. Then it stops

# Make sure to include the right headers for the data
sqlite3 "$db_file" <<'SQL'
CREATE TABLE IF NOT EXISTS simulation_results (
    electric_energy INTEGER,
    potential_difference REAL,
    capacitance REAL,
    col1 TEXT,
    col2 TEXT,
    col3 TEXT
);
SQL

# Overwrite old data from table and import CSV
sqlite3 "$db_file" <<'SQL'
DELETE from simulation_results;
.mode csv
.import results/iteration-results/results.csv simulation_results
.headers on
.mode columns
SQL

echo "All iterations done. Results stored in $db_file"
