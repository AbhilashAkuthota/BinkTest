1. Run the main.py
    - place the csv file on the project folder.
    - To run all script.
        * python main.py

2. Run specific each section by user input
    - To run to produce a list sorted by “Current Rent” in ascending order.
        * python main.py sort
    - To run to get first 5 items from the resultant list and output to the console.
        * python main.py top_5
    - To run to get a new list of mast data with “Lease Years” = 25 and the total rent for all items in this list.
        * python main.py lease_25
    - To run to create a dictionary containing tenant name and a count of masts for each tenant.
        * python main.py tenants
    - To run to get the list the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007.
        * python main.py filter_in_range

3. Excecute UnitTest
    - python -m unittest unit_test.py -v