import pandas as pd
import numpy as np
from src.process import update_target


def test_update_target():
    # Set the number of rows (n) for testing
    n = 3
    # Create sample data with n * 2000 rows
    data = {'mass_centre_x': list(range(1, n * 2001)),
            'target_x': [0] * (n * 2000)}
    df = pd.DataFrame(data)

    # Call the function
    update_target('mass_centre_x', 'target_x', df)

    # Verify the result
    expected_result = {'mass_centre_x': list(range(1, n * 2001)),
                       'target_x': list(range(2, 2001)) + [np.nan] + [0] * (n * 1998)}
    expected_df = pd.DataFrame(expected_result)

    # Check if the updated DataFrame is as expected
    assert df.equals(expected_df), "Test failed!"


# Run the test
test_update_target()
print("Test passed!")

# Run the test

test_update_target()

print("Test passed!")
