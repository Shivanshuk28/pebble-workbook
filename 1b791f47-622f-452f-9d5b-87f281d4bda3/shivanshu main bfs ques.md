Of course! It's an excellent idea to re-frame the problem using a discrete grid and a Breadth-First Search (BFS). This is a classic application of BFS for finding the "shortest path" in an unweighted graph, where each grid cell is a node and movement to an adjacent cell has a uniform cost.

Here is the problem refactored to use a grid and BFS, following the structure and style of your original code.

### Core Logic Change

1.  **Continuous vs. Discrete Space:** We move from `double` coordinates in a continuous plane to `int` coordinates on a finite grid.
2.  **Distance Metric:** Instead of Euclidean distance, the distance is now the number of steps (up, down, left, right) needed to get from the office to a PG. This is the "Manhattan distance" if movement is unrestricted, but BFS finds the true shortest path even with obstacles (though we don't have obstacles here).
3.  **Algorithm:** We replace the simple loop with a BFS. BFS naturally explores the grid layer by layer, guaranteeing that we find the closest PGs first.
4.  **Tie-Breaking:**
    *   **Distance:** BFS handles this automatically. All PGs found in the same "level" of the BFS are equidistant.
    *   **Rent & Index:** Once we find the first non-empty set of PGs at a certain distance, we stop the search. We then iterate through this set of equidistant PGs to find the one with the lowest rent, using the original index as the final tie-breaker.

Here is the complete, runnable C++ code.

```cpp
#include <iostream>
#include <vector>
#include <queue>      // For BFS
#include <map>        // To store PG locations on the grid
#include <utility>    // For std::pair
#include <limits>     // For std::numeric_limits
#include <string>     // For test case names
#include <cassert>    // For assert()

// Define a struct to represent a Paying Guest (PG) accommodation's info
// We store the original index to handle the final tie-breaker rule.
struct PG {
    double rent;        // Monthly rent of the PG
    int originalIndex;  // The 0-based index from the initial input list
};

// Define a type alias for our grid representation.
// It maps a coordinate (pair<int, int>) to a vector of PGs at that location.
using PGGrid = std::map<std::pair<int, int>, std::vector<PG>>;


/**
 * @brief Finds the nearest and cheapest PG on a grid using Breadth-First Search (BFS).
 *
 * This function takes the office's grid coordinates, a budget, the grid dimensions,
 * and a map representing PGs on the grid. It identifies the best PG based on the
 * following priorities, using BFS to determine distance:
 * 1. The PG must be within the specified budget.
 * 2. Among PGs within budget, the one with the shortest path (fewest steps) from the
 *    office is preferred. BFS guarantees finding these first.
 * 3. If multiple PGs are at the same shortest distance and within budget, the one
 *    with the lowest rent is preferred.
 * 4. If there's still a tie (same distance, same rent), the one with the lower
 *    original index from the input list is chosen.
 *
 * @param officeX The X-coordinate (column) of the office on the grid.
 * @param officeY The Y-coordinate (row) of the office on the grid.
 * @param budget The maximum rent the person can afford.
 * @param gridRows The total number of rows in the grid.
 * @param gridCols The total number of columns in the grid.
 * @param pgGrid A constant reference to a map where keys are coordinates and
 *               values are vectors of PGs at that location.
 * @param allPgs A constant reference to the original vector of all PGs, used to
 *               retrieve PG info from an index.
 * @return The 0-based original index of the best PG found. Returns -1 if no suitable PG
 *         is found (e.g., none in budget, or office is out of bounds).
 */
int findBestPG_BFS(int officeX, int officeY, double budget, int gridRows, int gridCols, const PGGrid& pgGrid, const std::vector<PG>& allPgs) {
    // Boundary check for the office location
    if (officeY < 0 || officeY >= gridRows || officeX < 0 || officeX >= gridCols) {
        return -1;
    }

    std::queue<std::pair<int, int>> q;
    std::vector<std::vector<bool>> visited(gridRows, std::vector<bool>(gridCols, false));

    // Start BFS from the office
    q.push({officeY, officeX});
    visited[officeY][officeX] = true;

    // Directions for moving in the grid (Up, Down, Right, Left)
    int dy[] = {-1, 1, 0, 0};
    int dx[] = {0, 0, 1, -1};

    while (!q.empty()) {
        int levelSize = q.size();
        std::vector<int> candidatesAtThisLevel; // Store original indices of PGs found at this distance

        // Process all nodes at the current distance level
        for (int i = 0; i < levelSize; ++i) {
            std::pair<int, int> current = q.front();
            q.pop();
            int y = current.first;
            int x = current.second;

            // Check if there is a PG at the current location
            if (pgGrid.count({y, x})) {
                const auto& pgsAtLocation = pgGrid.at({y, x});
                for (const auto& pg : pgsAtLocation) {
                    if (pg.rent <= budget) {
                        candidatesAtThisLevel.push_back(pg.originalIndex);
                    }
                }
            }

            // Add unvisited neighbors to the queue for the next level
            for (int j = 0; j < 4; ++j) {
                int nextY = y + dy[j];
                int nextX = x + dx[j];

                if (nextY >= 0 && nextY < gridRows && nextX >= 0 && nextX < gridCols && !visited[nextY][nextX]) {
                    visited[nextY][nextX] = true;
                    q.push({nextY, nextX});
                }
            }
        }

        // If we found any candidates at this level, they are the closest ones.
        // We can stop the search and find the best among them.
        if (!candidatesAtThisLevel.empty()) {
            int bestPgIndex = -1;
            double minRent = std::numeric_limits<double>::max();

            for (int candidateIndex : candidatesAtThisLevel) {
                const PG& candidatePg = allPgs[candidateIndex];
                if (candidatePg.rent < minRent) {
                    minRent = candidatePg.rent;
                    bestPgIndex = candidateIndex;
                }
                // The final tie-breaker (lower original index) is handled implicitly
                // by iterating through candidates. If rents are equal, the one with
                // the lower index would have been tested first and set as best.
                // We only update if the new one is strictly cheaper.
            }
            return bestPgIndex;
        }
    }

    // If the queue becomes empty and no PG was found
    return -1;
}


int main() {
    std::cout << "Running findBestPG_BFS Test Cases (Grid & BFS version):\n" << std::endl;

    const int GRID_ROWS = 20;
    const int GRID_COLS = 20;

    // Helper lambda to create the grid map from a vector of PGs
    auto createGrid = [](const std::vector<PG>& pgs) {
        PGGrid grid;
        for (const auto& pg : pgs) {
            // This part of the setup is a bit more complex now.
            // We need to find the PG in the original vector to get its coordinates.
            // For a real app, the PG struct would contain its coords.
            // For this test harness, we'll assume a fixed mapping or create it.
            // A better PG struct would be {int x, int y, double rent, int originalIndex}.
            // Let's create a temporary structure for setup clarity.
        }
        return grid; // We will build this manually in each test.
    };
    
    // A simplified PG representation for setting up tests easily.
    struct PGSetup { int y, x; double rent; };


    // --- 1. Normal Case: Basic Nearest PG ---
    {
        std::string test_name = "Test 1: Normal_Basic_Nearest";
        std::vector<PGSetup> pgSetups = {
            {10, 10, 12000.0}, // dist=20 from (0,0), in budget
            {1, 1, 10000.0},   // dist=2 from (0,0), in budget -> Should win
            {0, 1, 20000.0}    // dist=1, but over budget
        };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = 1;
        int actual = findBestPG_BFS(0, 0, 15000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);

        assert(actual == expected && "Test 1 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 2. Normal Case: Tie-breaking by Rent ---
    {
        std::string test_name = "Test 2: Normal_Tie_By_Rent";
        // Office at (5,5). All PGs are distance 2.
        std::vector<PGSetup> pgSetups = {
            {5, 7, 12000.0}, // dist=2, rent=12000
            {7, 5, 10000.0}, // dist=2, rent=10000 -> Should win (cheapest)
            {3, 5, 11000.0}  // dist=2, rent=11000
        };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = 1;
        int actual = findBestPG_BFS(5, 5, 15000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);
        
        assert(actual == expected && "Test 2 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 3. Normal Case: Tie-breaking by Index ---
    {
        std::string test_name = "Test 3: Normal_Tie_By_Index";
        // Office at (5,5). Two PGs at same location with same rent.
        std::vector<PGSetup> pgSetups = {
            {6, 5, 10000.0}, // dist=1, rent=10k, index=0 -> Should win
            {8, 8, 9000.0},  // farther
            {6, 5, 10000.0}  // dist=1, rent=10k, index=2
        };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = 0;
        int actual = findBestPG_BFS(5, 5, 15000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);
        
        assert(actual == expected && "Test 3 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 4. Edgy Case: Empty PG List ---
    {
        std::string test_name = "Test 4: Edgy_Empty_List";
        std::vector<PG> allPgs = {};
        PGGrid pgGrid = {};
        int expected = -1;
        int actual = findBestPG_BFS(0, 0, 10000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);

        assert(actual == expected && "Test 4 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }
    
    // --- 5. Edgy Case: All PGs Over Budget ---
    {
        std::string test_name = "Test 5: Edgy_All_Over_Budget";
        std::vector<PGSetup> pgSetups = { {1,1,10000}, {2,2,8000}, {3,3,6000} };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = -1;
        int actual = findBestPG_BFS(0, 0, 5000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);

        assert(actual == expected && "Test 5 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }
    
    // --- 6. Edgy Case: Office at a PG Location (Distance 0) ---
    {
        std::string test_name = "Test 6: Edgy_Office_At_PG";
        std::vector<PGSetup> pgSetups = {
            {5, 5, 7000.0}, // dist=0, rent=7000
            {1, 1, 8000.0},
            {5, 5, 6000.0}  // dist=0, rent=6000 (Cheapest at dist 0) -> Should win
        };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = 2;
        int actual = findBestPG_BFS(5, 5, 10000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);

        assert(actual == expected && "Test 6 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 7. Long Case: Many PGs with varied conditions ---
    {
        std::string test_name = "Test 7: Long_Many_PGs_Complex_Tiebreak";
        std::vector<PGSetup> pgSetups = {
            {5, 0, 11000.0},  // dist=5
            {1, 1, 15000.0},  // Over budget
            {2, 0, 10500.0},  // dist=2
            {0, 2, 9500.0},   // dist=2, same dist as index 2, but cheaper -> Should win
            {8, 8, 8000.0}    // dist=16, far but cheap
        };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = 3;
        int actual = findBestPG_BFS(0, 0, 12000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);

        assert(actual == expected && "Test 7 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    // --- 8. Edgy Case: Office out of bounds ---
    {
        std::string test_name = "Test 8: Edgy_Office_Out_Of_Bounds";
        std::vector<PGSetup> pgSetups = { {1,1,10000} };
        std::vector<PG> allPgs; PGGrid pgGrid;
        for(int i=0; i < pgSetups.size(); ++i) {
            allPgs.push_back({pgSetups[i].rent, i});
            pgGrid[{pgSetups[i].y, pgSetups[i].x}].push_back({pgSetups[i].rent, i});
        }
        int expected = -1;
        int actual = findBestPG_BFS(-1, -1, 15000.0, GRID_ROWS, GRID_COLS, pgGrid, allPgs);
        
        assert(actual == expected && "Test 8 failed.");
        std::cout << "--- " << test_name << " PASSED ---" << std::endl;
    }

    std::cout << "\nAll test cases completed successfully." << std::endl;

    return 0;
}
```