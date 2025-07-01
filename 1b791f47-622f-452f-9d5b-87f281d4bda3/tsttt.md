Of course. Here is the code with 10 different test cases written directly in `main`, without a helper function, following the exact `if/assert/print` structure you requested.

Each test is self-contained and uses distinct variable names to avoid conflicts within the `main` scope.

```cpp
#include <iostream>
#include <vector>
#include <cmath>      // For sqrt, pow
#include <limits>     // For std::numeric_limits
#include <string>     // For test case names
#include <cassert>    // For assert()

// Define a struct to represent a Paying Guest (PG) accommodation
struct PG {
    double x;    // X-coordinate of the PG
    double y;    // Y-coordinate of the PG
    double rent; // Monthly rent of the PG
};

// ... (findBestPG function and its helper calculateSquaredDistance go here) ...
// (I am including them again for a complete, runnable block)

/**
 * @brief Calculates the squared Euclidean distance between two points.
 */
double calculateSquaredDistance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return dx * dx + dy * dy;
}

/**
 * @brief Finds the nearest and cheapest PG (Paying Guest accommodation) within a given budget.
 *
 * This function takes the coordinates of an office, a budget, and a list of PGs
 * with their locations and rents. It identifies the best PG based on the following
 * priorities:
 * 1. The PG must be within the specified budget.
 * 2. Among PGs within budget, the closest one to the office is preferred.
 * 3. If multiple PGs are equally close and within budget, the one with the lowest rent is preferred.
 *    If there's still a tie (same distance, same rent), the one that appears earlier
 *    in the input `pgs` vector (lower index) is chosen.
 *
 * @param officeX The X-coordinate of the office.
 * @param officeY The Y-coordinate of the office.
 * @param budget The maximum rent the person can afford.
 * @param pgs A constant reference to a vector of PG objects.
 * @return The 0-based index of the best PG found in the 'pgs' vector. Returns -1 if no PG
 *         is found that meets the budget criteria.
 */
int findBestPG(double officeX, double officeY, double budget, const std::vector<PG>& pgs) {
    int bestPgIndex = -1;
    double minSquaredDistance = std::numeric_limits<double>::max();
    double minRent = std::numeric_limits<double>::max();

    for (size_t i = 0; i < pgs.size(); ++i) {
        const PG& currentPg = pgs[i];
        if (currentPg.rent <= budget) {
            double currentSquaredDistance = calculateSquaredDistance(officeX, officeY, currentPg.x, currentPg.y);
            if (currentSquaredDistance < minSquaredDistance) {
                bestPgIndex = i;
                minSquaredDistance = currentSquaredDistance;
                minRent = currentPg.rent;
            } else if (currentSquaredDistance == minSquaredDistance) {
                if (currentPg.rent < minRent) {
                    bestPgIndex = i;
                    minRent = currentPg.rent;
                }
            }
        }
    }
    return bestPgIndex;
}


int main() {
    std::cout << "Running findBestPG Test Cases:\n" << std::endl;

    // --- 1. Normal Case: Basic Nearest & Cheapest ---
    {
        std::string test_name = "Test 1: Normal_Basic_Nearest_Cheapest";
        std::vector<PG> pgs = {
            {10.0, 10.0, 12000.0}, // Far
            {1.0, 1.0, 10000.0},   // Closest and in budget
            {0.5, 0.5, 20000.0}    // Even closer, but over budget
        };
        int expected = 1;
        int actual = findBestPG(0.0, 0.0, 15000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 1 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 2. Normal Case: Tie-breaking by Rent ---
    {
        std::string test_name = "Test 2: Normal_Tie_By_Rent";
        std::vector<PG> pgs = {
            {3.0, 4.0, 12000.0}, // dist=5, rent=12000
            {5.0, 0.0, 10000.0}, // dist=5, rent=10000 (Same dist, cheaper)
            {0.0, 5.0, 11000.0}  // dist=5, rent=11000
        };
        int expected = 1;
        int actual = findBestPG(0.0, 0.0, 15000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 2 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 3. Normal Case: Tie-breaking by Index ---
    {
        std::string test_name = "Test 3: Normal_Tie_By_Index";
        std::vector<PG> pgs = {
            {1.0, 1.0, 10000.0}, // dist=sqrt(2), rent=10k
            {2.0, 2.0, 9000.0},  // farther
            {1.0, 1.0, 10000.0}  // Same dist, same rent as index 0. Should pick 0.
        };
        int expected = 0;
        int actual = findBestPG(0.0, 0.0, 15000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 3 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 4. Edgy Case: Empty PG List ---
    {
        std::string test_name = "Test 4: Edgy_Empty_List";
        std::vector<PG> pgs = {};
        int expected = -1;
        int actual = findBestPG(0.0, 0.0, 10000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 4 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 5. Edgy Case: All PGs Over Budget ---
    {
        std::string test_name = "Test 5: Edgy_All_Over_Budget";
        std::vector<PG> pgs = {
            {1.0, 1.0, 10000.0}, {2.0, 2.0, 8000.0}, {3.0, 3.0, 6000.0}
        };
        int expected = -1;
        int actual = findBestPG(0.0, 0.0, 5000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 5 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }
    
    // --- 6. Edgy Case: Office at a PG Location (Distance 0) ---
    {
        std::string test_name = "Test 6: Edgy_Office_At_PG";
        std::vector<PG> pgs = {
            {5.0, 5.0, 7000.0}, // dist=0, rent=7000
            {1.0, 1.0, 8000.0},
            {5.0, 5.0, 6000.0}  // dist=0, rent=6000 (Cheapest at dist 0)
        };
        int expected = 2;
        int actual = findBestPG(5.0, 5.0, 10000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 6 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 7. Edgy Case: Negative Coordinates ---
    {
        std::string test_name = "Test 7: Edgy_Negative_Coordinates";
        std::vector<PG> pgs = {
            {-9.0, -9.0, 9000.0},  // dist from (-10,-10) is sqrt(2), rent=9000
            {-5.0, -5.0, 8000.0},  // dist from (-10,-10) is sqrt(50), rent=8000
            {0.0, 0.0, 7000.0}     // dist from (-10,-10) is sqrt(200), rent=7000
        };
        int expected = 0;
        int actual = findBestPG(-10.0, -10.0, 10000.0, pgs);
        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 7 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 8. Long Case: Many PGs with varied conditions ---
    {
        std::string test_name = "Test 8: Long_Many_PGs_Complex_Tiebreak";
        std::vector<PG> pgs = {
            {5.0, 5.0, 11000.0},  // dist=sqrt(50)
            {10.0, 10.0, 9000.0}, // dist=sqrt(200)
            {1.0, 1.0, 15000.0},  // Over budget
            {2.0, 2.0, 10500.0},  // dist=sqrt(8)
            {0.5, 0.5, 10000.0},  // dist=sqrt(0.5)
            {3.0, 3.0, 9500.0},   // dist=sqrt(18)
            {0.5, 0.5, 11000.0},  // dist=sqrt(0.5)
            {20.0, 20.0, 8000.0}, // far but cheap
            {-0.5, -0.5, 9900.0}  // dist=sqrt(0.5), CHEAPER than index 4. This should win.
        };
        int expected = 8;
        int actual = findBestPG(0.0, 0.0, 12000.0, pgs);

        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 8 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 9. Edgy Case: Budget is exactly the rent ---
    {
        std::string test_name = "Test 9: Edgy_Exact_Budget_Match";
        std::vector<PG> pgs = {
            {1.0, 1.0, 9001.0}, // Over budget
            {2.0, 2.0, 9000.0}  // Exactly on budget, should be chosen
        };
        int expected = 1;
        int actual = findBestPG(0.0, 0.0, 9000.0, pgs);
        
        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 9 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 10. Edgy Case: Only one PG available ---
    {
        std::string test_name = "Test 10: Edgy_Single_PG_Available";
        std::vector<PG> pgs = { {5.0, 5.0, 18000.0} };
        int expected = 0;
        int actual = findBestPG(0.0, 0.0, 20000.0, pgs);
        
        if (actual != expected) {
            std::cerr << "--- " << test_name << " FAILED ---" << std::endl;
            std::cerr << "Expected: " << expected << ", Actual: " << actual << std::endl;
        }
        assert(actual == expected && "Test 10 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    std::cout << "\nAll test cases completed successfully." << std::endl;

    return 0;
}
```